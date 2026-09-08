#!/usr/bin/env python3
"""Generate CR-BP-21b artifacts (AgencyAndOrganization landing):
4 process contexts, 1 L1 group, 5 L2 processes. Mirrors the
CR-BP-21a (StrategyAndDirection) pattern but with substrate-neutral
naming per ADR-ECF-002 §5 / CR-ECF-007.

Run: python scripts/apply_phase_7b_tranche.py
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).parent.parent
CTX = ROOT / "contexts/v1-alpha"
ENT = ROOT / "entities/v1-alpha"
CHANGE_DATE = "2026-09-07"


CONTEXTS = [
    {
        "filename": "dea-pc-ao-conceive",
        "id": "dea:pc-ao-conceive",
        "domain": "AgencyAndOrganization",
        "stage": "Conceive",
        "name": "Agent Capacity and Organization Conception",
        "definition": (
            "The bounded enterprise context for **conceiving** the enterprise's "
            "agentive and organizational fabric in the **Agency & Organization** "
            "domain. This context addresses the front-end work of framing agent "
            "capacity strategy, framing the organization model, and conceiving "
            "the workforce-and-agent mix. v2.4.0: substrate-independent — "
            "applies to biological, artificial, and hybrid agents without "
            "reclassification (ADR-ECF-002 §5, CR-ECF-007)."
        ),
        "includes": [
            "Agent capacity strategy framing",
            "Organization model framing",
            "Workforce and agent mix conception",
            "Agent capability requirement conception",
        ],
        "excludes": [
            "Strategy and direction (strategy-direction x conceive; adjacent domain)",
            "Operational execution (enablement-operations x conceive; adjacent domain)",
            "Compensation decisions (finance-accounting x conceive; adjacent domain)",
            "Organizational architecture design (Design stage; adjacent context)",
            "Agent acquisition (Build stage; adjacent context)",
        ],
        "outcomes": [
            "Agent capacity strategy is framed for the enterprise.",
            "Organization model is framed as a stable subject.",
            "Workforce and agent mix is conceived substrate-neutrally.",
            "Agent capability requirements are documented.",
        ],
        "adjacent": [
            "dea:pc-ao-design", "dea:pc-ao-build", "dea:pc-ao-operate", "dea:pc-ao-improve",
        ],
        "processes": ["dea:process-frame-organization-and-agent-strategy"],
        "l1_candidates": ["Agent Capacity Conception", "Organization Conception"],
        "grounding_phrase": "conception of agent capacity, organization model, and workforce/agent mix",
        "enterprise_concern": "the conception of the enterprise's agentive and organizational fabric.",
        "lifecycle_concern": "framing agent capacity, organization model, and workforce/agent mix.",
        "combined_meaning": "The front-end work of framing agent capacity strategy, the organization model, and the workforce-and-agent mix as a substrate-neutral subject.",
    },
    {
        "filename": "dea-pc-ao-design",
        "id": "dea:pc-ao-design",
        "domain": "AgencyAndOrganization",
        "stage": "Design",
        "name": "Organization and Agent Topology Design",
        "definition": (
            "The bounded enterprise context for **designing** the organization "
            "structure, role catalogue, competency framework, and agent topology of "
            "the enterprise in the **Agency & Organization** domain. This context "
            "addresses the analytical work of producing designs for organizational "
            "architecture, agent topology, role definitions, and authority chains. "
            "v2.4.0: substrate-neutral — applies to biological, artificial, and "
            "hybrid agents without reclassification."
        ),
        "includes": [
            "Organization structure design",
            "Role catalogue design",
            "Competency framework design",
            "Agent topology design",
        ],
        "excludes": [
            "Agent capacity strategy framing (Conceive stage; adjacent context)",
            "Agent acquisition (Build stage; adjacent context)",
            "Strategic direction design (strategy-direction x design; adjacent domain)",
            "Product design (product-value x design; adjacent domain)",
        ],
        "outcomes": [
            "Organization structure is designed with bounded authority chains.",
            "Role catalogue is designed for the agentive mix.",
            "Competency framework is designed substrate-neutrally.",
            "Agent topology is designed for biological, artificial, and hybrid agents.",
        ],
        "adjacent": [
            "dea:pc-ao-conceive", "dea:pc-ao-build", "dea:pc-ao-operate", "dea:pc-ao-improve",
        ],
        "processes": ["dea:process-design-organization-structure"],
        "l1_candidates": ["Organization and Role Design", "Agent Topology Design"],
        "grounding_phrase": "design of organization structure, roles, competencies, and agent topology",
        "enterprise_concern": "the design of the enterprise's organizational architecture.",
        "lifecycle_concern": "designing organization structure, roles, competencies, and agent topology.",
        "combined_meaning": "The analytical work of producing designs for organizational architecture, agent topology, role definitions, and authority chains.",
    },
    {
        "filename": "dea-pc-ao-build",
        "id": "dea:pc-ao-build",
        "domain": "AgencyAndOrganization",
        "stage": "Build",
        "name": "Agent Acquisition and Onboarding",
        "definition": (
            "The bounded enterprise context for **acquiring and onboarding** the "
            "agents of the enterprise in the **Agency & Organization** domain. "
            "This context addresses the constructive work of sourcing and "
            "provisioning agents, onboarding and integrating them, and building "
            "the contractor and partner-agent pool. v2.4.0: substrate-neutral — "
            "acquisition covers recruitment (biological), model deployment and "
            "API integration (artificial), and hybrid provisioning."
        ),
        "includes": [
            "Agent acquisition",
            "Agent onboarding and integration",
            "Contractor and partner-agent pool build",
            "Agent provisioning configuration",
        ],
        "excludes": [
            "Organization structure design (Design stage; adjacent context)",
            "External party engagement (party-relationship x build; adjacent domain)",
            "Operational execution (enablement-operations x build; adjacent domain)",
        ],
        "outcomes": [
            "Agents are acquired for the enterprise.",
            "Agents are onboarded and integrated into the organization.",
            "Contractor and partner-agent pool is built and ready.",
            "Agent provisioning configurations are committed.",
        ],
        "adjacent": [
            "dea:pc-ao-conceive", "dea:pc-ao-design", "dea:pc-ao-operate", "dea:pc-ao-improve",
        ],
        "processes": ["dea:process-acquire-and-onboard-agents"],
        "l1_candidates": ["Agent Acquisition", "Agent Onboarding"],
        "grounding_phrase": "acquisition, provisioning, and onboarding of agents",
        "enterprise_concern": "the acquisition and provisioning of the enterprise's agents.",
        "lifecycle_concern": "acquiring, provisioning, and integrating agents into the organization.",
        "combined_meaning": "The constructive work of sourcing, provisioning, onboarding, and integrating agents (biological, artificial, and hybrid).",
    },
    {
        "filename": "dea-pc-ao-operate",
        "id": "dea:pc-ao-operate",
        "domain": "AgencyAndOrganization",
        "stage": "Operate",
        "name": "Agent Operations and Performance",
        "definition": (
            "The bounded enterprise context for **operating** the agent performance, "
            "collaboration, and lifecycle operations of the enterprise in the "
            "**Agency & Organization** domain. This context addresses the steady-"
            "state work of operating agent performance, coordination and "
            "collaboration, time and attendance, and learning and development "
            "operations. v2.4.0: substrate-neutral — applies to biological, "
            "artificial, and hybrid agents without reclassification."
        ),
        "includes": [
            "Agent performance operation",
            "Coordination and collaboration operation",
            "Time and attendance operation",
            "Compensation operation",
            "Learning and development operation",
        ],
        "excludes": [
            "Agent acquisition (Build stage; adjacent context)",
            "Agent development (Improve stage; adjacent context)",
            "Operational execution (enablement-operations x operate; adjacent domain)",
            "Compensation accounting (finance-accounting x operate; adjacent domain)",
        ],
        "outcomes": [
            "Agent performance is operated across the agentive mix.",
            "Coordination and collaboration are operated substrate-neutrally.",
            "Time and attendance are operated across the agentive mix.",
            "Compensation is operated against the workforce policy.",
            "Learning and development are operated across the agentive mix.",
        ],
        "adjacent": [
            "dea:pc-ao-conceive", "dea:pc-ao-design", "dea:pc-ao-build", "dea:pc-ao-improve",
        ],
        "processes": ["dea:process-operate-agent-performance"],
        "l1_candidates": ["Agent Operations", "Performance and Development Operation", "Coordination Operation"],
        "grounding_phrase": "operation of agent performance, collaboration, and lifecycle",
        "enterprise_concern": "the steady-state operation of the enterprise's agent performance.",
        "lifecycle_concern": "operating agent performance, collaboration, time and attendance, compensation, and learning.",
        "combined_meaning": "The steady-state work of operating agent performance, coordination, and lifecycle across biological, artificial, and hybrid agents.",
    },
    {
        "filename": "dea-pc-ao-improve",
        "id": "dea:pc-ao-improve",
        "domain": "AgencyAndOrganization",
        "stage": "Improve",
        "name": "Agent Development and Organization Improvement",
        "definition": (
            "The bounded enterprise context for **improving** the agents and "
            "organization of the enterprise in the **Agency & Organization** "
            "domain. This context addresses the learning and adaptation work of "
            "conducting engagement and alignment reviews, capability gap analysis, "
            "reorganization, and agent performance improvement. v2.4.0: "
            "substrate-neutral — applies to biological, artificial, and hybrid "
            "agents without reclassification."
        ),
        "includes": [
            "Engagement and alignment review",
            "Capability gap analysis",
            "Structure reorganization",
            "Agent performance improvement",
        ],
        "excludes": [
            "Agent performance operation (Operate stage; adjacent context)",
            "Strategic adaptation (strategy-direction x improve; adjacent domain)",
            "Capability improvement of receiving domains (owning domains)",
        ],
        "outcomes": [
            "Engagement and alignment review is conducted substrate-neutrally.",
            "Capability gap analysis is conducted.",
            "Structure reorganization is committed when needed.",
            "Agent performance improvement is delivered.",
        ],
        "adjacent": [
            "dea:pc-ao-conceive", "dea:pc-ao-design", "dea:pc-ao-build", "dea:pc-ao-operate",
        ],
        "processes": ["dea:process-develop-agents-and-organization"],
        "l1_candidates": ["Agent Development Improvement", "Organization Improvement"],
        "grounding_phrase": "improvement of agents and organization",
        "enterprise_concern": "the improvement of the enterprise's agents and organization.",
        "lifecycle_concern": "improving engagement, capability, structure, and agent performance.",
        "combined_meaning": "The learning and adaptation work of improving engagement, capability, structure, and agent performance substrate-neutrally.",
    },
]


def render_list(items, indent="    - "):
    return "\n".join(f"{indent}{i}" for i in items)


def render_adjacent_boundaries(stage, adjacent):
    lines = []
    for a in adjacent:
        short = a.replace("dea:", "")
        lines.append(f'    - "dea:{short} (adjacent context): agentive flow between {stage} and the adjacent cell."')
    return "\n".join(lines)


CONTEXT_TEMPLATE = """# Process Context Cell Charter: {domain} x {stage}.
#
# Lands as part of CR-BP-21b (AgencyAndOrganization landing, second
# unadmitted-domain tranche under ECF v2.4.0 register v2 / CR-BP-19).
# Carries the full Cell Charter (CR-BP-02 §7).
#
# v2.4.0 grounding: dea-metaframework/framework/domain-grounding.md §3.3
# (Agency & Organization: {grounding_phrase}).
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
  enterprise_concern: "Agency & Organization: {enterprise_concern}"
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
established_by: CR-BP-21b
established_at: '{CHANGE_DATE}'

# Change history.
change_history:
  - cr: CR-BP-21b
    date: '{CHANGE_DATE}'
    change: |
      Initial Process Context record; promoted from the CR-BP-19
      register v2 (ratified against ECF v2.4.0) as part of the
      AgencyAndOrganization landing tranche. Substrate-neutral
      per ADR-ECF-002 §5 / CR-ECF-007.

links:
  - rel: change-request
    href: change-requests/CR-BP-21b-agency-organization-landing.md
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


# ----- L1 Process Group: dea:group-organization-and-agent-conception -----

group_dir = ENT / "dea:group-organization-and-agent-conception"
group_dir.mkdir(parents=True, exist_ok=True)
(group_dir / "candidates").mkdir(exist_ok=True)
(group_dir / "retired").mkdir(exist_ok=True)
(group_dir / "research").mkdir(exist_ok=True)

(group_dir / "README.md").write_text(
    """# Canonical Process Group: `dea:group-organization-and-agent-conception`

This directory hosts the canonical Process Group record
for `dea:group-organization-and-agent-conception`. The Process Group is a
catalog-owned record (not an OpenDEA metamodel entity) that organises
the Business Process responsibilities of conceiving the enterprise's
agentive and organizational fabric in the **AgencyAndOrganization ×
Conceive** context (per ECF v2.4.0,
dea-metaframework/framework/domain-grounding.md §3.3).

Lands as part of CR-BP-21b (AgencyAndOrganization landing).
Substrate-neutral: applies to biological, artificial, and hybrid agents
without reclassification (ADR-ECF-002 §5, CR-ECF-007). The legacy
v2.3.0 "People & Organization" wording is replaced with "Agency &
Organization" to satisfy the Substrate Independence Stress Test.

Composes the L2 Business Processes assigned to the Conceive cell of
AgencyAndOrganization:

- `dea:process-frame-organization-and-agent-strategy` (lands under
  CR-BP-21b; remaining 2 Conceive L2s land in CR-BP-21b.1)
"""
)

(group_dir / "dea:group-organization-and-agent-conception.yaml").write_text(
    f"""id: dea:group-organization-and-agent-conception
type: ProcessGroup
version: 1.0.0

name: Organization and Agent Conception

# Normative definition (PG-006 / MECE).
definition: |
  The bounded Process Group that organises the Business Process
  responsibilities of conceiving the enterprise's agentive and
  organizational fabric in the AgencyAndOrganization × Conceive context.
  This group covers the front-end work of framing agent capacity
  strategy, framing the organization model, and conceiving the
  workforce-and-agent mix. v2.4.0 grounding (domain-grounding.md
  §3.3): the domain is substrate-independent; the constituent agents
  may be biological, artificial, or hybrid. The Process Group manages
  organization as a stable subject — the durable pattern of roles,
  authority, collaboration, and coordination through which agency is
  directed.

# Process Context reference (PG-003 enforces resolution).
process_context: dea:pc-ao-conceive

# Scope (MECE boundary; PG-006 depends on excludes).
scope:
  includes:
    - Agent capacity strategy framing
    - Organization model framing
    - Workforce and agent mix conception
    - Agent capability requirement conception
  excludes:
    - Constitutional mandate and authority (governance-existence x conceive)
    - Strategic direction conception (strategy-direction x conceive)
    - Operational execution (enablement-operations)
    - Compensation decisions (finance-accounting x conceive)
    - Organizational architecture design (Design stage; adjacent context)
    - Agent acquisition (Build stage; adjacent context)

# Intended enterprise outcomes.
outcomes:
  - Agent capacity strategy is framed for the enterprise.
  - Organization model is framed as a stable subject.
  - Workforce and agent mix is conceived substrate-neutrally.
  - Agent capability requirements are documented.

# Canonical containment (PG-004 / PG-005 / PG-006 enforce).
composes:
  - source_id: dea:group-organization-and-agent-conception
    target_id: dea:process-frame-organization-and-agent-strategy
    relationship_type: composes
    direction: source-to-target
    status: active
    asserted_by: dea-team
    rationale: |
      The L2 process frames the enterprise's organization and agent
      strategy, which is the v2.4.0 principal responsibility of the
      AgencyAndOrganization x Conceive cell. Lands under CR-BP-21b
      with substrate-neutral vocabulary per ADR-ECF-002 §5.
    evidence: docs/examples/frame-organization-and-agent-strategy.md
    provenance:
      type: architecture-review
      reference: CR-BP-21b
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
      domain: AgencyAndOrganization
      stage: Conceive
      identifier: ecf:agencyOrganization.conceive

# Evidence (CR-BP-11 register strength scale E0..E5).
evidence:
  - source: CR-BP-19 (register v2, ratified against ECF v2.4.0)
    claim: |
      This Process Group's coordinate is ratified-accepted in register
      v2. CR-BP-21b lands the corresponding L1 group substrate-
      neutrally; remaining 2 register v2 L2 candidates for Conceive
      land in CR-BP-21b.1.
    strength: E4
    reference: entities/v1-alpha/dea:group-customer-lifecycle-management/research/l1-register.yaml

# Metadata (PG-006 cross-context overlap exception path lives here).
metadata:
  established_by: CR-BP-21b
  established_at: '{CHANGE_DATE}'
  cross_context_overlap: []
  change_history:
    - cr: CR-BP-21b
      date: '{CHANGE_DATE}'
      change: |
        Initial Process Group record; promoted from the CR-BP-19 register
        v2 (ratified against ECF v2.4.0) as part of the
        AgencyAndOrganization landing tranche. Substrate-neutral per
        ADR-ECF-002 §5 / CR-ECF-007. Composes the L2
        dea:process-frame-organization-and-agent-strategy.

links:
  - rel: change-request
    href: change-requests/CR-BP-21b-agency-organization-landing.md
  - rel: predecessor
    href: change-requests/CR-BP-19-l1-register-rederivation-ecf-v240.md
  - rel: research-register
    href: entities/v1-alpha/dea:group-customer-lifecycle-management/research/l1-register.yaml
"""
)
print(f"wrote {group_dir}/dea:group-organization-and-agent-conception.yaml")


# ----- 5 L2 processes (substrate-neutral naming) -----

L2_TEMPLATES = {
    "dea:process-frame-organization-and-agent-strategy": {
        "name": "Frame Organization and Agent Strategy",
        "intent": "develop",
        "ptype": "management",
        "context": "dea:pc-ao-conceive",
        "verb": "Frame",
        "object": "Organization and Agent Strategy",
        "scope": "(all enterprise segments)",
        "trigger": "A new organization and agent strategy is needed because the enterprise is establishing a new agentive fabric, reframing an existing one, or responding to substrate shifts (e.g., introduction of artificial agents into the workforce mix) that require board-level realignment.",
        "description": "Operate the Frame Organization and Agent Strategy L2 process within the dea:pc-ao-conceive Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "An organization and agent strategy with bounded agent capacity, organization model, and workforce-and-agent mix is committed.",
        "outcome_statement": "An organization and agent strategy with bounded agent capacity, organization model, and workforce-and-agent mix is committed and ready to drive Design work, substrate-neutrally across biological, artificial, and hybrid agents.",
        "evidence_links": [
            {"type": "standard", "ref": "https://www.apqc.org/resource-overview/resource-library/apqc-process-classification-framework-pcf"},
        ],
    },
    "dea:process-design-organization-structure": {
        "name": "Design Organization Structure",
        "intent": "develop",
        "ptype": "management",
        "context": "dea:pc-ao-design",
        "verb": "Design",
        "object": "Organization Structure",
        "scope": "(all enterprise segments)",
        "trigger": "An organization structure design is needed because the framed organization and agent strategy requires bounded organizational architecture, agent topology, role definitions, and authority chains.",
        "description": "Operate the Design Organization Structure L2 process within the dea:pc-ao-design Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "An organization structure design with bounded authority chains, role catalogue, competency framework, and agent topology is committed.",
        "outcome_statement": "An organization structure design with bounded authority chains, role catalogue, competency framework, and agent topology is committed and ready for the Build cell, substrate-neutrally across biological, artificial, and hybrid agents.",
        "evidence_links": [
            {"type": "standard", "ref": "https://www.apqc.org/resource-overview/resource-library/apqc-process-classification-framework-pcf"},
        ],
    },
    "dea:process-acquire-and-onboard-agents": {
        "name": "Acquire and Onboard Agents",
        "intent": "develop",
        "ptype": "core",
        "context": "dea:pc-ao-build",
        "verb": "Acquire",
        "object": "Agents",
        "scope": "(all enterprise segments)",
        "trigger": "An agent acquisition is needed because the designed organization structure requires bounded agent provisioning, onboarding, and integration to staff the organization.",
        "description": "Operate the Acquire and Onboard Agents L2 process within the dea:pc-ao-build Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "Agents are acquired, onboarded, and integrated into the organization substrate-neutrally.",
        "outcome_statement": "Agents are acquired (recruitment for biological, model deployment and API integration for artificial), onboarded, integrated, and ready for the Operate cell, substrate-neutrally across the agentive mix.",
        "evidence_links": [
            {"type": "standard", "ref": "https://www.apqc.org/resource-overview/resource-library/apqc-process-classification-framework-pcf"},
        ],
    },
    "dea:process-operate-agent-performance": {
        "name": "Operate Agent Performance",
        "intent": "operate",
        "ptype": "management",
        "context": "dea:pc-ao-operate",
        "verb": "Operate",
        "object": "Agent Performance",
        "scope": "(all enterprise segments)",
        "trigger": "Agent performance operation is needed because the onboarded agents are now in active operation across the organization and require steady-state performance, coordination, compensation, and learning operations.",
        "description": "Operate the Operate Agent Performance L2 process within the dea:pc-ao-operate Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "Agent performance is operated substrate-neutrally across the agentive mix.",
        "outcome_statement": "Agent performance is operated substrate-neutrally across the agentive mix, including coordination and collaboration, time and attendance, compensation, and learning and development.",
        "evidence_links": [
            {"type": "standard", "ref": "https://www.apqc.org/resource-overview/resource-library/apqc-process-classification-framework-pcf"},
        ],
    },
    "dea:process-develop-agents-and-organization": {
        "name": "Develop Agents and Organization",
        "intent": "develop",
        "ptype": "management",
        "context": "dea:pc-ao-improve",
        "verb": "Develop",
        "object": "Agents and Organization",
        "scope": "(all enterprise segments)",
        "trigger": "Agent and organization development is needed because engagement signals, capability gaps, or structure reorganization requirements indicate that the agents or the organization itself need to be improved substrate-neutrally.",
        "description": "Operate the Develop Agents and Organization L2 process within the dea:pc-ao-improve Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "Agents and organization are developed through engagement review, capability gap analysis, reorganization, and agent performance improvement.",
        "outcome_statement": "Agents and organization are developed through engagement and alignment review, capability gap analysis, structure reorganization, and agent performance improvement, substrate-neutrally, ready to drive the next planning cycle.",
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
  established_by: CR-BP-21b
  established_at: '{CHANGE_DATE}'
  change_history:
  - cr: CR-BP-21b
    date: '{CHANGE_DATE}'
    change: |
      Initial L2 Process entry; lands as part of the CR-BP-21b
      AgencyAndOrganization landing tranche under ECF v2.4.0
      register v2 (CR-BP-19). Substrate-neutral per ADR-ECF-002
      §5 / CR-ECF-007: applies to biological, artificial, and
      hybrid agents without reclassification. One of the 5 L2
      landings targeting the 5 ratified cells of the
      AgencyAndOrganization domain.
links:
- rel: change-request
  href: change-requests/CR-BP-21b-agency-organization-landing.md
- rel: process-context
  href: contexts/v1-alpha/{context_file}.yaml
context:
- ref: {context_id}
"""


def render_evidence(links):
    return "\n".join(f'  - type: {l["type"]}\n    ref: {l["ref"]}' for l in links)


ECF_DOMAIN_MAP = {
    "AgencyAndOrganization": "agencyOrganization",
}


for eid, t in L2_TEMPLATES.items():
    pdir = ENT / eid
    pdir.mkdir(parents=True, exist_ok=True)
    (pdir / "candidates").mkdir(exist_ok=True)
    (pdir / "retired").mkdir(exist_ok=True)
    (pdir / "research").mkdir(exist_ok=True)
    context_id = t["context"]
    context_file = context_id.replace("dea:", "").replace(":", "-")
    domain = "AgencyAndOrganization"
    stage = context_id.split("-")[-1]
    stage_title = stage.capitalize()
    ecf_domain = ECF_DOMAIN_MAP[domain]
    ecf_stage = stage
    (pdir / "README.md").write_text(
        f"""# Canonical L2 Business Process: `{eid}`

This directory hosts the canonical L2 Business Process record
for `{eid}`. Lands as part of CR-BP-21b (AgencyAndOrganization
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
