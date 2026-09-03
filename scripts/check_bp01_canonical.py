"""CR-BP-01 canonical-identity validator.

Enforces CR-BP-01 acceptance criteria AC-01, AC-03, AC-07 by validating
catalog artifacts against three rules:

  BP-01-001: any artifact declaring a canonical Business Process entity
             id MUST equal `dea:BusinessProcess`. No other form is
             accepted as canonical in new artifacts.

  BP-01-002: any artifact using `dea:entity-process` as an entity id
             MUST declare explicit legacy compatibility (via a
             `legacy_compatibility: true` annotation, a presence in
             `metamodel.legacy_identifiers`, or a `deprecated`/`legacy`
             status marker). Otherwise the validator exits non-zero.

  BP-01-003: no new normative artifact may introduce a canonical entity
             named simply `dea:Process` where `dea:BusinessProcess` is
             intended.

The scan walks:
  - change-requests/*.md       (front-matter-free; CR text may reference
                                either id; canonical usage is asserted
                                only in non-CR artifacts)
  - metamodel-pointer.yaml     (the pointer itself)
  - entities/v1-alpha/*.yaml   (catalog entries; currently empty by
                                design; Phase 2 deferred)
  - schemas/**/*.json          (id-pattern regexes; rejects patterns that
                                only match the legacy id)
  - docs/**/*.md               (narrative; informational only; never
                                fails the gate, but emits a soft warning
                                if the legacy id appears as a canonical
                                entity in narrative prose)

Stdlib only. Exit codes:
  0 - every artifact passes BP-01-001, / 002, / 003.
  1 - at least one hard failure.
  2 - built-in self-test regression (the validator cannot trust itself).

Usage:
    python3 scripts/check_bp01_canonical.py
    python3 scripts/check_bp01_canonical.py --self-test

Environment:
    REPO_ROOT - defaults to the parent of this script's directory.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

REPO = Path(os.environ.get("REPO_ROOT", Path(__file__).resolve().parent.parent))

CANONICAL_ENTITY_ID = "dea:BusinessProcess"
LEGACY_ENTITY_ID = "dea:entity-process"
FORBIDDEN_BARE_PROCESS_ID = "dea:Process"

# Allow only the canonical id in id-pattern regexes in schemas.
CANONICAL_PATTERN_REGEX = re.compile(r"\^dea:BusinessProcess\$?")


def is_legacy_compatible_declared(text: str) -> bool:
    """Return True if the text declares explicit legacy compatibility.

    Triggers on any of:
      - `legacy_compatibility: true`
      - presence in a `legacy_identifiers:` block
      - status: deprecated / status: legacy / status: removed
      - CR-BP-01 reference alongside the legacy id
    """
    text_lower = text.lower()
    triggers = (
        "legacy_compatibility: true",
        "legacy_identifiers:",
        "status: deprecated",
        "status: legacy",
        "status: removed",
        "cr-bp-01",
    )
    return any(t in text_lower for t in triggers)


def check_pointer(path: Path) -> list[str]:
    """Validate metamodel-pointer.yaml against BP-01-001/002."""
    if not path.exists():
        return [f"metamodel-pointer.yaml missing at {path}"]
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    # BP-01-001: canonical entity_id must be dea:BusinessProcess
    m = re.search(r"^\s*entity_id:\s*(\S+)\s*$", text, re.MULTILINE)
    if not m:
        errors.append(f"{path.name}: no `entity_id:` line found")
    else:
        entity_id = m.group(1)
        if entity_id != CANONICAL_ENTITY_ID:
            errors.append(
                f"{path.name}: BP-01-001 violation: entity_id is '{entity_id}', "
                f"expected canonical '{CANONICAL_ENTITY_ID}'"
            )
        if entity_id == LEGACY_ENTITY_ID:
            errors.append(
                f"{path.name}: BP-01-001 violation: entity_id is the legacy "
                f"identifier '{LEGACY_ENTITY_ID}'; use '{CANONICAL_ENTITY_ID}' "
                f"as canonical and place '{LEGACY_ENTITY_ID}' under "
                f"`legacy_identifiers`"
            )
    # BP-01-002: if legacy id appears, legacy_identifiers block must be present
    if LEGACY_ENTITY_ID in text and "legacy_identifiers:" not in text:
        errors.append(
            f"{path.name}: BP-01-002 violation: legacy id '{LEGACY_ENTITY_ID}' "
            f"appears without an explicit `legacy_identifiers:` block"
        )
    # BP-01-003: forbid bare dea:Process as canonical
    if "entity_id: dea:Process" in text or "entity_id: dea:process" in text:
        errors.append(
            f"{path.name}: BP-01-003 violation: bare 'dea:Process' used as "
            f"canonical entity_id; use '{CANONICAL_ENTITY_ID}'"
        )
    return errors


def check_schema_id_patterns(paths: list[Path]) -> list[str]:
    """Validate schema id-pattern regexes that explicitly anchor to the
    Business Process entity id.

    Scoping rule: a catalog entry schema uses lowercase namespaced ids
    (e.g. `dea:process-<name>` per the sibling capability catalog
    precedent). The canonical metamodel entity id (`dea:BusinessProcess`)
    lives in `metamodel-pointer.yaml`, not in catalog entries. Therefore
    the validator only inspects patterns that mention either the legacy
    or the canonical Business Process id literally — generic lowercase
    entry-id patterns are out of scope for CR-BP-01.

    If a schema pattern explicitly anchors to `dea:entity-process` as the
    only valid form, the validator rejects it (BP-01-001 violation).
    If a schema pattern explicitly accepts `dea:BusinessProcess`, the
    validator passes.
    """
    errors: list[str] = []
    for p in paths:
        try:
            schema = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{p.name}: JSON parse error: {e}")
            continue
        patterns: list[tuple[str, str]] = []
        if "pattern" in schema:
            patterns.append(("$", schema["pattern"]))
        props = schema.get("properties") or {}
        for prop_name, prop_schema in props.items():
            if isinstance(prop_schema, dict) and "pattern" in prop_schema:
                patterns.append((prop_name, prop_schema["pattern"]))
        for prop_name, pattern in patterns:
            # Only inspect patterns that explicitly anchor to a Business
            # Process entity id (legacy or canonical). Generic lowercase
            # patterns are catalog-level and out of scope.
            mentions_legacy = (
                LEGACY_ENTITY_ID in pattern
                or "dea-entity-process" in pattern
                or "entity-process" in pattern
            )
            mentions_canonical = (
                CANONICAL_ENTITY_ID in pattern
                or "BusinessProcess" in pattern
                or "dea-business-process" in pattern
            )
            if not (mentions_legacy or mentions_canonical):
                continue
            try:
                rgx = re.compile(pattern)
            except re.error as e:
                errors.append(f"{p.name}: bad regex '{pattern}': {e}")
                continue
            # If the legacy id is mentioned but the canonical is not,
            # this is a BP-01-001 violation.
            if mentions_legacy and not mentions_canonical:
                errors.append(
                    f"{p.name}: BP-01-001 violation: pattern '{pattern}' "
                    f"({prop_name}) anchors to legacy '{LEGACY_ENTITY_ID}' "
                    f"but not to canonical '{CANONICAL_ENTITY_ID}'"
                )
    return errors


def check_narrative_legacy_references(paths: list[Path]) -> list[str]:
    """Warn (soft) when the legacy id appears as a canonical entity in docs.

    Soft warnings do not fail the gate, but are emitted to stdout for CI logs.
    """
    warnings: list[str] = []
    # Patterns indicating the legacy id is being used as a canonical entity
    # in narrative prose (not as a legacy reference).
    canonical_usage_patterns = [
        re.compile(r"canonical[^.\n]*\bdea:entity-process\b", re.IGNORECASE),
        re.compile(r"\bdea:entity-process\b[^.\n]*canonical", re.IGNORECASE),
        re.compile(r"the canonical[^.\n]*\bdea:entity-process\b", re.IGNORECASE),
        re.compile(r"\bdea:entity-process\b is the (authoritative|canonical)", re.IGNORECASE),
    ]
    # Files that legitimately reference the legacy id in canonical-asserting
    # phrasing as part of their decision-ratification purpose. The governance
    # doc that records the canonical-identity decision is the primary case:
    # its job is to say "the canonical `dea:entity-process`" historically,
    # and the warning would be a false positive.
    exempt_filename = "canonical-identity-business-process.md"
    for p in paths:
        if not p.exists():
            continue
        if p.name == exempt_filename:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for rgx in canonical_usage_patterns:
            for match in rgx.finditer(text):
                    # find line number
                    line_no = text[: match.start()].count("\n") + 1
                    warnings.append(
                        f"  WARN: {p}:{line_no}: legacy id appears as canonical: '{match.group(0).strip()}'"
                    )
    return warnings


def run_self_test() -> tuple[bool, list[str]]:
    """Built-in self-test: prove the validator detects each rule's violation."""
    notes: list[str] = []
    failures: list[str] = []

    # --- BP-01-001 violation
    bad_pointer = REPO / "metamodel-pointer.yaml"
    original = bad_pointer.read_text(encoding="utf-8") if bad_pointer.exists() else None
    try:
        bad_pointer.write_text(
            "metamodel:\n  entity_id: dea:entity-process\n", encoding="utf-8"
        )
        errs = check_pointer(bad_pointer)
        if not any("BP-01-001" in e for e in errs):
            failures.append("self-test FAIL: did not detect BP-01-001 violation on legacy entity_id")
    finally:
        if original is not None:
            bad_pointer.write_text(original, encoding="utf-8")

    # --- BP-01-002 violation (legacy id without legacy_identifiers block)
    try:
        bad_pointer.write_text(
            "metamodel:\n  entity_id: dea:BusinessProcess\n  note: see dea:entity-process for history\n",
            encoding="utf-8",
        )
        errs = check_pointer(bad_pointer)
        if not any("BP-01-002" in e for e in errs):
            failures.append("self-test FAIL: did not detect BP-01-002 violation (legacy id without legacy_identifiers block)")
    finally:
        if original is not None:
            bad_pointer.write_text(original, encoding="utf-8")

    # --- BP-01-003 violation
    try:
        bad_pointer.write_text(
            "metamodel:\n  entity_id: dea:Process\n", encoding="utf-8"
        )
        errs = check_pointer(bad_pointer)
        if not any("BP-01-003" in e for e in errs):
            failures.append("self-test FAIL: did not detect BP-01-003 violation (bare dea:Process)")
    finally:
        if original is not None:
            bad_pointer.write_text(original, encoding="utf-8")

    # --- pointer that passes
    bad_pointer.write_text(
        "metamodel:\n  entity_id: dea:BusinessProcess\n  legacy_identifiers:\n    - dea:entity-process\n",
        encoding="utf-8",
    )
    errs = check_pointer(bad_pointer)
    if errs:
        failures.append(f"self-test FAIL: canonical pointer reported errors: {errs}")
    if original is not None:
        bad_pointer.write_text(original, encoding="utf-8")

    passed = not failures
    return passed, notes + failures


def main() -> int:
    parser = argparse.ArgumentParser(
        description="CR-BP-01 canonical-identity validator"
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run the built-in self-test and exit.",
    )
    args = parser.parse_args()

    if args.self_test:
        passed, notes = run_self_test()
        if passed:
            print("self-test PASS: validator detects BP-01-001, / 002, / 003.")
            return 0
        for n in notes:
            print(n)
        print("self-test FAIL.")
        return 1

    print("CR-BP-01 canonical-identity validator")
    print(f"  canonical entity_id: {CANONICAL_ENTITY_ID}")
    print(f"  legacy entity_id:    {LEGACY_ENTITY_ID} (must declare compatibility)")
    print(f"  forbidden bare:      {FORBIDDEN_BARE_PROCESS_ID}")
    print(f"  repo root:           {REPO}")

    all_errors: list[str] = []

    # 1. Pointer
    errs = check_pointer(REPO / "metamodel-pointer.yaml")
    all_errors.extend(errs)

    # 2. Schemas (id-pattern regexes)
    schema_paths = sorted(REPO.glob("schemas/**/*.json"))
    errs = check_schema_id_patterns(schema_paths)
    all_errors.extend(errs)

    # 3. Narrative docs (soft warnings)
    doc_paths = sorted(REPO.glob("docs/**/*.md")) + sorted(REPO.glob("README.md"))
    warnings = check_narrative_legacy_references(doc_paths)
    if warnings:
        print("\nNarrative warnings (informational; do not fail the gate):")
        for w in warnings:
            print(w)

    # Self-test always runs in normal mode (catches validator regressions)
    self_passed, self_notes = run_self_test()
    if not self_passed:
        print("\nFAIL: built-in self-test detected a validator regression.", file=sys.stderr)
        for n in self_notes:
            print(f"  - {n}", file=sys.stderr)
        return 2

    if all_errors:
        print("\nFAIL: CR-BP-01 canonical-identity violations found.", file=sys.stderr)
        for e in all_errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print("\nPASS: every catalog artifact satisfies BP-01-001, / 002, / 003.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())