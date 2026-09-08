#!/usr/bin/env python3
"""Generate CR-BP-21a.1 artifacts (StrategyAndDirection completion):
4 non-Conceive L1 groups, 14 remaining L2 processes, composes-edge
update to the existing Conceive group, and processes-list updates to
the 5 SD Process Contexts. Closes the SD register v3 gap.

Run: python scripts/apply_phase_7a1_tranche.py
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).parent.parent
CTX = ROOT / "contexts/v1-alpha"
ENT = ROOT / "entities/v1-alpha"
CHANGE_DATE = "2026-09-08"
CR = "CR-BP-21a.1"
CR_FILE = "change-requests/CR-BP-21a.1-strategy-direction-completion.md"


# ----- 14 L2 processes (remaining register v2 candidates) -----

L2S = [
    # Conceive (join existing dea:group-strategy-direction-conception)
    {"eid": "dea:process-define-enterprise-purpose-and-ambition",
     "name": "Define Enterprise Purpose and Ambition",
     "verb": "Define", "object": "Enterprise Purpose and Ambition",
     "context": "dea:pc-sd-conceive", "stage": "Conceive", "intent": "develop",
     "trigger": "An enterprise purpose definition is needed because the enterprise is being established, reframed, or responding to mandate shifts that require the purpose and ambition to be re-anchored.",
     "outcome": "Enterprise purpose and ambition are defined and committed.",
     "outcome_statement": "Enterprise purpose and ambition are defined and committed as the anchor for strategic intent."},
    {"eid": "dea:process-conceive-strategic-intent",
     "name": "Conceive Strategic Intent",
     "verb": "Conceive", "object": "Strategic Intent",
     "context": "dea:pc-sd-conceive", "stage": "Conceive", "intent": "develop",
     "trigger": "A strategic intent conception is needed because the defined enterprise purpose and ambition requires bounded strategic intent to guide direction-setting.",
     "outcome": "Strategic intent is conceived and framed.",
     "outcome_statement": "Strategic intent is conceived and framed within the enterprise purpose and ambition."},
    {"eid": "dea:process-frame-strategic-horizons",
     "name": "Frame Strategic Horizons",
     "verb": "Frame", "object": "Strategic Horizons",
     "context": "dea:pc-sd-conceive", "stage": "Conceive", "intent": "develop",
     "trigger": "Strategic horizons framing is needed because the conceived strategic intent requires bounded timeframes and milestone anchors to structure planning.",
     "outcome": "Strategic horizons are framed with bounded timeframes.",
     "outcome_statement": "Strategic horizons are framed with bounded timeframes and milestone anchors for the strategic planning cycle."},
    # Design (new group dea:group-strategic-choices-design)
    {"eid": "dea:process-evaluate-strategic-alternatives",
     "name": "Evaluate Strategic Alternatives",
     "verb": "Evaluate", "object": "Strategic Alternatives",
     "context": "dea:pc-sd-design", "stage": "Design", "intent": "develop",
     "trigger": "A strategic alternatives evaluation is needed because the designed strategic options require bounded comparison against objectives, targets, and scenario fit.",
     "outcome": "Strategic alternatives are evaluated and the preferred option is committed.",
     "outcome_statement": "Strategic alternatives are evaluated against objectives, targets, and scenario fit, with the preferred option committed."},
    {"eid": "dea:process-design-objectives-and-targets",
     "name": "Design Objectives and Targets",
     "verb": "Design", "object": "Objectives and Targets",
     "context": "dea:pc-sd-design", "stage": "Design", "intent": "develop",
     "trigger": "An objectives and targets design is needed because the committed strategic option requires bounded measures and ownership to become steerable.",
     "outcome": "Objectives and targets are designed with bounded measures and ownership.",
     "outcome_statement": "Objectives and targets are designed with bounded measures and ownership, aligned to the strategic intent."},
    {"eid": "dea:process-design-strategic-scenarios",
     "name": "Design Strategic Scenarios",
     "verb": "Design", "object": "Strategic Scenarios",
     "context": "dea:pc-sd-design", "stage": "Design", "intent": "develop",
     "trigger": "A strategic scenarios design is needed because the strategic options require bounded assumptions and signposts to stress-test direction under uncertainty.",
     "outcome": "Strategic scenarios are designed with bounded assumptions and signposts.",
     "outcome_statement": "Strategic scenarios are designed with bounded assumptions and signposts, ready for strategic plan construction."},
    # Build (new group dea:group-strategic-plan-build)
    {"eid": "dea:process-build-strategic-roadmap",
     "name": "Build Strategic Roadmap",
     "verb": "Build", "object": "Strategic Roadmap",
     "context": "dea:pc-sd-build", "stage": "Build", "intent": "develop",
     "trigger": "A strategic roadmap build is needed because the designed strategic choices require sequenced initiatives and milestone anchors to become executable.",
     "outcome": "The strategic roadmap is built with sequenced initiatives and milestone anchors.",
     "outcome_statement": "The strategic roadmap is built with sequenced initiatives and milestone anchors, ready for initiative translation."},
    {"eid": "dea:process-translate-strategic-choices-into-initiatives",
     "name": "Translate Strategic Choices into Initiatives",
     "verb": "Translate", "object": "Strategic Choices into Initiatives",
     "context": "dea:pc-sd-build", "stage": "Build", "intent": "develop",
     "trigger": "A strategic choices translation is needed because the built strategic plan and roadmap require bounded initiatives with ownership and sequencing.",
     "outcome": "Strategic choices are translated into bounded initiatives.",
     "outcome_statement": "Strategic choices are translated into bounded initiatives with ownership, sequencing, and resourcing envelopes."},
    {"eid": "dea:process-set-resource-allocation-priorities",
     "name": "Set Resource Allocation Priorities",
     "verb": "Set", "object": "Resource Allocation Priorities",
     "context": "dea:pc-sd-build", "stage": "Build", "intent": "develop",
     "trigger": "Resource allocation priorities are needed because the translated initiatives require bounded resourcing envelopes to be actionable within the strategic plan.",
     "outcome": "Resource allocation priorities are set with bounded envelopes per initiative.",
     "outcome_statement": "Resource allocation priorities are set with bounded envelopes per initiative, aligned to the strategic plan."},
    # Operate (new group dea:group-strategic-steering-operation)
    {"eid": "dea:process-sense-environmental-signals",
     "name": "Sense Environmental Signals",
     "verb": "Sense", "object": "Environmental Signals",
     "context": "dea:pc-sd-operate", "stage": "Operate", "intent": "operate",
     "trigger": "Environmental sensing is needed because the operating strategy requires continuous signals to detect drift, disruption, and opportunity.",
     "outcome": "Environmental signals are sensed, filtered, and routed.",
     "outcome_statement": "Environmental signals are sensed, filtered, and routed to the strategic review cycle."},
    {"eid": "dea:process-steer-initiative-portfolio",
     "name": "Steer Initiative Portfolio",
     "verb": "Steer", "object": "Initiative Portfolio",
     "context": "dea:pc-sd-operate", "stage": "Operate", "intent": "operate",
     "trigger": "Initiative portfolio steering is needed because in-flight initiatives drift against strategic performance and require rebalancing decisions.",
     "outcome": "The initiative portfolio is steered with rebalancing decisions committed.",
     "outcome_statement": "The initiative portfolio is steered with rebalancing decisions committed per review cycle."},
    {"eid": "dea:process-operate-strategic-review-cycle",
     "name": "Operate Strategic Review Cycle",
     "verb": "Operate", "object": "Strategic Review Cycle",
     "context": "dea:pc-sd-operate", "stage": "Operate", "intent": "operate",
     "trigger": "The strategic review cycle operation is needed because strategic performance monitoring and steering require a standing cadence of review with recorded decisions.",
     "outcome": "The strategic review cycle is operated with cadence, inputs, and decisions recorded.",
     "outcome_statement": "The strategic review cycle is operated with cadence, inputs, and decisions recorded for the strategic record."},
    # Improve (new group dea:group-strategic-adaptation)
    {"eid": "dea:process-refresh-objectives-and-targets",
     "name": "Refresh Objectives and Targets",
     "verb": "Refresh", "object": "Objectives and Targets",
     "context": "dea:pc-sd-improve", "stage": "Improve", "intent": "develop",
     "trigger": "An objectives refresh is needed because strategic performance evidence or environmental signals indicate that current objectives and targets no longer fit the direction.",
     "outcome": "Objectives and targets are refreshed against performance evidence.",
     "outcome_statement": "Objectives and targets are refreshed against strategic performance evidence and environmental signals."},
    {"eid": "dea:process-review-strategy-effectiveness",
     "name": "Review Strategy Effectiveness",
     "verb": "Review", "object": "Strategy Effectiveness",
     "context": "dea:pc-sd-improve", "stage": "Improve", "intent": "develop",
     "trigger": "A strategy effectiveness review is needed because the adaptation cycle requires committed findings on whether the current direction is producing the intended outcomes.",
     "outcome": "Strategy effectiveness is reviewed with findings committed.",
     "outcome_statement": "Strategy effectiveness is reviewed against strategic intent and performance evidence, with findings committed to the next adaptation cycle."},
]


L2_TEMPLATE = """id: {eid}
name: {name}
type: Process
version: 1.0.0
lifecycle_status: candidate
status: candidate
process_intent: {intent}
process_type: strategic
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
  target_id: ecf:strategyDirection.{ecf_stage}
ecfConformance:
  framework: EnterpriseConceptFramework
  contractVersion: 1.0.0
  profile: dea:ecf@1.0.0
  status: conformant
  affiliation: inherits-catalog
  canonicalReferences:
  - kind: coordinate
    domain: StrategyAndDirection
    stage: {stage}
    identifier: ecf:strategyDirection.{ecf_stage}
metadata:
  established_by: {CR}
  established_at: '{CHANGE_DATE}'
  change_history:
  - cr: {CR}
    date: '{CHANGE_DATE}'
    change: |
      Initial L2 Process entry; lands as part of the {CR}
      StrategyAndDirection completion tranche under ECF v2.4.0
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
for `{eid}`. Lands as part of {CR} (StrategyAndDirection
completion). Process Context: `{context_id}`.
"""
    )
    (pdir / f"{eid}.yaml").write_text(
        L2_TEMPLATE.format(
            eid=eid,
            name=t["name"],
            intent=t["intent"],
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


# ----- 4 new L1 Process Groups (non-Conceive SD cells) -----

GROUPS = [
    {
        "gid": "dea:group-strategic-choices-design",
        "name": "Strategic Choices Design",
        "context": "dea:pc-sd-design",
        "stage": "Design",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of designing strategic choices in the "
            "StrategyAndDirection x Design context. This group covers the "
            "analytical work of designing strategic options, evaluating "
            "strategic alternatives, designing objectives and targets, and "
            "designing strategic scenarios. v2.4.0 grounding "
            "(domain-grounding.md §3.2): Strategy & Direction directs within "
            "the frame that Governance & Existence authorises."
        ),
        "includes": [
            "Strategic option design",
            "Strategic alternatives evaluation",
            "Objectives and targets design",
            "Strategic scenarios design",
        ],
        "excludes": [
            "Operational planning (enablement-operations x design)",
            "Financial plan design (finance-accounting x design)",
            "Strategic intent conception (Conceive stage; adjacent context)",
        ],
        "outcomes": [
            "Strategic options are designed and evaluated.",
            "Objectives and targets are designed with bounded measures.",
            "Strategic scenarios are designed with bounded assumptions.",
        ],
        "composes": [
            ("dea:process-design-strategic-options", "landed CR-BP-21a"),
            ("dea:process-evaluate-strategic-alternatives", CR),
            ("dea:process-design-objectives-and-targets", CR),
            ("dea:process-design-strategic-scenarios", CR),
        ],
        "ecf_stage": "design",
    },
    {
        "gid": "dea:group-strategic-plan-build",
        "name": "Strategic Plan Build",
        "context": "dea:pc-sd-build",
        "stage": "Build",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of building the strategic plan in the "
            "StrategyAndDirection x Build context. This group covers the "
            "constructive work of building the strategic plan, building the "
            "strategic roadmap, translating strategic choices into "
            "initiatives, and setting resource allocation priorities. "
            "v2.4.0 grounding (domain-grounding.md §3.2)."
        ),
        "includes": [
            "Strategic plan build",
            "Strategic roadmap build",
            "Strategic choices translation into initiatives",
            "Resource allocation priorities",
        ],
        "excludes": [
            "Budget construction (finance-accounting x build)",
            "Capability build (owning domains)",
            "Strategic choices design (Design stage; adjacent context)",
        ],
        "outcomes": [
            "Strategic plan is built and committed.",
            "Strategic roadmap is built with sequenced initiatives.",
            "Resource allocation priorities are set per initiative.",
        ],
        "composes": [
            ("dea:process-build-strategic-plan", "landed CR-BP-21a"),
            ("dea:process-build-strategic-roadmap", CR),
            ("dea:process-translate-strategic-choices-into-initiatives", CR),
            ("dea:process-set-resource-allocation-priorities", CR),
        ],
        "ecf_stage": "build",
    },
    {
        "gid": "dea:group-strategic-steering-operation",
        "name": "Strategic Steering Operation",
        "context": "dea:pc-sd-operate",
        "stage": "Operate",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of operating strategic steering in the "
            "StrategyAndDirection x Operate context. This group covers the "
            "steady-state work of monitoring strategic performance, sensing "
            "environmental signals, steering the initiative portfolio, and "
            "operating the strategic review cycle. v2.4.0 grounding "
            "(domain-grounding.md §3.2)."
        ),
        "includes": [
            "Strategic performance monitoring",
            "Environmental sensing",
            "Initiative portfolio steering",
            "Strategic review cycle operation",
        ],
        "excludes": [
            "Operational performance management (enablement-operations x operate)",
            "Initiative execution (enablement-operations x operate)",
            "Strategic plan build (Build stage; adjacent context)",
        ],
        "outcomes": [
            "Strategic performance is monitored against objectives.",
            "Environmental signals are sensed and routed.",
            "Initiative portfolio is steered with rebalancing decisions.",
            "Strategic review cycle is operated on cadence.",
        ],
        "composes": [
            ("dea:process-monitor-strategic-performance", "landed CR-BP-21a"),
            ("dea:process-sense-environmental-signals", CR),
            ("dea:process-steer-initiative-portfolio", CR),
            ("dea:process-operate-strategic-review-cycle", CR),
        ],
        "ecf_stage": "operate",
    },
    {
        "gid": "dea:group-strategic-adaptation",
        "name": "Strategic Adaptation",
        "context": "dea:pc-sd-improve",
        "stage": "Improve",
        "definition": (
            "The bounded Process Group that organises the Business Process "
            "responsibilities of adapting the strategic direction in the "
            "StrategyAndDirection x Improve context. This group covers the "
            "learning and adaptation work of adapting strategic direction, "
            "refreshing objectives and targets, and reviewing strategy "
            "effectiveness. v2.4.0 grounding (domain-grounding.md §3.2)."
        ),
        "includes": [
            "Strategic direction adaptation",
            "Objectives and targets refresh",
            "Strategy effectiveness review",
        ],
        "excludes": [
            "Capability improvement (owning domains)",
            "Strategic steering operation (Operate stage; adjacent context)",
        ],
        "outcomes": [
            "Strategic direction is adapted on evidence.",
            "Objectives and targets are refreshed.",
            "Strategy effectiveness is reviewed with findings committed.",
        ],
        "composes": [
            ("dea:process-adapt-strategic-direction", "landed CR-BP-21a"),
            ("dea:process-refresh-objectives-and-targets", CR),
            ("dea:process-review-strategy-effectiveness", CR),
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
      domain: StrategyAndDirection
      stage: {stage}
      identifier: ecf:strategyDirection.{ecf_stage}

# Evidence (CR-BP-11 register strength scale E0..E5).
evidence:
  - source: CR-BP-19 (register v2, ratified against ECF v2.4.0)
    claim: |
      This Process Group's coordinate is ratified-accepted in register
      v2. {CR} lands the corresponding L1 group as part of the
      StrategyAndDirection completion tranche.
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
        StrategyAndDirection completion tranche.

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
(StrategyAndDirection x {g['stage']}). Lands as part of {CR}
(StrategyAndDirection completion). Composes the L2 Business Processes
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
        composes_yaml=render_composes(g["composes"]),
        stage=g["stage"],
        ecf_stage=g["ecf_stage"],
        CR=CR,
        CR_FILE=CR_FILE,
        CHANGE_DATE=CHANGE_DATE,
    ).replace("{GID}", gid)
    (gdir / f"{gid}.yaml").write_text(body)
    print(f"wrote {gdir}/{gid}.yaml")


# ----- Update existing Conceive group + 5 SD contexts -----
#
# NOTE: these two updates were applied as surgical text patches (not a
# YAML round-trip) to preserve the authored comment blocks and scalar
# formatting of the existing files. The edits:
#
#   1. dea:group-strategy-direction-conception.yaml — 3 new composes
#      edges (define-enterprise-purpose-and-ambition,
#      conceive-strategic-intent, frame-strategic-horizons) plus a
#      CR-BP-21a.1 change_history entry.
#   2. dea-pc-sd-{conceive,design,build,operate,improve}.yaml —
#      processes: list extended with the new cell L2s plus a
#      CR-BP-21a.1 change_history entry.
#
# A yaml.safe_load -> yaml.dump round-trip strips comments and
# re-wraps folded scalars; do not use it for in-place edits of
# authored catalog files.

print("\nDone. Next: dispositions + tranche plan + register audit + regenerate + gates.")
