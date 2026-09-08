#!/usr/bin/env python3
"""Generate CR-BP-21b.1 artifacts (AgencyAndOrganization completion):
4 non-Conceive L1 groups + 13 remaining register v2 L2 processes.
Mirrors scripts/apply_phase_7a1_tranche.py (CR-BP-21a.1) with AO data.
Substrate-neutral vocabulary per CR-BP-21b §5 / ADR-ECF-002 §5.

Existing-record edits (Conceive group composes edges; AO context
processes lists) are applied as surgical text patches outside this
script — see the note at the bottom.

Run: python scripts/apply_phase_7b1_tranche.py
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).parent.parent
CTX = ROOT / "contexts/v1-alpha"
ENT = ROOT / "entities/v1-alpha"
CHANGE_DATE = "2026-09-08"
CR = "CR-BP-21b.1"
CR_FILE = "change-requests/CR-BP-21b.1-agency-organization-completion.md"

# ----- 13 L2 processes (remaining register v2 candidates) -----

L2S = [
    # Conceive (join existing dea:group-organization-and-agent-conception)
    {"eid": "dea:process-frame-organization-model",
     "name": "Frame Organization Model",
     "verb": "Frame", "object": "Organization Model",
     "context": "dea:pc-ao-conceive", "stage": "Conceive", "intent": "develop",
     "ptype": "management",
     "trigger": "An organization model framing is needed because the committed organization and agent strategy requires bounded structure principles, reporting spans, and coordination boundaries to become designable.",
     "outcome": "The organization model is framed with structure principles, reporting spans, and coordination boundaries.",
     "outcome_statement": "The organization model is framed with structure principles, reporting spans, and coordination boundaries, ready for role design."},
    {"eid": "dea:process-conceive-workforce-and-agent-mix",
     "name": "Conceive Workforce and Agent Mix",
     "verb": "Conceive", "object": "Workforce and Agent Mix",
     "context": "dea:pc-ao-conceive", "stage": "Conceive", "intent": "develop",
     "ptype": "management",
     "trigger": "A workforce and agent mix conception is needed because the committed organization and agent strategy requires bounded substrate proportions and capacity envelopes.",
     "outcome": "The workforce and agent mix is conceived with substrate proportions and capacity envelopes.",
     "outcome_statement": "The workforce and agent mix is conceived with substrate proportions and capacity envelopes, aligned to the agent capacity plan."},
    # Design (new group dea:group-organization-and-role-design)
    {"eid": "dea:process-design-role-catalogue",
     "name": "Design Role Catalogue",
     "verb": "Design", "object": "Role Catalogue",
     "context": "dea:pc-ao-design", "stage": "Design", "intent": "develop",
     "ptype": "management",
     "trigger": "A role catalogue design is needed because the framed organization model requires bounded role families, levels, and accountability boundaries.",
     "outcome": "The role catalogue is designed with role families, levels, and accountability boundaries.",
     "outcome_statement": "The role catalogue is designed with role families, levels, and accountability boundaries, ready for organization planning."},
    {"eid": "dea:process-design-competency-framework",
     "name": "Design Competency Framework",
     "verb": "Design", "object": "Competency Framework",
     "context": "dea:pc-ao-design", "stage": "Design", "intent": "develop",
     "ptype": "management",
     "trigger": "A competency framework design is needed because the designed organization structure requires bounded proficiency levels and assessment anchors.",
     "outcome": "The competency framework is designed with proficiency levels and assessment anchors.",
     "outcome_statement": "The competency framework is designed with proficiency levels and assessment anchors, ready for capability gap monitoring."},
    {"eid": "dea:process-design-agent-topology",
     "name": "Design Agent Topology",
     "verb": "Design", "object": "Agent Topology",
     "context": "dea:pc-ao-design", "stage": "Design", "intent": "develop",
     "ptype": "management",
     "trigger": "An agent topology design is needed because the framed organization model requires bounded human, artificial, and hybrid placement decisions.",
     "outcome": "The agent topology is designed with human, artificial, and hybrid placement and coordination patterns.",
     "outcome_statement": "The agent topology is designed with human, artificial, and hybrid placement and coordination patterns, ready for acquisition planning."},
    # Build (new group dea:group-agent-acquisition-and-onboarding)
    {"eid": "dea:process-build-contractor-and-partner-agent-pool",
     "name": "Build Contractor and Partner-Agent Pool",
     "verb": "Build", "object": "Contractor and Partner-Agent Pool",
     "context": "dea:pc-ao-build", "stage": "Build", "intent": "develop",
     "ptype": "core",
     "trigger": "A contractor and partner-agent pool build is needed because direct acquisition cannot serve surge or specialist demand within the required timeframes.",
     "outcome": "The contractor and partner-agent pool is built with vetted sources and activation paths.",
     "outcome_statement": "The contractor and partner-agent pool is built with vetted sources and activation paths, ready to serve surge demand."},
    # Operate (new group dea:group-agent-operations)
    {"eid": "dea:process-operate-payroll-and-benefits",
     "name": "Operate Payroll and Benefits",
     "verb": "Operate", "object": "Payroll and Benefits",
     "context": "dea:pc-ao-operate", "stage": "Operate", "intent": "operate",
     "ptype": "core",
     "trigger": "Payroll and benefits operation is needed because agents in service require accurate, on-time disbursement and statutory filings each cycle.",
     "outcome": "Payroll and benefits are operated with accurate, on-time disbursement.",
     "outcome_statement": "Payroll and benefits are operated with accurate, on-time disbursement and statutory filings recorded."},
    {"eid": "dea:process-operate-time-and-attendance",
     "name": "Operate Time and Attendance",
     "verb": "Operate", "object": "Time and Attendance",
     "context": "dea:pc-ao-operate", "stage": "Operate", "intent": "operate",
     "ptype": "core",
     "trigger": "Time and attendance operation is needed because agent service delivery requires accurate capture and exception handling to feed payroll execution.",
     "outcome": "Time and attendance are operated with accurate capture and exception handling.",
     "outcome_statement": "Time and attendance are operated with accurate capture and exception handling, feeding payroll execution."},
    {"eid": "dea:process-operate-learning-and-development",
     "name": "Operate Learning and Development",
     "verb": "Operate", "object": "Learning and Development",
     "context": "dea:pc-ao-operate", "stage": "Operate", "intent": "operate",
     "ptype": "core",
     "trigger": "Learning and development operation is needed because agents in service require scheduled delivery of development programmes with completion recorded.",
     "outcome": "Learning and development are operated with scheduled delivery and completion recorded.",
     "outcome_statement": "Learning and development are operated with scheduled delivery and completion recorded per agent."},
    {"eid": "dea:process-coordinate-collaboration",
     "name": "Coordinate Collaboration",
     "verb": "Coordinate", "object": "Collaboration",
     "context": "dea:pc-ao-operate", "stage": "Operate", "intent": "operate",
     "ptype": "management",
     "trigger": "Collaboration coordination is needed because agents and teams in service require shared workspaces and interaction norms to work coherently.",
     "outcome": "Collaboration is coordinated across agents and teams.",
     "outcome_statement": "Collaboration is coordinated across agents and teams with shared workspaces and interaction norms."},
    # Improve (new group dea:group-agent-and-organization-improvement)
    {"eid": "dea:process-conduct-engagement-and-alignment-review",
     "name": "Conduct Engagement and Alignment Review",
     "verb": "Conduct", "object": "Engagement and Alignment Review",
     "context": "dea:pc-ao-improve", "stage": "Improve", "intent": "develop",
     "ptype": "management",
     "trigger": "An engagement and alignment review is needed because the operating organization requires periodic evidence that agents remain engaged and aligned to direction.",
     "outcome": "Engagement and alignment are reviewed with findings committed.",
     "outcome_statement": "Engagement and alignment are reviewed, with findings feeding the workforce planning cycle."},
    {"eid": "dea:process-conduct-capability-gap-analysis",
     "name": "Conduct Capability Gap Analysis",
     "verb": "Conduct", "object": "Capability Gap Analysis",
     "context": "dea:pc-ao-improve", "stage": "Improve", "intent": "develop",
     "ptype": "management",
     "trigger": "A capability gap analysis is needed because the designed competency framework must be compared against the current agent population to expose gaps.",
     "outcome": "Capability gaps are analyzed with priorities committed.",
     "outcome_statement": "Capability gaps are analyzed against the competency framework, with priorities committed to the development plan."},
    {"eid": "dea:process-reorganize-structures",
     "name": "Reorganize Structures",
     "verb": "Reorganize", "object": "Structures",
     "context": "dea:pc-ao-improve", "stage": "Improve", "intent": "develop",
     "ptype": "management",
     "trigger": "A structures reorganization is needed because review findings or direction changes require bounded structural change with transition sequencing.",
     "outcome": "Structures are reorganized with transition sequencing and accountability handovers recorded.",
     "outcome_statement": "Structures are reorganized with transition sequencing and accountability handovers recorded, aligned to the organization plan."},
]

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
  scope: (all enterprise segments)
  outcome_statement: '{outcome_statement}
    '
  evidence_links:
  - type: standard
    ref: https://www.apqc.org/resource-overview/resource-library/apqc-process-classification-framework-pcf
relationships:
- source_id: {eid}
  relationship_type: serves
  target_id: ecf:agencyOrganization.{ecf_stage}
ecfConformance:
  framework: EnterpriseConceptFramework
  contractVersion: 1.0.0
  profile: dea:ecf@1.0.0
  status: conformant
  affiliation: inherits-catalog
  canonicalReferences:
  - kind: coordinate
    domain: AgencyAndOrganization
    stage: {stage}
    identifier: ecf:agencyOrganization.{ecf_stage}
metadata:
  established_by: {CR}
  established_at: '{CHANGE_DATE}'
  change_history:
  - cr: {CR}
    date: '{CHANGE_DATE}'
    change: |
      Initial L2 Process entry; lands as part of the {CR}
      AgencyAndOrganization completion tranche under ECF v2.4.0
      register v2 (CR-BP-19). Substrate-neutral per ADR-ECF-002
      section 5 / CR-ECF-007: applies to biological, artificial,
      and hybrid agents without reclassification. Closes the
      remaining register v2 L2 candidates for this cell.
links:
- rel: change-request
  href: {CR_FILE}
- rel: process-context
  href: contexts/v1-alpha/{context_file}.yaml
context:
- ref: {context_id}
"""

for t in L2S:
    eid = t["eid"]
    pdir = ENT / eid
    pdir.mkdir(parents=True, exist_ok=True)
    for sub in ("candidates", "retired", "research"):
        (pdir / sub).mkdir(exist_ok=True)
    context_id = t["context"]
    context_file = context_id.replace("dea:", "").replace(":", "-")
    ecf_stage = t["stage"].lower()
    (pdir / "README.md").write_text(
        f"""# Canonical L2 Business Process: `{eid}`

This directory hosts the canonical L2 Business Process record
for `{eid}`. Lands as part of {CR} (AgencyAndOrganization
completion). Process Context: `{context_id}`.
"""
    )
    (pdir / f"{eid}.yaml").write_text(
        L2_TEMPLATE.format(
            eid=eid,
            name=t["name"],
            intent=t["intent"],
            ptype=t["ptype"],
            description=(
                f"Operate the {t['name']} L2 process within the {context_id} "
                "Cell Charter. See trigger and outcome for the bounded work this "
                "process owns; see identity.outcome_statement for the testable "
                "outcome the process produces."
            ),
            trigger=t["trigger"],
            outcome=t["outcome"],
            outcome_statement=t["outcome_statement"],
            verb=t["verb"],
            object=t["object"],
            context=context_id,
            context_id=context_id,
            context_file=context_file,
            stage=t["stage"],
            ecf_stage=ecf_stage,
            CR=CR,
            CR_FILE=CR_FILE,
            CHANGE_DATE=CHANGE_DATE,
        )
    )
    print(f"wrote {pdir}/{eid}.yaml")


# ----- 4 new L1 Process Groups (non-Conceive AO cells) -----

GROUPS = [
    {
        "gid": "dea:group-organization-and-role-design",
        "name": "Organization and Role Design",
        "context": "dea:pc-ao-design",
        "stage": "Design",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of designing the organization, its roles, its "
            "competency framework, and its agent topology in the "
            "AgencyAndOrganization x Design context. Substrate-neutral per "
            "ADR-ECF-002 section 5: covers biological, artificial, and "
            "hybrid agents. v2.4.0 grounding (domain-grounding.md §3.3)."
        ),
        "includes": [
            "Organization structure design",
            "Role catalogue design",
            "Competency framework design",
            "Agent topology design (human/artificial/hybrid)",
        ],
        "excludes": [
            "Specific job description authoring (Build stage; adjacent context)",
            "Organization model framing (Conceive stage; adjacent context)",
            "Product or service design (product-value x design)",
        ],
        "outcomes": [
            "Organization structure is designed with bounded spans.",
            "Role catalogue and competency framework are designed.",
            "Agent topology is designed with substrate placement decisions.",
        ],
        "composes": [
            ("dea:process-design-organization-structure", "landed CR-BP-21b"),
            ("dea:process-design-role-catalogue", CR),
            ("dea:process-design-competency-framework", CR),
            ("dea:process-design-agent-topology", CR),
        ],
        "ecf_stage": "design",
    },
    {
        "gid": "dea:group-agent-acquisition-and-onboarding",
        "name": "Agent Acquisition and Onboarding",
        "context": "dea:pc-ao-build",
        "stage": "Build",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of acquiring and onboarding agents of all "
            "substrates in the AgencyAndOrganization x Build context: "
            "sourcing and recruiting human talent, provisioning artificial "
            "agents (model deployment, API integration), onboarding and "
            "integrating agents, and building the contractor and "
            "partner-agent pool. v2.4.0 grounding (domain-grounding.md "
            "§3.3, Acquisition and Onboarding sub-concern)."
        ),
        "includes": [
            "Agent sourcing, recruiting, provisioning (all substrates)",
            "Agent onboarding and integration",
            "Contractor and partner-agent pool build",
        ],
        "excludes": [
            "Supplier relationship onboarding (party-relationship)",
            "Agent topology design (Design stage; adjacent context)",
            "Agent performance operation (Operate stage; adjacent context)",
        ],
        "outcomes": [
            "Agents are acquired and onboarded per the designed topology.",
            "Contractor and partner-agent pool is built with vetted sources.",
        ],
        "composes": [
            ("dea:process-acquire-and-onboard-agents", "landed CR-BP-21b"),
            ("dea:process-build-contractor-and-partner-agent-pool", CR),
        ],
        "ecf_stage": "build",
    },
    {
        "gid": "dea:group-agent-operations",
        "name": "Agent Operations",
        "context": "dea:pc-ao-operate",
        "stage": "Operate",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of operating agents in service in the "
            "AgencyAndOrganization x Operate context: agent performance "
            "operation, payroll and benefits, time and attendance, learning "
            "and development delivery (training for humans, fine-tuning for "
            "artificial agents), and collaboration coordination. "
            "Substrate-neutral per ADR-ECF-002 section 5. v2.4.0 grounding "
            "(domain-grounding.md §3.3)."
        ),
        "includes": [
            "Agent performance operation",
            "Payroll and benefits operation",
            "Time and attendance operation",
            "Learning and development delivery (all substrates)",
            "Collaboration coordination",
        ],
        "excludes": [
            "Agent capacity planning (Conceive/Design; adjacent contexts)",
            "Service delivery to customers (product-value x operate)",
            "Agent development improvement (Improve stage; adjacent context)",
        ],
        "outcomes": [
            "Agent performance is operated with review cadence.",
            "Payroll, benefits, time, and attendance are operated accurately.",
            "Learning and development are delivered with completion recorded.",
            "Collaboration is coordinated across agents and teams.",
        ],
        "composes": [
            ("dea:process-operate-agent-performance", "landed CR-BP-21b"),
            ("dea:process-operate-payroll-and-benefits", CR),
            ("dea:process-operate-time-and-attendance", CR),
            ("dea:process-operate-learning-and-development", CR),
            ("dea:process-coordinate-collaboration", CR),
        ],
        "ecf_stage": "operate",
    },
    {
        "gid": "dea:group-agent-and-organization-improvement",
        "name": "Agent and Organization Improvement",
        "context": "dea:pc-ao-improve",
        "stage": "Improve",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of improving agents and the organization in "
            "the AgencyAndOrganization x Improve context: agent and "
            "organization development, engagement and alignment review, "
            "capability gap analysis, and structural reorganization. "
            "v2.4.0 grounding (domain-grounding.md §3.3)."
        ),
        "includes": [
            "Agent and organization development",
            "Engagement and alignment review",
            "Capability gap analysis",
            "Structural reorganization",
        ],
        "excludes": [
            "Continuous improvement of business capabilities (owning domains)",
            "Learning delivery operation (Operate stage; adjacent context)",
        ],
        "outcomes": [
            "Agents and the organization are developed on evidence.",
            "Engagement, alignment, and capability gaps are reviewed.",
            "Structures are reorganized with transition sequencing.",
        ],
        "composes": [
            ("dea:process-develop-agents-and-organization", "landed CR-BP-21b"),
            ("dea:process-conduct-engagement-and-alignment-review", CR),
            ("dea:process-conduct-capability-gap-analysis", CR),
            ("dea:process-reorganize-structures", CR),
        ],
        "ecf_stage": "improve",
    },
]


def render_composes(composes):
    lines = []
    for target, note in composes:
        lines.append(f"""  - source_id: {{GID}}
    target_id: {target}
    relationship_type: composes
    direction: source-to-target
    status: active
    asserted_by: dea-team
    rationale: |
      The L2 process belongs to this cell per register v2 ({note}).
    provenance:
      type: architecture-review
      reference: {CR}
      asserted_by: dea-team
      asserted_at: '{CHANGE_DATE}'""")
    return "\n".join(lines)


GROUP_TEMPLATE = """id: {GID}
type: ProcessGroup
version: 1.0.0

name: {name}

# Normative definition (PG-006 / MECE).
definition: |
  {definition}

# Process Context reference (PG-003 enforces resolution).
process_context: {context}

# Scope (MECE boundary; PG-006 depends on excludes).
scope:
  includes:
{includes_yaml}
  excludes:
{excludes_yaml}

# Intended enterprise outcomes.
outcomes:
{outcomes_yaml}

# Canonical containment (PG-004 / PG-005 / PG-006 enforce).
composes:
{composes_yaml}

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
      domain: AgencyAndOrganization
      stage: {stage}
      identifier: ecf:agencyOrganization.{ecf_stage}

# Evidence (CR-BP-11 register strength scale E0..E5).
evidence:
  - source: CR-BP-19 (register v2, ratified against ECF v2.4.0)
    claim: |
      This Process Group's coordinate is ratified-accepted in register
      v2. {CR} lands the corresponding L1 group as part of the
      AgencyAndOrganization completion tranche.
    strength: E4
    reference: entities/v1-alpha/dea:group-customer-lifecycle-management/research/l1-register.yaml

# Metadata (PG-006 cross-context overlap exception path lives here).
metadata:
  established_by: {CR}
  established_at: '{CHANGE_DATE}'
  cross_context_overlap: []
  change_history:
    - cr: {CR}
      date: '{CHANGE_DATE}'
      change: |
        Initial Process Group record; promoted from the CR-BP-19 register
        v2 (ratified against ECF v2.4.0) as part of the {CR}
        AgencyAndOrganization completion tranche. Substrate-neutral per
        ADR-ECF-002 section 5 / CR-ECF-007.

links:
  - rel: change-request
    href: {CR_FILE}
  - rel: predecessor
    href: change-requests/CR-BP-19-l1-register-rederivation-ecf-v240.md
  - rel: research-register
    href: entities/v1-alpha/dea:group-customer-lifecycle-management/research/l1-register.yaml
"""


def render_simple_list(items, indent="    - "):
    return "\n".join(f"{indent}{i}" for i in items)


for g in GROUPS:
    gid = g["gid"]
    gdir = ENT / gid
    gdir.mkdir(parents=True, exist_ok=True)
    for sub in ("candidates", "retired", "research"):
        (gdir / sub).mkdir(exist_ok=True)
    (gdir / "README.md").write_text(
        f"""# Canonical Process Group: `{gid}`

This directory hosts the canonical Process Group record for `{gid}`
(AgencyAndOrganization x {g['stage']}). Lands as part of {CR}
(AgencyAndOrganization completion). Composes the L2 Business Processes
of the {g['stage']} cell.
"""
    )
    body = GROUP_TEMPLATE.format(
        GID=gid,
        name=g["name"],
        definition=g["definition"],
        context=g["context"],
        includes_yaml=render_simple_list(g["includes"]),
        excludes_yaml=render_simple_list(g["excludes"]),
        outcomes_yaml=render_simple_list(g["outcomes"], indent="  - "),
        composes_yaml=render_composes(g["composes"]).format(GID=gid),
        stage=g["stage"],
        ecf_stage=g["ecf_stage"],
        CR=CR,
        CR_FILE=CR_FILE,
        CHANGE_DATE=CHANGE_DATE,
    )
    (gdir / f"{gid}.yaml").write_text(body)
    print(f"wrote {gdir}/{gid}.yaml")

# NOTE: in-place edits applied as surgical text patches outside this
# script (a yaml round-trip strips authored comments):
#   1. dea:group-organization-and-agent-conception.yaml — +2 composes
#      edges (frame-organization-model, conceive-workforce-and-agent-mix)
#      plus a CR-BP-21b.1 change_history entry.
#   2. dea-pc-ao-{conceive,design,build,operate,improve}.yaml —
#      processes: list extended with the new cell L2s plus a
#      CR-BP-21b.1 change_history entry.

print("\nDone. Next: text-patch existing records, dispositions, "
      "tranche plan, register audit, regenerate, gates.")
