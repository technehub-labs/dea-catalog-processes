# The Reconciliation and Conformance Programme

**Source:** CR-BP-13, CR-BP-14, CR-BP-15 (with CR-BP-15-IMP) and
CR-BP-16, distilled for readers and contributors. Where this document
and a Change Request disagree, the Change Request governs.

This document explains **how the catalog is governed over time**: how
research becomes canonical knowledge, how the existing population stays
coherent, and why canonical status means more than record existence.

## The closed governance loop

The catalog operates as a controlled loop, not as an accumulation of
individually acceptable records:

```text
RESEARCH
   │
   ▼
CANDIDATE
   │
   ▼
ASSESSMENT
   │
   ▼
RECONCILIATION        CR-BP-15: one-time correction of the baseline
   │
   ▼
CONFORMANCE           CR-BP-16: the permanent gate
   │
   ▼
GOVERNANCE
   │
   ▼
CANONICAL
   │
   ▼
CONTINUOUS CONFORMANCE
   │
   └──────────► EVOLUTION
```

The governing pattern is DEFINE → RECONCILE → VALIDATE → ADMIT →
EVOLVE, never RESEARCH → ADD → ADD → REPAIR.

## The CR lineage

| Stage | CR | Contribution |
|---|---|---|
| Kernel anchor | CR-BP-SPEC-BP-01 | The catalog is the Business Process specialization of the OpenDEA Process kernel |
| Context | CR-BP-02 | Process Context register: ECF Domain × Lifecycle Stage cells |
| Architecture | CR-BP-03 / 03A / 03C | Classification axes, identity contract, contribution-driven admission |
| Discovery | CR-BP-11 | Research across all 49 ECF coordinates |
| Group profile | CR-BP-12 | First-class catalog-owned Process Group record |
| Ratification | CR-BP-13 | The 49-coordinate register ratified (38 accepted, 11 backlog-deferred) |
| Admission | CR-BP-13a / 13b | CustomerAndDemand and GovernanceAndExistence tranches |
| Constitution | CR-BP-14 | The semantic contract: distinct Intent, Classification, Specialization, Context, Relationships |
| Reconciliation | CR-BP-15 (+ CR-BP-15-IMP) | Every existing record assessed and dispositioned against the contract |
| Conformance | CR-BP-16 | The permanent gate that keeps the baseline true |

## Canonicality is earned

A record is not canonical because it exists in the canonical directory.
It is canonical because it satisfies the applicable conformance gates
and carries an approved governance decision:

```text
Identity + Context + Boundary + Intent + Classification
+ Specialization + Evidence + Relationships + Governance
```

## Reconciliation: the one-time correction

CR-BP-15 reconciles the existing canonical population against the
semantic contract. Every record receives exactly one primary
disposition:

| Disposition | Meaning |
|---|---|
| RETAIN | Semantically valid; no change required |
| RENAME | Identity valid; name corrected to the naming contract |
| RECLASSIFY | Process valid; landscape classification corrected |
| RECONTEXTUALIZE | Process valid; context or audience relationship corrected |
| RESPECIALIZE | Parent, direction or basis of specialization corrected |
| MERGE | Two records are the same semantic unit of work |
| SPLIT | One record contains multiple coherent units of work |
| MOVE | Process valid; placed under a different scope, group or context |
| DEFER | Insufficient evidence or unresolved ambiguity; traceable, not canonical |
| RETIRE | Obsolete, duplicate, out of scope or superseded; historically traceable |

Reconciliation is not renaming: a name problem, an identity problem, a
classification problem, a specialization problem and a boundary problem
are distinct findings with distinct corrections. Correction is
preferred over identity churn; provenance is never lost. Merged records
preserve all predecessor identities; split records preserve the
originating identity; retired records remain historically resolvable.

## Conformance: the permanent control

CR-BP-16 evaluates every subsequent change across five dimensions:
structural, semantic, architectural, evidence and governance
conformance. Different change types carry different gate depth: a
documentation change passes structural checks; a merge, split,
retirement or new process passes the full gate.

Results are CONFORMANT, CONFORMANT-WITH-WARNINGS or NON-CONFORMANT.
Warnings are surfaced, never silently suppressed. Architectural
regressions (for example treating an ECF coordinate as a process, or
collapsing Intent into Classification) are detected as such.

Conformance levels distinguish unassessed (L0), structurally
conformant (L1), semantically conformant (L2), architecturally
conformant (L3) and canonically conformant (L4) records. Only L4
records are canonical.

## What this means for contributors

- Research and candidate contributions remain open at all times.
- Canonical admission passes the admission gate: evidence, identity,
  context, group fit, boundary, intent, classification, specialization,
  sibling analysis, MECE review, schema validation, provenance and
  governance approval.
- An empty ECF coordinate is legitimate. ECF coverage is not process
  completeness; no process is created solely because a coordinate has
  none.
- Sibling overlap findings trigger architectural review, not automatic
  merges.
- While the CR-BP-14 / CR-BP-15 reconciliation programme is in flight,
  no new canonical admission tranche is considered architecturally
  final (CR-BP-14 §24).

## Repository status model

Records and Change Requests carry explicit status: Candidate, Research,
Proposed, Canonical, Deferred, Retired, Superseded for records;
Proposed, Accepted, Implemented, Deferred, Superseded, Retired for CRs.
A research candidate never appears indistinguishably alongside a
canonical process. The CR register at
[`change-requests/README.md`](../../change-requests/README.md) is the
authoritative source for implementation status.

## See also

- [`docs/semantic-contract.md`](../semantic-contract.md): the semantic
  contract the programme defends
- [`change-requests/CR-BP-15-process-catalog-reconciliation.md`](../../change-requests/CR-BP-15-process-catalog-reconciliation.md)
- [`change-requests/CR-BP-16-process-catalog-conformance-gate.md`](../../change-requests/CR-BP-16-process-catalog-conformance-gate.md)
