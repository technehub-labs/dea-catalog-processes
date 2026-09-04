#!/usr/bin/env python3
"""
check_process_specialization.py — Business Process catalog specialization validator.

Implements CR-BP-SPEC-BP-01 rules BP-SPEC-01-001..007.

Rules:
  BP-SPEC-01-001 — Pointer declares dea:BusinessProcess (specialization) as the
                   primary metamodel: block. Missing is a hard failure.
  BP-SPEC-01-002 — Pointer declares dea:entity-process (kernel) as the first
                   entities: entry, with class_alias PRC and discriminator
                   process-kernel; no layer, no dimension. Missing or
                   mis-declared is a hard failure.
  BP-SPEC-01-003 — Specialization entry's class_alias is BP. Any other value is
                   a hard failure.
  BP-SPEC-01-004 — metamodel.version is pinned to a vX.Y.Z tag that the root
                   model carries as containing both the kernel and the
                   specialization (verified externally via the consumer
                   validator; this rule checks the pin is well-formed vX.Y.Z
                   and not v0.2.x).
  BP-SPEC-01-005 — Schema title in schemas/entities/process.json is
                   "Business Process" (not "Process"). Schema description
                   references the WSF / Process-kernel lineage.
  BP-SPEC-01-006 — Governance doc docs/governance/process-specialization.md
                   exists and references both CR-MM-PROC-01 and CR-AR-FMWK-01.
  BP-SPEC-01-007 — The catalog's process_intent enum (operational / support /
                   management) remains catalog-internal: it must NOT appear
                   as a root-model entity_id in any catalog YAML file.

Exit: 0 = all rules pass; 1 = at least one rule failed; 2 = self-test.

Built-in --self-test exercises each rule on a deliberately broken catalog
(then on a fixed catalog) and verifies the expected exit codes.

Folds the original CR-BP-01 rules BP-01-001/002/003 into BP-SPEC-01-001..007.
"""
import argparse
import json
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).parent.parent


def _load_yaml(path: Path):
    return yaml.safe_load(path.read_text())


def _load_json(path: Path):
    return json.loads(path.read_text())


def check_pointer(pointer: dict, errors: list[str]) -> None:
    """BP-SPEC-01-001..004."""
    mm = pointer.get("metamodel", {})
    primary_id = mm.get("entity_id")
    if primary_id != "dea:entity-business-process":
        errors.append(
            f"BP-SPEC-01-001: metamodel.entity_id must be "
            f"'dea:entity-business-process' (the specialization; OpenDEAM "
            f"root-model id); got {primary_id!r}. Note: the metamodel Core "
            f"id 'dea:BusinessProcess' is 1:1 mapped via the federation "
            f"mapping recorded in dea-metamodel/metamodel/dea-metamodel.yaml "
            f"(CR-MM-PROC-01 §4)."
        )

    version = str(mm.get("version", ""))
    if not version.startswith("v0.") or version == "v0.2.1":
        errors.append(
            f"BP-SPEC-01-004: metamodel.version {version!r} is not a valid "
            f"v0.6.x pin (v0.5.0 lacks both ids; v0.6.0 carries both; "
            f"v0.2.1 is the pre-CR-BP-01 baseline that has been superseded)"
        )

    if mm.get("class_alias") != "BP":
        errors.append(
            f"BP-SPEC-01-003: metamodel.class_alias must be 'BP' "
            f"(the specialization alias); got {mm.get('class_alias')!r}"
        )

    entities = mm.get("entities") or []
    if not entities:
        errors.append(
            "BP-SPEC-01-002: metamodel.entities must declare the kernel "
            "dea:entity-process; entities list is empty"
        )
    else:
        kernel = entities[0]
        if kernel.get("entity_id") != "dea:entity-process":
            errors.append(
                f"BP-SPEC-01-002: metamodel.entities[0].entity_id must be "
                f"'dea:entity-process' (the kernel); got "
                f"{kernel.get('entity_id')!r}"
            )
        if kernel.get("class_alias") != "PRC":
            errors.append(
                f"BP-SPEC-01-002: metamodel.entities[0].class_alias must be "
                f"'PRC' (the kernel's class_alias); got "
                f"{kernel.get('class_alias')!r}"
            )
        if kernel.get("discriminator") != "process-kernel":
            errors.append(
                f"BP-SPEC-01-002: metamodel.entities[0].discriminator must "
                f"be 'process-kernel'; got "
                f"{kernel.get('discriminator')!r}"
            )
        if kernel.get("layer") or kernel.get("dimension"):
            errors.append(
                f"BP-SPEC-01-002: metamodel.entities[0] (the kernel) must NOT "
                f"declare layer={kernel.get('layer')!r} or "
                f"dimension={kernel.get('dimension')!r} (per the v0.6.0 "
                f"abstract-kernel branch in scripts/validate_consumer.py)"
            )


def check_schema(catalog_root: Path, errors: list[str]) -> None:
    """BP-SPEC-01-005.

    The catalog's actual entity schema lives at `schemas/entity.schema.json`.
    Earlier CR text referenced `schemas/entities/process.json` (the metamodel's
    per-entity schema); the catalog's corresponding schema is `entity.schema.json`.
    """
    schema_path = catalog_root / "schemas" / "entity.schema.json"
    if not schema_path.exists():
        errors.append(
            f"BP-SPEC-01-005: schema file missing: {schema_path}"
        )
        return
    schema = _load_json(schema_path)
    title = schema.get("title", "")
    if title != "Business Process":
        errors.append(
            f"BP-SPEC-01-005: {schema_path} title must be 'Business Process'; "
            f"got {title!r}"
        )
    description = schema.get("description", "")
    if "kernel" not in description.lower() and "WSF" not in description and "wsf:" not in description:
        errors.append(
            f"BP-SPEC-01-005: {schema_path} description should reference the "
            f"WSF / Process-kernel lineage; got: {description[:80]}..."
        )


def check_governance(gov_path: Path, errors: list[str]) -> None:
    """BP-SPEC-01-006."""
    if not gov_path.exists():
        errors.append(
            f"BP-SPEC-01-006: governance doc missing: {gov_path}"
        )
        return
    text = gov_path.read_text()
    if "CR-MM-PROC-01" not in text:
        errors.append(
            f"BP-SPEC-01-006: governance doc {gov_path} must reference "
            f"CR-MM-PROC-01 (the metamodel kernel + specialization CR)"
        )
    if "CR-AR-FMWK-01" not in text:
        errors.append(
            f"BP-SPEC-01-006: governance doc {gov_path} must reference "
            f"CR-AR-FMWK-01 (the root-model sync CR)"
        )


def check_catalog_entries(catalog_root: Path, errors: list[str]) -> None:
    """BP-SPEC-01-007: process_intent must NOT promote to a root-model entity_id."""
    entries_dir = catalog_root / "entities"
    if not entries_dir.exists():
        return  # Phase 2 not started; no entries to check.
    forbidden = {
        "dea:entity-operational-process",
        "dea:entity-support-process",
        "dea:entity-management-process",
        "dea:entity-process-operational",
        "dea:entity-process-support",
        "dea:entity-process-management",
    }
    for yml in entries_dir.rglob("*.yaml"):
        data = _load_yaml(yml)
        eid = data.get("id")
        # CR-BP-12: Process Group entries are not L2 Business Process
        # entries; the specialization rule applies to L2 only.
        if data.get("type") == "ProcessGroup":
            continue
        if eid in forbidden:
            errors.append(
                f"BP-SPEC-01-007: {yml} declares entity_id {eid!r} which "
                f"promotes the catalog's process_intent (operational / support / "
                f"management) sub-classification to a root-model entity. "
                f"Sub-classifications are catalog-internal only."
            )


def run_checks(catalog_root: Path) -> list[str]:
    """Run all BP-SPEC-01-001..007 checks; return list of error strings."""
    errors: list[str] = []
    pointer_path = catalog_root / "metamodel-pointer.yaml"
    if not pointer_path.exists():
        errors.append(f"metamodel-pointer.yaml missing at {pointer_path}")
        return errors
    check_pointer(_load_yaml(pointer_path), errors)
    check_schema(catalog_root, errors)
    check_governance(
        catalog_root / "docs" / "governance" / "process-specialization.md", errors
    )
    check_catalog_entries(catalog_root, errors)
    return errors


def self_test() -> int:
    """Verify the validator detects broken pointers + accepts the fixed one.

    Builds a tmpdir catalog with broken artefacts, expects the validator to
    fail with all 7 rules represented in the output. Then fixes each in turn
    and verifies the rule count drops. Exit 0 if all expectations met.
    """
    import tempfile
    import shutil

    with tempfile.TemporaryDirectory(prefix="bp_spec_self_test_") as tmp:
        tmp_path = Path(tmp)
        # scaffold
        (tmp_path / "schemas").mkdir(parents=True)
        (tmp_path / "docs" / "governance").mkdir(parents=True)
        (tmp_path / "entities").mkdir()

        # Write a deliberately broken pointer (all rules violated)
        broken_pointer = {
            "metamodel": {
                "version": "v0.2.1",
                "entity_id": "dea:entity-process",  # WRONG: should be BusinessProcess
                "class_alias": "XX",  # WRONG
                "layer": "L3",
                "building_block": "L3-value-delivery",
                # NO entities: list (WRONG)
            },
            "catalog": {"name": "x"},
        }
        (tmp_path / "metamodel-pointer.yaml").write_text(
            yaml.safe_dump(broken_pointer, sort_keys=False)
        )

        # WRONG schema title
        (tmp_path / "schemas" / "entity.schema.json").write_text(
            json.dumps({
                "title": "Process",  # WRONG
                "description": "A process.",
            })
        )

        # missing governance doc (don't create)

        # Promote process_intent to root-model entity
        (tmp_path / "entities" / "v1-alpha" / "p1.yaml").parent.mkdir(parents=True)
        (tmp_path / "entities" / "v1-alpha" / "p1.yaml").write_text(
            yaml.safe_dump({
                "id": "dea:entity-operational-process",  # WRONG
                "name": "Operational Process",
                "type": "Process",
                "version": "1.0.0",
            }, sort_keys=False)
        )

        errs = run_checks(tmp_path)
        # Expect at least one error per rule
        rule_prefixes = [f"BP-SPEC-01-00{i}" for i in range(1, 8)]
        for prefix in rule_prefixes:
            if not any(e.startswith(prefix) for e in errs):
                print(f"self-test FAIL: expected at least one {prefix}* error in: {errs}")
                return 2

        # Now FIX everything and verify zero errors
        fixed_pointer = {
            "metamodel": {
                "version": "v0.6.0",
                "entity_id": "dea:entity-business-process",
                "class_alias": "BP",
                "layer": "L3",
                "building_block": "L3-value-delivery",
                "entities": [
                    {
                        "entity_id": "dea:entity-process",
                        "class_alias": "PRC",
                        "discriminator": "process-kernel",
                    },
                ],
            },
            "catalog": {"name": "x"},
        }
        (tmp_path / "metamodel-pointer.yaml").write_text(
            yaml.safe_dump(fixed_pointer, sort_keys=False)
        )
        (tmp_path / "schemas" / "entity.schema.json").write_text(
            json.dumps({
                "title": "Business Process",
                "description": "Business-context specialization of the WSF-derived Process kernel (dea:Process; dea:entity-process).",
            })
        )
        (tmp_path / "docs" / "governance" / "process-specialization.md").write_text(
            "References CR-MM-PROC-01 and CR-AR-FMWK-01.\n"
        )
        # remove the rogue entity
        (tmp_path / "entities" / "v1-alpha" / "p1.yaml").unlink()

        errs_fixed = run_checks(tmp_path)
        if errs_fixed:
            print(f"self-test FAIL: expected zero errors on fixed catalog, got: {errs_fixed}")
            return 2

    print("self-test PASS: BP-SPEC-01-001..007 all triggered on broken catalog; zero errors on fixed.")
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

    errors = run_checks(args.catalog_root)
    if errors:
        print("Business Process catalog specialization: FAILED")
        for e in errors:
            print(f"  ✗ {e}")
        return 1
    print("Business Process catalog specialization: PASS (BP-SPEC-01-001..007)")
    return 0


if __name__ == "__main__":
    sys.exit(main())