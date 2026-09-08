#!/usr/bin/env python3
"""Generate CR-BP-21c.1 artifacts (ProductAndValue completion):
4 non-Conceive L1 groups + 11 remaining register v2 L2 processes.
Mirrors scripts/apply_phase_7a1_tranche.py (CR-BP-21a.1) with PV data.

Existing-record edits (Conceive group composes edges; PV context
processes lists) are applied as surgical text patches outside this
script — see the note at the bottom.

Run: python scripts/apply_phase_7c1_tranche.py
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).parent.parent
CTX = ROOT / "contexts/v1-alpha"
ENT = ROOT / "entities/v1-alpha"
CHANGE_DATE = "2026-09-08"
CR = "CR-BP-21c.1"
CR_FILE = "change-requests/CR-BP-21c.1-product-value-completion.md"

# ----- 11 L2 processes (remaining register v2 candidates) -----

L2S = [
    # Conceive (join existing dea:group-proposition-conception)
    {"eid": "dea:process-frame-portfolio-direction",
     "name": "Frame Portfolio Direction",
     "verb": "Frame", "object": "Portfolio Direction",
     "context": "dea:pc-pv-conceive", "stage": "Conceive", "intent": "develop",
     "ptype": "management",
     "trigger": "A portfolio direction framing is needed because the enterprise has multiple value propositions competing for bounded investment and requires a coherent portfolio-level direction.",
     "outcome": "Portfolio direction is framed with investment envelopes and priority orderings.",
     "outcome_statement": "Portfolio direction is framed with investment envelopes and priority orderings, coordinated with the enterprise direction and ready for proposition planning."},
    {"eid": "dea:process-frame-innovation-thesis",
     "name": "Frame Innovation Thesis",
     "verb": "Frame", "object": "Innovation Thesis",
     "context": "dea:pc-pv-conceive", "stage": "Conceive", "intent": "develop",
     "ptype": "management",
     "trigger": "An innovation thesis framing is needed because the enterprise requires a bounded thesis for where and how it will innovate beyond current propositions.",
     "outcome": "The innovation thesis is framed with focus areas and experimentation boundaries.",
     "outcome_statement": "The innovation thesis is framed with focus areas and experimentation boundaries, ready to guide innovation experiment design."},
    # Design (new group dea:group-proposition-design)
    {"eid": "dea:process-design-packaging-and-configuration",
     "name": "Design Packaging and Configuration",
     "verb": "Design", "object": "Packaging and Configuration",
     "context": "dea:pc-pv-design", "stage": "Design", "intent": "develop",
     "ptype": "management",
     "trigger": "A packaging and configuration design is needed because the designed proposition requires bounded physical or digital packaging and configuration options for different market segments.",
     "outcome": "Packaging and configuration are designed with segment-appropriate options.",
     "outcome_statement": "Packaging and configuration are designed with segment-appropriate options, ready for product development."},
    {"eid": "dea:process-design-innovation-experiment",
     "name": "Design Innovation Experiment",
     "verb": "Design", "object": "Innovation Experiment",
     "context": "dea:pc-pv-design", "stage": "Design", "intent": "develop",
     "ptype": "management",
     "trigger": "An innovation experiment design is needed because the innovation thesis requires bounded experiments with hypotheses, success criteria, and timeboxes to validate new propositions.",
     "outcome": "The innovation experiment is designed with hypothesis, success criteria, and timebox.",
     "outcome_statement": "The innovation experiment is designed with hypothesis, success criteria, and timebox, ready for prototype build."},
    # Build (new group dea:group-product-development)
    {"eid": "dea:process-build-service-capability",
     "name": "Build Service Capability",
     "verb": "Build", "object": "Service Capability",
     "context": "dea:pc-pv-build", "stage": "Build", "intent": "develop",
     "ptype": "core",
     "trigger": "A service capability build is needed because the designed proposition requires the operational capability to deliver the service to customers.",
     "outcome": "The service capability is built and ready for market readiness.",
     "outcome_statement": "The service capability is built with delivery procedures, quality anchors, and tooling, ready for market readiness preparation."},
    {"eid": "dea:process-build-innovation-prototype",
     "name": "Build Innovation Prototype",
     "verb": "Build", "object": "Innovation Prototype",
     "context": "dea:pc-pv-build", "stage": "Build", "intent": "develop",
     "ptype": "core",
     "trigger": "An innovation prototype build is needed because the designed experiment requires a working prototype to test the hypothesis.",
     "outcome": "The innovation prototype is built and ready for testing.",
     "outcome_statement": "The innovation prototype is built with testable fidelity, ready for hypothesis validation."},
    {"eid": "dea:process-prepare-market-readiness",
     "name": "Prepare Market Readiness",
     "verb": "Prepare", "object": "Market Readiness",
     "context": "dea:pc-pv-build", "stage": "Build", "intent": "develop",
     "ptype": "management",
     "trigger": "Market readiness preparation is needed because the built product or service requires go-to-market assets, pricing, and channel setup before launch.",
     "outcome": "Market readiness is prepared with go-to-market assets and pricing.",
     "outcome_statement": "Market readiness is prepared with go-to-market assets, pricing, and channel setup, ready for launch."},
    # Operate (new group dea:group-portfolio-management-operation)
    {"eid": "dea:process-manage-portfolio-performance",
     "name": "Manage Portfolio Performance",
     "verb": "Manage", "object": "Portfolio Performance",
     "context": "dea:pc-pv-operate", "stage": "Operate", "intent": "operate",
     "ptype": "management",
     "trigger": "Portfolio performance management is needed because the enterprise requires continuous visibility into proposition performance against investment theses.",
     "outcome": "Portfolio performance is managed with continuous visibility and rebalancing.",
     "outcome_statement": "Portfolio performance is monitored and managed with continuous visibility into proposition performance, with rebalancing decisions committed."},
    {"eid": "dea:process-manage-proposition-lifecycle",
     "name": "Manage Proposition Lifecycle",
     "verb": "Manage", "object": "Proposition Lifecycle",
     "context": "dea:pc-pv-operate", "stage": "Operate", "intent": "operate",
     "ptype": "management",
     "trigger": "Proposition lifecycle management is needed because each proposition requires managed transitions across introduction, growth, maturity, and decline stages.",
     "outcome": "The proposition lifecycle is managed with stage transitions and gate decisions.",
     "outcome_statement": "The proposition lifecycle is managed with stage transitions and gate decisions, monitored against portfolio performance."},
    # Improve (new group dea:group-product-evolution)
    {"eid": "dea:process-evolve-products-and-services",
     "name": "Evolve Products and Services",
     "verb": "Evolve", "object": "Products and Services",
     "context": "dea:pc-pv-improve", "stage": "Improve", "intent": "develop",
     "ptype": "management",
     "trigger": "Product and service evolution is needed because market feedback, competitive pressure, or technology shifts require propositions to evolve beyond their current form.",
     "outcome": "Products and services are evolved with bounded enhancements.",
     "outcome_statement": "Products and services are evolved with bounded enhancements, aligned to the proposition performance review findings."},
    {"eid": "dea:process-rationalize-portfolio",
     "name": "Rationalize Portfolio",
     "verb": "Rationalize", "object": "Portfolio",
     "context": "dea:pc-pv-improve", "stage": "Improve", "intent": "develop",
     "ptype": "management",
     "trigger": "Portfolio rationalization is needed because the portfolio accumulates propositions that no longer justify their investment envelopes.",
     "outcome": "The portfolio is rationalized with retire-or-pivot decisions.",
     "outcome_statement": "The portfolio is rationalized with retire-or-pivot decisions committed for underperforming propositions, supervised by the portfolio review cycle."},
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
  target_id: ecf:productValue.{ecf_stage}
ecfConformance:
  framework: EnterpriseConceptFramework
  contractVersion: 1.0.0
  profile: dea:ecf@1.0.0
  status: conformant
  affiliation: inherits-catalog
  canonicalReferences:
  - kind: coordinate
    domain: ProductAndValue
    stage: {stage}
    identifier: ecf:productValue.{ecf_stage}
metadata:
  established_by: {CR}
  established_at: '{CHANGE_DATE}'
  change_history:
  - cr: {CR}
    date: '{CHANGE_DATE}'
    change: |
      Initial L2 Process entry; lands as part of the {CR}
      ProductAndValue completion tranche under ECF v2.4.0
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
for `{eid}`. Lands as part of {CR} (ProductAndValue
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


# ----- 4 new L1 Process Groups (non-Conceive PV cells) -----

GROUPS = [
    {
        "gid": "dea:group-proposition-design",
        "name": "Proposition Design",
        "context": "dea:pc-pv-design",
        "stage": "Design",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of designing product and service propositions, "
            "their packaging and configuration, and innovation experiments "
            "in the ProductAndValue x Design context. v2.4.0 grounding "
            "(domain-grounding.md §3.5)."
        ),
        "includes": [
            "Product and service proposition design",
            "Packaging and configuration design",
            "Innovation experiment design",
        ],
        "excludes": [
            "Technology platform architecture (operations-enablement)",
            "Value proposition thesis conception (Conceive stage; adjacent context)",
            "Product variant development (Build stage; adjacent context)",
        ],
        "outcomes": [
            "Propositions are designed with bounded specifications.",
            "Packaging and configuration are designed for target segments.",
            "Innovation experiments are designed with hypotheses and timeboxes.",
        ],
        "composes": [
            ("dea:process-design-product-and-service-propositions", "landed CR-BP-21c"),
            ("dea:process-design-packaging-and-configuration", CR),
            ("dea:process-design-innovation-experiment", CR),
        ],
        "ecf_stage": "design",
    },
    {
        "gid": "dea:group-product-development",
        "name": "Product Development",
        "context": "dea:pc-pv-build",
        "stage": "Build",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of building product variants, service "
            "capabilities, innovation prototypes, and market readiness in "
            "the ProductAndValue x Build context. v2.4.0 grounding "
            "(domain-grounding.md §3.5)."
        ),
        "includes": [
            "Product variant development",
            "Service capability build",
            "Innovation prototype build",
            "Market readiness preparation",
        ],
        "excludes": [
            "Technology build (operations-enablement)",
            "Proposition design (Design stage; adjacent context)",
            "Catalogue operation (Operate stage; adjacent context)",
        ],
        "outcomes": [
            "Product variants and service capabilities are built.",
            "Innovation prototypes are built for hypothesis testing.",
            "Market readiness is prepared with go-to-market assets.",
        ],
        "composes": [
            ("dea:process-develop-product-variants", "landed CR-BP-21c"),
            ("dea:process-build-service-capability", CR),
            ("dea:process-build-innovation-prototype", CR),
            ("dea:process-prepare-market-readiness", CR),
        ],
        "ecf_stage": "build",
    },
    {
        "gid": "dea:group-portfolio-management-operation",
        "name": "Portfolio Management Operation",
        "context": "dea:pc-pv-operate",
        "stage": "Operate",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of operating the product catalogue, managing "
            "portfolio performance, and managing the proposition lifecycle "
            "in the ProductAndValue x Operate context. v2.4.0 grounding "
            "(domain-grounding.md §3.5)."
        ),
        "includes": [
            "Product catalogue operation",
            "Portfolio performance management",
            "Proposition lifecycle management",
        ],
        "excludes": [
            "Operational delivery of the product (operations-enablement)",
            "Partner alliance programme (party-relationship)",
            "Workforce operation (agency-organization)",
        ],
        "outcomes": [
            "Product catalogue is operated with accurate listings.",
            "Portfolio performance is managed with rebalancing decisions.",
            "Proposition lifecycle is managed with gate decisions.",
        ],
        "composes": [
            ("dea:process-operate-product-catalogue", "landed CR-BP-21c"),
            ("dea:process-manage-portfolio-performance", CR),
            ("dea:process-manage-proposition-lifecycle", CR),
        ],
        "ecf_stage": "operate",
    },
    {
        "gid": "dea:group-product-evolution",
        "name": "Product Evolution",
        "context": "dea:pc-pv-improve",
        "stage": "Improve",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of conducting proposition performance reviews, "
            "evolving products and services, and rationalizing the portfolio "
            "in the ProductAndValue x Improve context. v2.4.0 grounding "
            "(domain-grounding.md §3.5)."
        ),
        "includes": [
            "Proposition performance review",
            "Product and service evolution",
            "Portfolio rationalization",
        ],
        "excludes": [
            "Capability improvement (owning domains)",
            "Portfolio performance operation (Operate stage; adjacent context)",
        ],
        "outcomes": [
            "Proposition performance is reviewed with findings committed.",
            "Products and services are evolved with bounded enhancements.",
            "Portfolio is rationalized with retire-or-pivot decisions.",
        ],
        "composes": [
            ("dea:process-conduct-proposition-performance-review", "landed CR-BP-21c"),
            ("dea:process-evolve-products-and-services", CR),
            ("dea:process-rationalize-portfolio", CR),
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
      domain: ProductAndValue
      stage: {stage}
      identifier: ecf:productValue.{ecf_stage}

# Evidence (CR-BP-11 register strength scale E0..E5).
evidence:
  - source: CR-BP-19 (register v2, ratified against ECF v2.4.0)
    claim: |
      This Process Group's coordinate is ratified-accepted in register
      v2. {CR} lands the corresponding L1 group as part of the
      ProductAndValue completion tranche.
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
        ProductAndValue completion tranche.

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
(ProductAndValue x {g['stage']}). Lands as part of {CR}
(ProductAndValue completion). Composes the L2 Business Processes
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
#   1. dea:group-proposition-conception.yaml — +2 composes edges
#      (frame-portfolio-direction, frame-innovation-thesis) plus a
#      CR-BP-21c.1 change_history entry.
#   2. dea-pc-pv-{conceive,design,build,operate,improve}.yaml —
#      processes: list extended with the new cell L2s plus a
#      CR-BP-21c.1 change_history entry.

print("\nDone. Next: text-patch existing records, dispositions, "
      "tranche plan, register audit, regenerate, gates.")
