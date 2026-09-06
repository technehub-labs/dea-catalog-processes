"""Tests for the CR-BP-15-IMP Phase 1 inventory + STRUCT conformance.

Locks behaviour for `scripts/build_inventory.py` (regenerates the
inventory + baseline deterministically) and `scripts/check_struct.py`
(guards the reconciliation scaffolding against typos).
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "scripts"


def _run(script: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / script), *args],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
    )


def test_build_inventory_self_test_strict_passes() -> None:
    """The inventory + baseline must round-trip byte-identically."""
    res = _run("build_inventory.py", "--self-test", "--strict")
    assert res.returncode == 0, res.stderr or res.stdout
    assert "PASS" in res.stdout


def test_build_inventory_outputs_exist() -> None:
    """The committed inventory + baseline files exist and are non-empty."""
    inv = REPO_ROOT / "reconciliation/inventory.yaml"
    base = REPO_ROOT / "reconciliation/baseline/v1.yaml"
    assert inv.exists() and inv.stat().st_size > 0
    assert base.exists() and base.stat().st_size > 0


def test_build_inventory_records_match_canonical_population() -> None:
    """Counts must match the 18 + 10 + 10 canonical population."""
    import yaml
    inv = yaml.safe_load(
        (REPO_ROOT / "reconciliation/inventory.yaml").read_text()
    )
    recs = inv["records"]
    assert len(recs["business_processes"]) == 18
    assert len(recs["process_groups"]) == 10
    assert len(recs["process_contexts"]) == 10


def test_build_inventory_legacy_findings_present() -> None:
    """The 14 unmigrated records carry the documented legacy findings;
    the 4 records migrated in CR-BP-15-IMP Phase 5 (cd-b + cd-c) do not.

    This test reflects the current reconciliation state and will be
    progressively relaxed as further tranches land (Phase 5 -> Phase 7).
    """
    import yaml
    inv = yaml.safe_load(
        (REPO_ROOT / "reconciliation/inventory.yaml").read_text()
    )
    procs = inv["records"]["business_processes"]
    with_audience = sum(1 for p in procs
                        if any(f.startswith("audience:") for f in p["legacy_findings"]))
    with_ctx_scalar = sum(1 for p in procs
                          if "ctx-scalar" in p["legacy_findings"])
    with_no_context = sum(1 for p in procs
                          if "no-context-block" in p["legacy_findings"])
    # Phase 5 first tranche (cd-b + cd-c, PR-33): -4 records
    # Phase 5 second tranche (cd-d + cd-im + cd-op, PR-7): -5 records
    # 18 - 4 - 5 = 9 records still carry the legacy fields.
    assert with_audience == 9
    assert with_ctx_scalar == 9
    assert with_no_context == 9


def test_baseline_has_sha256_for_every_record() -> None:
    """Every entry in the baseline must have a sha256."""
    import yaml
    base = yaml.safe_load(
        (REPO_ROOT / "reconciliation/baseline/v1.yaml").read_text()
    )
    assert base["baseline_version"] == "v1"
    for entry in base["records"]:
        assert "sha256" in entry
        assert len(entry["sha256"]) == 64


def test_baseline_sha256_matches_actual_files() -> None:
    """The SHA-256 entries must match the on-disk bytes."""
    import hashlib
    import yaml
    base = yaml.safe_load(
        (REPO_ROOT / "reconciliation/baseline/v1.yaml").read_text()
    )
    for entry in base["records"]:
        path = REPO_ROOT / entry["path"]
        if not path.exists():
            # CR file may not exist on this checkout (e.g. archived CRs)
            pytest.skip(f"missing on disk: {entry['path']}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        assert actual == entry["sha256"], entry["path"]


def test_check_struct_self_test_passes() -> None:
    res = _run("check_struct.py", "--self-test")
    assert res.returncode == 0, res.stderr or res.stdout
    assert "PASS" in res.stdout


def test_check_struct_clean_repo_passes() -> None:
    """When run on a recognised repo root, only tolerated extras appear."""
    res = _run("check_struct.py")
    # We expect warnings (the reconciliation/ and 01_plan/ scratch dirs),
    # not failures, on a normal checkout.
    assert res.returncode == 0, res.stderr
    assert "STRUCT-OK" in res.stderr


def test_check_struct_strict_fails_on_typo(tmp_path: Path) -> None:
    """A misspelt top-level entry must be caught."""
    bad_name = "reconcilliation"  # common typo of "reconciliation"
    (tmp_path / bad_name).mkdir()
    for known in ["reconciliation", "entities", "contexts", ".github",
                  "README.md", "CHANGELOG.md", "CATALOG.yaml"]:
        if known.startswith("."):
            (tmp_path / known).mkdir(parents=True, exist_ok=True)
        elif "." in known:
            (tmp_path / known).write_text("")
        else:
            (tmp_path / known).mkdir(parents=True, exist_ok=True)
    res = subprocess.run(
        [sys.executable, str(SCRIPTS / "check_struct.py"),
         "--strict", "--root", str(tmp_path)],
        capture_output=True, text=True,
    )
    assert res.returncode != 0
    assert "reconcilliation" in res.stderr
