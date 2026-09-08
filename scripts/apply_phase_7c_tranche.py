#!/usr/bin/env python3
"""Generate CR-BP-21c artifacts (ProductAndValue landing):
5 process contexts, 1 L1 group, 5 L2 processes. Mirrors the
CR-BP-21b (AgencyAndOrganization) pattern. Substrate-neutral
per ADR-ECF-002 §5 / CR-ECF-007.

Run: python scripts/apply_phase_7c_tranche.py
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).parent.parent
CTX = ROOT / "contexts/v1-alpha"
ENT = ROOT / "entities/v1-alpha"
CHANGE_DATE = "2026-09-08"


CONTEXTS = [
    {
        "filename": "dea-pc-pv-conceive",
        "id": "dea:pc-pv-conceive",
        "domain": "ProductAndValue",
        "stage": "Conceive",
        "name": "Proposition and Portfolio Conception",
        "definition": (
            "The bounded enterprise context for **conceiving** the enterprise's "
            "value-bearing propositions in the **Product & Value** "
            "domain. This context addresses the front-end work of framing value "
            "proposition theses, framing portfolio direction, and framing "
            "innovation theses. v2.4.0: the domain manages the complete lifecycle "
            "of whatever the enterprise creates, shapes, packages, and makes "
            "available for exchange with external parties; 'Offering' was dropped "
            "as vague (domain-grounding.md §3.5)."
        ),
        "includes": [
            "Value proposition thesis framing",
            "Portfolio direction framing",
            "Innovation thesis framing",
            "Proposition concept validation",
        ],
        "excludes": [
            "Strategic portfolio investment decisions (strategy-direction x conceive; adjacent domain)",
            "Capability strategy (governance-existence x conceive; adjacent domain)",
            "Proposition design (Design stage; adjacent context)",
            "Product development (Build stage; adjacent context)",
            "Alliance and partnership thesis (party-relationship x conceive; adjacent domain)",
        ],
        "outcomes": [
            "Value proposition thesis is framed for the enterprise.",
            "Portfolio direction is framed with bounded scope.",
            "Innovation thesis is framed and validated.",
            "Proposition concepts are validated against market evidence.",
        ],
        "adjacent": [
            "dea:pc-pv-design", "dea:pc-pv-build", "dea:pc-pv-operate", "dea:pc-pv-improve",
        ],
        "processes": ["dea:process-frame-value-proposition-thesis"],
        "l1_candidates": ["Proposition Conception", "Portfolio Direction Conception"],
        "grounding_phrase": "conception of value propositions, portfolio direction, and innovation theses",
        "enterprise_concern": "the conception of the enterprise's value-bearing propositions.",
        "lifecycle_concern": "framing value proposition theses, portfolio direction, and innovation theses.",
        "combined_meaning": "The front-end work of framing value proposition theses, portfolio direction, and innovation theses as the conception of value-bearing propositions.",
    },
    {
        "filename": "dea-pc-pv-design",
        "id": "dea:pc-pv-design",
        "domain": "ProductAndValue",
        "stage": "Design",
        "name": "Proposition and Packaging Design",
        "definition": (
            "The bounded enterprise context for **designing** the propositions, "
            "packaging, configuration, and innovation experiments of the "
            "enterprise in the **Product & Value** domain. This context "
            "addresses the analytical work of producing designs for product and "
            "service propositions, packaging and configuration, and innovation "
            "experiments. v2.4.0: the domain owns the value-bearing proposition, "
            "not every form of value in the enterprise (domain-grounding.md §3.5)."
        ),
        "includes": [
            "Proposition design",
            "Packaging and configuration design",
            "Innovation experiment design",
            "Proposition architecture design",
        ],
        "excludes": [
            "Proposition conception (Conceive stage; adjacent context)",
            "Product development (Build stage; adjacent context)",
            "Technology platform architecture (operations-enablement x design; adjacent domain)",
            "Strategic direction design (strategy-direction x design; adjacent domain)",
        ],
        "outcomes": [
            "Product and service propositions are designed with bounded scope.",
            "Packaging and configuration designs are committed.",
            "Innovation experiments are designed and ready for Build.",
            "Proposition architecture is designed for the portfolio.",
        ],
        "adjacent": [
            "dea:pc-pv-conceive", "dea:pc-pv-build", "dea:pc-pv-operate", "dea:pc-pv-improve",
        ],
        "processes": ["dea:process-design-product-and-service-propositions"],
        "l1_candidates": ["Proposition Design", "Packaging and Configuration Design"],
        "grounding_phrase": "design of propositions, packaging, configuration, and innovation experiments",
        "enterprise_concern": "the design of the enterprise's propositions and packaging.",
        "lifecycle_concern": "designing propositions, packaging, configuration, and innovation experiments.",
        "combined_meaning": "The analytical work of producing designs for propositions, packaging, configuration, and innovation experiments.",
    },
    {
        "filename": "dea-pc-pv-build",
        "id": "dea:pc-pv-build",
        "domain": "ProductAndValue",
        "stage": "Build",
        "name": "Product Development and Market Readiness Build",
        "definition": (
            "The bounded enterprise context for **building** the products, "
            "prototypes, and market readiness of the enterprise in the "
            "**Product & Value** domain. This context addresses the "
            "constructive work of developing product variants, building service "
            "capability, building innovation prototypes, and preparing market "
            "readiness. v2.4.0: technology build is Operations & Enablement; "
            "this cell covers the proposition-side construction "
            "(domain-grounding.md §3.5)."
        ),
        "includes": [
            "Product variant development",
            "Service capability build",
            "Innovation prototype build",
            "Market readiness preparation",
        ],
        "excludes": [
            "Proposition design (Design stage; adjacent context)",
            "Technology platform build (operations-enablement x build; adjacent domain)",
            "Operational delivery build (operations-enablement x build; adjacent domain)",
        ],
        "outcomes": [
            "Product variants are developed and ready for market.",
            "Service capability is built and ready for operation.",
            "Innovation prototypes are built and validated.",
            "Market readiness is prepared for the Operate cell.",
        ],
        "adjacent": [
            "dea:pc-pv-conceive", "dea:pc-pv-design", "dea:pc-pv-operate", "dea:pc-pv-improve",
        ],
        "processes": ["dea:process-develop-product-variants"],
        "l1_candidates": ["Product Development", "Market Readiness Build"],
        "grounding_phrase": "development of product variants, service capability, prototypes, and market readiness",
        "enterprise_concern": "the construction of the enterprise's products and market readiness.",
        "lifecycle_concern": "developing product variants, building service capability, building prototypes, and preparing market readiness.",
        "combined_meaning": "The constructive work of developing product variants, building service capability, building innovation prototypes, and preparing market readiness.",
    },
    {
        "filename": "dea-pc-pv-operate",
        "id": "dea:pc-pv-operate",
        "domain": "ProductAndValue",
        "stage": "Operate",
        "name": "Portfolio Management and Proposition Lifecycle Operation",
        "definition": (
            "The bounded enterprise context for **operating** the product "
            "catalogue, portfolio performance, and proposition lifecycle of the "
            "enterprise in the **Product & Value** domain. This context "
            "addresses the steady-state work of operating the product catalogue, "
            "managing portfolio performance, and managing the proposition "
            "lifecycle. v2.4.0: operational delivery of the product is "
            "Operations & Enablement; this cell covers the proposition-side "
            "operation (domain-grounding.md §3.5)."
        ),
        "includes": [
            "Product catalogue operation",
            "Portfolio performance management",
            "Proposition lifecycle management",
            "Proposition performance monitoring",
        ],
        "excludes": [
            "Product development (Build stage; adjacent context)",
            "Operational delivery of the product (operations-enablement x operate; adjacent domain)",
            "Partner alliance programme (party-relationship x operate; adjacent domain)",
            "Workforce operation (agency-organization x operate; adjacent domain)",
        ],
        "outcomes": [
            "Product catalogue is operated across the portfolio.",
            "Portfolio performance is managed against targets.",
            "Proposition lifecycle is managed from launch to retirement.",
            "Proposition performance is monitored and reported.",
        ],
        "adjacent": [
            "dea:pc-pv-conceive", "dea:pc-pv-design", "dea:pc-pv-build", "dea:pc-pv-improve",
        ],
        "processes": ["dea:process-operate-product-catalogue"],
        "l1_candidates": ["Portfolio Management Operation", "Proposition Lifecycle Operation"],
        "grounding_phrase": "operation of product catalogue, portfolio performance, and proposition lifecycle",
        "enterprise_concern": "the steady-state operation of the enterprise's product portfolio.",
        "lifecycle_concern": "operating product catalogue, portfolio performance, and proposition lifecycle.",
        "combined_meaning": "The steady-state work of operating the product catalogue, managing portfolio performance, and managing the proposition lifecycle.",
    },
    {
        "filename": "dea-pc-pv-improve",
        "id": "dea:pc-pv-improve",
        "domain": "ProductAndValue",
        "stage": "Improve",
        "name": "Product Evolution and Portfolio Rationalization",
        "definition": (
            "The bounded enterprise context for **improving** the products and "
            "portfolio of the enterprise in the **Product & Value** "
            "domain. This context addresses the learning and adaptation work of "
            "conducting proposition performance reviews, evolving products and "
            "services, and rationalizing the portfolio. v2.4.0: capability "
            "improvement is the owning domain's concern; this cell covers "
            "proposition-side evolution (domain-grounding.md §3.5)."
        ),
        "includes": [
            "Proposition performance review",
            "Product and service evolution",
            "Portfolio rationalization",
            "Proposition lifecycle optimization",
        ],
        "excludes": [
            "Proposition performance operation (Operate stage; adjacent context)",
            "Capability improvement (owning domains; adjacent domains)",
            "Strategic adaptation (strategy-direction x improve; adjacent domain)",
        ],
        "outcomes": [
            "Proposition performance review is conducted and findings are committed.",
            "Products and services are evolved based on performance evidence.",
            "Portfolio is rationalized against strategic fit and performance.",
            "Proposition lifecycle is optimized for the next planning cycle.",
        ],
        "adjacent": [
            "dea:pc-pv-conceive", "dea:pc-pv-design", "dea:pc-pv-build", "dea:pc-pv-operate",
        ],
        "processes": ["dea:process-conduct-proposition-performance-review"],
        "l1_candidates": ["Product Evolution"],
        "grounding_phrase": "improvement of propositions, products, and portfolio",
        "enterprise_concern": "the improvement of the enterprise's products and portfolio.",
        "lifecycle_concern": "improving proposition performance, evolving products and services, and rationalizing the portfolio.",
        "combined_meaning": "The learning and adaptation work of conducting proposition performance reviews, evolving products and services, and rationalizing the portfolio.",
    },
]


def render_list(items, indent="    - "):
    return "\n".join(f"{indent}{i}" for i in items)


def render_adjacent_boundaries(stage, adjacent):
    lines = []
    for a in adjacent:
        short = a.replace("dea:", "")
        lines.append(f'    - "dea:{short} (adjacent context): proposition flow between {stage} and the adjacent cell."')
    return "\n".join(lines)


CONTEXT_TEMPLATE = """# Process Context Cell Charter: {domain} x {stage}.
#
# Lands as part of CR-BP-21c (ProductAndValue landing, third
# unadmitted-domain tranche under ECF v2.4.0 register v2 / CR-BP-19).
# Carries the full Cell Charter (CR-BP-02 §7).
#
# v2.4.0 grounding: dea-metaframework/framework/domain-grounding.md §3.5
# (Product & Value: {grounding_phrase}).
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
  enterprise_concern: "Product & Value: {enterprise_concern}"
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
established_by: CR-BP-21c
established_at: '{CHANGE_DATE}'

# Change history.
change_history:
  - cr: CR-BP-21c
    date: '{CHANGE_DATE}'
    change: |
      Initial Process Context record; promoted from the CR-BP-19
      register v2 (ratified against ECF v2.4.0) as part of the
      ProductAndValue landing tranche. Substrate-neutral
      per ADR-ECF-002 §5 / CR-ECF-007.

links:
  - rel: change-request
    href: change-requests/CR-BP-21c-product-value-landing.md
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


# ----- L1 Process Group: dea:group-proposition-conception -----

group_dir = ENT / "dea:group-proposition-conception"
group_dir.mkdir(parents=True, exist_ok=True)
(group_dir / "candidates").mkdir(exist_ok=True)
(group_dir / "retired").mkdir(exist_ok=True)
(group_dir / "research").mkdir(exist_ok=True)

(group_dir / "README.md").write_text(
    """# Canonical Process Group: `dea:group-proposition-conception`

This directory hosts the canonical Process Group record
for `dea:group-proposition-conception`. The Process Group is a
catalog-owned record (not an OpenDEA metamodel entity) that organises
the Business Process responsibilities of conceiving the enterprise's
value-bearing propositions in the **ProductAndValue x
Conceive** context (per ECF v2.4.0,
dea-metaframework/framework/domain-grounding.md §3.5).

Lands as part of CR-BP-21c (ProductAndValue landing).
Substrate-neutral: applies to biological, artificial, and hybrid agents
without reclassification (ADR-ECF-002 §5, CR-ECF-007).

Composes the L2 Business Processes assigned to the Conceive cell of
ProductAndValue:

- `dea:process-frame-value-proposition-thesis` (lands under
  CR-BP-21c; remaining 2 Conceive L2s land in CR-BP-21c.1)
"""
)

(group_dir / "dea:group-proposition-conception.yaml").write_text(
    f"""id: dea:group-proposition-conception
type: ProcessGroup
version: 1.0.0

name: Proposition Conception

# Normative definition (PG-006 / MECE).
definition: |
  The bounded Process Group that organises the Business Process
  responsibilities of conceiving the enterprise's value-bearing
  propositions in the ProductAndValue x Conceive context.
  This group covers the front-end work of framing value proposition
  theses, framing portfolio direction, and framing innovation theses.
  v2.4.0 grounding (domain-grounding.md §3.5): the domain manages the
  complete lifecycle of whatever the enterprise creates, shapes,
  packages, and makes available for exchange with external parties.
  The Process Group manages the proposition as a stable subject: the
  value-bearing entity (product, service, solution, experience,
  platform, intellectual property) that the enterprise designs,
  builds, evolves, and eventually retires.

# Process Context reference (PG-003 enforces resolution).
process_context: dea:pc-pv-conceive

# Scope (MECE boundary; PG-006 depends on excludes).
scope:
  includes:
    - Value proposition thesis framing
    - Portfolio direction framing
    - Innovation thesis framing
    - Proposition concept validation
  excludes:
    - Strategic portfolio investment decisions (strategy-direction x conceive)
    - Capability strategy (governance-existence x conceive)
    - Proposition design (Design stage; adjacent context)
    - Product development (Build stage; adjacent context)
    - Alliance and partnership thesis (party-relationship x conceive)

# Intended enterprise outcomes.
outcomes:
  - Value proposition thesis is framed for the enterprise.
  - Portfolio direction is framed with bounded scope.
  - Innovation thesis is framed and validated.
  - Proposition concepts are validated against market evidence.

# Canonical containment (PG-004 / PG-005 / PG-006 enforce).
composes:
  - source_id: dea:group-proposition-conception
    target_id: dea:process-frame-value-proposition-thesis
    relationship_type: composes
    direction: source-to-target
    status: active
    asserted_by: dea-team
    rationale: |
      The L2 process frames the enterprise's value proposition thesis,
      which is the v2.4.0 principal responsibility of the
      ProductAndValue x Conceive cell. Lands under CR-BP-21c.
    evidence: docs/examples/frame-value-proposition-thesis.md
    provenance:
      type: architecture-review
      reference: CR-BP-21c
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
      domain: ProductAndValue
      stage: Conceive
      identifier: ecf:productValue.conceive

# Evidence (CR-BP-11 register strength scale E0..E5).
evidence:
  - source: CR-BP-19 (register v2, ratified against ECF v2.4.0)
    claim: |
      This Process Group's coordinate is ratified-accepted in register
      v2. CR-BP-21c lands the corresponding L1 group; remaining 2
      register v2 L2 candidates for Conceive land in CR-BP-21c.1.
    strength: E4
    reference: entities/v1-alpha/dea:group-customer-lifecycle-management/research/l1-register.yaml

# Metadata (PG-006 cross-context overlap exception path lives here).
metadata:
  established_by: CR-BP-21c
  established_at: '{CHANGE_DATE}'
  cross_context_overlap: []
  change_history:
    - cr: CR-BP-21c
      date: '{CHANGE_DATE}'
      change: |
        Initial Process Group record; promoted from the CR-BP-19 register
        v2 (ratified against ECF v2.4.0) as part of the
        ProductAndValue landing tranche. Composes the L2
        dea:process-frame-value-proposition-thesis.

links:
  - rel: change-request
    href: change-requests/CR-BP-21c-product-value-landing.md
  - rel: predecessor
    href: change-requests/CR-BP-19-l1-register-rederivation-ecf-v240.md
  - rel: research-register
    href: entities/v1-alpha/dea:group-customer-lifecycle-management/research/l1-register.yaml
"""
)
print(f"wrote {group_dir}/dea:group-proposition-conception.yaml")


# ----- 5 L2 processes -----

L2_TEMPLATES = {
    "dea:process-frame-value-proposition-thesis": {
        "name": "Frame Value Proposition Thesis",
        "intent": "develop",
        "ptype": "management",
        "context": "dea:pc-pv-conceive",
        "verb": "Frame",
        "object": "Value Proposition Thesis",
        "scope": "(all enterprise segments)",
        "trigger": "A value proposition thesis is needed because the enterprise is establishing a new value-bearing proposition, reframing an existing one, or responding to market shifts that require a re-conception of the value-bearing proposition.",
        "description": "Operate the Frame Value Proposition Thesis L2 process within the dea:pc-pv-conceive Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "A value proposition thesis with bounded scope, target parties, and value claim is committed.",
        "outcome_statement": "A value proposition thesis with bounded scope, target parties, and value claim is committed and ready to drive Design work, covering the value-bearing proposition (product, service, solution, experience, platform, or intellectual property).",
        "evidence_links": [
            {"type": "standard", "ref": "https://www.apqc.org/resource-overview/resource-library/apqc-process-classification-framework-pcf"},
        ],
    },
    "dea:process-design-product-and-service-propositions": {
        "name": "Design Product and Service Propositions",
        "intent": "develop",
        "ptype": "management",
        "context": "dea:pc-pv-design",
        "verb": "Design",
        "object": "Product and Service Propositions",
        "scope": "(all enterprise segments)",
        "trigger": "A product or service proposition design is needed because the framed value proposition thesis requires bounded proposition architecture, packaging and configuration, and innovation experiment designs.",
        "description": "Operate the Design Product and Service Propositions L2 process within the dea:pc-pv-design Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "Product and service propositions are designed with bounded architecture, packaging, and configuration.",
        "outcome_statement": "Product and service propositions are designed with bounded architecture, packaging, and configuration, ready for the Build cell, covering the value-bearing proposition across products, services, solutions, experiences, and platforms.",
        "evidence_links": [
            {"type": "standard", "ref": "https://www.apqc.org/resource-overview/resource-library/apqc-process-classification-framework-pcf"},
        ],
    },
    "dea:process-develop-product-variants": {
        "name": "Develop Product Variants",
        "intent": "develop",
        "ptype": "core",
        "context": "dea:pc-pv-build",
        "verb": "Develop",
        "object": "Product Variants",
        "scope": "(all enterprise segments)",
        "trigger": "A product variant development is needed because the designed propositions require bounded construction of product variants, service capability, and innovation prototypes.",
        "description": "Operate the Develop Product Variants L2 process within the dea:pc-pv-build Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "Product variants are developed and ready for market readiness preparation.",
        "outcome_statement": "Product variants are developed, service capability is built, and innovation prototypes are validated, ready for the Operate cell.",
        "evidence_links": [
            {"type": "standard", "ref": "https://www.apqc.org/resource-overview/resource-library/apqc-process-classification-framework-pcf"},
        ],
    },
    "dea:process-operate-product-catalogue": {
        "name": "Operate Product Catalogue",
        "intent": "operate",
        "ptype": "core",
        "context": "dea:pc-pv-operate",
        "verb": "Operate",
        "object": "Product Catalogue",
        "scope": "(all enterprise segments)",
        "trigger": "Product catalogue operation is needed because the developed products are now in active operation and require steady-state catalogue, portfolio performance, and proposition lifecycle management.",
        "description": "Operate the Operate Product Catalogue L2 process within the dea:pc-pv-operate Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "Product catalogue is operated with bounded portfolio performance and proposition lifecycle management.",
        "outcome_statement": "Product catalogue is operated with bounded portfolio performance and proposition lifecycle management, covering the full lifecycle from launch to retirement across the value-bearing proposition portfolio.",
        "evidence_links": [
            {"type": "standard", "ref": "https://www.apqc.org/resource-overview/resource-library/apqc-process-classification-framework-pcf"},
        ],
    },
    "dea:process-conduct-proposition-performance-review": {
        "name": "Conduct Proposition Performance Review",
        "intent": "develop",
        "ptype": "management",
        "context": "dea:pc-pv-improve",
        "verb": "Conduct",
        "object": "Proposition Performance Review",
        "scope": "(all enterprise segments)",
        "trigger": "A proposition performance review is needed because performance signals, portfolio gaps, or rationalization requirements indicate that the propositions or the portfolio itself need to be evolved.",
        "description": "Operate the Conduct Proposition Performance Review L2 process within the dea:pc-pv-improve Cell Charter. See trigger and outcome for the bounded work this process owns; see identity.outcome_statement for the testable outcome the process produces.",
        "outcome": "Proposition performance review is conducted with findings committed for product evolution and portfolio rationalization.",
        "outcome_statement": "Proposition performance review is conducted with findings committed for product evolution and portfolio rationalization, ready to drive the next planning cycle.",
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
  established_by: CR-BP-21c
  established_at: '{CHANGE_DATE}'
  change_history:
  - cr: CR-BP-21c
    date: '{CHANGE_DATE}'
    change: |
      Initial L2 Process entry; lands as part of the CR-BP-21c
      ProductAndValue landing tranche under ECF v2.4.0
      register v2 (CR-BP-19). Substrate-neutral per ADR-ECF-002
      §5 / CR-ECF-007: applies to biological, artificial, and
      hybrid agents without reclassification. One of the 5 L2
      landings targeting the 5 ratified cells of the
      ProductAndValue domain.
links:
- rel: change-request
  href: change-requests/CR-BP-21c-product-value-landing.md
- rel: process-context
  href: contexts/v1-alpha/{context_file}.yaml
context:
- ref: {context_id}
"""


def render_evidence(links):
    return "\n".join(f'  - type: {l["type"]}\n    ref: {l["ref"]}' for l in links)


ECF_DOMAIN_MAP = {
    "ProductAndValue": "productValue",
}


for eid, t in L2_TEMPLATES.items():
    pdir = ENT / eid
    pdir.mkdir(parents=True, exist_ok=True)
    (pdir / "candidates").mkdir(exist_ok=True)
    (pdir / "retired").mkdir(exist_ok=True)
    (pdir / "research").mkdir(exist_ok=True)
    context_id = t["context"]
    context_file = context_id.replace("dea:", "").replace(":", "-")
    domain = "ProductAndValue"
    stage = context_id.split("-")[-1]
    stage_title = stage.capitalize()
    ecf_domain = ECF_DOMAIN_MAP[domain]
    ecf_stage = stage
    (pdir / "README.md").write_text(
        f"""# Canonical L2 Business Process: `{eid}`

This directory hosts the canonical L2 Business Process record
for `{eid}`. Lands as part of CR-BP-21c (ProductAndValue
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
