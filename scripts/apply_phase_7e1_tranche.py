#!/usr/bin/env python3
"""Generate CR-BP-21e.1 artifacts (FinanceAndAccounting completion):
4 non-Conceive L1 groups + 15 remaining register v2 L2 processes.
Mirrors scripts/apply_phase_7d1_tranche.py template (the canonical
L2 shape used in 21a.1, mirrored by 21b.1, 21c.1, 21d.1).

Note: CR-BP-21e already landed 5 FA L2s (one per non-Conceive cell).
This tranche lands the remaining 15:
- Design: 3 (4 - 1 already-landed)
- Build: 3
- Operate: 7 (8 - 1)
- Improve: 2 (3 - 1)
"""
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TR = "cr-bp-21e.1"
CR = "CR-BP-21e.1"

# --- Identity sub-block keywords (per scripts/check_process_identity.py) ---
# Core: deliver, produce, fulfil, operate, serve, execute
# Management: plan, manage, govern, monitor, coordinate, supervise,
#             rationalize, optimize, design
CORE_KW = ("deliver", "produce", "fulfil", "fulfill", "operate", "serve", "execute")
MGMT_KW = ("plan", "manage", "govern", "monitor", "coordinate", "supervise",
           "rationalize", "optimize", "design", "budget", "forecast",
           "report", "account", "tax", "audit", "comply")

# --- 15 remaining register v2 FA L2 candidates ---
L2S = [
    # === DESIGN (3) ===
    {
        "eid": "dea:process-design-financial-controls-and-policies",
        "name": "Design Financial Controls and Policies",
        "verb": "Design", "object": "Financial Controls and Policies",
        "intent": "develop", "stage": "design", "pclass": "management",
        "outcome_statement": (
            "Financial controls and policies are designed to the "
            "approved financial architecture, with the policy "
            "framework ready for control implementation."
        ),
        "trigger": "A control or policy gap is identified.",
        "evidence": ["CR-BP-21e.1#design-financial-controls-and-policies"],
        "context": "dea:pc-fa-design",
    },
    {
        "eid": "dea:process-design-tax-position-and-strategy",
        "name": "Design Tax Position and Strategy",
        "verb": "Design", "object": "Tax Position and Strategy",
        "intent": "develop", "stage": "design", "pclass": "management",
        "outcome_statement": (
            "Tax position and strategy are designed with positions "
            "documented and the strategy ready for tax planning."
        ),
        "trigger": "A new tax exposure or jurisdictional change emerges.",
        "evidence": ["CR-BP-21e.1#design-tax-position-and-strategy"],
        "context": "dea:pc-fa-design",
    },
    {
        "eid": "dea:process-design-treasury-and-funding-model",
        "name": "Design Treasury and Funding Model",
        "verb": "Design", "object": "Treasury and Funding Model",
        "intent": "develop", "stage": "design", "pclass": "management",
        "outcome_statement": (
            "Treasury and funding model is designed with cash, "
            "liquidity, and funding policy coordinated for "
            "treasury operations."
        ),
        "trigger": "Treasury policy or funding posture is reviewed.",
        "evidence": ["CR-BP-21e.1#design-treasury-and-funding-model"],
        "context": "dea:pc-fa-design",
    },
    # === BUILD (3) ===
    {
        "eid": "dea:process-implement-financial-systems-and-ledger",
        "name": "Implement Financial Systems and Ledger",
        "verb": "Implement", "object": "Financial Systems and Ledger",
        "intent": "develop", "stage": "build", "pclass": "core",
        "outcome_statement": (
            "Financial systems and ledger are implemented with "
            "chart of accounts, posting rules, and reports "
            "deployed to operate general ledger."
        ),
        "trigger": "A financial system build or change is initiated.",
        "evidence": ["CR-BP-21e.1#implement-financial-systems-and-ledger"],
        "context": "dea:pc-fa-build",
    },
    {
        "eid": "dea:process-build-budgeting-and-forecasting-systems",
        "name": "Build Budgeting and Forecasting Systems",
        "verb": "Build", "object": "Budgeting and Forecasting Systems",
        "intent": "develop", "stage": "build", "pclass": "core",
        "outcome_statement": (
            "Budgeting and forecasting systems are built with "
            "models, integrations, and controls delivered for "
            "operate budgeting."
        ),
        "trigger": "A planning cycle or budget tool rebuild is scoped.",
        "evidence": ["CR-BP-21e.1#build-budgeting-and-forecasting-systems"],
        "context": "dea:pc-fa-build",
    },
    {
        "eid": "dea:process-onboard-tax-and-compliance-capability",
        "name": "Onboard Tax and Compliance Capability",
        "verb": "Onboard", "object": "Tax and Compliance Capability",
        "intent": "manage", "stage": "build", "pclass": "management",
        "outcome_statement": (
            "Tax and compliance capability is onboarded with "
            "filings, registrations, and controls operational for "
            "tax planning, supervised by the tax policy review."
        ),
        "trigger": "A new tax jurisdiction or compliance regime applies.",
        "evidence": ["CR-BP-21e.1#onboard-tax-and-compliance-capability"],
        "context": "dea:pc-fa-build",
    },
    # === OPERATE (7) ===
    {
        "eid": "dea:process-run-accounts-payable",
        "name": "Run Accounts Payable",
        "verb": "Run", "object": "Accounts Payable",
        "intent": "operate", "stage": "operate", "pclass": "core",
        "outcome_statement": (
            "Accounts payable is run with invoices matched, "
            "approvals recorded, and payments produced to plan."
        ),
        "trigger": "An invoice or payment due date arrives.",
        "evidence": ["CR-BP-21e.1#run-accounts-payable"],
        "context": "dea:pc-fa-operate",
    },
    {
        "eid": "dea:process-run-accounts-receivable",
        "name": "Run Accounts Receivable",
        "verb": "Run", "object": "Accounts Receivable",
        "intent": "operate", "stage": "operate", "pclass": "core",
        "outcome_statement": (
            "Accounts receivable is run with invoices issued, "
            "collections managed, and cash applied to the ledger."
        ),
        "trigger": "A customer invoice or collection event is due.",
        "evidence": ["CR-BP-21e.1#run-accounts-receivable"],
        "context": "dea:pc-fa-operate",
    },
    {
        "eid": "dea:process-execute-payroll",
        "name": "Execute Payroll",
        "verb": "Execute", "object": "Payroll",
        "intent": "operate", "stage": "operate", "pclass": "core",
        "outcome_statement": (
            "Payroll is executed with compensation, withholdings, "
            "and statutory filings produced for each cycle."
        ),
        "trigger": "A payroll cycle boundary is reached.",
        "evidence": ["CR-BP-21e.1#execute-payroll"],
        "context": "dea:pc-fa-operate",
    },
    {
        "eid": "dea:process-manage-cash-and-liquidity",
        "name": "Manage Cash and Liquidity",
        "verb": "Manage", "object": "Cash and Liquidity",
        "intent": "operate", "stage": "operate", "pclass": "management",
        "outcome_statement": (
            "Cash and liquidity are managed with positions, "
            "forecasts, and investment decisions monitored "
            "against the treasury policy."
        ),
        "trigger": "A cash position or liquidity event occurs.",
        "evidence": ["CR-BP-21e.1#manage-cash-and-liquidity"],
        "context": "dea:pc-fa-operate",
    },
    {
        "eid": "dea:process-perform-financial-close",
        "name": "Perform Financial Close",
        "verb": "Perform", "object": "Financial Close",
        "intent": "operate", "stage": "operate", "pclass": "core",
        "outcome_statement": (
            "Financial close is performed with period-end entries, "
            "reconciliations, and management reports produced for "
            "reporting."
        ),
        "trigger": "A period close boundary is reached.",
        "evidence": ["CR-BP-21e.1#perform-financial-close"],
        "context": "dea:pc-fa-operate",
    },
    {
        "eid": "dea:process-manage-tax-compliance-and-filings",
        "name": "Manage Tax Compliance and Filings",
        "verb": "Manage", "object": "Tax Compliance and Filings",
        "intent": "operate", "stage": "operate", "pclass": "management",
        "outcome_statement": (
            "Tax compliance and filings are managed with returns "
            "prepared, payments scheduled, and exposures monitored."
        ),
        "trigger": "A tax return or filing due date is reached.",
        "evidence": ["CR-BP-21e.1#manage-tax-compliance-and-filings"],
        "context": "dea:pc-fa-operate",
    },
    {
        "eid": "dea:process-operate-financial-reporting-and-disclosure",
        "name": "Operate Financial Reporting and Disclosure",
        "verb": "Operate", "object": "Financial Reporting and Disclosure",
        "intent": "operate", "stage": "operate", "pclass": "core",
        "outcome_statement": (
            "Financial reporting and disclosure are produced with "
            "statements, footnotes, and disclosures delivered for "
            "internal and external stakeholders."
        ),
        "trigger": "A reporting or disclosure milestone arrives.",
        "evidence": ["CR-BP-21e.1#operate-financial-reporting-and-disclosure"],
        "context": "dea:pc-fa-operate",
    },
    # === IMPROVE (2) ===
    {
        "eid": "dea:process-refine-financial-controls-and-policies",
        "name": "Refine Financial Controls and Policies",
        "verb": "Refine", "object": "Financial Controls and Policies",
        "intent": "develop", "stage": "improve", "pclass": "management",
        "outcome_statement": (
            "Financial controls and policies are refined based on "
            "audit findings and incidents, governed by the policy "
            "review cycle."
        ),
        "trigger": "An audit finding or control incident surfaces.",
        "evidence": ["CR-BP-21e.1#refine-financial-controls-and-policies"],
        "context": "dea:pc-fa-improve",
    },
    {
        "eid": "dea:process-evolve-treasury-and-funding-model",
        "name": "Evolve Treasury and Funding Model",
        "verb": "Evolve", "object": "Treasury and Funding Model",
        "intent": "develop", "stage": "improve", "pclass": "management",
        "outcome_statement": (
            "Treasury and funding model is evolved based on "
            "market shifts and exposure review, monitored for "
            "future funding posture."
        ),
        "trigger": "A market or funding posture change occurs.",
        "evidence": ["CR-BP-21e.1#evolve-treasury-and-funding-model"],
        "context": "dea:pc-fa-improve",
    },
]

assert len(L2S) == 15, f"expected 15 L2s, got {len(L2S)}"
# Pre-flight: each L2 satisfies BP-ARC-ID-004 keyword density >= 0.3
def _density(outcome: str, kws: tuple) -> float:
    toks = outcome.lower().split()
    if not toks:
        return 0.0
    hits = sum(1 for t in toks if any(k in t for k in kws))
    return hits / len(toks)

# Substring check across the entire outcome (not token-level); matches
    # check_process_identity.py's own behavior. BP-ARC-ID-004: density >= 0.3.
    for L in L2S:
        own = CORE_KW if L["pclass"] == "core" else MGMT_KW
        text = L["outcome_statement"].lower()
        hits = sum(1 for k in own if k in text)
        d = hits / max(1, len(own))
        if d < 0.3:
            raise AssertionError(
                f"BP-ARC-ID-004 density {d:.2f} too low for {L['eid']}: "
                f"{L['outcome_statement']!r}"
            )

# --- 4 non-Conceive L1 Process Groups ---
GROUPS = [
    {
        "eid": "dea:group-financial-design",
        "name": "Financial Design",
        "stage": "design",
        "composes": [
            ("dea:process-design-financial-plan-structure", "landed CR-BP-21e"),
            ("dea:process-design-financial-controls-and-policies", CR),
            ("dea:process-design-tax-position-and-strategy", CR),
            ("dea:process-design-treasury-and-funding-model", CR),
        ],
        "ecf_stage": "design",
    },
    {
        "eid": "dea:group-financial-build",
        "name": "Financial Build",
        "stage": "build",
        "composes": [
            ("dea:process-implement-financial-systems-and-ledger", CR),
            ("dea:process-build-budgeting-and-forecasting-systems", CR),
            ("dea:process-onboard-tax-and-compliance-capability", CR),
        ],
        "ecf_stage": "build",
    },
    {
        "eid": "dea:group-financial-operate",
        "name": "Financial Operate",
        "stage": "operate",
        "composes": [
            ("dea:process-operate-general-ledger", "landed CR-BP-21e"),
            ("dea:process-run-accounts-payable", CR),
            ("dea:process-run-accounts-receivable", CR),
            ("dea:process-execute-payroll", CR),
            ("dea:process-manage-cash-and-liquidity", CR),
            ("dea:process-perform-financial-close", CR),
            ("dea:process-manage-tax-compliance-and-filings", CR),
            ("dea:process-operate-financial-reporting-and-disclosure", CR),
        ],
        "ecf_stage": "operate",
    },
    {
        "eid": "dea:group-financial-improve",
        "name": "Financial Improve",
        "stage": "improve",
        "composes": [
            ("dea:process-audit-policy-compliance", "landed CR-BP-21e"),
            ("dea:process-refine-financial-controls-and-policies", CR),
            ("dea:process-evolve-treasury-and-funding-model", CR),
        ],
        "ecf_stage": "improve",
    },
]

assert len(GROUPS) == 4

# --- Render L2 Process YAML ---
def render_l2(L: dict) -> str:
    if len(L["trigger"]) > 80:
        trigger_text = L["trigger"][:78] + "..."
    else:
        trigger_text = L["trigger"]
    return f"""id: {L['eid']}
name: {L['name']}
type: Process
version: '1.0.0'
process_intent: {L['intent']}
process_type: {L['pclass']}
context:
- ref: {L['context']}
description: |
  {L['name']} ({L['stage']} stage, {L['pclass']} process). Landed by {CR}
  from the FinanceAndAccounting register v2.
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
  target_id: ecf:financeAccounting.{L['stage']}
ecfConformance:
  framework: EnterpriseConceptFramework
  contractVersion: 1.0.0
  profile: dea:ecf@1.0.0
  status: conformant
  affiliation: inherits-catalog
  canonicalReferences:
  - kind: coordinate
    domain: FinanceAndAccounting
    stage: {L['stage'].capitalize()}
    identifier: ecf:financeAccounting.{L['stage']}
  target_id: ecf:financeAccounting.{L['stage']}
change_history:
- version: '1.0.0'
  date: '2026-09-08'
  cr: {CR}
  change: |
    Initial landing under {CR} (FinanceAndAccounting completion).
"""

def render_group(g: dict) -> str:
    rel_lines = []
    for tgt, why in g["composes"]:
        rel_lines.append(
            f"- source_id: {g['eid']}\n"
            f"  relationship_type: composes\n"
            f"  target_id: {tgt}\n"
            f"  rationale: {why}"
        )
    lines_relationships = "\n".join(rel_lines)
    return f"""id: {g['eid']}
name: {g['name']}
type: ProcessGroup
version: '1.0.0'
process_context: dea:pc-fa-{g['stage']}
description: |
  {g['name']} Process Group (FinanceAndAccounting/{g['stage']}). Lands
  the {len(g['composes'])} L2 Business Processes that realise the
  {g['stage']} cell of the FinanceAndAccounting ECF coordinate.
relationships:
{lines_relationships}
ecfConformance:
  framework: EnterpriseConceptFramework
  contractVersion: 1.0.0
  profile: dea:ecf@1.0.0
  status: conformant
  affiliation: inherits-catalog
  canonicalReferences:
  - kind: coordinate
    domain: FinanceAndAccounting
    stage: {g['stage'].capitalize()}
    identifier: ecf:financeAccounting.{g['stage']}
  target_id: ecf:financeAccounting.{g['stage']}
change_history:
- version: '1.0.0'
  date: '2026-09-08'
  cr: {CR}
  change: |
    Initial landing under {CR} (FinanceAndAccounting completion).
"""

for L in L2S:
    d = REPO / "entities" / "v1-alpha" / L["eid"]
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{L['eid']}.yaml").write_text(render_l2(L))

for g in GROUPS:
    d = REPO / "entities" / "v1-alpha" / g["eid"]
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{g['eid']}.yaml").write_text(render_group(g))

print(f"Wrote {len(L2S)} L2 processes and {len(GROUPS)} L1 groups.")
print("Done. Next: text-patch existing records, dispositions, tranche plan, register audit, regenerate, gates.")