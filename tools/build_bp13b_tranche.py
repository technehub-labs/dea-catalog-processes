"""Generate CR-BP-13b tranche files (GovernanceAndExistence).

Produces 5 Process Context cells + 5 Process Group records + 9 L2
Process entries + per-entity README files. Reuses the renderer
helpers from tools/build_bp13a_tranche.py (CR-BP-13a).

This is a per-tranche generator: it declares the 5+5+9 entries
specific to GovernanceAndExistence and delegates the YAML rendering
to the imported helpers.

The generator's renderers are parameterised on `process_context`,
`process_group`, and the per-entry data; they don't depend on the
domain name. We override STAGE_NAMES and ECF_IDENTIFIERS to add the
GovernanceAndExistence (ge) Process Context ids.

Usage:
    python tools/build_bp13b_tranche.py
    python tools/build_bp13b_tranche.py --dry-run
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Reuse CR-BP-13a renderers and infrastructure.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_bp13a_tranche import (  # noqa: E402
    CRATED_AT,
    PROCESS_CONTEXTS as _CD_CONTEXTS,
    PROCESS_GROUPS as _CD_GROUPS,
    L2_PROCESSES as _CD_L2,
    REPO_ROOT,
    render_l2_process,
    render_process_context,
    render_process_group,
    write_file,
)

# Note: STAGE_NAMES and ECF_IDENTIFIERS are imported (transitively,
# via the shared renderer module) by the build_bp13a_tranche
# renderers, which are the single source of truth for those
# lookups. The shared renderers use DOMAIN_NAMES (a lookup by
# mid-segment of the Process Context id) to pick the right domain
# name when emitting the ECF canonical reference, so per-tranche
# scripts do not need to override anything.

CR = "CR-BP-13b"


# ---------------------------------------------------------------------------
# Process Context cells
# ---------------------------------------------------------------------------

PROCESS_CONTEXTS = [
    {
        "id": "dea:pc-ge-c",
        "domain": "GovernanceAndExistence",
        "stage": "Conceive",
        "name": "Strategy and Governance Conception",
        "definition": (
            "The bounded enterprise context for **conceiving** the "
            "strategy, mandate, and policy direction of the "
            "organization in the **governance and existence** domain. "
            "This context addresses the front-end work of framing the "
            "enterprise's governance strategy, policy posture, and "
            "charter direction: deciding what the organization exists "
            "to do, what policies govern its operation, and what "
            "charters define its authorities."
        ),
        "includes": [
            "Governance strategy framing",
            "Policy and mandate initiation",
            "Charter direction",
            "Board mandate conception",
        ],
        "excludes": [
            "Governance system design (Design stage; adjacent context)",
            "Governance body establishment (Build stage; adjacent context)",
            "Governance oversight (Operate stage; adjacent context)",
        ],
        "outcomes": [
            "Governance strategy is framed with a defensible mandate.",
            "Policy and charter direction is committed.",
            "Board mandate is articulated.",
        ],
        "adjacent": [
            ("dea:pc-ge-d", "Design"),
            ("dea:pc-ge-b", "Build"),
            ("dea:pc-ge-op", "Operate"),
            ("dea:pc-ge-im", "Improve"),
        ],
        "l2_processes": [
            "dea:process-develop-governance-strategy",
            "dea:process-initiate-policy-and-charter",
        ],
        "enterprise_concern": (
            "Governance and existence: the enterprise's mandate, "
            "policy posture, and charter direction."
        ),
        "lifecycle_concern": (
            "Conceive: framing governance strategy, mandate, and "
            "policy direction."
        ),
        "combined_semantic_meaning": (
            "The front-end work of framing what the organization "
            "exists to do, what policies govern its operation, and "
            "what charters define its authorities."
        ),
        "expected_outcomes": [
            "Governance strategy is framed with a defensible mandate.",
            "Policy and charter direction is committed.",
            "Board mandate is articulated.",
        ],
        "inclusions": [
            "Governance strategy framing",
            "Policy and mandate initiation",
            "Charter direction",
        ],
        "exclusions": [
            "Governance system design (Design stage)",
            "Governance body establishment (Build stage)",
            "Governance oversight (Operate stage)",
        ],
        "adjacent_boundaries": [
            "dea:pc-ge-d (Design): strategy flows into governance system design.",
            "dea:pc-ge-b (Build): designs flow into body and charter construction.",
            "dea:pc-ge-op (Operate): framed strategy is realised in board and committee operations.",
            "dea:pc-ge-im (Improve): framed strategy is reviewed and refreshed.",
        ],
    },
    {
        "id": "dea:pc-ge-d",
        "domain": "GovernanceAndExistence",
        "stage": "Design",
        "name": "Governance System Design",
        "definition": (
            "The bounded enterprise context for **designing** the "
            "governance system, control objectives, and policy "
            "architecture in the **governance and existence** domain. "
            "This context addresses the work of translating strategy "
            "and mandate into a designed governance architecture, a "
            "set of control objectives, and an articulated policy "
            "architecture that the enterprise can build."
        ),
        "includes": [
            "Governance system architecture",
            "Control objectives",
            "Policy architecture",
            "Authority delegation design",
        ],
        "excludes": [
            "Strategy framing (Conceive stage)",
            "Body and charter construction (Build stage)",
            "Governance operation (Operate stage)",
        ],
        "outcomes": [
            "Governance system is designed and testable.",
            "Control objectives are articulated.",
            "Policy architecture is ready to be built.",
        ],
        "adjacent": [
            ("dea:pc-ge-c", "Conceive"),
            ("dea:pc-ge-b", "Build"),
            ("dea:pc-ge-op", "Operate"),
            ("dea:pc-ge-im", "Improve"),
        ],
        "l2_processes": [
            "dea:process-design-governance-system",
            "dea:process-design-policies-and-controls",
        ],
        "enterprise_concern": (
            "Governance and existence: the enterprise's mandate, "
            "policy posture, and charter direction."
        ),
        "lifecycle_concern": (
            "Design: articulating how governance and policy will be "
            "structured and controlled."
        ),
        "combined_semantic_meaning": (
            "Translating strategy and mandate into a designed "
            "governance architecture, control objectives, and policy "
            "architecture."
        ),
        "expected_outcomes": [
            "Governance system is designed and testable.",
            "Control objectives are articulated.",
            "Policy architecture is ready to be built.",
        ],
        "inclusions": [
            "Governance system architecture",
            "Control objectives",
            "Policy architecture",
        ],
        "exclusions": [
            "Strategy framing (Conceive stage)",
            "Body and charter construction (Build stage)",
            "Governance operation (Operate stage)",
        ],
        "adjacent_boundaries": [
            "dea:pc-ge-c (Conceive): the prior lifecycle stage; strategy flows into design.",
            "dea:pc-ge-b (Build): designs flow into body and charter construction.",
            "dea:pc-ge-op (Operate): designed system is realised in board and committee operations.",
            "dea:pc-ge-im (Improve): designed system is reviewed and refreshed.",
        ],
    },
    {
        "id": "dea:pc-ge-b",
        "domain": "GovernanceAndExistence",
        "stage": "Build",
        "name": "Governance Body Establishment",
        "definition": (
            "The bounded enterprise context for **building** the "
            "governance bodies, charters, and policy artefacts in "
            "the **governance and existence** domain. This context "
            "addresses the work of standing up the operational "
            "artefacts that constitute governance: boards, "
            "committees, charters, codified policies, and standards."
        ),
        "includes": [
            "Board and committee establishment",
            "Charter codification",
            "Policy artefact construction",
            "Standard and procedure documentation",
        ],
        "excludes": [
            "Strategy framing (Conceive stage)",
            "Governance system design (Design stage)",
            "Governance operation (Operate stage)",
        ],
        "outcomes": [
            "Governance bodies are established and operational.",
            "Charters are codified.",
            "Policy artefacts are operational.",
        ],
        "adjacent": [
            ("dea:pc-ge-c", "Conceive"),
            ("dea:pc-ge-d", "Design"),
            ("dea:pc-ge-op", "Operate"),
            ("dea:pc-ge-im", "Improve"),
        ],
        "l2_processes": [
            "dea:process-establish-governance-bodies",
            "dea:process-codify-charters-and-policies",
        ],
        "enterprise_concern": (
            "Governance and existence: the enterprise's mandate, "
            "policy posture, and charter direction."
        ),
        "lifecycle_concern": (
            "Build: standing up the governance bodies, charters, and "
            "policy artefacts."
        ),
        "combined_semantic_meaning": (
            "Standing up the operational artefacts that constitute "
            "governance: boards, committees, charters, codified "
            "policies, and standards."
        ),
        "expected_outcomes": [
            "Governance bodies are established and operational.",
            "Charters are codified.",
            "Policy artefacts are operational.",
        ],
        "inclusions": [
            "Board and committee establishment",
            "Charter codification",
            "Policy artefact construction",
        ],
        "exclusions": [
            "Strategy framing (Conceive stage)",
            "Governance system design (Design stage)",
            "Governance operation (Operate stage)",
        ],
        "adjacent_boundaries": [
            "dea:pc-ge-c (Conceive): strategy is the build's input.",
            "dea:pc-ge-d (Design): governance system designs guide the build.",
            "dea:pc-ge-op (Operate): built bodies and charters operate.",
            "dea:pc-ge-im (Improve): built bodies and charters are reviewed.",
        ],
    },
    {
        "id": "dea:pc-ge-op",
        "domain": "GovernanceAndExistence",
        "stage": "Operate",
        "name": "Governance Oversight",
        "definition": (
            "The bounded enterprise context for **operating** the "
            "governance oversight, board and committee cycles, risk "
            "oversight, and policy compliance execution in the "
            "**governance and existence** domain. This context "
            "addresses the day-to-day work of running the governance "
            "machinery: convening boards, executing risk reviews, "
            "auditing policy compliance, and making governance "
            "decisions."
        ),
        "includes": [
            "Board and committee cycle operation",
            "Risk oversight",
            "Policy compliance execution",
            "Audit and assurance",
        ],
        "excludes": [
            "Strategy framing (Conceive stage)",
            "Governance system design (Design stage)",
            "Body establishment (Build stage)",
        ],
        "outcomes": [
            "Board and committee cycles run on schedule.",
            "Risk is identified and mitigated.",
            "Policy compliance is maintained.",
        ],
        "adjacent": [
            ("dea:pc-ge-c", "Conceive"),
            ("dea:pc-ge-d", "Design"),
            ("dea:pc-ge-b", "Build"),
            ("dea:pc-ge-im", "Improve"),
        ],
        "l2_processes": [
            "dea:process-operate-governance-oversight",
            "dea:process-audit-policy-compliance",
        ],
        "enterprise_concern": (
            "Governance and existence: the enterprise's mandate, "
            "policy posture, and charter direction."
        ),
        "lifecycle_concern": (
            "Operate: running the governance machinery on a "
            "continuous cycle."
        ),
        "combined_semantic_meaning": (
            "The day-to-day work of running the governance "
            "machinery: boards, committees, risk oversight, "
            "compliance execution."
        ),
        "expected_outcomes": [
            "Board and committee cycles run on schedule.",
            "Risk is identified and mitigated.",
            "Policy compliance is maintained.",
        ],
        "inclusions": [
            "Board and committee cycle operation",
            "Risk oversight",
            "Policy compliance execution",
        ],
        "exclusions": [
            "Strategy framing (Conceive stage)",
            "Governance system design (Design stage)",
            "Body establishment (Build stage)",
        ],
        "adjacent_boundaries": [
            "dea:pc-ge-c (Conceive): insights from operation shape strategy.",
            "dea:pc-ge-d (Design): operation reveals design gaps.",
            "dea:pc-ge-b (Build): operation runs the built governance bodies.",
            "dea:pc-ge-im (Improve): operation is reviewed and improved.",
        ],
    },
    {
        "id": "dea:pc-ge-im",
        "domain": "GovernanceAndExistence",
        "stage": "Improve",
        "name": "Governance Review and Learning",
        "definition": (
            "The bounded enterprise context for **improving** the "
            "governance bodies, policy regimes, and oversight "
            "machinery in the **governance and existence** domain. "
            "This context addresses the work of reviewing "
            "governance effectiveness, scoring audit findings, and "
            "feeding the lessons back into Conceive/Design/Build/"
            "Operate cycles."
        ),
        "includes": [
            "Governance effectiveness review",
            "Audit finding scoring",
            "Policy regime refinement",
            "Lessons-learned propagation",
        ],
        "excludes": [
            "Governance operation (Operate stage)",
            "Strategy framing (Conceive stage)",
            "Governance system design (Design stage)",
        ],
        "outcomes": [
            "Governance effectiveness is measured.",
            "Audit findings drive improvement.",
            "Lessons learned feed back into Conceive/Design cycles.",
        ],
        "adjacent": [
            ("dea:pc-ge-c", "Conceive"),
            ("dea:pc-ge-d", "Design"),
            ("dea:pc-ge-b", "Build"),
            ("dea:pc-ge-op", "Operate"),
        ],
        "l2_processes": [
            "dea:process-review-governance-effectiveness",
        ],
        "enterprise_concern": (
            "Governance and existence: the enterprise's mandate, "
            "policy posture, and charter direction."
        ),
        "lifecycle_concern": (
            "Improve: closing the loop between governance insight and "
            "conceive/design/build/operate cycles."
        ),
        "combined_semantic_meaning": (
            "Reviewing governance effectiveness, scoring audit "
            "findings, and feeding lessons back into Conceive/Design/"
            "Build/Operate cycles."
        ),
        "expected_outcomes": [
            "Governance effectiveness is measured.",
            "Audit findings drive improvement.",
            "Lessons learned feed back into Conceive/Design cycles.",
        ],
        "inclusions": [
            "Governance effectiveness review",
            "Audit finding scoring",
            "Policy regime refinement",
        ],
        "exclusions": [
            "Governance operation (Operate stage)",
            "Strategy framing (Conceive stage)",
            "Governance system design (Design stage)",
        ],
        "adjacent_boundaries": [
            "dea:pc-ge-c (Conceive): insights shape strategy framing.",
            "dea:pc-ge-d (Design): insights sharpen governance design.",
            "dea:pc-ge-b (Build): insights reveal body and charter gaps.",
            "dea:pc-ge-op (Operate): insights refine day-to-day governance operation.",
        ],
    },
]


# ---------------------------------------------------------------------------
# Process Groups
# ---------------------------------------------------------------------------

PROCESS_GROUPS = [
    {
        "id": "dea:group-strategy-and-governance-conception",
        "name": "Strategy and Governance Conception",
        "context": "dea:pc-ge-c",
        "definition": (
            "The bounded Process Group that organizes the Business "
            "Process responsibilities of conceiving strategy, mandate, "
            "and policy direction in the GovernanceAndExistence x "
            "Conceive context. This group captures the front-end work "
            "of framing the enterprise's governance strategy, policy "
            "posture, and charter direction. The group is the "
            "canonical Process Group for the strategy-and-governance "
            "value stream."
        ),
        "includes": [
            "Governance strategy framing",
            "Policy and mandate initiation",
            "Charter direction",
            "Board mandate conception",
        ],
        "excludes": [
            "Governance system design (Design stage; adjacent context)",
            "Governance body establishment (Build stage; adjacent context)",
            "Governance oversight (Operate stage)",
        ],
        "outcomes": [
            "Governance strategy is framed with a defensible mandate.",
            "Policy and charter direction is committed.",
            "Board mandate is articulated.",
        ],
        "composes": [
            "dea:process-develop-governance-strategy",
            "dea:process-initiate-policy-and-charter",
        ],
        "coordinate": "ecf:governanceExistence.conceive",
    },
    {
        "id": "dea:group-governance-system-design",
        "name": "Governance System Design",
        "context": "dea:pc-ge-d",
        "definition": (
            "The bounded Process Group that organizes the Business "
            "Process responsibilities of designing the governance "
            "system, control objectives, and policy architecture in "
            "the GovernanceAndExistence x Design context. This group "
            "captures the work of translating strategy and mandate "
            "into a designed governance architecture, control "
            "objectives, and policy architecture. The group is the "
            "canonical Process Group for the governance-design value "
            "stream."
        ),
        "includes": [
            "Governance system architecture",
            "Control objectives",
            "Policy architecture",
            "Authority delegation design",
        ],
        "excludes": [
            "Strategy framing (Conceive stage)",
            "Body and charter construction (Build stage)",
            "Governance operation (Operate stage)",
        ],
        "outcomes": [
            "Governance system is designed and testable.",
            "Control objectives are articulated.",
            "Policy architecture is ready to be built.",
        ],
        "composes": [
            "dea:process-design-governance-system",
            "dea:process-design-policies-and-controls",
        ],
        "coordinate": "ecf:governanceExistence.design",
    },
    {
        "id": "dea:group-governance-body-establishment",
        "name": "Governance Body Establishment",
        "context": "dea:pc-ge-b",
        "definition": (
            "The bounded Process Group that organizes the Business "
            "Process responsibilities of building governance bodies, "
            "charters, and policy artefacts in the "
            "GovernanceAndExistence x Build context. This group "
            "captures the work of standing up the operational "
            "artefacts that constitute governance: boards, "
            "committees, charters, codified policies, and standards."
        ),
        "includes": [
            "Board and committee establishment",
            "Charter codification",
            "Policy artefact construction",
            "Standard and procedure documentation",
        ],
        "excludes": [
            "Strategy framing (Conceive stage)",
            "Governance system design (Design stage)",
            "Governance operation (Operate stage)",
        ],
        "outcomes": [
            "Governance bodies are established and operational.",
            "Charters are codified.",
            "Policy artefacts are operational.",
        ],
        "composes": [
            "dea:process-establish-governance-bodies",
            "dea:process-codify-charters-and-policies",
        ],
        "coordinate": "ecf:governanceExistence.build",
    },
    {
        "id": "dea:group-governance-oversight",
        "name": "Governance Oversight",
        "context": "dea:pc-ge-op",
        "definition": (
            "The bounded Process Group that organizes the Business "
            "Process responsibilities of operating governance "
            "oversight, board and committee cycles, risk oversight, "
            "and policy compliance execution in the "
            "GovernanceAndExistence x Operate context. This group "
            "captures the day-to-day work of running the governance "
            "machinery: convening boards, executing risk reviews, "
            "auditing policy compliance, and making governance "
            "decisions."
        ),
        "includes": [
            "Board and committee cycle operation",
            "Risk oversight",
            "Policy compliance execution",
            "Audit and assurance",
        ],
        "excludes": [
            "Strategy framing (Conceive stage)",
            "Governance system design (Design stage)",
            "Body establishment (Build stage)",
        ],
        "outcomes": [
            "Board and committee cycles run on schedule.",
            "Risk is identified and mitigated.",
            "Policy compliance is maintained.",
        ],
        "composes": [
            "dea:process-operate-governance-oversight",
            "dea:process-audit-policy-compliance",
        ],
        "coordinate": "ecf:governanceExistence.operate",
    },
    {
        "id": "dea:group-governance-review-and-learning",
        "name": "Governance Review and Learning",
        "context": "dea:pc-ge-im",
        "definition": (
            "The bounded Process Group that organizes the Business "
            "Process responsibilities of improving governance "
            "effectiveness in the GovernanceAndExistence x Improve "
            "context. This group captures the work of reviewing "
            "governance effectiveness, scoring audit findings, and "
            "feeding lessons back into Conceive/Design/Build/Operate "
            "cycles."
        ),
        "includes": [
            "Governance effectiveness review",
            "Audit finding scoring",
            "Policy regime refinement",
            "Lessons-learned propagation",
        ],
        "excludes": [
            "Governance operation (Operate stage)",
            "Strategy framing (Conceive stage)",
            "Governance system design (Design stage)",
        ],
        "outcomes": [
            "Governance effectiveness is measured.",
            "Audit findings drive improvement.",
            "Lessons learned feed back into Conceive/Design cycles.",
        ],
        "composes": [
            "dea:process-review-governance-effectiveness",
        ],
        "coordinate": "ecf:governanceExistence.improve",
    },
]


# ---------------------------------------------------------------------------
# L2 Process entries
# ---------------------------------------------------------------------------

L2_PROCESSES = [
    # Conceive
    {
        "id": "dea:process-develop-governance-strategy",
        "name": "Develop Governance Strategy",
        "process_context": "dea:pc-ge-c",
        "process_group": "dea:group-strategy-and-governance-conception",
        "process_intent": "management",
        "process_type": "strategic",
        "verb": "Develop",
        "object": "Governance Strategy",
        "trigger": (
            "A new governance strategy framing is needed because "
            "the enterprise is establishing a new mandate, "
            "reframing an existing one, or responding to a "
            "regulatory or strategic shift that requires board-level "
            "realignment."
        ),
        "outcome": (
            "A governance strategy document with bounded mandate, "
            "strategic posture, and policy direction is committed."
        ),
        "outcome_statement": (
            "A governance strategy document with bounded mandate, "
            "strategic posture, and policy direction is committed "
            "and ready to drive Design work."
        ),
        "evidence_links": [
            {"type": "standard", "ref": "https://www.iso.org/standard/27036.html"},
            {"type": "documentation", "ref": "docs/examples/develop-governance-strategy.md"},
        ],
    },
    {
        "id": "dea:process-initiate-policy-and-charter",
        "name": "Initiate Policy and Charter",
        "process_context": "dea:pc-ge-c",
        "process_group": "dea:group-strategy-and-governance-conception",
        "process_intent": "management",
        "process_type": "strategic",
        "verb": "Initiate",
        "object": "Policy and Charter",
        "trigger": (
            "A new policy regime, charter, or board mandate must be "
            "initiated because of a new governance strategy, a new "
            "regulatory requirement, or a reorganisation of the "
            "enterprise."
        ),
        "outcome": (
            "An initial policy and charter document with proposed "
            "scope, authority, and decision rights is committed."
        ),
        "outcome_statement": (
            "An initial policy and charter document with proposed "
            "scope, authority, and decision rights is committed and "
            "ready to drive the Design of the governance system."
        ),
        "evidence_links": [
            {"type": "standard", "ref": "https://www.iso.org/standard/27036.html"},
            {"type": "documentation", "ref": "docs/examples/initiate-policy-and-charter.md"},
        ],
    },
    # Design
    {
        "id": "dea:process-design-governance-system",
        "name": "Design Governance System",
        "process_context": "dea:pc-ge-d",
        "process_group": "dea:group-governance-system-design",
        "process_intent": "management",
        "process_type": "strategic",
        "verb": "Design",
        "object": "Governance System",
        "trigger": (
            "A governance strategy has been committed; the "
            "governance system (boards, committees, authority "
            "delegations, decision rights) must now be designed to "
            "realise that strategy."
        ),
        "outcome": (
            "A governance system design with articulated bodies, "
            "authority delegations, and decision rights is "
            "committed."
        ),
        "outcome_statement": (
            "A governance system design with articulated bodies, "
            "authority delegations, and decision rights is committed "
            "and ready to drive Body Establishment in the Build "
            "context."
        ),
        "evidence_links": [
            {"type": "standard", "ref": "https://www.opengroup.org/togaf"},
            {"type": "documentation", "ref": "docs/examples/design-governance-system.md"},
        ],
    },
    {
        "id": "dea:process-design-policies-and-controls",
        "name": "Design Policies and Controls",
        "process_context": "dea:pc-ge-d",
        "process_group": "dea:group-governance-system-design",
        "process_intent": "management",
        "process_type": "standardization",
        "verb": "Design",
        "object": "Policies and Controls",
        "trigger": (
            "A governance system has been designed; the policies "
            "and controls (policy artefacts, control objectives, "
            "compliance regime) must now be designed to instantiate "
            "the system."
        ),
        "outcome": (
            "A policy and control design with articulated policy "
            "artefacts, control objectives, and compliance regime is "
            "committed."
        ),
        "outcome_statement": (
            "A policy and control design with articulated policy "
            "artefacts, control objectives, and compliance regime is "
            "committed and ready to drive Build and Operate "
            "contexts."
        ),
        "evidence_links": [
            {"type": "standard", "ref": "https://www.coso.org/Pages/default.aspx"},
            {"type": "documentation", "ref": "docs/examples/design-policies-and-controls.md"},
        ],
    },
    # Build
    {
        "id": "dea:process-establish-governance-bodies",
        "name": "Establish Governance Bodies",
        "process_context": "dea:pc-ge-b",
        "process_group": "dea:group-governance-body-establishment",
        "process_intent": "operational",
        "process_type": "core",
        "verb": "Establish",
        "object": "Governance Bodies",
        "trigger": (
            "A governance system design has been committed; the "
            "boards, committees, and other governance bodies must "
            "now be established with charters, members, and "
            "operating rhythms."
        ),
        "outcome": (
            "Governance bodies are established, chartered, and "
            "ready to convene on a regular cycle."
        ),
        "outcome_statement": (
            "Governance bodies are established, chartered, and "
            "ready to convene on a regular cycle in the Operate "
            "context."
        ),
        "evidence_links": [
            {"type": "standard", "ref": "https://www.iso.org/standard/27036.html"},
            {"type": "documentation", "ref": "docs/examples/establish-governance-bodies.md"},
        ],
    },
    {
        "id": "dea:process-codify-charters-and-policies",
        "name": "Codify Charters and Policies",
        "process_context": "dea:pc-ge-b",
        "process_group": "dea:group-governance-body-establishment",
        "process_intent": "operational",
        "process_type": "core",
        "verb": "Codify",
        "object": "Charters and Policies",
        "trigger": (
            "Governance bodies are being established; the "
            "associated charters, policies, and standard artefacts "
            "must be codified for the bodies to operate."
        ),
        "outcome": (
            "Charters, policies, and standard artefacts are "
            "codified and accessible to the governance bodies."
        ),
        "outcome_statement": (
            "Charters, policies, and standard artefacts are "
            "codified, accessible to the governance bodies, and "
            "ready to be operated on."
        ),
        "evidence_links": [
            {"type": "standard", "ref": "https://www.opengroup.org/togaf"},
            {"type": "documentation", "ref": "docs/examples/codify-charters-and-policies.md"},
        ],
    },
    # Operate
    {
        "id": "dea:process-operate-governance-oversight",
        "name": "Operate Governance Oversight",
        "process_context": "dea:pc-ge-op",
        "process_group": "dea:group-governance-oversight",
        "process_intent": "management",
        "process_type": "strategic",
        "verb": "Operate",
        "object": "Governance Oversight",
        "trigger": (
            "Governance bodies are chartered and policies are "
            "codified; the day-to-day governance machinery (board "
            "cycles, risk oversight, decision making) must now run."
        ),
        "outcome": (
            "Board and committee cycles run on schedule; risk is "
            "identified and mitigated; governance decisions are made."
        ),
        "outcome_statement": (
            "Board and committee cycles run on schedule; risk is "
            "identified and mitigated; governance decisions are made "
            "and recorded."
        ),
        "evidence_links": [
            {"type": "standard", "ref": "https://www.iso.org/standard/27036.html"},
            {"type": "documentation", "ref": "docs/examples/operate-governance-oversight.md"},
        ],
    },
    {
        "id": "dea:process-audit-policy-compliance",
        "name": "Audit Policy Compliance",
        "process_context": "dea:pc-ge-op",
        "process_group": "dea:group-governance-oversight",
        "process_intent": "support",
        "process_type": "standardization",
        "verb": "Audit",
        "object": "Policy Compliance",
        "trigger": (
            "Policies are codified and bodies are operating; "
            "periodic audits must verify compliance with the "
            "policies and report findings to the appropriate "
            "governance body."
        ),
        "outcome": (
            "Audit reports with findings, recommendations, and "
            "follow-up actions are delivered to the appropriate "
            "governance body."
        ),
        "outcome_statement": (
            "Audit reports with findings, recommendations, and "
            "follow-up actions are delivered to the appropriate "
            "governance body; non-compliances are tracked to "
            "remediation."
        ),
        "evidence_links": [
            {"type": "standard", "ref": "https://www.isaca.org/resources/cobit"},
            {"type": "documentation", "ref": "docs/examples/audit-policy-compliance.md"},
        ],
    },
    # Improve
    {
        "id": "dea:process-review-governance-effectiveness",
        "name": "Review Governance Effectiveness",
        "process_context": "dea:pc-ge-im",
        "process_group": "dea:group-governance-review-and-learning",
        "process_intent": "management",
        "process_type": "core",
        "verb": "Review",
        "object": "Governance Effectiveness",
        "trigger": (
            "Governance bodies have been operating; periodic "
            "effectiveness reviews must measure governance "
            "performance against the strategy and feed lessons back "
            "into Conceive/Design/Build/Operate cycles."
        ),
        "outcome": (
            "Effectiveness reviews with measured outcomes, "
            "lessons learned, and recommendations are delivered to "
            "the governance bodies."
        ),
        "outcome_statement": (
            "Effectiveness reviews with measured outcomes, lessons "
            "learned, and recommendations are delivered to the "
            "governance bodies; the lessons feed back into the "
            "Conceive/Design/Build/Operate cycles."
        ),
        "evidence_links": [
            {"type": "standard", "ref": "https://www.opengroup.org/togaf"},
            {"type": "documentation", "ref": "docs/examples/review-governance-effectiveness.md"},
        ],
    },
]


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="build-bp13b-tranche")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    print("=== Process Context cells ===")
    for c in PROCESS_CONTEXTS:
        path = REPO_ROOT / f"contexts/v1-alpha/{c['id'].replace(':', '-')}.yaml"
        write_file(path, render_process_context(c), args.dry_run)

    print("\n=== Process Group records ===")
    for g in PROCESS_GROUPS:
        path = REPO_ROOT / f"entities/v1-alpha/{g['id']}/{g['id']}.yaml"
        write_file(path, render_process_group(g), args.dry_run)
        # Stub folders.
        for sub in ("research", "candidates", "retired"):
            stub = REPO_ROOT / f"entities/v1-alpha/{g['id']}/{sub}/.gitkeep"
            if not args.dry_run:
                stub.parent.mkdir(parents=True, exist_ok=True)
                stub.touch()
        # Per-group README.
        readme = REPO_ROOT / f"entities/v1-alpha/{g['id']}/README.md"
        write_file(
            readme,
            (
                f"# Canonical Process Group: `{g['id']}`\n\n"
                f"This directory hosts the canonical Process Group record\n"
                f"for `{g['id']}`. The Process Group is a catalog-owned\n"
                f"record (not an OpenDEA metamodel entity) that organises\n"
                f"the L2 Business Process entries composing into it within\n"
                f"the {g['context']} Process Context.\n\n"
                "## Composition\n\n"
                "This Process Group composes the following L2 Business\n"
                "Process specialization(s):\n\n"
            ),
            args.dry_run,
        )
        if not args.dry_run:
            with readme.open("a", encoding="utf-8") as f:
                for c in g["composes"]:
                    f.write(f"- `{c}`\n")
                f.write(
                    "\n## Change history\n\n"
                    "See the canonical YAML's `metadata.change_history` "
                    "for the per-CR history.\n\n"
                    "## Governing CR\n\n"
                    f"- **{CR}** (this tranche): admission of the "
                    f"Process Group into the GovernanceAndExistence "
                    "value stream.\n"
                )
        # Research README placeholder.
        research_readme = (
            REPO_ROOT / f"entities/v1-alpha/{g['id']}/research/README.md"
        )
        write_file(
            research_readme,
            (
                f"# Research register: `{g['id']}`\n\n"
                "This directory holds research artifacts specific to\n"
                "this Process Group. No L1-specific research has\n"
                "been moved into this subtree yet; the coordinate's\n"
                "research lives in the CR-BP-11 49-coordinate\n"
                "register (ratified by CR-BP-13; record under\n"
                "`dea:group-customer-lifecycle-management/research/`).\n"
                "Group-specific evidence will accumulate here as it\n"
                "is produced.\n\n"
                "## Provenance\n\n"
                f"Established by {CR} on {CRATED_AT}.\n\n"
                "## Governing CR\n\n"
                f"- **{CR}**: admission of the Process Group into\n"
                "  the GovernanceAndExistence value stream.\n"
            ),
            args.dry_run,
        )

    print("\n=== L2 Process entries ===")
    for p_obj in L2_PROCESSES:
        path = REPO_ROOT / (
            f"entities/v1-alpha/{p_obj['id']}/{p_obj['id']}.yaml"
        )
        write_file(path, render_l2_process(p_obj), args.dry_run)
        # Stub folders.
        for sub in ("research", "candidates", "retired"):
            stub = REPO_ROOT / f"entities/v1-alpha/{p_obj['id']}/{sub}/.gitkeep"
            if not args.dry_run:
                stub.parent.mkdir(parents=True, exist_ok=True)
                stub.touch()
        # Per-process README.
        readme = REPO_ROOT / f"entities/v1-alpha/{p_obj['id']}/README.md"
        write_file(
            readme,
            (
                f"# Canonical Business Process: `{p_obj['id']}`\n\n"
                f"This directory hosts the canonical L2 Business Process\n"
                f"entry for `{p_obj['id']}`. The process composes into\n"
                f"the `{p_obj['process_group']}` Process Group within\n"
                f"the {p_obj['process_context']} Process Context.\n\n"
                "## Governing CR\n\n"
                f"- **{CR}**: initial admission as part of the\n"
                f"  GovernanceAndExistence admission tranche.\n"
            ),
            args.dry_run,
        )
        # Research README placeholder.
        research_readme = (
            REPO_ROOT / f"entities/v1-alpha/{p_obj['id']}/research/README.md"
        )
        write_file(
            research_readme,
            (
                f"# Research register: `{p_obj['id']}`\n\n"
                "This directory holds research artifacts specific to\n"
                "this L2 Business Process. No L2-specific research\n"
                "has been moved into this subtree yet; the\n"
                "coordinate's research lives in the CR-BP-11\n"
                "49-coordinate register (ratified by CR-BP-13; record\n"
                "under `dea:group-customer-lifecycle-management/research/`).\n"
                "Process-specific evidence will accumulate here as it\n"
                "is produced.\n\n"
                "## Provenance\n\n"
                f"Established by {CR} on {CRATED_AT}.\n\n"
                "## Governing CR\n\n"
                f"- **{CR}**: initial admission as part of the\n"
                "  GovernanceAndExistence admission tranche.\n"
            ),
            args.dry_run,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())