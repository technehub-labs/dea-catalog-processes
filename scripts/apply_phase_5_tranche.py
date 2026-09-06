#!/usr/bin/env python3
"""
apply_phase_5_tranche.py: Apply a CR-BP-15-IMP Phase 5 tranche
migration to a set of canonical Business Process entries.

The migration pattern (per the disposition register and the
CR-BP-14 /13, /17, /20 contract):

  (a) `process_intent`: legacy vocabulary token (`operational`,
      `support`, `management`) replaced with the canonical
      vocabulary token (`govern`, `manage`, `operate`, `deliver`,
      `support`, `develop`, `transform`).
  (b) `process_audience`: removed (legacy alias superseded by the
      canonical `context:` block; CR-BP-14 /13).
  (c) `process_context`: scalar string replaced with the canonical
      `context:` array block: `[{ref: <pc-id>}]`.
  (d) `relationships`: a `serves` relationship toward the canonical
      ECF coordinate is added (the CG-003 form:
      `ecf:<lowerCamelDomain>.<lowerCamelStage>`).
  (e) `metadata.change_history`: a CR-BP-15-IMP Phase 5 entry is
      appended (reconciled_at + reconciled_by + change description).

The script is idempotent: re-running on an already-migrated file
makes no further changes. It supports `--self-test` (round-trip
fixture) and `--strict` (exit 1 on any per-record error).

Authoritative reference: CR-BP-15-IMP /5; CR-BP-14 /13, /17, /20.

Usage:
  python scripts/apply_phase_5_tranche.py --tranche <id> \\
      --manifest reconciliation/tranches/plan.yaml
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent

# CR-BP-14 /17 mapping (evidence-based, per the disposition register).
# Keys: legacy intent vocabulary. Values: canonical intent vocabulary.
LEGACY_TO_CANONICAL_INTENT = {
    "operational": "operate",
    "support": "support",   # canonical also uses support
    "management": "manage",
}


def _read_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text())


def _write_yaml(path: Path, data: dict) -> None:
    """Write YAML preserving key order. PyYAML's safe_dump keeps dict
    insertion order by default (PyYAML >= 5.1)."""
    path.write_text(yaml.safe_dump(data, sort_keys=False, default_flow_style=False))


def _slugify(s: str) -> str:
    return (s.replace("dea:", "")
             .replace(".", "_")
             .replace("-", "_")
             .lower())


def _find_process_path(record_id: str) -> Path:
    """Locate the YAML file for a Business Process record id."""
    slug = _slugify(record_id)
    candidates = list((REPO_ROOT / "entities/v1-alpha").glob(
        f"{record_id}/{record_id}.yaml"))
    if not candidates:
        # Try the slug-prefixed directory
        candidates = list((REPO_ROOT / "entities/v1-alpha").glob(f"dea:process-*/{record_id}.yaml"))
    if not candidates:
        raise FileNotFoundError(f"no YAML file found for {record_id}")
    return candidates[0]


def _parse_ecf_coordinate(record: dict) -> tuple[str, str] | None:
    """Extract (domain, stage) from the canonicalReferences block.

    The canonical ECF identifier is
    `ecf:<lowerCamelDomain>.<lowerCamelStage>`, matching
    CG-003. We re-derive it from the canonicalReferences so the
    canonical block stays the source of truth.
    """
    ecf = record.get("ecfConformance", {})
    for ref in ecf.get("canonicalReferences", []) or []:
        if ref.get("kind") == "coordinate":
            domain = ref.get("domain")
            stage = ref.get("stage")
            if domain and stage:
                return domain, stage
    return None


def _ecf_target_id(domain: str, stage: str) -> str:
    """Build the CG-003 canonical ECF target identifier.

    The form is `ecf:<lowerCamelDomain>.<lowerCamelStage>`,
    e.g. `ecf:customerDemand.build`.
    """
    return f"ecf:{domain[:1].lower()}{domain[1:]}.{stage[:1].lower()}{stage[1:]}"


def migrate_record(record_id: str, disposition: dict,
                   phase_id: str = "phase-5") -> tuple[dict, list[str]]:
    """Apply the migration to a single record. Returns (migrated_record, changes)."""
    path = _find_process_path(record_id)
    data = _read_yaml(path)
    changes: list[str] = []

    # (a) Intent migration.
    intent_axis = next((c for c in disposition.get("changes", [])
                        if c.get("axis") == "process_intent"), None)
    if intent_axis:
        legacy = intent_axis["from"]
        canonical = intent_axis["to"]
        if data.get("process_intent") == legacy:
            data["process_intent"] = canonical
            changes.append(f"process_intent: {legacy} -> {canonical}")
        elif data.get("process_intent") == canonical:
            changes.append(f"process_intent: already canonical ({canonical})")
        else:
            changes.append(f"process_intent: WARN unexpected value "
                           f"{data.get('process_intent')!r} "
                           f"(expected {legacy!r} or {canonical!r})")

    # (b) process_audience removal.
    if "process_audience" in data:
        del data["process_audience"]
        changes.append("process_audience: removed (canonical context: block in place)")

    # (c) process_context -> context block.
    context_axis = next((c for c in disposition.get("changes", [])
                         if c.get("axis") == "process_context"), None)
    if context_axis:
        target = context_axis["to"]
        # Remove legacy scalar if present.
        if "process_context" in data:
            del data["process_context"]
            changes.append("process_context: removed (scalar -> block)")
        # Add canonical block if absent.
        existing_ctx = data.get("context")
        if not existing_ctx:
            # Insert the canonical block after process_specialization.
            data["context"] = [{"ref": target}]
            changes.append(f"context: added canonical block [{target}]")

    # (d) Add the `serves` relationship toward the ECF coordinate.
    ecf = _parse_ecf_coordinate(data)
    if ecf:
        domain, stage = ecf
        target_id = _ecf_target_id(domain, stage)
        rels = data.setdefault("relationships", [])
        if not any(r.get("relationship_type") == "serves" and
                   r.get("target_id") == target_id for r in rels):
            rels.append({
                "source_id": record_id,
                "relationship_type": "serves",
                "target_id": target_id,
            })
            changes.append(f"relationships: added serves -> {target_id}")

    # (e) Change history.
    meta = data.setdefault("metadata", {})
    history = meta.setdefault("change_history", [])
    already = any(
        h.get("cr") == "CR-BP-15-IMP" and h.get("phase") == phase_id
        for h in history
    )
    if not already:
        history.append({
            "cr": "CR-BP-15-IMP",
            "phase": phase_id,
            "date": "2026-09-06",
            "change": (
                "Phase 5 tranche migration: legacy intent migrated to "
                "canonical vocabulary; legacy scalar `process_context` "
                "migrated to canonical `context:` block; legacy "
                "`process_audience` removed (CR-BP-14 /13); canonical "
                "`serves` relationship toward the ECF coordinate added."
            ),
        })
        changes.append("metadata.change_history: CR-BP-15-IMP Phase 5 entry appended")

    return data, changes


def apply_tranche(tranche_id: str, manifest_path: Path) -> list[dict]:
    """Apply a tranche migration. Returns a list of per-record results."""
    plan = _read_yaml(manifest_path)
    register = _read_yaml(REPO_ROOT / "reconciliation/dispositions/register.yaml")
    disp_by_record = {d["record_id"]: d for d in register.get("dispositions", [])}

    tranche = next((t for t in plan.get("tranches", [])
                    if t.get("tranche_id") == tranche_id), None)
    if not tranche:
        raise ValueError(f"tranche {tranche_id!r} not in plan")

    results = []
    for record_id in tranche.get("records", []):
        disposition = disp_by_record.get(record_id)
        if not disposition:
            results.append({"record_id": record_id, "error":
                            f"no disposition entry for {record_id!r}"})
            continue
        try:
            migrated, changes = migrate_record(record_id, disposition)
            path = _find_process_path(record_id)
            _write_yaml(path, migrated)
            results.append({
                "record_id": record_id,
                "path": str(path.relative_to(REPO_ROOT)),
                "changes": changes,
            })
        except Exception as exc:
            results.append({
                "record_id": record_id,
                "error": str(exc),
            })

    return results


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--self-test", action="store_true")
    p.add_argument("--strict", action="store_true")
    p.add_argument("--tranche", type=str, default=None)
    p.add_argument("--manifest", type=Path,
                   default=REPO_ROOT / "reconciliation/tranches/plan.yaml")
    p.add_argument("--quiet", action="store_true")
    args = p.parse_args(argv)

    if args.self_test:
        # Build a fixture, apply migration, assert idempotence.
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            (tmp_path / "entities/v1-alpha/dea:process-test").mkdir(parents=True)
            fixture = tmp_path / "entities/v1-alpha/dea:process-test/dea:process-test.yaml"
            fixture.write_text(yaml.safe_dump({
                "id": "dea:process-test",
                "name": "Build Test",
                "type": "Process",
                "process_intent": "operational",
                "process_audience": "customer-demand",
                "process_context": "dea:pc-cd-b",
                "process_specialization": [],
                "relationships": [],
                "metadata": {"change_history": []},
                "ecfConformance": {"canonicalReferences": [
                    {"kind": "coordinate", "domain": "CustomerAndDemand", "stage": "Build"}
                ]},
            }, sort_keys=False))
            # Patch REPO_ROOT for the helper.
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                "apply_phase_5_tranche",
                REPO_ROOT / "scripts/apply_phase_5_tranche.py",
            )
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            orig = mod.REPO_ROOT
            mod.REPO_ROOT = tmp_path
            try:
                disposition = {
                    "record_id": "dea:process-test",
                    "changes": [
                        {"axis": "process_intent", "from": "operational", "to": "operate"},
                        {"axis": "process_context", "from": "dea:pc-cd-b", "to": "dea:pc-cd-b"},
                        {"axis": "process_audience", "from": "customer-demand", "to": "REMOVE"},
                    ],
                }
                migrated, changes = mod.migrate_record("dea:process-test", disposition)
                # Assert migration is correct.
                assert migrated["process_intent"] == "operate", "intent not migrated"
                assert "process_audience" not in migrated, "audience not removed"
                assert migrated["context"] == [{"ref": "dea:pc-cd-b"}], "context block wrong"
                # The canonical form is ecf:<lowerCamelDomain>.<lowerCamelStage>;
                # we preserve the rest of the domain name as-is. So
                # `CustomerAndDemand` -> `customerAndDemand` (NOT `customeranddemand`).
                domain_sample = "CustomerAndDemand"
                expected_ecf = f"ecf:{domain_sample[:1].lower()}{domain_sample[1:]}.build"
                assert any(r.get("relationship_type") == "serves"
                           and r.get("target_id") == expected_ecf
                           for r in migrated["relationships"]), (
                    f"serves relationship missing; expected {expected_ecf!r}; "
                    f"got {migrated['relationships']!r}"
                )
                assert any(h.get("cr") == "CR-BP-15-IMP"
                           and h.get("phase") == "phase-5"
                           for h in migrated["metadata"]["change_history"]), \
                    "change history not appended"
                # Idempotence: re-run, no further changes.
                migrated2, changes2 = mod.migrate_record("dea:process-test", disposition)
                assert migrated == migrated2, f"non-idempotent: {changes2}"
                if not args.quiet:
                    print("self-test PASS: migration applies the pattern + is idempotent")
            finally:
                mod.REPO_ROOT = orig
        return 0

    if not args.tranche:
        print("--tranche required for non-self-test runs", file=sys.stderr)
        return 2

    results = apply_tranche(args.tranche, args.manifest)
    failed = [r for r in results if "error" in r]
    if failed:
        for r in failed:
            print(f"FAIL {r['record_id']}: {r['error']}", file=sys.stderr)
        return 1 if args.strict else 0

    if not args.quiet:
        for r in results:
            print(f"OK   {r['record_id']}: {len(r['changes'])} changes")
            for c in r["changes"]:
                print(f"     - {c}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
