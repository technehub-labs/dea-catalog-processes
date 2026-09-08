#!/usr/bin/env python3
"""Generate CR-BP-21d.1 artifacts (EnablementAndOperations completion):
4 non-Conceive L1 groups + 23 remaining register v2 L2 processes.
Mirrors scripts/apply_phase_7a1_tranche.py (CR-BP-21a.1) with OE data.
Canonical ECF identifiers: ecf:enablementAndOperations.<stage> (short
form; see CR-BP-21c.1 repair for the namespace lesson).

Existing-record edits (Conceive group composes edges; OE context
processes lists) are applied as surgical text patches outside this
script — see the note at the bottom.

Run: python scripts/apply_phase_7d1_tranche.py
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).parent.parent
CTX = ROOT / "contexts/v1-alpha"
ENT = ROOT / "entities/v1-alpha"
CHANGE_DATE = "2026-09-08"
CR = "CR-BP-21d.1"
CR_FILE = "change-requests/CR-BP-21d.1-enablement-operations-completion.md"

# ----- 23 L2 processes (remaining register v2 candidates) -----

L2S = [
    # Conceive (join existing dea:group-operations-model-conception)
    {"eid": "dea:process-frame-delivery-model-conception",
     "name": "Frame Delivery Model Conception",
     "verb": "Frame", "object": "Delivery Model Conception",
     "context": "dea:pc-oe-conceive", "stage": "Conceive", "intent": "develop",
     "ptype": "management",
     "trigger": "A delivery model conception is needed because the operations strategy requires a bounded delivery model (channels, service levels, fulfilment patterns) before design can proceed.",
     "outcome": "The delivery model is conceived with channels, service levels, and fulfilment patterns.",
     "outcome_statement": "The delivery model is conceived with channels, service levels, and fulfilment patterns, coordinated with the operations strategy and ready for delivery model design."},
    {"eid": "dea:process-frame-technology-enablement-approach",
     "name": "Frame Technology Enablement Approach",
     "verb": "Frame", "object": "Technology Enablement Approach",
     "context": "dea:pc-oe-conceive", "stage": "Conceive", "intent": "develop",
     "ptype": "management",
     "trigger": "A technology enablement approach framing is needed because the operations strategy requires bounded decisions on which technology platforms will enable the operating model.",
     "outcome": "The technology enablement approach is framed with platform families and sourcing principles.",
     "outcome_statement": "The technology enablement approach is framed with platform families and sourcing principles, aligned to the operations planning cycle."},
    {"eid": "dea:process-frame-physical-asset-approach",
     "name": "Frame Physical Asset Approach",
     "verb": "Frame", "object": "Physical Asset Approach",
     "context": "dea:pc-oe-conceive", "stage": "Conceive", "intent": "develop",
     "ptype": "management",
     "trigger": "A physical asset approach framing is needed because the operations strategy requires bounded decisions on facility and asset footprints before blueprint design.",
     "outcome": "The physical asset approach is framed with footprint principles and lifecycle envelopes.",
     "outcome_statement": "The physical asset approach is framed with footprint principles and lifecycle envelopes, coordinated with the operations planning cycle."},
    # Design (new group dea:group-process-and-enablement-design)
    {"eid": "dea:process-design-delivery-model",
     "name": "Design Delivery Model",
     "verb": "Design", "object": "Delivery Model",
     "context": "dea:pc-oe-design", "stage": "Design", "intent": "develop",
     "ptype": "management",
     "trigger": "A delivery model design is needed because the conceived delivery model requires bounded channel configurations, service levels, and fulfilment flows.",
     "outcome": "The delivery model is designed with channel configurations and service levels.",
     "outcome_statement": "The delivery model is designed with channel configurations and service levels, ready for delivery capability planning."},
    {"eid": "dea:process-design-technology-platform-architecture",
     "name": "Design Technology Platform Architecture",
     "verb": "Design", "object": "Technology Platform Architecture",
     "context": "dea:pc-oe-design", "stage": "Design", "intent": "develop",
     "ptype": "management",
     "trigger": "A technology platform architecture design is needed because the framed enablement approach requires bounded platform components, integration patterns, and deployment topologies.",
     "outcome": "The technology platform architecture is designed with components and integration patterns.",
     "outcome_statement": "The technology platform architecture is designed with components and integration patterns, ready for acquisition planning."},
    {"eid": "dea:process-design-facility-and-asset-blueprint",
     "name": "Design Facility and Asset Blueprint",
     "verb": "Design", "object": "Facility and Asset Blueprint",
     "context": "dea:pc-oe-design", "stage": "Design", "intent": "develop",
     "ptype": "management",
     "trigger": "A facility and asset blueprint design is needed because the framed physical asset approach requires bounded layouts, equipment specifications, and capacity envelopes.",
     "outcome": "The facility and asset blueprint is designed with layouts and capacity envelopes.",
     "outcome_statement": "The facility and asset blueprint is designed with layouts and capacity envelopes, ready for provisioning planning."},
    {"eid": "dea:process-design-logistics-and-routing",
     "name": "Design Logistics and Routing",
     "verb": "Design", "object": "Logistics and Routing",
     "context": "dea:pc-oe-design", "stage": "Design", "intent": "develop",
     "ptype": "management",
     "trigger": "A logistics and routing design is needed because the delivery model requires bounded transport modes, routing logic, and network nodes.",
     "outcome": "Logistics and routing are designed with transport modes and network nodes.",
     "outcome_statement": "Logistics and routing are designed with transport modes and network nodes, coordinated with the delivery model design."},
    # Build (new group dea:group-operations-and-enablement-build)
    {"eid": "dea:process-commission-production-line",
     "name": "Commission Production Line",
     "verb": "Commission", "object": "Production Line",
     "context": "dea:pc-oe-build", "stage": "Build", "intent": "develop",
     "ptype": "core",
     "trigger": "A production line stand-up is needed because the designed operations model requires a working production line before it can produce at rate.",
     "outcome": "The production line is stood up and producing at trial rate.",
     "outcome_statement": "The production line is stood up with equipment commissioned and trial rate achieved, ready to produce at full rate."},
    {"eid": "dea:process-build-logistics-network",
     "name": "Build Logistics Network",
     "verb": "Build", "object": "Logistics Network",
     "context": "dea:pc-oe-build", "stage": "Build", "intent": "develop",
     "ptype": "core",
     "trigger": "A logistics network build is needed because the designed routing requires physical network nodes, carrier contracts, and warehouse capacity to be in place.",
     "outcome": "The logistics network is built with nodes and carriers contracted.",
     "outcome_statement": "The logistics network is built with nodes and carriers contracted, ready to execute delivery flows."},
    {"eid": "dea:process-acquire-technology-assets",
     "name": "Acquire Technology Assets",
     "verb": "Acquire", "object": "Technology Assets",
     "context": "dea:pc-oe-build", "stage": "Build", "intent": "develop",
     "ptype": "core",
     "trigger": "Technology asset acquisition and installation is needed because the designed platform architecture requires procured and installed hardware and software before operation.",
     "outcome": "Technology assets are acquired, installed, and commissioned.",
     "outcome_statement": "Technology assets are acquired, installed, and commissioned, ready to serve operational workloads."},
    {"eid": "dea:process-provision-facilities",
     "name": "Provision Facilities",
     "verb": "Provision", "object": "Facilities",
     "context": "dea:pc-oe-build", "stage": "Build", "intent": "develop",
     "ptype": "core",
     "trigger": "Facility acquisition and provisioning is needed because the designed blueprint requires physical facilities to be secured and fitted before production or delivery can begin.",
     "outcome": "Facilities are acquired, fitted, and provisioned.",
     "outcome_statement": "Facilities are acquired, fitted, and provisioned, ready to serve production and delivery operations."},
    # Operate (new group dea:group-execution-and-fulfillment)
    {"eid": "dea:process-run-production-line",
     "name": "Run Production Line",
     "verb": "Run", "object": "Production Line",
     "context": "dea:pc-oe-operate", "stage": "Operate", "intent": "operate",
     "ptype": "core",
     "trigger": "Production line operation is needed because the stood-up line must produce output to plan on each cycle.",
     "outcome": "The production line is run to plan with output and quality recorded.",
     "outcome_statement": "The production line produces output to plan, with quality recorded per cycle."},
    {"eid": "dea:process-operate-logistics",
     "name": "Operate Logistics",
     "verb": "Operate", "object": "Logistics",
     "context": "dea:pc-oe-operate", "stage": "Operate", "intent": "operate",
     "ptype": "core",
     "trigger": "Logistics operation is needed because the built network must execute transport and delivery flows to serve customers and production.",
     "outcome": "Logistics are operated with on-time delivery and exception handling.",
     "outcome_statement": "Logistics are operated with on-time delivery and exception handling recorded per shipment."},
    {"eid": "dea:process-operate-warehouse-and-inventory",
     "name": "Operate Warehouse and Inventory",
     "verb": "Operate", "object": "Warehouse and Inventory",
     "context": "dea:pc-oe-operate", "stage": "Operate", "intent": "operate",
     "ptype": "core",
     "trigger": "Warehouse and inventory operation is needed because production and delivery require accurate stock holding, picking, and replenishment.",
     "outcome": "Warehouse and inventory are operated with accurate stock records.",
     "outcome_statement": "Warehouse and inventory are operated with accurate stock records, picking, and replenishment executed per demand."},
    {"eid": "dea:process-operate-quality-control",
     "name": "Operate Quality Control",
     "verb": "Operate", "object": "Quality Control",
     "context": "dea:pc-oe-operate", "stage": "Operate", "intent": "operate",
     "ptype": "core",
     "trigger": "Quality control operation is needed because production output must be inspected against specifications before it can serve customers.",
     "outcome": "Quality control is operated with inspections and dispositions recorded.",
     "outcome_statement": "Quality control is operated with inspections and dispositions recorded per batch."},
    {"eid": "dea:process-operate-technology-platforms",
     "name": "Operate Technology Platforms",
     "verb": "Operate", "object": "Technology Platforms",
     "context": "dea:pc-oe-operate", "stage": "Operate", "intent": "operate",
     "ptype": "core",
     "trigger": "Technology platform operation is needed because the installed platforms must serve operational workloads with agreed availability.",
     "outcome": "Technology platforms are operated with availability targets met.",
     "outcome_statement": "Technology platforms are operated with availability targets met and incidents recorded per service window."},
    {"eid": "dea:process-operate-facility-management",
     "name": "Operate Facility Management",
     "verb": "Operate", "object": "Facility Management",
     "context": "dea:pc-oe-operate", "stage": "Operate", "intent": "operate",
     "ptype": "core",
     "trigger": "Facility management operation is needed because provisioned facilities must be maintained as safe, compliant working environments.",
     "outcome": "Facilities are operated with safety and compliance maintained.",
     "outcome_statement": "Facilities are operated with safety and compliance maintained and work orders executed per schedule."},
    {"eid": "dea:process-operate-asset-maintenance",
     "name": "Operate Asset Maintenance",
     "verb": "Operate", "object": "Asset Maintenance",
     "context": "dea:pc-oe-operate", "stage": "Operate", "intent": "operate",
     "ptype": "core",
     "trigger": "Asset maintenance operation is needed because installed assets degrade and require scheduled and reactive maintenance to sustain availability.",
     "outcome": "Asset maintenance is operated with scheduled and reactive work completed.",
     "outcome_statement": "Asset maintenance is operated with scheduled and reactive work completed and asset availability recorded."},
    {"eid": "dea:process-operate-procurement-cycle",
     "name": "Operate Procurement Cycle",
     "verb": "Operate", "object": "Procurement Cycle",
     "context": "dea:pc-oe-operate", "stage": "Operate", "intent": "operate",
     "ptype": "core",
     "trigger": "Procurement cycle operation is needed because operations require a steady flow of materials and services purchased within policy.",
     "outcome": "The procurement cycle is operated with purchase orders executed within policy.",
     "outcome_statement": "The procurement cycle is operated with purchase orders executed within policy and receipts recorded."},
    # Improve (new group dea:group-operations-and-enablement-improvement)
    {"eid": "dea:process-conduct-logistics-optimization",
     "name": "Conduct Logistics Optimization",
     "verb": "Conduct", "object": "Logistics Optimization",
     "context": "dea:pc-oe-improve", "stage": "Improve", "intent": "develop",
     "ptype": "management",
     "trigger": "A logistics optimization is needed because routing and network performance evidence reveals cost or service-level improvement opportunities.",
     "outcome": "Logistics optimization is conducted with route and network changes committed.",
     "outcome_statement": "Logistics optimization is conducted with route and network changes committed to the operations planning cycle."},
    {"eid": "dea:process-conduct-lean-six-sigma-programme",
     "name": "Conduct Lean Six Sigma Programme",
     "verb": "Conduct", "object": "Lean Six Sigma Programme",
     "context": "dea:pc-oe-improve", "stage": "Improve", "intent": "develop",
     "ptype": "management",
     "trigger": "A lean six sigma programme is needed because sustained waste and variation reduction requires a structured improvement programme with bounded projects.",
     "outcome": "The lean six sigma programme is conducted with improvement projects delivered.",
     "outcome_statement": "The lean six sigma programme is conducted with improvement projects delivered and control plans committed."},
    {"eid": "dea:process-optimize-asset-utilization",
     "name": "Optimize Asset Utilization",
     "verb": "Optimize", "object": "Asset Utilization",
     "context": "dea:pc-oe-improve", "stage": "Improve", "intent": "develop",
     "ptype": "management",
     "trigger": "Asset utilization optimization is needed because maintenance and performance evidence reveals underutilized or bottlenecked assets.",
     "outcome": "Asset utilization is optimized with redeployment decisions committed.",
     "outcome_statement": "Asset utilization is optimized with redeployment and reallocation decisions committed to the asset plan."},
    {"eid": "dea:process-improve-technology-platforms",
     "name": "Improve Technology Platforms",
     "verb": "Improve", "object": "Technology Platforms",
     "context": "dea:pc-oe-improve", "stage": "Improve", "intent": "develop",
     "ptype": "standardization",
     "trigger": "Technology platform improvement is needed because platform performance and incident evidence reveals reliability, capacity, or capability gaps.",
     "outcome": "Technology platforms are improved with reliability and capacity upgrades committed.",
     "outcome_statement": "Technology platforms are improved with reliability and capacity upgrades committed to the platform improvement backlog."},
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
  target_id: ecf:enablementAndOperations.{ecf_stage}
ecfConformance:
  framework: EnterpriseConceptFramework
  contractVersion: 1.0.0
  profile: dea:ecf@1.0.0
  status: conformant
  affiliation: inherits-catalog
  canonicalReferences:
  - kind: coordinate
    domain: EnablementAndOperations
    stage: {stage}
    identifier: ecf:enablementAndOperations.{ecf_stage}
metadata:
  established_by: {CR}
  established_at: '{CHANGE_DATE}'
  change_history:
  - cr: {CR}
    date: '{CHANGE_DATE}'
    change: |
      Initial L2 Process entry; lands as part of the {CR}
      EnablementAndOperations completion tranche under ECF v2.4.0
      register v2 (CR-BP-19). Closes the remaining register v2 L2
      candidates for this cell.
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
for `{eid}`. Lands as part of {CR} (EnablementAndOperations
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


# ----- 4 new L1 Process Groups (non-Conceive OE cells) -----

GROUPS = [
    {
        "gid": "dea:group-process-and-enablement-design",
        "name": "Process and Enablement Design",
        "context": "dea:pc-oe-design",
        "stage": "Design",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of designing the operations model, delivery "
            "model, technology platform architecture, facility and asset "
            "blueprint, and logistics and routing in the "
            "EnablementAndOperations x Design context. v2.4.0 grounding "
            "(domain-grounding.md §3.6)."
        ),
        "includes": [
            "Operations model design",
            "Delivery model design",
            "Technology platform architecture design",
            "Facility and asset blueprint design",
            "Logistics and routing design",
        ],
        "excludes": [
            "Capability design (owning domains)",
            "Operations strategy framing (Conceive stage; adjacent context)",
            "Physical build (Build stage; adjacent context)",
        ],
        "outcomes": [
            "Operations and delivery models are designed.",
            "Technology platform architecture is designed.",
            "Facility blueprint and logistics routing are designed.",
        ],
        "composes": [
            ("dea:process-design-operations-model", "landed CR-BP-21d"),
            ("dea:process-design-delivery-model", CR),
            ("dea:process-design-technology-platform-architecture", CR),
            ("dea:process-design-facility-and-asset-blueprint", CR),
            ("dea:process-design-logistics-and-routing", CR),
        ],
        "ecf_stage": "design",
    },
    {
        "gid": "dea:group-operations-and-enablement-build",
        "name": "Operations and Enablement Build",
        "context": "dea:pc-oe-build",
        "stage": "Build",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of building production lines, delivery "
            "capability, logistics networks, technology assets, and "
            "facilities in the EnablementAndOperations x Build context. "
            "v2.4.0 grounding (domain-grounding.md §3.6)."
        ),
        "includes": [
            "Production line stand-up",
            "Delivery capability build",
            "Logistics network build",
            "Technology asset acquisition and installation",
            "Facility acquisition and provisioning",
        ],
        "excludes": [
            "Agent provisioning (agency-organization)",
            "Platform architecture design (Design stage; adjacent context)",
            "Day-to-day operation (Operate stage; adjacent context)",
        ],
        "outcomes": [
            "Production lines are stood up at trial rate.",
            "Delivery capability and logistics network are built.",
            "Technology assets and facilities are acquired and provisioned.",
        ],
        "composes": [
            ("dea:process-build-delivery-capability", "landed CR-BP-21d"),
            ("dea:process-commission-production-line", CR),
            ("dea:process-build-logistics-network", CR),
            ("dea:process-acquire-technology-assets", CR),
            ("dea:process-provision-facilities", CR),
        ],
        "ecf_stage": "build",
    },
    {
        "gid": "dea:group-execution-and-fulfillment",
        "name": "Execution and Fulfilment",
        "context": "dea:pc-oe-operate",
        "stage": "Operate",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of day-to-day operations execution: production, "
            "service delivery, logistics, warehousing, quality control, "
            "technology platform operation, facility management, asset "
            "maintenance, and procurement execution in the "
            "EnablementAndOperations x Operate context. v2.4.0 grounding "
            "(domain-grounding.md §3.6)."
        ),
        "includes": [
            "Production line operation",
            "Service delivery operation",
            "Logistics, warehouse, and inventory operation",
            "Quality control operation",
            "Technology platform operation",
            "Facility management and asset maintenance operation",
            "Procurement cycle execution",
        ],
        "excludes": [
            "Supplier relationship management (party-relationship)",
            "Customer relationship (party-relationship)",
            "Operations improvement (Improve stage; adjacent context)",
        ],
        "outcomes": [
            "Production and service delivery operate to plan.",
            "Logistics, warehousing, and quality control operate with records.",
            "Technology platforms, facilities, and assets are operated.",
            "Procurement cycle is executed within policy.",
        ],
        "composes": [
            ("dea:process-operate-service-delivery", "landed CR-BP-21d"),
            ("dea:process-run-production-line", CR),
            ("dea:process-operate-logistics", CR),
            ("dea:process-operate-warehouse-and-inventory", CR),
            ("dea:process-operate-quality-control", CR),
            ("dea:process-operate-technology-platforms", CR),
            ("dea:process-operate-facility-management", CR),
            ("dea:process-operate-asset-maintenance", CR),
            ("dea:process-operate-procurement-cycle", CR),
        ],
        "ecf_stage": "operate",
    },
    {
        "gid": "dea:group-operations-and-enablement-improvement",
        "name": "Operations and Enablement Improvement",
        "context": "dea:pc-oe-improve",
        "stage": "Improve",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of reviewing operations performance, optimizing "
            "logistics and asset utilization, conducting lean programmes, "
            "and improving technology platforms in the "
            "EnablementAndOperations x Improve context. v2.4.0 grounding "
            "(domain-grounding.md §3.6)."
        ),
        "includes": [
            "Operations performance review",
            "Logistics optimization",
            "Lean six sigma programme",
            "Asset utilization optimization",
            "Technology platform improvement",
        ],
        "excludes": [
            "Capability improvement (owning domains)",
            "Operations execution (Operate stage; adjacent context)",
        ],
        "outcomes": [
            "Operations performance is reviewed with findings committed.",
            "Logistics and asset utilization are optimized.",
            "Lean programmes deliver improvement projects.",
            "Technology platforms are improved on evidence.",
        ],
        "composes": [
            ("dea:process-conduct-operations-performance-review", "landed CR-BP-21d"),
            ("dea:process-conduct-logistics-optimization", CR),
            ("dea:process-conduct-lean-six-sigma-programme", CR),
            ("dea:process-optimize-asset-utilization", CR),
            ("dea:process-improve-technology-platforms", CR),
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
      domain: EnablementAndOperations
      stage: {stage}
      identifier: ecf:enablementAndOperations.{ecf_stage}

# Evidence (CR-BP-11 register strength scale E0..E5).
evidence:
  - source: CR-BP-19 (register v2, ratified against ECF v2.4.0)
    claim: |
      This Process Group's coordinate is ratified-accepted in register
      v2. {CR} lands the corresponding L1 group as part of the
      EnablementAndOperations completion tranche.
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
        EnablementAndOperations completion tranche.

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
(EnablementAndOperations x {g['stage']}). Lands as part of {CR}
(EnablementAndOperations completion). Composes the L2 Business
Processes of the {g['stage']} cell.
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
#   1. dea:group-operations-model-conception.yaml — +3 composes edges
#      (frame-delivery-model-conception, frame-technology-enablement-
#      approach, frame-physical-asset-approach) plus a CR-BP-21d.1
#      change_history entry.
#   2. dea-pc-oe-{conceive,design,build,operate,improve}.yaml —
#      processes: list extended with the new cell L2s plus a
#      CR-BP-21d.1 change_history entry.

print("\nDone. Next: text-patch existing records, dispositions, "
      "tranche plan, register audit, regenerate, gates.")
