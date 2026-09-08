#!/usr/bin/env python3
"""apply_register_audit.py: Apply CR-BP-22 audit_status to the v2 register.

For every coordinate in `entities/v1-alpha/dea:group-customer-lifecycle-management/research/l1-register.yaml`,
compute audit_status from the catalog reality (canonical L1 records) and
write it back. Also bump ratification.version to 3 and add audit_counts.

Idempotent: re-running is a no-op once audit_status is filled.

Run: python scripts/apply_register_audit.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
ENTITIES_DIR = REPO_ROOT / "entities/v1-alpha"
REGISTER_PATH = ENTITIES_DIR / "dea:group-customer-lifecycle-management/research/l1-register.yaml"
UNIVERSE_PATH = ENTITIES_DIR / "dea:group-customer-lifecycle-management/research/l1-candidate-universe.yaml"

DOMAIN_ABBR = {
    "ge": "GovernanceAndExistence",
    "sd": "StrategyAndDirection",
    "ao": "AgencyAndOrganization",
    "pr": "PartyAndRelationship",
    "pv": "ProductAndValue",
    "oe": "EnablementAndOperations",
    "fa": "FinanceAndAccounting",
}


def _parse_stage(s: str) -> str:
    if s in ("c", "conceive"): return "Conceive"
    if s in ("d", "design"): return "Design"
    if s in ("b", "build"): return "Build"
    if s in ("a", "activate"): return "Activate"
    if s in ("o", "op", "operate"): return "Operate"
    if s in ("im", "i", "improve"): return "Improve"
    if s in ("r", "retire"): return "Retire"
    return s


def _collect_landed() -> dict[tuple[str, str], list[str]]:
    landed: dict[tuple[str, str], list[str]] = {}
    for entry in sorted(ENTITIES_DIR.iterdir()):
        if not entry.name.startswith("dea:group-"):
            continue
        fpath = entry / f"{entry.name}.yaml"
        if not fpath.exists():
            continue
        with fpath.open() as f:
            doc = yaml.safe_load(f)
        pc = doc.get("process_context", "")
        m = re.match(r"dea:pc-([a-z]+)-(.+)", pc)
        if not m: continue
        dom = DOMAIN_ABBR.get(m.group(1), "?")
        st = _parse_stage(m.group(2))
        landed.setdefault((dom, st), []).append(entry.name)
    return landed


def _expected_audit(disposition: str, landed_count: int) -> str:
    if disposition == "ratified-accepted":
        return "landed" if landed_count >= 1 else "ratified-pending-landing"
    if disposition == "backlog-deferred":
        return "backlog-deferred"
    return disposition


def apply_register(dry_run: bool = False) -> tuple[int, int, int, int]:
    landed = _collect_landed()
    with REGISTER_PATH.open() as f:
        reg = yaml.safe_load(f)

    counts = {"landed": 0, "ratified-pending-landing": 0, "backlog-deferred": 0}
    changes = 0

    for dom, stages in reg["register"].items():
        for st, payload in stages.items():
            disposition = payload.get("disposition", "?")
            landed_count = len(landed.get((dom, st), []))
            expected = _expected_audit(disposition, landed_count)
            counts[expected] += 1
            actual = payload.get("audit_status")
            if actual != expected:
                payload["audit_status"] = expected
                # Add tranche pointer for pending cells
                if expected == "ratified-pending-landing":
                    dom_to_tranche = {
                        "StrategyAndDirection": "CR-BP-21a.1",
                        "AgencyAndOrganization": "CR-BP-21b.1",
                        "ProductAndValue": "CR-BP-21c",
                        "EnablementAndOperations": "CR-BP-21d",
                        "FinanceAndAccounting": "CR-BP-21e",
                    }
                    payload["planned_tranche"] = dom_to_tranche.get(dom, "TBD")
                    payload["planned_at"] = "2026-09-08"
                changes += 1

    # Update ratification block
    rat = reg.setdefault("ratification", {})
    if rat.get("version") != 3:
        rat["version"] = 3
        rat["cr"] = "CR-BP-22"
        rat["ratified_at"] = "2026-09-08"
        rat["supersedes"] = "version 2 (CR-BP-19, ratified 2026-09-07)"
        changes += 1

    # Add audit_counts
    reg["audit_counts"] = {
        "landed": counts["landed"],
        "ratified-pending-landing": counts["ratified-pending-landing"],
        "backlog-deferred": counts["backlog-deferred"],
        "total": sum(counts.values()),
        "audit_cr": "CR-BP-22",
        "audited_at": "2026-09-08",
    }
    changes += 1

    if not dry_run:
        with REGISTER_PATH.open("w") as f:
            yaml.safe_dump(reg, f, sort_keys=False, default_flow_style=False, width=120)

    return counts["landed"], counts["ratified-pending-landing"], counts["backlog-deferred"], changes


def apply_universe(dry_run: bool = False) -> int:
    landed = _collect_landed()
    with UNIVERSE_PATH.open() as f:
        uni = yaml.safe_load(f)

    changes = 0
    # Inherit audit_status from the coordinate (default)
    for cand in uni.get("l1_candidates", []):
        dom = cand.get("domain")
        stage = cand.get("stage")
        disposition = cand.get("disposition", "?")
        landed_count = len(landed.get((dom, stage), []))
        expected = _expected_audit(disposition, landed_count)
        actual = cand.get("audit_status")
        if actual != expected:
            cand["audit_status"] = expected
            changes += 1

    # Update ratification block
    rat = uni.setdefault("ratification", {})
    if rat.get("version") != 3:
        rat["version"] = 3
        rat["cr"] = "CR-BP-22"
        rat["ratified_at"] = "2026-09-08"
        rat["supersedes"] = "version 2 (CR-BP-19, ratified 2026-09-07)"
        changes += 1

    if not dry_run:
        with UNIVERSE_PATH.open("w") as f:
            yaml.safe_dump(uni, f, sort_keys=False, default_flow_style=False, width=120)

    return changes


def main() -> int:
    print("Applying CR-BP-22 audit_status to register v2...")
    l, p, d, chg = apply_register(dry_run=False)
    print(f"  Register: landed={l} pending={p} deferred={d} total={l+p+d} changes={chg}")
    print("Applying CR-BP-22 audit_status to L1 candidate universe...")
    uchg = apply_universe(dry_run=False)
    print(f"  Universe: changes={uchg}")
    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())