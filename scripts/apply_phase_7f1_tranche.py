#!/usr/bin/env python3
"""Generate CR-BP-21f.1 artifacts (GovernanceAndExistence completion):
7 register v2 GE L2 candidates that are not covered by the 9 GE seed BPs.

GE was landed pre-register-v2-completion discipline (seeds landed under
CR-BP-13a / legacy tranches), so its register v2 candidate list was never
fully populated. The uncovered candidates form the risk-framework track
(Conceive/Design/Build/Operate/Improve) plus assurance-review,
audit-findings-scoring, and policy-framework-improvement:

- Conceive: 1 (Frame Risk Framework Direction)
- Design:   1 (Design Risk Framework)
- Build:    1 (Establish Risk and Control Apparatus)
- Operate:  2 (Operate Enterprise Risk Oversight, Conduct Assurance Review)
- Improve:  2 (Score Audit Findings, Improve Policy and Control Framework)

L1 Process Groups already exist for all 5 GE cells; this generator only
writes the 7 L2 records. Group composes-edge and context processes-list
patches are applied as surgical text edits afterwards.

Template: mirrors scripts/apply_phase_7e1_tranche.py's render_l2 with the
CST-004 fix (lifecycle_status + status) folded in.
"""
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TR = "cr-bp-21f.1"
CR = "CR-BP-21f.1"
DATE = "2026-09-08"
DOMAIN = "GovernanceAndExistence"
ECF = "ecf:governanceExistence"

# Gate keyword sets (scripts/check_process_identity.py TYPE_KEYWORDS).
TYPE_KEYWORDS = {
    "strategic":      ["direction", "vision", "goal", "strategic", "portfolio", "governance"],
    "management":     ["plan", "monitor", "control", "coordinate", "allocate", "supervise"],
    "core":           ["deliver", "produce", "fulfil", "operate", "serve", "execute", "manage customer", "manage order"],
    "support":        ["tooling", "internal service", "HR", "facilities", "IT support", "admin"],
    "standardization": ["compliance", "standard", "audit", "measure", "improve", "quality"],
}

# --- 7 uncovered register v2 GE L2 candidates ---
L2S = [
    # === CONCEIVE (1) ===
    {
        "eid": "dea:process-frame-risk-framework-direction",
        "name": "Frame Risk Framework Direction",
        "verb": "Frame", "object": "Risk Framework Direction",
        "intent": "govern", "stage": "conceive", "pclass": "strategic",
        "outcome_statement": (
            "Risk framework direction is framed with risk appetite, "
            "tolerance bands, and governance posture defined, setting "
            "the strategic direction for risk framework design."
        ),
        "trigger": "A governance mandate requires an enterprise risk posture.",
        "context": "dea:pc-ge-c",
    },
    # === DESIGN (1) ===
    {
        "eid": "dea:process-design-risk-framework",
        "name": "Design Risk Framework",
        "verb": "Design", "object": "Risk Framework",
        "intent": "develop", "stage": "design", "pclass": "strategic",
        "outcome_statement": (
            "The risk framework is designed with taxonomy, assessment "
            "scales, and governance integration committed, providing "
            "the risk direction for the build stage."
        ),
        "trigger": "The risk framework direction is committed.",
        "context": "dea:pc-ge-d",
    },
    # === BUILD (1) ===
    {
        "eid": "dea:process-establish-risk-and-control-apparatus",
        "name": "Establish Risk and Control Apparatus",
        "verb": "Establish", "object": "Risk and Control Apparatus",
        "intent": "manage", "stage": "build", "pclass": "core",
        "outcome_statement": (
            "Risk and control apparatus is established with registers, "
            "monitoring tooling, and reporting lines delivered, ready "
            "to operate in the Operate context."
        ),
        "trigger": "The risk framework design is approved for build.",
        "context": "dea:pc-ge-b",
    },
    # === OPERATE (2) ===
    {
        "eid": "dea:process-operate-enterprise-risk-oversight",
        "name": "Operate Enterprise Risk Oversight",
        "verb": "Operate", "object": "Enterprise Risk Oversight",
        "intent": "operate", "stage": "operate", "pclass": "core",
        "outcome_statement": (
            "Enterprise risk oversight is operated with risk reviews "
            "executed, exposures surfaced, and mitigations delivered "
            "to the governance bodies."
        ),
        "trigger": "A risk review cycle boundary is reached.",
        "context": "dea:pc-ge-op",
    },
    {
        "eid": "dea:process-conduct-assurance-review",
        "name": "Conduct Assurance Review",
        "verb": "Conduct", "object": "Assurance Review",
        "intent": "operate", "stage": "operate", "pclass": "standardization",
        "outcome_statement": (
            "Assurance reviews are conducted with evidence measured "
            "against standards, findings reported, and audit quality "
            "maintained."
        ),
        "trigger": "An assurance cycle or audit mandate arrives.",
        "context": "dea:pc-ge-op",
    },
    # === IMPROVE (2) ===
    {
        "eid": "dea:process-score-audit-findings",
        "name": "Score Audit Findings",
        "verb": "Score", "object": "Audit Findings",
        "intent": "develop", "stage": "improve", "pclass": "standardization",
        "outcome_statement": (
            "Audit findings are scored for severity and recurrence, "
            "measured against standards, and quality trends reported "
            "to the governance bodies."
        ),
        "trigger": "An audit report is delivered with findings.",
        "context": "dea:pc-ge-im",
    },
    {
        "eid": "dea:process-improve-policy-and-control-framework",
        "name": "Improve Policy and Control Framework",
        "verb": "Improve", "object": "Policy and Control Framework",
        "intent": "develop", "stage": "improve", "pclass": "standardization",
        "outcome_statement": (
            "The policy and control framework is improved with gaps "
            "measured, standards updated, and compliance posture "
            "strengthened."
        ),
        "trigger": "Audit findings or policy gaps surface.",
        "context": "dea:pc-ge-im",
    },
]

assert len(L2S) == 7, f"expected 7 L2s, got {len(L2S)}"

# Pre-flight: BP-ARC-ID-004 own-type keyword density >= 0.3
for L in L2S:
    own = TYPE_KEYWORDS[L["pclass"]]
    other = [k for t, kws in TYPE_KEYWORDS.items() if t != L["pclass"] for k in kws]
    text = L["outcome_statement"].lower()
    own_hits = sum(1 for k in own if k in text)
    other_hits = sum(1 for k in other if k in text)
    total = own_hits + other_hits
    density = own_hits / total if total else 0.5
    if density < 0.3:
        raise AssertionError(
            f"BP-ARC-ID-004 density {density:.2f} too low for {L['eid']}: "
            f"own={own_hits} other={other_hits} {L['outcome_statement']!r}"
        )

# --- Render L2 Process YAML (21e.1 template + CST-004 lifecycle_status) ---
def render_l2(L: dict) -> str:
    trigger_text = L["trigger"][:78] + "..." if len(L["trigger"]) > 80 else L["trigger"]
    return f"""id: {L['eid']}
name: {L['name']}
type: Process
version: '1.0.0'
lifecycle_status: candidate
status: candidate
process_intent: {L['intent']}
process_type: {L['pclass']}
context:
- ref: {L['context']}
description: |
  {L['name']} ({L['stage']} stage, {L['pclass']} process). Landed by {CR}
  from the GovernanceAndExistence register v2.
trigger: {trigger_text}
outcome: {L['outcome_statement']}
triggers:
  - {L['trigger']}
outcomes:
  - {L['outcome_statement']}
identity:
  verb: {L['verb']}
  object: {L['object']}
  outcome_statement: {L['outcome_statement']}
  evidence_links:
    - type: documentation
      ref: change-requests/{CR}.md
relationships:
- source_id: {L['eid']}
  relationship_type: serves
  target_id: {ECF}.{L['stage']}
ecfConformance:
  framework: EnterpriseConceptFramework
  contractVersion: 1.0.0
  profile: dea:ecf@1.0.0
  status: conformant
  affiliation: inherits-catalog
  canonicalReferences:
  - kind: coordinate
    domain: {DOMAIN}
    stage: {L['stage'].capitalize()}
    identifier: {ECF}.{L['stage']}
  target_id: {ECF}.{L['stage']}
change_history:
- version: '1.0.0'
  date: '{DATE}'
  cr: {CR}
  change: |
    Initial landing under {CR} (GovernanceAndExistence completion).
"""

for L in L2S:
    d = REPO / "entities" / "v1-alpha" / L["eid"]
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{L['eid']}.yaml").write_text(render_l2(L))

print(f"Wrote {len(L2S)} L2 processes (no new L1 groups; GE groups exist).")
print("Done. Next: text-patch GE group composes edges + contexts, "
      "dispositions, tranche plan, regenerate, gates.")
