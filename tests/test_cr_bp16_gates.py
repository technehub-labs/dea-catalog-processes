"""Tests for the CR metadata validator (CR-BP-16 S16; CR-META-001..006),
documentation conformance checker (CR-BP-16 S22; DOC-001..003),
and admission gate (CR-BP-16 S15; ADM-001..008).
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT_CR_META = ROOT / "scripts" / "check_cr_metadata.py"
SCRIPT_DOC = ROOT / "scripts" / "check_documentation_conformance.py"
SCRIPT_ADM = ROOT / "scripts" / "check_admission_gate.py"


def _run(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, *args], capture_output=True, text=True, cwd=str(ROOT),
    )


# CR metadata


def test_cr_meta_self_test_passes():
    r = _run([str(SCRIPT_CR_META), "--self-test"])
    assert r.returncode == 0, r.stdout + r.stderr
    assert "self-test PASS" in r.stdout


def test_cr_meta_runs_advisory_on_live():
    """Live run is advisory (returns 0) and surfaces findings for
    legacy CRs without S21 metadata."""
    r = _run([str(SCRIPT_CR_META)])
    assert r.returncode == 0, r.stdout + r.stderr
    # CR-BP-13A is the §21 reference and should not appear in findings.
    assert "CR-BP-13a" not in r.stdout or "0 findings" in r.stdout


def test_cr_meta_strict_passes_when_no_new_failures():
    """--strict returns 0 when no NEW CR (mtime >= cutoff) fails."""
    r = _run([str(SCRIPT_CR_META), "--strict"])
    # After PR-13, all touched-in-this-session CRs have S21 metadata
    # and pass. Legacy CRs are advisory. So returncode MUST be 0.
    assert r.returncode == 0, r.stdout + r.stderr
    # The verdict should be ADVISORY-LEGACY or CONFORMANT
    assert any(s in r.stdout for s in ("ADVISORY-LEGACY", "CONFORMANT"))


def test_cr_meta_strict_fails_on_new_bad_fixture(tmp_path):
    """A new CR file (touch -d "now") without S21 metadata must
    fail --strict."""
    import os
    from datetime import datetime, timezone
    sandbox = tmp_path / "sandbox"
    cr_dir = sandbox / "change-requests"
    cr_dir.mkdir(parents=True)
    bad = (
        "# CR-BP-XX-bad\n\n"
        "Some prose, no metadata.\n"
    )
    p = cr_dir / "CR-XX-bad.md"
    p.write_text(bad)
    # Set mtime to 2099-01-01 to ensure the file is "new" by the cutoff
    future = datetime(2099, 1, 1, tzinfo=timezone.utc).timestamp()
    os.utime(p, (future, future))
    r = _run([str(SCRIPT_CR_META), "--strict", "--catalog-root", str(sandbox)])
    assert r.returncode != 0, r.stdout + r.stderr
    assert "NON-CONFORMANT" in r.stdout


def test_cr_meta_strict_passes_on_legacy_bad_fixture(tmp_path):
    """A legacy CR file (mtime < cutoff) without S21 metadata must
    pass --strict (advisory only)."""
    import os
    from datetime import datetime, timezone
    sandbox = tmp_path / "sandbox"
    cr_dir = sandbox / "change-requests"
    cr_dir.mkdir(parents=True)
    bad = (
        "# CR-BP-YY-bad\n\n"
        "Some prose, no metadata.\n"
    )
    p = cr_dir / "CR-YY-bad.md"
    p.write_text(bad)
    # Set mtime to 2000-01-01 (way before any cutoff)
    past = datetime(2000, 1, 1, tzinfo=timezone.utc).timestamp()
    os.utime(p, (past, past))
    r = _run([str(SCRIPT_CR_META), "--strict", "--catalog-root", str(sandbox)])
    assert r.returncode == 0, r.stdout + r.stderr
    assert "ADVISORY-LEGACY" in r.stdout


def test_cr_meta_accepts_layer_with_parenthetical_qualifier():
    """`L1 (Process Catalog)` MUST be accepted as a valid Layer."""
    r = _run([str(SCRIPT_CR_META), "--json"])
    import json
    data = json.loads(r.stdout)
    # CR-BP-13A uses L1 (Process Catalog). Should NOT have CR-META-002.
    rule_002_new = [f for f in data["new_findings"]
                    if f["rule"] == "CR-META-002" and "13a" in f["path"]]
    assert not rule_002_new, (
        "Layer 'L1 (Process Catalog)' should be accepted (normalized to L1)"
    )


def test_cr_meta_accepts_status_with_date_qualifier():
    """`Proposed (2026-09-03)` MUST be accepted as a valid Status."""
    r = _run([str(SCRIPT_CR_META), "--json"])
    import json
    data = json.loads(r.stdout)
    # CR-BP-03C uses Proposed (2026-09-03). Should NOT have CR-META-001
    # due to status (only due to legacy or some other rule).
    rule_001_new = [f for f in data["new_findings"]
                    if f["rule"] == "CR-META-001" and "03C" in f["path"]]
    assert not rule_001_new, (
        "Status 'Proposed (2026-09-03)' should be accepted "
        "(normalized to Proposed)"
    )


def test_cr_meta_json_shape():
    r = _run([str(SCRIPT_CR_META), "--json"])
    assert r.returncode == 0, r.stdout + r.stderr
    import json
    data = json.loads(r.stdout)
    assert "verdict" in data
    assert "findings" in data


def test_cr_meta_detects_missing_metadata(tmp_path):
    """A bad CR fixture triggers CR-META-001..004 + 006."""
    sandbox = tmp_path / "sandbox"
    sandbox.mkdir()
    cr_dir = sandbox / "change-requests"
    cr_dir.mkdir()
    bad = (
        "# CR-BP-XX-bad\n\n"
        "**Layer**: L99\n"
        "**Owner**: \n"
        "**Depends on**: nothing here\n"
    )
    (cr_dir / "CR-XX-bad.md").write_text(bad)
    r = _run([str(SCRIPT_CR_META), "--catalog-root", str(sandbox), "--json"])
    import json
    data = json.loads(r.stdout)
    rules = {f["rule"] for f in data["findings"]}
    for code in ("CR-META-001", "CR-META-002", "CR-META-003", "CR-META-004", "CR-META-006"):
        assert code in rules, f"expected {code} to fire"


# Documentation conformance


def test_doc_self_test_passes():
    r = _run([str(SCRIPT_DOC), "--self-test"])
    assert r.returncode == 0, r.stdout + r.stderr
    assert "self-test PASS" in r.stdout


def test_doc_runs_on_live():
    r = _run([str(SCRIPT_DOC)])
    assert r.returncode == 0, r.stdout + r.stderr


def test_doc_json_shape():
    r = _run([str(SCRIPT_DOC), "--json"])
    import json
    data = json.loads(r.stdout)
    assert "verdict" in data
    assert "findings" in data


# Admission gate


def test_adm_self_test_passes():
    r = _run([str(SCRIPT_ADM), "--self-test"])
    assert r.returncode == 0, r.stdout + r.stderr
    assert "self-test PASS" in r.stdout


def test_adm_live_runs_against_locked_records():
    """On the locked population, all 18 canonical BPs are checked.
    Some legacy fields (triggers, outcomes) MAY produce findings;
    that's expected (advisory mode)."""
    r = _run([str(SCRIPT_ADM)])
    assert r.returncode == 0, r.stdout + r.stderr


def test_adm_strict_fails_on_bad_fixture(tmp_path):
    """A candidate with missing required fields MUST fail --strict."""
    sandbox = tmp_path / "sandbox"
    shutil.copytree(ROOT / "entities", sandbox / "entities")
    shutil.copytree(ROOT / "contexts", sandbox / "contexts")
    bad_dir = sandbox / "entities" / "v1-alpha" / "dea:process-bad-candidate"
    bad_dir.mkdir()
    (bad_dir / "dea:process-bad-candidate.yaml").write_text(
        "id: dea:process-bad-candidate\n"
        "name: Bad\n"
        "type: Process\n"
        "version: '1.0.0'\n"
        "process_intent: harmonise\n"  # bad intent
        "process_type: core\n"
        "context: [{ref: dea:pc-unknown}]\n"  # unresolved
        "change_history: []\n"  # empty
    )
    r = _run([str(SCRIPT_ADM), "--strict", "--catalog-root", str(sandbox)])
    assert r.returncode != 0, r.stdout + r.stderr
    assert "ADM-003" in r.stdout or "ADM-006" in r.stdout or "ADM-008" in r.stdout


def test_adm_json_shape():
    r = _run([str(SCRIPT_ADM), "--json"])
    import json
    data = json.loads(r.stdout)
    assert "verdict" in data
    assert "findings" in data
    assert "candidate_count" in data
    assert data["candidate_count"] == 18  # 18 canonical BPs