#!/usr/bin/env python3
"""Generate CR-BP-21e artifacts (FinanceAndAccounting landing):
5 process contexts, 1 L1 group, 5 L2 processes. Mirrors the
CR-BP-21d (OperationsAndEnablement) pattern. Substrate-neutral
per ADR-ECF-002 §5 / CR-ECF-007.

Run: python scripts/apply_phase_7e_tranche.py
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).parent.parent
CTX = ROOT / "contexts/v1-alpha"
ENT = ROOT / "entities/v1-alpha"
CHANGE_DATE = "2026-09-08"


CONTEXTS = [
    {
        "filename": "dea-pc-fa-conceive",
        "id": "dea:pc-fa-conceive",
        "domain": "FinanceAndAccounting",
        "stage": "Conceive",
        "name": "Financial Model and Funding Conception",
        "definition": (
            "The bounded enterprise context for **conceiving** the enterprise's "
            "monetary model, finance strategy, and funding and capital approach "
            "in the **Finance & Accounting** domain. This context addresses the "
            "front-end work of framing the finance strategy, the monetary model, "
            "and the funding and capital approach. v2.4.0: the domain is scoped "
            "to monetary consequence; abstract 'value' was removed "
            "(domain-grounding.md §3.7)."
        ),
        "includes": [
            "Finance strategy framing",
            "Monetary model framing",
            "Funding and capital approach framing",
        ],
        "excludes": [
            "Strategic investment choices (strategy-direction x conceive; adjacent domain)",
            "Investment strategy governance (governance-existence x conceive; adjacent domain)",
            "Financial planning design (Design stage; adjacent context)",
            "Finance capability build (Build stage; adjacent context)",
        ],
        "outcomes": [
            "Finance strategy is framed for the enterprise.",
            "Monetary model is framed with bounded scope.",
            "Funding and capital approach is framed.",
        ],
        "adjacent": [
            "dea:pc-fa-design", "dea:pc-fa-build", "dea:pc-fa-operate", "dea:pc-fa-improve",
        ],
        "processes": ["dea:process-frame-finance-strategy"],
        "l1_candidates": ["Financial Model Conception", "Funding Strategy Conception"],
        "grounding_phrase": "conception of monetary model, finance strategy, and funding and capital approach",
        "enterprise_concern": "the conception of the enterprise's monetary model and funding approach.",
        "lifecycle_concern": "framing finance strategy, monetary model, and funding and capital approach.",
        "combined_meaning": "The front-end work of framing the finance strategy, the monetary model, and the funding and capital approach as monetary-consequence subjects.",
    },
    {
        "filename": "dea-pc-fa-design",
        "id": "dea:pc-fa-design",
        "domain": "FinanceAndAccounting",
        "stage": "Design",
        "name": "Financial Planning and Accounting Architecture Design",
        "definition": (
            "The bounded enterprise context for **designing** the chart of "
            "accounts, cost allocation model, financial plan structure, and "
            "financial controls of the enterprise in the **Finance & "
            "Accounting** domain. This context addresses the analytical work of "
            "producing finance architecture, planning structure, accounting "
            "architecture, and financial control designs. v2.4.0: value "
            "architecture design and value measurement frameworks were removed "
            "per the monetary scoping (domain-grounding.md §3.7)."
        ),
        "includes": [
            "Chart of accounts design",
            "Cost allocation model design",
            "Financial plan structure design",
            "Financial controls design",
        ],
        "excludes": [
            "Finance strategy conception (Conceive stage; adjacent context)",
            "Finance capability build (Build stage; adjacent context)",
            "Investment design (strategy-direction x design; adjacent domain)",
        ],
        "outcomes": [
            "Chart of accounts is designed.",
            "Cost allocation model is designed.",
            "Financial plan structure is designed.",
            "Financial controls are designed.",
        ],
        "adjacent": [
            "dea:pc-fa-conceive", "dea:pc-fa-build", "dea:pc-fa-operate", "dea:pc-fa-improve",
        ],
        "processes": ["dea:process-design-financial-plan-structure"],
        "l1_candidates": ["Financial Planning Design", "Accounting Architecture Design"],
        "grounding_phrase": "design of chart of accounts, cost allocation, plan structure, and financial controls",
        "enterprise_concern": "the design of the enterprise's finance and accounting architecture.",
        "lifecycle_concern": "designing chart of accounts, cost allocation model, financial plan structure, and financial controls.",
        "combined_meaning": "The analytical work of producing designs for the chart of accounts, cost allocation model, financial plan structure, and financial controls.",
    },
    {
        "filename": "dea-pc-fa-build",
        "id": "dea:pc-fa-build",
        "domain": "FinanceAndAccounting",
        "stage": "Build",
        "name": "Finance Capability and System Build",
        "definition": (
            "The bounded enterprise context for **building** the finance "
            "function, finance systems, and funding facilities of the "
            "enterprise in the **Finance & Accounting** domain. This context "
            "addresses the constructive work of standing up the finance "
            "function, deploying ERP finance modules, and securing funding "
            "facilities. v2.4.0: scoped to monetary consequence "
            "(domain-grounding.md §3.7)."
        ),
        "includes": [
            "Finance function stand-up",
            "ERP finance module deployment",
            "Funding facility establishment",
        ],
        "excludes": [
            "Financial planning design (Design stage; adjacent context)",
            "Building non-finance capabilities (owning domains; adjacent domains)",
            "Technology platform build (operations-enablement x build; adjacent domain)",
        ],
        "outcomes": [
            "Finance function is stood up and staffed.",
            "ERP finance module is deployed and configured.",
            "Funding facilities are secured.",
        ],
        "adjacent": [
            "dea:pc-fa-conceive", "dea:pc-fa-design", "dea:pc-fa-operate", "dea:pc-fa-improve",
        ],
        "processes": ["dea:process-secure-funding-facilities"],
        "l1_candidates": ["Finance Capability Build", "Financial System Build"],
        "grounding_phrase": "build of finance function, finance systems, and funding facilities",
        "enterprise_concern": "the construction of the enterprise's finance capability and systems.",
        "lifecycle_concern": "standing up the finance function, deploying finance systems, and securing funding facilities.",
        "combined_meaning": "The constructive work of standing up the finance function, deploying ERP finance modules, and securing funding facilities.",
    },
    {
        "filename": "dea-pc-fa-operate",
        "id": "dea:pc-fa-operate",
        "domain": "FinanceAndAccounting",
        "stage": "Operate",
        "name": "Accounting, Reporting, and Treasury Operation",
        "definition": (
            "The bounded enterprise context for **operating** the general "
            "ledger, accounts payable and receivable, treasury, tax compliance, "
            "financial close, financial planning and analysis, and financial "
            "reporting and disclosure of the enterprise in the **Finance & "
            "Accounting** domain. This context addresses the steady-state work "
            "of monetary recording and reporting. v2.4.0: procure-to-pay and "
            "order-to-cash operational execution moved to operations-enablement "
            "x operate; the monetary recording of those cycles remains here "
            "(domain-grounding.md §3.7)."
        ),
        "includes": [
            "General ledger operation",
            "Accounts payable and receivable operation",
            "Treasury operation",
            "Tax compliance operation",
            "Financial close operation",
            "Financial planning and analysis operation",
            "Financial reporting and disclosure operation",
        ],
        "excludes": [
            "Finance capability build (Build stage; adjacent context)",
            "Procurement transaction execution (operations-enablement x operate; adjacent domain)",
            "Agent compensation operation (agency-organization x operate; adjacent domain)",
        ],
        "outcomes": [
            "General ledger is operated to period close.",
            "Accounts payable and receivable are operated.",
            "Treasury is operated within policy.",
            "Tax compliance is operated.",
            "Financial close is operated on schedule.",
            "Financial reporting and disclosure are produced.",
        ],
        "adjacent": [
            "dea:pc-fa-conceive", "dea:pc-fa-design", "dea:pc-fa-build", "dea:pc-fa-improve",
        ],
        "processes": ["dea:process-operate-general-ledger"],
        "l1_candidates": ["Accounting and Reporting", "Financial Planning and Analysis", "Treasury Operation", "Tax and Compliance"],
        "grounding_phrase": "operation of accounting, reporting, treasury, tax, and financial close",
        "enterprise_concern": "the steady-state monetary recording and reporting of the enterprise.",
        "lifecycle_concern": "operating the general ledger, payables, receivables, treasury, tax compliance, financial close, and reporting.",
        "combined_meaning": "The steady-state work of operating the general ledger, accounts payable and receivable, treasury, tax compliance, financial close, financial planning and analysis, and financial reporting and disclosure.",
    },
    {
        "filename": "dea-pc-fa-improve",
        "id": "dea:pc-fa-improve",
        "domain": "FinanceAndAccounting",
        "stage": "Improve",
        "name": "Finance and Financial Control Improvement",
        "definition": (
            "The bounded enterprise context for **improving** the cost "
            "position, reporting and disclosure, and financial controls of the "
            "enterprise in the **Finance & Accounting** domain. This context "
            "addresses the learning and adaptation work of conducting cost "
            "optimization reviews, improving reporting and disclosure, and "
            "strengthening financial controls. v2.4.0: margin and value "
            "analysis retained only in the monetary-consequence sense "
            "(domain-grounding.md §3.7)."
        ),
        "includes": [
            "Cost optimization review",
            "Reporting and disclosure improvement",
            "Financial control strengthening",
        ],
        "excludes": [
            "Financial reporting operation (Operate stage; adjacent context)",
            "Capability improvement (owning domains; adjacent domains)",
            "Strategic adaptation (strategy-direction x improve; adjacent domain)",
        ],
        "outcomes": [
            "Cost optimization review is conducted and findings committed.",
            "Reporting and disclosure are improved.",
            "Financial controls are strengthened.",
        ],
        "adjacent": [
            "dea:pc-fa-conceive", "dea:pc-fa-design", "dea:pc-fa-build", "dea:pc-fa-operate",
        ],
        "processes": ["dea:process-conduct-cost-optimization-review"],
        "l1_candidates": ["Finance Improvement", "Financial Control Improvement"],
        "grounding_phrase": "improvement of cost position, reporting, disclosure, and financial controls",
        "enterprise_concern": "the improvement of the enterprise's monetary position and controls.",
        "lifecycle_concern": "improving cost position, reporting and disclosure, and financial controls.",
        "combined_meaning": "The learning and adaptation work of conducting cost optimization reviews, improving reporting and disclosure, and strengthening financial controls.",
    },
]


def render_list(items, indent="    - "):
    return "\n".join(f"{indent}{i}" for i in items)


def render_adjacent_boundaries(stage, adjacent):
    lines = []
    for a in adjacent:
        short = a.replace("dea:", "")
        lines.append(f'    - "dea:{short} (adjacent context): monetary flow between {stage} and the adjacent cell."')
    return "\n".join(lines)


CONTEXT_TEMPLATE = """# Process Context Cell Charter: {domain} x {stage}.
#
# Lands as part of CR-BP-21e (FinanceAndAccounting landing, fifth and
# final unadmitted-domain tranche under ECF v2.4.0 register v2 /
# CR-BP-19). Carries the full Cell Charter (CR-BP-02 §7).
#
# v2.4.0 grounding: dea-metaframework/framework/domain-grounding.md §3.7
# (Finance & Accounting: {grounding_phrase}).
#
# Substrate independence (ADR-ECF-002 §5, CR-ECF-007): this context
# applies to biological, artificial, and hybrid agents without
# reclassification.

id: {id}
domain: {domain}
lifecycle_stage: {stage}
name: {name}

# Normative definition (PC-006).
definition: |
  {definition}

# Scope (PC-005).
scope:
  includes:
{includes_yaml}
  excludes:
{excludes_yaml}

# Intended outcomes.
outcomes:
{outcomes_yaml}

# Adjacent contexts (CR-BP-02 §11).
adjacent_contexts:
{adjacent_yaml}

# Business Processes belonging to this context (PC-008).
processes:
{processes_yaml}

# Cell Charter (CR-BP-02 §7; PC-006).
cell_charter:
  enterprise_concern: "Finance & Accounting: {enterprise_concern}"
  lifecycle_concern: "{stage}: {lifecycle_concern}"
  combined_semantic_meaning: |
    {combined_meaning}
  expected_outcomes:
{outcomes_yaml}
  inclusions:
{includes_yaml}
  exclusions:
{excludes_yaml}
  adjacent_boundaries:
{adjacent_boundaries_yaml}

# Lifecycle status (CR-BP-02 §17).
lifecycle_status: candidate
status: candidate

# Provenance.
established_by: CR-BP-21e
established_at: '{CHANGE_DATE}'

# Change history.
change_history:
  - cr: CR-BP-21e
    date: '{CHANGE_DATE}'
    change: |
      Initial Process Context record; promoted from the CR-BP-19
      register v2 (ratified against ECF v2.4.0) as part of the
      FinanceAndAccounting landing tranche. Substrate-neutral
      per ADR-ECF-002 §5 / CR-ECF-007.

links:
  - rel: change-request
    href: change-requests/CR-BP-21e-finance-accounting-landing.md
  - rel: predecessor
    href: change-requests/CR-BP-19-l1-register-rederivation-ecf-v240.md
  - rel: research-register
    href: entities/v1-alpha/dea:group-customer-lifecycle-management/research/l1-register.yaml
"""


for c in CONTEXTS:
    out = CTX / f"{c['filename']}.yaml"
    out.write_text(
        CONTEXT_TEMPLATE.format(
            domain=c["domain"],
            stage=c["stage"],
            id=c["id"],
            name=c["name"],
            definition=c["definition"],
            includes_yaml=render_list(c["includes"]),
            excludes_yaml=render_list(c["excludes"]),
            outcomes_yaml=render_list(c["outcomes"]),
            adjacent_yaml=render_list(c["adjacent"]),
            processes_yaml=render_list(c["processes"]),
            adjacent_boundaries_yaml=render_adjacent_boundaries(c["stage"], c["adjacent"]),
            enterprise_concern=c["enterprise_concern"],
            lifecycle_concern=c["lifecycle_concern"],
            combined_meaning=c["combined_meaning"],
            grounding_phrase=c["grounding_phrase"],
            CHANGE_DATE=CHANGE_DATE,
        )
    )
    print(f"wrote {out}")


# ----- L1 Process Group: dea:group-financial-model-conception -----

group_dir = ENT / "dea:group-financial-model-conception"
group_dir.mkdir(parents=True, exist_ok=True)
(group_dir / "candidates").mkdir(exist_ok=True)
(group_dir / "retired").mkdir(exist_ok=True)
(group_dir / "research").mkdir(exist_ok=True)

(group_dir / "README.md").write_text(
    """# Canonical Process Group: `dea:group-financial-model-conception`

This directory hosts the canonical Process Group record
for `dea:group-financial-model-conception`. The Process Group is a
catalog-owned record (not an OpenDEA metamodel entity) that organises
the Business Process responsibilities of conceiving the enterprise's
monetary model, finance strategy, and funding approach in the
**FinanceAndAccounting x Conceive** context (per ECF v2.4.0,
dea-metaframework/framework/domain-grounding.md §3.7).

Lands as part of CR-BP-21e (FinanceAndAccounting landing).
Substrate-neutral: applies to biological, artificial, and hybrid agents
without reclassification (ADR-ECF-002 §5, CR-ECF-007).

Composes the L2 Business Processes assigned to the Conceive cell of
FinanceAndAccounting:

- `dea:process-frame-finance-strategy` (lands under
  CR-BP-21e; remaining 2 Conceive L2s land in CR-BP-21e.1)
"""
)

(group_dir / "dea:group-financial-model-conception.yaml").write_text(
    f"""id: dea:group-financial-model-conception
type: ProcessGroup
version: 1.0.0

name: Financial Model Conception

# Normative definition (PG-006 / MECE).
definition: |
  The bounded Process Group that organises the Business Process
  responsibilities of conceiving the enterprise's monetary model,
  finance strategy, and funding and capital approach in the
  FinanceAndAccounting x Conceive context. This group covers the
  front-end work of framing the finance strategy, the monetary model,
  and the funding and capital approach. v2.4.0 grounding
  (domain-grounding.md §3.7): the domain is scoped to monetary
  consequence; planning (Finance) and recording (Accounting) are
  inseparable complements, and abstract 'value' is explicitly out of
  scope.

# Process Context reference (PG-003 enforces resolution).
process_context: dea:pc-fa-conceive

# Scope (MECE boundary; PG-006 depends on excludes).
scope:
  includes:
    - Finance strategy framing
    - Monetary model framing
    - Funding and capital approach framing
  excludes:
    - Strategic investment choices (strategy-direction x conceive)
    - Investment strategy governance (governance-existence x conceive)
    - Financial planning design (Design stage; adjacent context)
    - Finance capability build (Build stage; adjacent context)

# Intended enterprise outcomes.
outcomes:
  - Finance strategy is framed for the enterprise.
  - Monetary model is framed with bounded scope.
  - Funding and capital approach is framed.

# Canonical containment (PG-004 / PG-005 / PG-006 enforce).
composes:
  - source_id: dea:group-financial-model-conception
    target_id: dea:process-frame-finance-strategy
    relationship_type: composes
    direction: source-to-target
    status: active
    asserted_by: dea-team
    rationale: |
      The L2 process frames the enterprise's finance strategy,
      which is the v2.4.0 principal responsibility of the
      FinanceAndAccounting x Conceive cell. Lands under CR-BP-21e.
    evidence: docs/examples/frame-finance-strategy.md
    provenance:
      type: architecture-review
      reference: CR-BP-21e
      asserted_by: dea-team
      asserted_at: '{CHANGE_DATE}'

# Process Group kind (PG-007 enforces controlled vocabulary).
process_group_kind: end-to-end

# Discovery / governance status (mirrors CR-BP-19 register values).
status: accepted

# Catalog entry lifecycle (PG-008 enforces).
lifecycle_status: candidate

# ECF Conformance Gate (CR-ECF-CG-001..004).
ecfConformance:
  framework: EnterpriseConceptFramework
  contractVersion: '1.0.0'
  profile: dea:ecf@1.0.0
  status: conformant
  affiliation: inherits-catalog
  canonicalReferences:
    - kind: coordinate
      domain: FinanceAndAccounting
      stage: Conceive
      identifier: ecf:financeAccounting.conceive

# Evidence (CR-BP-11 register strength scale E0..E5).
evidence:
  - source: CR-BP-19 (register v2, ratified against ECF v2.4.0)
    claim: |
      This Process Group's coordinate is ratified-accepted in register
      v2. CR-BP-21e lands the corresponding L1 group; remaining 2
      register v2 L2 candidates for Conceive land in CR-BP-21e.1.
    strength: E4
    reference: entities/v1-alpha/dea:group-customer-lifecycle-management/research/l1-register.yaml

# Metadata (PG-006 cross-context overlap exception path lives here).
metadata:
  established_by: CR-BP-21e
  established_at: '{CHANGE_DATE}'
  cross_context_overlap: []
  change_history:
    - cr: CR-BP-21e
      date: '{CHANGE_DATE}'
      change: |
        Initial Process Group record; promoted from the CR-BP-19 register
        v2 (ratified against ECF v2.4.0) as part of the
        FinanceAndAccounting landing tranche. Composes the L2
        dea:process-frame-finance-strategy.

links:
  - rel: change-request
    href: change-requests/CR-BP-21e-finance-accounting-landing.md
  - rel: predecessor
    href: change-requests/CR-BP-19-l1-register-rederivation-ecf-v240.md
  - rel: research-register
    href: entities/v1-alpha/dea:group-customer-lifecycle-management/research/l1-register.yaml
"""
)
print(f"wrote {group_dir}/dea:group-financial-model-conception.yaml")


# ----- 5 L2 processes -----

L2_TEMPLATES = {
    "dea:process-frame-finance-strategy": {
        "name": "Frame Finance Strategy",
        "intent": "develop",
        "ptype": "management",
        "context": "dea:pc-fa-conceive",
        "verb": "Frame",
        "object": "Finance Strategy",
        "scope": "(all enterprise segments)",
        "trigger": "A finance strategy is needed because the enterprise is establishing a new monetary model, reframing an existing one, or responding to funding and capital shifts that require a re-conception of the finance strategy.",
        "description": "Operate the Frame Finance Strategy L2 process within the dea:pc-fa-conceive Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "A finance strategy with bounded monetary model and funding and capital approach is committed.",
        "outcome_statement": "A finance strategy with bounded monetary model and funding and capital approach is committed and ready to drive Design-stage planning.",
        "evidence_links": [
            {"type": "standard", "ref": "https://www.apqc.org/resource-overview/resource-library/apqc-process-classification-framework-pcf"},
        ],
    },
    "dea:process-design-financial-plan-structure": {
        "name": "Design Financial Plan Structure",
        "intent": "develop",
        "ptype": "management",
        "context": "dea:pc-fa-design",
        "verb": "Design",
        "object": "Financial Plan Structure",
        "scope": "(all enterprise segments)",
        "trigger": "A financial plan structure design is needed because the framed finance strategy requires bounded chart of accounts, cost allocation model, and financial controls designs.",
        "description": "Operate the Design Financial Plan Structure L2 process within the dea:pc-fa-design Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "A financial plan structure with chart of accounts, cost allocation model, and financial controls design is committed.",
        "outcome_statement": "A financial plan structure with chart of accounts, cost allocation model, and financial controls design is committed and ready for Build-stage planning.",
        "evidence_links": [
            {"type": "standard", "ref": "https://www.apqc.org/resource-overview/resource-library/apqc-process-classification-framework-pcf"},
        ],
    },
    "dea:process-secure-funding-facilities": {
        "name": "Secure Funding Facilities",
        "intent": "develop",
        "ptype": "core",
        "context": "dea:pc-fa-build",
        "verb": "Secure",
        "object": "Funding Facilities",
        "scope": "(all enterprise segments)",
        "trigger": "Funding facilities need to be secured because the designed financial plan structure requires committed funding lines, a stood-up finance function, and a deployed ERP finance module.",
        "description": "Operate the Secure Funding Facilities L2 process within the dea:pc-fa-build Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "Funding lines are secured, the finance function is stood up, and the ERP finance module is deployed.",
        "outcome_statement": "Funding lines are secured, the finance function is stood up, and the ERP finance module is deployed, ready for the Operate cell.",
        "evidence_links": [
            {"type": "standard", "ref": "https://www.apqc.org/resource-overview/resource-library/apqc-process-classification-framework-pcf"},
        ],
    },
    "dea:process-operate-general-ledger": {
        "name": "Operate General Ledger",
        "intent": "operate",
        "ptype": "core",
        "context": "dea:pc-fa-operate",
        "verb": "Operate",
        "object": "General Ledger",
        "scope": "(all enterprise segments)",
        "trigger": "General ledger operation is needed because the built finance capability is now in active operation and requires steady-state accounting, treasury, tax compliance, financial close, and reporting.",
        "description": "Operate the Operate General Ledger L2 process within the dea:pc-fa-operate Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "The general ledger is operated with accounts payable, accounts receivable, treasury, tax compliance, financial close, and reporting executed to period plan.",
        "outcome_statement": "The general ledger is operated with accounts payable, accounts receivable, treasury, tax compliance, financial close, and reporting executed to period plan.",
        "evidence_links": [
            {"type": "standard", "ref": "https://www.apqc.org/resource-overview/resource-library/apqc-process-classification-framework-pcf"},
        ],
    },
    "dea:process-conduct-cost-optimization-review": {
        "name": "Conduct Cost Optimization Review",
        "intent": "develop",
        "ptype": "management",
        "context": "dea:pc-fa-improve",
        "verb": "Conduct",
        "object": "Cost Optimization Review",
        "scope": "(all enterprise segments)",
        "trigger": "A cost optimization review is needed because cost signals, margin pressure, or control findings indicate that the monetary position, reporting, or financial controls need to be strengthened.",
        "description": "Operate the Conduct Cost Optimization Review L2 process within the dea:pc-fa-improve Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "Cost optimization review is conducted with findings committed for reporting, disclosure, and financial control strengthening.",
        "outcome_statement": "Cost optimization review is conducted with findings committed for reporting, disclosure, and financial control strengthening, ready to drive the next planning cycle.",
        "evidence_links": [
            {"type": "standard", "ref": "https://www.apqc.org/resource-overview/resource-library/apqc-process-classification-framework-pcf"},
        ],
    },
}


L2_TEMPLATE = """id: {eid}
name: {name}
type: Process
version: 1.0.0
lifecycle_status: candidate
status: candidate
process_intent: {intent}
process_type: {ptype}
process_specialization: []
description: '{description}
  '
trigger: '{trigger}
  '
outcome: '{outcome}
  '
identity:
  verb: {verb}
  object: {object}
  scope: {scope}
  outcome_statement: '{outcome_statement}
    '
  evidence_links:
{evidence_yaml}
relationships:
- source_id: {eid}
  relationship_type: serves
  target_id: {ecf_id}
ecfConformance:
  framework: EnterpriseConceptFramework
  contractVersion: 1.0.0
  profile: dea:ecf@1.0.0
  status: conformant
  affiliation: inherits-catalog
  canonicalReferences:
  - kind: coordinate
    domain: {domain}
    stage: {stage}
    identifier: ecf:{ecf_domain}.{ecf_stage}
metadata:
  established_by: CR-BP-21e
  established_at: '{CHANGE_DATE}'
  change_history:
  - cr: CR-BP-21e
    date: '{CHANGE_DATE}'
    change: |
      Initial L2 Process entry; lands as part of the CR-BP-21e
      FinanceAndAccounting landing tranche under ECF v2.4.0
      register v2 (CR-BP-19). Substrate-neutral per ADR-ECF-002
      §5 / CR-ECF-007: applies to biological, artificial, and
      hybrid agents without reclassification. One of the 5 L2
      landings targeting the 5 ratified cells of the
      FinanceAndAccounting domain.
links:
- rel: change-request
  href: change-requests/CR-BP-21e-finance-accounting-landing.md
- rel: process-context
  href: contexts/v1-alpha/{context_file}.yaml
context:
- ref: {context_id}
"""


def render_evidence(links):
    return "\n".join(f'  - type: {l["type"]}\n    ref: {l["ref"]}' for l in links)


ECF_DOMAIN_MAP = {
    "FinanceAndAccounting": "financeAccounting",
}


for eid, t in L2_TEMPLATES.items():
    pdir = ENT / eid
    pdir.mkdir(parents=True, exist_ok=True)
    (pdir / "candidates").mkdir(exist_ok=True)
    (pdir / "retired").mkdir(exist_ok=True)
    (pdir / "research").mkdir(exist_ok=True)
    context_id = t["context"]
    context_file = context_id.replace("dea:", "").replace(":", "-")
    domain = "FinanceAndAccounting"
    stage = context_id.split("-")[-1]
    stage_title = stage.capitalize()
    ecf_domain = ECF_DOMAIN_MAP[domain]
    ecf_stage = stage
    (pdir / "README.md").write_text(
        f"""# Canonical L2 Business Process: `{eid}`

This directory hosts the canonical L2 Business Process record
for `{eid}`. Lands as part of CR-BP-21e (FinanceAndAccounting
landing). Process Context: `{context_id}`. Substrate-neutral
(ADR-ECF-002 §5 / CR-ECF-007): applies to biological, artificial,
and hybrid agents without reclassification.
"""
    )
    (pdir / f"{eid}.yaml").write_text(
        L2_TEMPLATE.format(
            eid=eid,
            name=t["name"],
            intent=t["intent"],
            ptype=t["ptype"],
            description=t["description"],
            trigger=t["trigger"],
            outcome=t["outcome"],
            outcome_statement=t["outcome_statement"],
            verb=t["verb"],
            object=t["object"],
            scope=t["scope"],
            evidence_yaml=render_evidence(t["evidence_links"]),
            context=context_id,
            context_id=context_id,
            context_file=context_file,
            domain=domain,
            stage=stage_title,
            ecf_id=f"ecf:{ecf_domain}.{ecf_stage}",
            ecf_domain=ecf_domain,
            ecf_stage=ecf_stage,
            CHANGE_DATE=CHANGE_DATE,
        )
    )
    print(f"wrote {pdir}/{eid}.yaml")


print("\nDone. Next: regenerate CATALOG.yaml, append dispositions + tranche entries, run gates.")
