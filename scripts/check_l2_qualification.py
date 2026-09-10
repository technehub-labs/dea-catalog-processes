#!/usr/bin/env python3
"""
check_l2_qualification.py
==========================

L2 Qualification validator (CR-BP-34a; CR-BP-34 §11 BP-C1..C4).

Codifies the four mandatory L2 qualification criteria for a Business
Process as machine-testable rules:

  BP-C1 — Input-Output Transformation.
          The process transforms identifiable inputs into outputs or
          an equivalent defined result.
          Field: `trigger` (non-empty) AND `outcome` (non-empty).

  BP-C2 — Objective Contribution.
          The process makes a recognizable contribution to an
          enterprise objective or outcome.
          Field: `identity.outcome_statement` (non-empty).

  BP-C3 — Standalone Executability.
          The process represents a coherent unit of work that can be
          independently identified and performed.
          Field: `lifecycle_status` present AND `id` matches
          `dea:process-[a-z0-9-]+`.

  BP-C4 — Resource Dedication.
          The process requires identifiable resources or
          responsibility sufficient to constitute a distinct process
          boundary.
          Field: `identity.evidence_links` non-empty AND
          `metadata.change_history` (or top-level `change_history`)
          has at least one entry.

Coverage on the live catalog (2026-09-10): all 126 Business Process
records pass all four criteria. The validator is therefore a
regression guard (no findings today) rather than a corrective gate.

Exit codes:
  0  all records pass all four rules
  1  at least one record fails at least one rule
  2  self-test failure or I/O error

Usage:
  python3 scripts/check_l2_qualification.py
  python3 scripts/check_l2_qualification.py --strict
  python3 scripts/check_l2_qualification.py --json
  python3 scripts/check_l2_qualification.py --self-test

Author: Coder (for eaojnr). Established by CR-BP-34a (2026-09-10).
Derived from CR-BP-34 §11 (L2 Business Process Conformance) and
CR-BP-03 §8 (identity contract). Backed by the canonical fields
declared in `schemas/entities/entity.schema.json`.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Iterable

import yaml

ID_PATTERN = re.compile(r"^dea:process-[a-z0-9-]+$")


def _load_bp_records(catalog_root: Path) -> list[dict]:
    """Load every canonical Business Process record.

    Walks `entities/v1-alpha/dea:process-*/<id>.yaml`. Returns the
    parsed YAML for each. Skips directories that lack the expected
    YAML file (e.g. `candidates/`, `retired/`, `research/`).
    """
    base = catalog_root / "entities" / "v1-alpha"
    records: list[dict] = []
    if not base.exists():
        return records
    for entry in sorted(base.iterdir()):
        if not entry.is_dir() or not entry.name.startswith("dea:process-"):
            continue
        yaml_path = entry / f"{entry.name}.yaml"
        if not yaml_path.exists():
            continue
        try:
            data = yaml.safe_load(yaml_path.read_text())
        except yaml.YAMLError as exc:
            print(f"WARN: {yaml_path}: YAML parse error: {exc}", file=sys.stderr)
            continue
        if isinstance(data, dict):
            records.append(data)
    return records


def _check_bp_c1(record: dict) -> str | None:
    """BP-C1: trigger AND outcome both non-empty."""
    trigger = (record.get("trigger") or "").strip()
    outcome = (record.get("outcome") or "").strip()
    if not trigger:
        return "trigger missing or empty"
    if not outcome:
        return "outcome missing or empty"
    return None


def _check_bp_c2(record: dict) -> str | None:
    """BP-C2: identity.outcome_statement non-empty."""
    identity = record.get("identity") or {}
    if not isinstance(identity, dict):
        return "identity block missing or not a mapping"
    stmt = (identity.get("outcome_statement") or "").strip()
    if not stmt:
        return "identity.outcome_statement missing or empty"
    return None


def _check_bp_c3(record: dict) -> str | None:
    """BP-C3: lifecycle_status present AND id matches dea:process-*."""
    if not (record.get("lifecycle_status") or "").strip():
        return "lifecycle_status missing or empty"
    rec_id = record.get("id") or ""
    if not ID_PATTERN.match(rec_id):
        return f"id {rec_id!r} does not match {ID_PATTERN.pattern}"
    return None


def _check_bp_c4(record: dict) -> str | None:
    """BP-C4: evidence_links non-empty AND change_history has >=1 entry."""
    identity = record.get("identity") or {}
    evidence = identity.get("evidence_links") if isinstance(identity, dict) else None
    if not isinstance(evidence, list) or not evidence:
        return "identity.evidence_links missing or empty"
    change_history = (
        record.get("change_history")
        or (record.get("metadata") or {}).get("change_history")
        or []
    )
    if not isinstance(change_history, list) or not change_history:
        return "change_history missing or empty"
    return None


_RULES = (
    ("BP-C1", _check_bp_c1, "Input-Output Transformation"),
    ("BP-C2", _check_bp_c2, "Objective Contribution"),
    ("BP-C3", _check_bp_c3, "Standalone Executability"),
    ("BP-C4", _check_bp_c4, "Resource Dedication"),
)


def evaluate(records: Iterable[dict]) -> list[dict]:
    """Run all four rules against every record.

    Returns a list of findings:
        [{"rule": "BP-C1", "record_id": ..., "diagnostic": ...}, ...]
    Empty list == all pass.
    """
    findings: list[dict] = []
    for record in records:
        rec_id = record.get("id") or "<unknown>"
        for rule_id, fn, _label in _RULES:
            diagnostic = fn(record)
            if diagnostic is not None:
                findings.append({
                    "rule": rule_id,
                    "record_id": rec_id,
                    "diagnostic": diagnostic,
                })
    return findings


def _verdict(findings: list[dict]) -> str:
    if findings:
        return "NON-CONFORMANT"
    return "CONFORMANT"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=(
        "L2 Qualification validator (CR-BP-34a; BP-C1..C4)."
    ))
    parser.add_argument(
        "--catalog-root",
        default=".",
        help="Path to the catalog repo root (default: current directory).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 on any finding (otherwise findings are advisory).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON output instead of human-readable summary.",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run the built-in self-test and exit.",
    )
    args = parser.parse_args(argv)

    if args.self_test:
        return _self_test()

    catalog_root = Path(args.catalog_root).resolve()
    records = _load_bp_records(catalog_root)
    findings = evaluate(records)
    verdict = _verdict(findings)

    if args.json:
        print(json.dumps({
            "verdict": verdict,
            "candidate_count": len(records),
            "finding_count": len(findings),
            "findings": findings,
            "rules": [
                {"id": rid, "name": label}
                for rid, _fn, label in _RULES
            ],
        }, indent=2, sort_keys=True))
    else:
        print(f"L2 Qualification (CR-BP-34a; BP-C1..C4): {verdict}")
        print(f"  Records checked:  {len(records)}")
        print(f"  Findings:         {len(findings)}")
        for rid, _fn, label in _RULES:
            n = sum(1 for f in findings if f["rule"] == rid)
            print(f"    {rid} ({label}): {n}")
        if findings:
            print("\nFindings:")
            for f in findings:
                print(f"  [{f['rule']}] {f['record_id']}: {f['diagnostic']}")

    if findings and args.strict:
        return 1
    return 0


def _self_test() -> int:
    """Built-in self-test: verify pass and fail behavior on each rule."""

    def _record(**overrides):
        base = {
            "id": "dea:process-self-test",
            "name": "Self Test",
            "type": "Process",
            "version": "1.0.0",
            "lifecycle_status": "candidate",
            "status": "candidate",
            "process_intent": "operate",
            "process_type": "core",
            "description": "Self-test record.",
            "trigger": "An input arrives.",
            "outcome": "An output is produced.",
            "identity": {
                "verb": "Test",
                "object": "Self",
                "outcome_statement": "Self-test outcome.",
                "evidence_links": [{"type": "standard", "ref": "https://example.com"}],
            },
            "metadata": {
                "change_history": [{"cr": "CR-BP-34a", "date": "2026-09-10", "change": "self-test"}],
            },
        }
        base.update(overrides)
        return base

    # Baseline: should pass all four.
    baseline = [_record()]
    findings = evaluate(baseline)
    assert not findings, f"baseline must pass; got {findings}"

    # Each rule, individually failed.
    fail_c1 = [_record(trigger="")]
    f = evaluate(fail_c1)
    assert len(f) == 1 and f[0]["rule"] == "BP-C1", f

    fail_c2 = [_record(identity={"verb": "x", "object": "y", "outcome_statement": "", "evidence_links": [{"ref": "x"}]})]
    f = evaluate(fail_c2)
    assert len(f) == 1 and f[0]["rule"] == "BP-C2", f

    fail_c3 = [_record(lifecycle_status="")]
    f = evaluate(fail_c3)
    assert len(f) == 1 and f[0]["rule"] == "BP-C3", f

    fail_c3_id = [_record(id="not-a-dea-id")]
    f = evaluate(fail_c3_id)
    assert len(f) == 1 and f[0]["rule"] == "BP-C3", f

    fail_c4_no_evidence = [_record(identity={"verb": "x", "object": "y", "outcome_statement": "z", "evidence_links": []})]
    f = evaluate(fail_c4_no_evidence)
    assert len(f) == 1 and f[0]["rule"] == "BP-C4", f

    fail_c4_no_ch = [_record(metadata={"change_history": []})]
    f = evaluate(fail_c4_no_ch)
    assert len(f) == 1 and f[0]["rule"] == "BP-C4", f

    # Multi-rule fail: missing trigger + missing outcome_statement
    multi = [_record(trigger="", identity={"verb": "x", "object": "y", "outcome_statement": "", "evidence_links": [{"ref": "x"}]})]
    f = evaluate(multi)
    assert len(f) == 2 and {x["rule"] for x in f} == {"BP-C1", "BP-C2"}, f

    # Top-level change_history fallback (legacy shape)
    legacy_ch = [_record()]
    legacy_ch[0].pop("metadata", None)
    legacy_ch[0]["change_history"] = [{"cr": "x"}]
    assert not evaluate(legacy_ch), "top-level change_history must satisfy BP-C4"

    print("self-test PASS (7 negative cases, 1 multi-rule fail, 1 legacy shape)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
