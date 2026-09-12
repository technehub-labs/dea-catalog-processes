"""Tests for the CR-BP-37 Cross-Repository Integrity validator.

Locks behaviour for XRI-001..005 by exercising both the in-process
`evaluate()` function and the CLI self-test entry point, plus a
live-catalog assertion that the catalog currently emits zero
findings (the pointer and README Cross-repo context are in good
standing).

The tests cover:

* XRI-001  metamodel-pointer.yaml structure (top-level keys present)
* XRI-002  entity entry completeness (kernel vs opt-in role checks)
* XRI-003  federation mapping + canonical CR lineage references
* XRI-004  entity_id uniqueness across metamodel.entities[]
* XRI-005  companion CR lineage references in README resolve
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "check_cross_repo_integrity.py"

sys.path.insert(0, str(ROOT / "scripts"))
from check_cross_repo_integrity import (  # noqa: E402
    CANONICAL_LINEAGE_CRS,
    COMPANION_CRS,
    _check_xri_001,
    _check_xri_002,
    _check_xri_003,
    _check_xri_004,
    _check_xri_005,
    evaluate,
)


def _run(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        check=False,
        capture_output=True,
        text=True,
    )


# -----------------------------------------------------------------------------
# CLI-level tests
# -----------------------------------------------------------------------------


def test_cli_self_test_passes():
    result = _run(["--self-test"])
    assert result.returncode == 0, result.stdout + result.stderr
    assert "self-test PASS" in result.stdout


def test_cli_live_run_returns_conformant():
    """Live run: 0 findings (pointer and README in good standing)."""
    result = _run([])
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Cross-Repository Integrity (CR-BP-37; XRI-001..005): CONFORMANT" in result.stdout
    assert "Findings: 0" in result.stdout


def test_cli_json_shape():
    result = _run(["--json"])
    assert result.returncode == 0, result.stdout + result.stderr
    data = json.loads(result.stdout)
    assert data["verdict"] == "CONFORMANT"
    assert data["finding_count"] == 0
    rule_ids = {r["id"] for r in data["rules"]}
    assert "XRI-001" in rule_ids
    assert "XRI-005" in rule_ids
    assert set(data["canonical_lineage"]) == set(CANONICAL_LINEAGE_CRS)
    assert data["companion_crs_count"] == len(COMPANION_CRS)


# -----------------------------------------------------------------------------
# Rule-level tests
# -----------------------------------------------------------------------------


def test_xri_001_missing_pointer(tmp_path):
    findings = _check_xri_001(None)
    assert any("missing" in f for f in findings)


def test_xri_001_no_metamodel_block(tmp_path):
    findings = _check_xri_001({"catalog": {}})
    assert any("metamodel" in f for f in findings)


def test_xri_001_no_entities():
    findings = _check_xri_001({
        "metamodel": {"entity_id": "dea:entity-business-process",
                     "class_alias": "BP", "layer": "L3"},
        "catalog": {},
    })
    assert any("entities" in f for f in findings)


def test_xri_001_valid_pointer():
    findings = _check_xri_001({
        "metamodel": {"version": "v0.6.0",
                     "entity_id": "dea:entity-business-process",
                     "class_alias": "BP", "layer": "L3",
                     "entities": [{"entity_id": "dea:entity-process"}]},
        "catalog": {"name": "X", "repo": "x/y"},
    })
    assert findings == []


def test_xri_002_kernel_missing_class_alias():
    findings = _check_xri_002({
        "metamodel": {"entities": [
            {"entity_id": "dea:entity-process",
             "discriminator": "process-kernel"},
        ]},
    })
    assert any("class_alias" in f for f in findings)


def test_xri_002_kernel_missing_discriminator():
    findings = _check_xri_002({
        "metamodel": {"entities": [
            {"entity_id": "dea:entity-process", "class_alias": "PRC"},
        ]},
    })
    assert any("discriminator" in f for f in findings)


def test_xri_002_opt_in_valid():
    findings = _check_xri_002({
        "metamodel": {"entities": [
            {"entity_id": "dea:Activity", "lifecycle": "proposed"},
        ]},
    })
    assert findings == []


def test_xri_002_opt_in_invalid_lifecycle():
    findings = _check_xri_002({
        "metamodel": {"entities": [
            {"entity_id": "dea:Activity", "lifecycle": "weird"},
        ]},
    })
    assert any("weird" in f for f in findings)


def test_xri_002_missing_entity_id():
    findings = _check_xri_002({
        "metamodel": {"entities": [{}]},
    })
    assert any("entity_id" in f for f in findings)


def test_xri_003_empty_pointer():
    """Empty pointer text yields 0 XRI-003 findings (XRI-001 covers absence)."""
    findings = _check_xri_003("")
    assert findings == []


def test_xri_003_missing_federation_mapping():
    findings = _check_xri_003("# no federation mapping here\n")
    assert any("federation" in f.lower() for f in findings)


def test_xri_003_missing_canonical_cr():
    findings = _check_xri_003(
        "# 1:1 LOSSLESS mapping\n"
        "dea:Process <-> dea:entity-process\n"
        "dea:BusinessProcess <-> dea:entity-business-process\n"
    )
    assert any("CR-MM-PROC-01" in f for f in findings)


def test_xri_003_complete_pointer():
    findings = _check_xri_003(
        "# CR-MM-PROC-01; CR-AR-FMWK-01\n"
        "# 1:1 LOSSLESS mapping:\n"
        "#   dea:Process <-> dea:entity-process\n"
        "#   dea:BusinessProcess <-> dea:entity-business-process\n"
    )
    assert findings == []


def test_xri_004_unique_entities():
    findings = _check_xri_004({
        "metamodel": {"entities": [
            {"entity_id": "dea:entity-process",
             "class_alias": "PRC", "discriminator": "process-kernel"},
            {"entity_id": "dea:Workflow", "lifecycle": "proposed"},
        ]},
    })
    assert findings == []


def test_xri_004_duplicate_entity_id():
    findings = _check_xri_004({
        "metamodel": {"entities": [
            {"entity_id": "dea:entity-process",
             "class_alias": "PRC", "discriminator": "process-kernel"},
            {"entity_id": "dea:entity-process",
             "class_alias": "PRC2", "discriminator": "pk2"},
        ]},
    })
    assert any("duplicates" in f for f in findings)


def test_xri_005_no_readme(tmp_path):
    findings = _check_xri_005(tmp_path)
    assert findings == []


def test_xri_005_no_cross_repo_section(tmp_path):
    cr_dir = tmp_path / "change-requests"
    cr_dir.mkdir()
    (cr_dir / "README.md").write_text("# CRs\n")
    findings = _check_xri_005(tmp_path)
    assert findings == []


def test_xri_005_unknown_companion_cr(tmp_path):
    cr_dir = tmp_path / "change-requests"
    cr_dir.mkdir()
    (cr_dir / "README.md").write_text(
        "# CRs\n\n## Cross-repo context\n"
        "CG-007 lives somewhere.\n"
    )
    findings = _check_xri_005(tmp_path)
    assert any("CG-007" in f for f in findings)


def test_xri_005_known_companion_cr(tmp_path):
    cr_dir = tmp_path / "change-requests"
    cr_dir.mkdir()
    (cr_dir / "README.md").write_text(
        "# CRs\n\n## Cross-repo context\n"
        "CR-MM-PROC-01 lands in dea-metamodel.\n"
        "CG-001 lands in dea-metaframework.\n"
    )
    findings = _check_xri_005(tmp_path)
    assert findings == []


def test_xri_005_local_companion_cr_file(tmp_path):
    cr_dir = tmp_path / "change-requests"
    cr_dir.mkdir()
    (cr_dir / "README.md").write_text(
        "# CRs\n\n## Cross-repo context\n"
        "CR-MM-PROC-01 lands in dea-metamodel.\n"
        "CR-LOCAL-99 lands here.\n"
    )
    (cr_dir / "CR-LOCAL-99.md").write_text("# Local CR\n")
    findings = _check_xri_005(tmp_path)
    assert findings == []
