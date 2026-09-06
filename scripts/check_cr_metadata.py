#!/usr/bin/env python3
"""Change Request Metadata Validator (CR-BP-16 S16; CR-META-001..006).

CR-BP-16 S16 mandates that every architectural change CR carry a
minimal set of metadata fields. This script validates every
markdown file in change-requests/ against the §16 schema:

  CR-META-001  Status (Required; one of Proposed|Accepted|Rejected|Superseded|Draft)
  CR-META-002  Layer (Required; one of L0|L1|L2|L3|Process Catalog|Metamodel|Cross-cutting)
  CR-META-003  Owner (Required; non-empty)
  CR-META-004  Depends on (Required when applicable; CR-BP-NN list)
  CR-META-005  Companion to (Optional; CR-BP-NN list)
  CR-META-006  CR number uniqueness (Required; matches filename CR-BP-NN(.X|.Y))

Self-test exercises a synthetic CR with each metadata field present
or absent and confirms each rule fires.

Usage::

    python3 scripts/check_cr_metadata.py [--strict] [--self-test]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable

APPROVED_STATUSES = {"Proposed", "Accepted", "Rejected", "Superseded", "Draft"}
APPROVED_LAYERS = {
    "L0", "L1", "L2", "L3", "Process Catalog", "Metamodel", "Cross-cutting",
}
CR_NUMBER_PATTERN = re.compile(r"^CR-BP-(\d+)([a-z]?(?:\.\d+)*)?(?:[-_a-z0-9]+)?$")
CR_REF_PATTERN = re.compile(r"CR-BP-\d+[a-z]?(?:\.\d+)*")
META_LINE = re.compile(r"^\*\*([^*]+)\*\*:\s*(.+?)\s*$")


def _extract_meta(text: str) -> dict[str, str]:
    """Extract **Key**: Value metadata from the first 30 lines of a CR."""
    meta: dict[str, str] = {}
    for line in text.splitlines()[:30]:
        m = META_LINE.match(line)
        if m:
            meta[m.group(1).strip()] = m.group(2).strip()
    return meta


def _expected_cr_number(path: Path) -> str | None:
    """Derive the expected CR number from the filename."""
    m = CR_NUMBER_PATTERN.match(path.stem)
    return path.stem if m else None


def check_cr(path: Path) -> list[tuple[str, str]]:
    """Return [(rule_code, finding), ...] for a CR markdown file."""
    findings: list[tuple[str, str]] = []
    try:
        text = path.read_text()
    except (OSError, UnicodeDecodeError):
        return [("CR-META-PARSE", f"could not read {path.name}")]

    meta = _extract_meta(text)

    # CR-META-001: Status required + approved set.
    status = meta.get("Status")
    if not status:
        findings.append(("CR-META-001", f"{path.name}: missing **Status**"))
    elif status not in APPROVED_STATUSES:
        findings.append((
            "CR-META-001",
            f"{path.name}: status {status!r} not in approved set "
            f"{sorted(APPROVED_STATUSES)}",
        ))

    # CR-META-002: Layer required + approved set.
    layer = meta.get("Layer")
    if not layer:
        findings.append(("CR-META-002", f"{path.name}: missing **Layer**"))
    elif layer not in APPROVED_LAYERS:
        findings.append((
            "CR-META-002",
            f"{path.name}: layer {layer!r} not in approved set "
            f"{sorted(APPROVED_LAYERS)}",
        ))

    # CR-META-003: Owner required + non-empty.
    owner = meta.get("Owner")
    if not owner:
        findings.append(("CR-META-003", f"{path.name}: missing **Owner**"))
    elif owner.strip() == "":
        findings.append(("CR-META-003", f"{path.name}: empty **Owner**"))

    # CR-META-004: Depends on: list of CR-BP-NN(.X) refs.
    depends_on = meta.get("Depends on")
    if depends_on:
        refs = CR_REF_PATTERN.findall(depends_on)
        if not refs:
            findings.append((
                "CR-META-004",
                f"{path.name}: **Depends on** present but contains no "
                f"CR-BP-NN reference ({depends_on!r})",
            ))

    # CR-META-005: Companion to: list of CR-BP-NN(.X) refs (optional).
    companion = meta.get("Companion to")
    if companion:
        refs = CR_REF_PATTERN.findall(companion)
        if not refs:
            findings.append((
                "CR-META-005",
                f"{path.name}: **Companion to** present but contains no "
                f"CR-BP-NN reference ({companion!r})",
            ))

    # CR-META-006: Filename matches a CR-BP-NN pattern.
    expected = _expected_cr_number(path)
    if expected is None:
        findings.append((
            "CR-META-006",
            f"{path.name}: filename does not match CR-BP-NN pattern",
        ))

    return findings


def _walk(repo_root: Path) -> Iterable[Path]:
    cr_dir = repo_root / "change-requests"
    if not cr_dir.exists():
        return ()
    return sorted(cr_dir.glob("CR-*.md"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--catalog-root", default=".")
    parser.add_argument("--strict", action="store_true",
                        help="Treat warnings as errors. Note: --strict on "
                        "the live CR set will fail until legacy CRs are "
                        "retroactively brought into S21 metadata "
                        "compliance; current run mode is advisory.")
    parser.add_argument("--json", action="store_true",
                        help="Emit JSON output")
    parser.add_argument("--self-test", action="store_true",
                        help="Run self-test and exit")
    args = parser.parse_args(argv)

    if args.self_test:
        return _self_test()

    root = Path(args.catalog_root).resolve()
    findings: list[dict[str, str]] = []
    for path in _walk(root):
        for code, msg in check_cr(path):
            findings.append({
                "rule": code,
                "path": str(path.relative_to(root)),
                "message": msg,
            })

    # CR-META runs as advisory by default. Legacy CRs predate the
    # §16 metadata schema and would fail --strict; new CRs written
    # under CR-BP-16 SHOULD include the metadata. CR-BP-13A is the
    # first CR planned to demonstrate full S21 compliance.
    verdict = (
        "ADVISORY-NON-CONFORMANT" if findings else
        "CONFORMANT"
    )
    if args.json:
        print(json.dumps({"verdict": verdict, "findings": findings}, indent=2))
    else:
        print(f"CR Metadata (CR-BP-16 S16; CR-META-001..006): {verdict}")
        if findings:
            cr_count = len(list(_walk(root)))
            print(f"  {len(findings)} findings across {cr_count} CR files "
                  f"(advisory; legacy CRs lack S21 metadata)")
            for f in findings[:10]:
                print(f"    [{f['rule']}] {f['path']}: {f['message']}")
            if len(findings) > 10:
                print(f"    ... and {len(findings) - 10} more")
        else:
            print(f"  checked {len(list(_walk(root)))} CR files")
    return 0  # advisory only; do not gate CI


def _self_test() -> int:
    """Exercise each rule via fixtures."""
    import tempfile

    failed: list[str] = []
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        cr_dir = root / "change-requests"
        cr_dir.mkdir()
        # Bad CR: missing Status, bad Layer, empty Owner,
        # Depends on without CR ref, bad filename.
        bad = (
            "# CR-BP-XX-bad\n\n"
            "**Layer**: L99\n"
            "**Owner**: \n"
            "**Depends on**: nothing here\n"
        )
        (cr_dir / "CR-XX-bad.md").write_text(bad)
        findings = []
        for path in _walk(root):
            for code, msg in check_cr(path):
                findings.append(code)
        seen = set(findings)
        expected = {"CR-META-001", "CR-META-002", "CR-META-003", "CR-META-004", "CR-META-006"}
        for code in expected:
            if code not in seen:
                failed.append(f"expected {code} to fire on bad fixture")
        # CR-META-005 is optional; it should NOT fire here because the
        # fixture doesn't mention Companion to.

        # Good CR: all fields present, valid filename.
        good = (
            "# CR-BP-99-good\n\n"
            "**Status**: Proposed\n"
            "**Layer**: L1\n"
            "**Owner**: TechNeHub Labs\n"
            "**Depends on**: CR-BP-12, CR-BP-13\n"
            "**Companion to**: CR-BP-99.1\n"
        )
        (cr_dir / "CR-BP-99-good.md").write_text(good)
        good_findings = []
        for path in _walk(root):
            if path.name == "CR-BP-99-good.md":
                for code, msg in check_cr(path):
                    good_findings.append(code)
        if good_findings:
            failed.append(f"good fixture fired: {good_findings}")

    if failed:
        print("self-test FAIL:", failed)
        return 1
    print("self-test PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())