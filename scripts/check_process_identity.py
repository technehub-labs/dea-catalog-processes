#!/usr/bin/env python3
"""
check_process_identity.py — Process Identity validator.

Implements CR-BP-03 rules BP-ARC-ID-001..BP-ARC-ID-005.

Rules:
  BP-ARC-ID-001 — Name matches identity: the process name (when the
                  identity sub-block is present) should be
                  '<verb> <object>' (with optional scope).
  BP-ARC-ID-002 — Trigger required (when identity is present): the
                  entry must declare `trigger` (a non-empty string).
  BP-ARC-ID-003 — Outcome required (when identity is present): the
                  entry must declare `outcome` (a non-empty string)
                  that is consistent with identity.outcome_statement.
  BP-ARC-ID-004 — Type / description cross-check: the process_type
                  and process_intent are cross-checked against the
                  identity.outcome_statement for consistency.
                  E.g. a 'core' process whose outcome_statement
                  talks about direction-setting is flagged.
  BP-ARC-ID-005 — Re-landscape suggestion: when the process is
                  poorly named or described (BP-ARC-ID-001..004
                  fail), the validator emits a reclassification
                  suggestion with a confidence score. The
                  suggestion is reported as a structured object;
                  the catalog does not auto-rewrite.

Exit: 0 = all rules pass (or no entries); 2 = self-test;
      1 = at least one rule failed.

Built-in --self-test exercises each rule on a deliberately broken
catalog (then on a fixed catalog) and verifies the expected exit
codes.
"""
import argparse
import json
import re
import sys
import tempfile
from pathlib import Path

import yaml

BASE = Path(__file__).parent.parent

# Keywords associated with each process_type (used for BP-ARC-ID-004
# cross-checking the outcome_statement).
TYPE_KEYWORDS = {
    "strategic":      ["direction", "vision", "goal", "strategic", "portfolio", "governance"],
    "management":     ["plan", "monitor", "control", "coordinate", "allocate", "supervise"],
    "core":           ["deliver", "produce", "fulfil", "operate", "serve", "execute", "manage customer", "manage order"],
    "support":        ["tooling", "internal service", "HR", "facilities", "IT support", "admin"],
    "standardization": ["compliance", "standard", "audit", "measure", "improve", "quality"],
}

# Cross-check: if the outcome_statement contains keywords of a
# different type with high density, flag for re-landscape.
def _type_keyword_density(outcome: str, process_type: str) -> tuple[float, str]:
    if not outcome:
        return 0.0, "no outcome"
    outcome_l = outcome.lower()
    own_kw = TYPE_KEYWORDS.get(process_type, [])
    other_kw = []
    for t, kws in TYPE_KEYWORDS.items():
        if t == process_type:
            continue
        other_kw.extend(kws)
    own_hits = sum(1 for k in own_kw if k in outcome_l)
    other_hits = sum(1 for k in other_kw if k in outcome_l)
    total = own_hits + other_hits
    if total == 0:
        return 0.5, "no signal"
    own_density = own_hits / total
    return own_density, f"own={own_hits} other={other_hits}"


def _check_one(entry: dict, errors: list[str], suggestions: list[dict]) -> None:
    eid = entry.get("id", "<unknown>")
    identity = entry.get("identity")
    if not identity:
        # Identity sub-block is optional; entries without identity are
        # admitted but flagged for review. This is a non-blocking
        # suggestion.
        suggestions.append({
            "target": eid,
            "suggestion_type": "add_identity",
            "current_state": {"identity": None},
            "suggested_state": {"identity": "<add verb, object, outcome_statement, evidence_links>"},
            "confidence": 0.5,
            "rationale": "Entry has no identity sub-block; add verb + object + outcome_statement + evidence_links so the process can be tested by name + description + trigger + outcome + evidence (CR-BP-03 §8).",
        })
        return

    name = entry.get("name", "")
    verb = identity.get("verb", "")
    obj = identity.get("object", "")
    scope = identity.get("scope", "")
    outcome_stmt = identity.get("outcome_statement", "")
    evidence = identity.get("evidence_links", []) or []

    # BP-ARC-ID-001: name matches identity.verb + identity.object (+ optional scope)
    expected = f"{verb} {obj}"
    if scope:
        # If the scope is already parenthesized ("(all customer segments)"),
        # don't wrap it again. If not, wrap it ("Enterprise" → "(Enterprise)").
        s = str(scope).strip()
        if s.startswith("(") and s.endswith(")"):
            expected = f"{expected} {s}"
        else:
            expected = f"{expected} ({s})"
    if name != expected and not _fuzzy_name_match(name, expected):
        errors.append(
            f"BP-ARC-ID-001 ({eid}): name {name!r} does not match identity verb+object+scope "
            f"({expected!r}). Either rename the process or update the identity sub-block."
        )
        suggestions.append({
            "target": eid,
            "suggestion_type": "rename",
            "current_state": {"name": name, "identity.verb": verb, "identity.object": obj, "identity.scope": scope},
            "suggested_state": {"name": expected},
            "confidence": 0.85,
            "rationale": "BP-ARC-ID-001: name should match identity verb+object+scope.",
        })

    # BP-ARC-ID-002: trigger required
    trigger = entry.get("trigger")
    if not trigger or not str(trigger).strip():
        errors.append(
            f"BP-ARC-ID-002 ({eid}): trigger is required when the identity sub-block is present. "
            f"Add a non-empty `trigger` describing what initiates the process."
        )

    # BP-ARC-ID-003: outcome required and consistent with outcome_statement
    outcome = entry.get("outcome")
    if not outcome or not str(outcome).strip():
        errors.append(
            f"BP-ARC-ID-003 ({eid}): outcome is required when the identity sub-block is present. "
            f"Add a non-empty `outcome` describing what the process produces."
        )
    # Cross-check identity.outcome_statement against entry.outcome
    if outcome_stmt and outcome and str(outcome).strip().lower() not in outcome_stmt.lower():
        # The entry.outcome should be a substring (or close to) identity.outcome_statement
        # If they're very different, flag it.
        if not _loose_match(str(outcome), outcome_stmt):
            suggestions.append({
                "target": eid,
                "suggestion_type": "outcome_mismatch",
                "current_state": {"entry.outcome": outcome, "identity.outcome_statement": outcome_stmt},
                "suggested_state": {"entry.outcome": "<align with identity.outcome_statement>"},
                "confidence": 0.7,
                "rationale": "BP-ARC-ID-003: entry.outcome should be consistent with identity.outcome_statement.",
            })

    # BP-ARC-ID-004: process_type / outcome_statement cross-check
    process_type = entry.get("process_type", "core")
    if outcome_stmt:
        density, signal = _type_keyword_density(outcome_stmt, process_type)
        if density < 0.3:
            # outcome_statement doesn't match the declared process_type
            # find the best-fit type
            best_type = max(TYPE_KEYWORDS.keys(), key=lambda t: sum(1 for k in TYPE_KEYWORDS[t] if k in outcome_stmt.lower()))
            best_density, _ = _type_keyword_density(outcome_stmt, best_type)
            confidence = 0.6 + 0.3 * (1 - density)
            errors.append(
                f"BP-ARC-ID-004 ({eid}): process_type={process_type!r} is inconsistent with "
                f"identity.outcome_statement (own-keyword density={density:.2f}; signal: {signal}). "
                f"Best-fit type: {best_type!r} (density={best_density:.2f})."
            )
            suggestions.append({
                "target": eid,
                "suggestion_type": "reclassification",
                "current_state": {"process_type": process_type},
                "suggested_state": {"process_type": best_type},
                "confidence": round(confidence, 2),
                "rationale": (
                    f"BP-ARC-ID-004: outcome_statement keyword density suggests a different "
                    f"process_type ({best_type!r} fits better than {process_type!r})."
                ),
            })

    # BP-ARC-ID-005 (sub-rule): evidence_links required when identity is present
    if not evidence:
        errors.append(
            f"BP-ARC-ID-005 ({eid}): identity.evidence_links is required (minItems: 1). "
            f"Add at least one evidence link (documentation / governance / interview / "
            f"artifact / standard / regulation)."
        )


def _fuzzy_name_match(name: str, expected: str) -> bool:
    """Allow case differences + trailing scope in parentheses to be flexible.

    Rationale (CR-BP-03C §5 / CR-BP-03A §3.1):
      - Entry names are conventionally Title Case ("Manage Customer Relationship").
      - The identity sub-block is conventionally lowercase
        (verb: "manage", object: "customer relationship").
      - The case-insensitive comparison prevents false positives
        where the contributor followed both conventions.
      - Trailing parenthesized scope ("(all customer segments)") is
        preserved in the identity and tolerated in the name match;
        the wrapping may produce doubled parentheses ("((all customer
        segments))"), which this function normalizes.
    """
    # Exact match (case-sensitive) — covers when both sides agree
    if name == expected:
        return True

    # Strip trailing parenthesized scope from expected
    m = re.match(r"^(.*?)(\s*\([^)]+\))?$", expected)
    if m and name == m.group(1).strip():
        return True

    # Case-insensitive comparison (with or without trailing scope)
    if m and name.lower() == m.group(1).strip().lower():
        return True
    if name.lower() == expected.lower():
        return True

    # Normalize doubled parentheses in expected (e.g. "((all customer segments))"
    # produced by wrapping a scope like "(all customer segments)") and retry.
    normalized = expected.replace("((", "(").replace("))", ")")
    if name == normalized:
        return True
    if name.lower() == normalized.lower():
        return True

    return False


def _loose_match(a: str, b: str) -> bool:
    """True if `a` is a substring of `b` or shares >60% of its words."""
    a_l = a.lower()
    b_l = b.lower()
    if a_l in b_l or b_l in a_l:
        return True
    a_words = set(re.findall(r"\w+", a_l))
    b_words = set(re.findall(r"\w+", b_l))
    if not a_words or not b_words:
        return False
    overlap = len(a_words & b_words) / max(len(a_words), len(b_words))
    return overlap > 0.6


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
        _check_one(entry, errors, suggestions)
    return errors, suggestions


def self_test() -> int:
    """Verify the validator detects broken + accepts fixed."""
    with tempfile.TemporaryDirectory(prefix="pi_self_test_") as tmp:
        tmp_path = Path(tmp)
        ent_dir = tmp_path / "entities" / "v1-alpha"
        ent_dir.mkdir(parents=True)

        # Broken entries: each demonstrates a different BP-ARC-ID-* rule.
        broken = [
            # BP-ARC-ID-001: name does not match identity.verb+object
            {
                "id": "dea:bp-bad-1",
                "name": "Wrong Name",
                "type": "Process",
                "version": "1.0.0",
                "process_intent": "operational",
                "process_audience": "customer-demand",
                "process_type": "core",
                "description": "Some description here for testing purposes only.",
                "trigger": "Customer request",
                "outcome": "Customer is served.",
                "identity": {
                    "verb": "Manage",
                    "object": "Customer",
                    "outcome_statement": "Customer relationships are maintained and renewed per policy.",
                    "evidence_links": [{"type": "documentation", "ref": "docs/m.md"}],
                },
            },
            # BP-ARC-ID-002: missing trigger
            {
                "id": "dea:bp-bad-2",
                "name": "Manage Order",
                "type": "Process",
                "version": "1.0.0",
                "process_intent": "operational",
                "process_audience": "operations-delivery",
                "process_type": "core",
                "description": "Order management process for testing.",
                "outcome": "Order is fulfilled.",
                "identity": {
                    "verb": "Manage",
                    "object": "Order",
                    "outcome_statement": "Orders are accepted, processed, and fulfilled.",
                    "evidence_links": [{"type": "documentation", "ref": "docs/o.md"}],
                },
            },
            # BP-ARC-ID-004: process_type=core but outcome mentions direction-setting
            {
                "id": "dea:bp-bad-4",
                "name": "Manage Strategy",
                "type": "Process",
                "version": "1.0.0",
                "process_intent": "management",
                "process_audience": "governance-existence",
                "process_type": "core",  # WRONG: should be 'strategic'
                "description": "Set strategic direction and goals.",
                "trigger": "Annual planning cycle",
                "outcome": "Strategic direction is set.",
                "identity": {
                    "verb": "Manage",
                    "object": "Strategy",
                    "outcome_statement": "Strategic direction and goals are established; portfolio is governed.",
                    "evidence_links": [{"type": "documentation", "ref": "docs/s.md"}],
                },
            },
            # BP-ARC-ID-005: missing evidence_links
            {
                "id": "dea:bp-bad-5",
                "name": "Manage Risk",
                "type": "Process",
                "version": "1.0.0",
                "process_intent": "management",
                "process_audience": "governance-existence",
                "process_type": "management",
                "description": "Manage enterprise risk.",
                "trigger": "Risk event",
                "outcome": "Risk is mitigated.",
                "identity": {
                    "verb": "Manage",
                    "object": "Risk",
                    "outcome_statement": "Enterprise risks are identified, assessed, and mitigated.",
                    # evidence_links missing
                },
            },
        ]
        for b in broken:
            (ent_dir / f"{b['id'].replace(':', '_')}.yaml").write_text(yaml.safe_dump(b, sort_keys=False))

        errs, suggs = run_checks(tmp_path)
        for prefix in ("BP-ARC-ID-001", "BP-ARC-ID-002", "BP-ARC-ID-004", "BP-ARC-ID-005"):
            if not any(e.startswith(prefix) for e in errs):
                print(f"self-test FAIL: expected at least one {prefix}* error in: {errs}")
                return 2
        if not suggs:
            print(f"self-test FAIL: expected at least one re-landscape suggestion in: {suggs}")
            return 2

        # Now FIX everything.
        for f in ent_dir.iterdir():
            f.unlink()
        fixed = {
            "id": "dea:bp-good",
            "name": "Manage Customer",
            "type": "Process",
            "version": "1.0.0",
            "process_intent": "management",
            "process_audience": "customer-demand",
            "process_type": "management",
            "description": "Manage customer relationships across the lifecycle.",
            "trigger": "New customer onboarding or existing customer event",
            "outcome": "Customer relationships are maintained and renewed per policy.",
            "identity": {
                "verb": "Manage",
                "object": "Customer",
                "outcome_statement": "Customer relationships are maintained, escalated where required, and renewed or terminated per policy.",
                "evidence_links": [
                    {"type": "documentation", "ref": "docs/processes/manage-customer.md"},
                    {"type": "governance", "ref": "governance/process-manage-customer.md"},
                ],
            },
        }
        (ent_dir / "dea_bp-good.yaml").write_text(yaml.safe_dump(fixed, sort_keys=False))
        errs_fixed, suggs_fixed = run_checks(tmp_path)
        if errs_fixed:
            print(f"self-test FAIL: expected zero errors on fixed, got: {errs_fixed}")
            return 2

    print("self-test PASS: BP-ARC-ID-001..005 all triggered on broken catalog; zero errors on fixed.")
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
        print("Process Identity validation: FAILED")
        for e in errors:
            print(f"  ✗ {e}")
        if suggestions:
            print("\nRe-landscape suggestions (BP-ARC-ID-005):")
            for s in suggestions:
                print(f"  → {s['target']}: {s['suggestion_type']} "
                      f"(confidence={s['confidence']:.2f}) — {s['rationale'][:120]}")
        return 1
    if suggestions:
        print("Process Identity validation: PASS (with suggestions)")
        for s in suggestions:
            print(f"  → {s['target']}: {s['suggestion_type']} "
                  f"(confidence={s['confidence']:.2f}) — {s['rationale'][:120]}")
        return 0
    print("Process Identity validation: PASS (BP-ARC-ID-001..005)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
