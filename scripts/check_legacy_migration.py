#!/usr/bin/env python3
"""
check_legacy_migration.py — Legacy Field Migration validator.

Implements CR-BP-03A rules BP-MIG-001..BP-MIG-005.

Rules:
  BP-MIG-001 — parent_process NOT declared: the field has been
               REMOVED from the schema (CR-BP-03A §3.2). It was a
               catalog invention from CR-BP-01; the metamodel's
               process.json does not declare it. No entry may
               declare it.
  BP-MIG-002 — child_processes NOT declared: same as BP-MIG-001
               for child_processes.
  BP-MIG-003 — capabilities_delivered IS EMPTY (soft-deprecated):
               the canonical form is
               relationships[relationship_type=realizes]
               (CR-BP-03A §3.3). The field is retained for
               backward-compat with the metamodel but is
               soft-deprecated; entries that declare it trigger
               a migration recommendation.
  BP-MIG-004 — relationships array entries are well-formed:
               each entry has source_id, target_id,
               relationship_type; source_id matches the entry's
               own id.
  BP-MIG-005 — Migration report: for any entry that triggers
               BP-MIG-001..003, emit a structured migration
               recommendation showing the canonical form.

Exit: 0 = all rules pass (or no entries); 2 = self-test;
      1 = at least one rule failed.
"""
import argparse
import json
import sys
import tempfile
from pathlib import Path

import yaml

BASE = Path(__file__).parent.parent

# Authoritative relationship-instance shape (mirrors
# technehub-labs/dea-metamodel/schemas/relationships/relationship-instance.json).
# The catalog primarily uses 'composes' and 'realizes'; a small set
# of other types are admitted when the contributor can defend the
# choice.
ALLOWED_RELATIONSHIP_TYPES = {
    "composes", "realizes", "specializes", "aggregates",
    "depends-on", "produces", "consumes", "flows-to",
    "governs", "owns", "responsible-for", "supports",
    "triggers", "executes", "orchestrates",
}


def _check_one(entry: dict, errors: list[str], suggestions: list[dict]) -> None:
    eid = entry.get("id", "<unknown>")

    # BP-MIG-001: parent_process NOT declared
    if "parent_process" in entry:
        errors.append(
            f"BP-MIG-001 ({eid}): parent_process is declared. "
            f"This field has been REMOVED from the catalog schema "
            f"(CR-BP-03A §3.2). It was a CR-BP-01 invention; the "
            f"metamodel's process.json does not declare it. Remove "
            f"the field and express the relationship as "
            f"relationships[relationship_type=composes]."
        )
        suggestions.append({
            "target": eid,
            "suggestion_type": "migration",
            "rule": "BP-MIG-001",
            "current_state": {"parent_process": entry.get("parent_process")},
            "suggested_state": {
                "relationships": [
                    {
                        "source_id": entry.get("parent_process"),  # NOTE: inverse direction
                        "target_id": eid,
                        "relationship_type": "composes",
                        "rationale": "Migrated from legacy parent_process; the parent is the source in a 'composes' view (or this entry is the target of a 'composed-by' view).",
                    }
                ],
            },
            "confidence": 0.95,
            "rationale": "parent_process is a CR-BP-01 catalog invention; the metamodel uses typed relationship instances (CR-002).",
        })

    # BP-MIG-002: child_processes NOT declared
    if "child_processes" in entry and entry["child_processes"]:
        errors.append(
            f"BP-MIG-002 ({eid}): child_processes is declared "
            f"({len(entry['child_processes'])} items). This field "
            f"has been REMOVED from the catalog schema (CR-BP-03A "
            f"§3.2). It was a CR-BP-01 invention; the metamodel's "
            f"process.json does not declare it. Remove the field "
            f"and express the relationships as "
            f"relationships[relationship_type=composes]."
        )
        suggestions.append({
            "target": eid,
            "suggestion_type": "migration",
            "rule": "BP-MIG-002",
            "current_state": {"child_processes": entry.get("child_processes")},
            "suggested_state": {
                "relationships": [
                    {
                        "source_id": eid,
                        "target_id": child_id,
                        "relationship_type": "composes",
                        "rationale": "Migrated from legacy child_processes.",
                    }
                    for child_id in entry.get("child_processes", [])
                ],
            },
            "confidence": 0.95,
            "rationale": "child_processes is a CR-BP-01 catalog invention; the metamodel uses typed relationship instances (CR-002).",
        })

    # BP-MIG-003: capabilities_delivered IS EMPTY (soft-deprecated)
    if "capabilities_delivered" in entry and entry["capabilities_delivered"]:
        errors.append(
            f"BP-MIG-003 ({eid}): capabilities_delivered is declared "
            f"({len(entry['capabilities_delivered'])} items). This "
            f"field is soft-deprecated (CR-BP-03A §3.3); the "
            f"canonical form is relationships[relationship_type=realizes] "
            f"with full provenance. Remove the field and express the "
            f"realizations as relationship instances."
        )
        suggestions.append({
            "target": eid,
            "suggestion_type": "migration",
            "rule": "BP-MIG-003",
            "current_state": {"capabilities_delivered": entry.get("capabilities_delivered")},
            "suggested_state": {
                "relationships": [
                    {
                        "source_id": eid,
                        "target_id": cap_id,
                        "relationship_type": "realizes",
                        "status": "active",
                        "rationale": "Migrated from legacy capabilities_delivered.",
                        "provenance": {
                            "type": "migration",
                            "asserted_at": "<YYYY-MM-DD>",
                        },
                    }
                    for cap_id in entry.get("capabilities_delivered", [])
                ],
            },
            "confidence": 0.95,
            "rationale": "capabilities_delivered is a metamodel backward-compat shim; the canonical form is relationships[relationship_type=realizes] with full provenance.",
        })

    # BP-MIG-004: relationships array entries are well-formed
    relationships = entry.get("relationships", []) or []
    for i, rel in enumerate(relationships):
        rel_id = f"{eid}#relationships[{i}]"
        if not isinstance(rel, dict):
            errors.append(
                f"BP-MIG-004 ({rel_id}): relationship is not an object."
            )
            continue
        for required in ("source_id", "target_id", "relationship_type"):
            if not rel.get(required):
                errors.append(
                    f"BP-MIG-004 ({rel_id}): missing required field {required!r}."
                )
        if rel.get("source_id") and rel["source_id"] != eid:
            errors.append(
                f"BP-MIG-004 ({rel_id}): source_id {rel['source_id']!r} "
                f"does not match the entry's own id {eid!r}. For an L2 "
                f"Business Process entry, source_id is the entry's own id."
            )
        rt = rel.get("relationship_type")
        if rt and rt not in ALLOWED_RELATIONSHIP_TYPES:
            errors.append(
                f"BP-MIG-004 ({rel_id}): relationship_type {rt!r} is not "
                f"in the allowed set {sorted(ALLOWED_RELATIONSHIP_TYPES)}."
            )

    # BP-MIG-005: report is emitted (suggestions list is populated for
    # any entry that triggered BP-MIG-001..003). The caller (CI) is
    # responsible for posting the report as a PR comment.


def run_checks(catalog_root: Path) -> tuple[list[str], list[dict]]:
    errors: list[str] = []
    suggestions: list[dict] = []
    ent_dir = catalog_root / "entities" / "v1-alpha"
    if not ent_dir.exists():
        return errors, suggestions
    for yml in sorted(ent_dir.rglob("*.yaml")):
        entry = yaml.safe_load(yml.read_text())
        if not isinstance(entry, dict):
            continue
        # CR-BP-12: Process Group entries are not L2 Business Process
        # entries; the legacy migration rule applies to L2 only.
        if entry.get("type") == "ProcessGroup":
            continue
        _check_one(entry, errors, suggestions)
    return errors, suggestions


def self_test() -> int:
    """Verify the validator detects broken + accepts fixed."""
    with tempfile.TemporaryDirectory(prefix="mig_self_test_") as tmp:
        tmp_path = Path(tmp)
        ent_dir = tmp_path / "entities" / "v1-alpha"
        ent_dir.mkdir(parents=True)

        # Broken: declares all 3 legacy fields + has a malformed relationship
        broken = {
            "id": "dea:bp-bad-mig",
            "name": "Manage Legacy",
            "type": "Process",
            "version": "1.0.0",
            "process_intent": "operational",
            "process_audience": "customer-demand",
            "process_type": "management",
            "description": "Legacy entry that uses the old fields.",
            "trigger": "x",
            "outcome": "y",
            "parent_process": "dea:bp-parent",  # BP-MIG-001
            "child_processes": ["dea:bp-child-1", "dea:bp-child-2"],  # BP-MIG-002
            "capabilities_delivered": ["dea:cap-1"],  # BP-MIG-003
            "relationships": [
                # BP-MIG-004: source_id does not match entry's id
                {
                    "source_id": "dea:bp-other",
                    "target_id": "dea:cap-2",
                    "relationship_type": "realizes",
                },
                # BP-MIG-004: bad relationship_type
                {
                    "source_id": "dea:bp-bad-mig",
                    "target_id": "dea:bp-other",
                    "relationship_type": "unknown-type",
                },
            ],
        }
        (ent_dir / "dea_bp-bad-mig.yaml").write_text(yaml.safe_dump(broken, sort_keys=False))

        errs, suggs = run_checks(tmp_path)
        for prefix in ("BP-MIG-001", "BP-MIG-002", "BP-MIG-003", "BP-MIG-004"):
            if not any(e.startswith(prefix) for e in errs):
                print(f"self-test FAIL: expected at least one {prefix}* error in: {errs}")
                return 2
        if len(suggs) < 3:
            print(f"self-test FAIL: expected at least 3 migration suggestions, got: {len(suggs)}")
            return 2

        # Now FIX everything.
        for f in ent_dir.iterdir():
            f.unlink()
        fixed = {
            "id": "dea:bp-good-mig",
            "name": "Manage Customer",
            "type": "Process",
            "version": "1.0.0",
            "process_intent": "management",
            "process_audience": "customer-demand",
            "process_type": "management",
            "description": "Fully canonical entry.",
            "trigger": "Customer event",
            "outcome": "Customer is managed.",
            "identity": {
                "verb": "Manage",
                "object": "Customer",
                "outcome_statement": "Customer relationships are maintained per policy.",
                "evidence_links": [{"type": "documentation", "ref": "docs/m.md"}],
            },
            "relationships": [
                {
                    "source_id": "dea:bp-good-mig",
                    "target_id": "dea:bp-good-mig-child",
                    "relationship_type": "composes",
                    "status": "active",
                    "rationale": "Structural composition.",
                    "provenance": {
                        "type": "manual",
                        "asserted_at": "2026-09-03",
                    },
                },
                {
                    "source_id": "dea:bp-good-mig",
                    "target_id": "dea:capability:manage-customer",
                    "relationship_type": "realizes",
                    "status": "active",
                    "rationale": "Capability realization.",
                    "provenance": {
                        "type": "manual",
                        "asserted_at": "2026-09-03",
                    },
                },
            ],
        }
        (ent_dir / "dea_bp-good-mig.yaml").write_text(yaml.safe_dump(fixed, sort_keys=False))
        errs_fixed, suggs_fixed = run_checks(tmp_path)
        if errs_fixed:
            print(f"self-test FAIL: expected zero errors on fixed, got: {errs_fixed}")
            return 2

    print("self-test PASS: BP-MIG-001..004 all triggered on broken catalog; zero errors on fixed.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument(
        "--catalog-root", type=Path, default=BASE,
        help="Catalog root directory (default: parent of scripts/)",
    )
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    errors, suggestions = run_checks(args.catalog_root)
    if errors:
        print("Legacy Migration validation: FAILED")
        for e in errors:
            print(f"  ✗ {e}")
        if suggestions:
            print("\nMigration recommendations (BP-MIG-005):")
            for s in suggestions:
                print(f"  → {s['target']}: {s['rule']} "
                      f"(confidence={s['confidence']:.2f}) — {s['rationale'][:120]}")
        return 1
    if suggestions:
        print("Legacy Migration validation: PASS (with migration recommendations)")
        for s in suggestions:
            print(f"  → {s['target']}: {s['rule']} "
                  f"(confidence={s['confidence']:.2f}) — {s['rationale'][:120]}")
        return 0
    print("Legacy Migration validation: PASS (BP-MIG-001..005)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
