# Worked example: `dea:process-manage-customer-relationship`

This document walks the **canonical pattern** for a Business
Process entry in the catalog. Future contributors should
treat this as the **reference example**.

## The entry at a glance

| Field | Value |
|---|---|
| **Id** | `dea:process-manage-customer-relationship` |
| **Name** | Manage Customer Relationship |
| **Process context** | `dea:pc-cd-op` (CustomerAndDemand × Operate) |
| **Process intent** | `management` |
| **Process type** | `management` (Mintzberg Middle Line) |
| **Process specialization** | `[]` (root; no parent) |
| **Process audience** | `customer-demand` |
| **Realizes** | `dea:entity-capability:manage-customer-relationship` |
| **ECF conformance** | `conformant-with-extension`; inherits-catalog |
| **Evidence** | [APQC PCF](https://www.apqc.org/resource-library/resource-collections/56391) |

## The 4-axis classification

A Business Process entry must declare values for all 4
classification axes (CR-BP-03 §2.1; CR-BP-03A §3.2):

| Axis | This entry | Why |
|---|---|---|
| **`process_intent`** (existing; CR-BP-SPEC-BP-01) | `management` | Coordinates, monitors, plans, controls. Not operational (no direct value-delivery work) and not support (not an internal enabler). |
| **`process_type`** (NEW in CR-BP-03) | `management` | Mintzberg Middle Line — plan, monitor, and control allocation of resources. See [`classifications/process-types.yaml`](../../classifications/process-types.yaml). |
| **`process_specialization`** (NEW in CR-BP-03) | `[]` | Root of the customer-relationship specialization. Future BPs (e.g. `dea:bp:manage-enterprise-customer`) will declare THIS id in their `process_specialization` list. |
| **`process_audience`** (existing; CR-ECF-CG-004 §10) | `customer-demand` | The ECF Domain `CustomerAndDemand` is the principal audience. Note: `process_audience` is a kebab-case audience axis, NOT a canonical ECF coordinate (CR-ECF-CG-004 §10). |

## The Process Identity contract

A Business Process entry must declare an `identity` sub-block
(CR-BP-03 §5.4) AND `trigger` / `outcome` fields
(BP-ARC-ID-002..003):

| Field | This entry |
|---|---|
| **`identity.verb`** | `manage` |
| **`identity.object`** | `customer relationship` |
| **`identity.scope`** | `(all customer segments)` |
| **`identity.outcome_statement`** | An active customer relationship is sustained across its lifecycle... |
| **`identity.evidence_links`** | `[APQC PCF](...)` |
| **`trigger`** | A customer enters the active relationship lifecycle... |
| **`outcome`** | An active customer relationship is sustained across its lifecycle... |

The name **must** match `identity.verb + identity.object +
identity.scope` (case-insensitive; BP-ARC-ID-001). The
outcome_statement's keyword density **must** be consistent
with `process_type` (BP-ARC-ID-004).

## The canonical relationships

The `relationships` field is an **array of relationship
instances** conforming to the metamodel's
`relationship-instance.json` shape (CR-BP-03A §3.1). Each
entry has `source_id`, `target_id`, `relationship_type`,
plus optional `direction`, `status`, `effective_from/to`,
`asserted_by`, `rationale`, `evidence`, and `provenance`.

This entry has **one** relationship:

```yaml
relationships:
  - source_id: dea:process-manage-customer-relationship
    target_id: dea:entity-capability:manage-customer-relationship
    relationship_type: realizes
    status: active
    direction: outgoing
    rationale: |
      The Business Process realizes the Business Capability
      `Manage Customer Relationship`.
    asserted_by: DEa team
    asserted_at: '2026-09-03'
    provenance:
      type: manual
      asserted_by: DEa team
      asserted_at: '2026-09-03'
      evidence: https://www.apqc.org/resource-library/resource-collections/56391
```

The catalog primarily uses `composes` (structural composition)
and `realizes` (capability realization).

## The L0/L1/L2 conceptual hierarchy

The L0/L1/L2 hierarchy is a **conceptual model** documented in
[`docs/architecture.md`](../architecture.md). It is **NOT**
separate top-level directories and **NOT** separate catalog
entities.

For this entry:

| Level | Construct | Sample |
|---|---|---|
| **Context** | `dea:pc-cd-op` (Cell Charter) | `CustomerAndDemand × Operate` |
| **Scope (L0)** | The bounded enterprise context | Customer-facing operations |
| **Group (L1)** | A loose grouping of related BPs | Customer Lifecycle Management |
| **Business Process (L2)** | `dea:process-manage-customer-relationship` | Manage Customer Relationship (this entry) |

The Scope and Group are recorded in the entry's `metadata`
field as documentation; they are **NOT** promoted to separate
catalog entities (per CR-BP-03 §3: classification ≠ ontology).

## The Process Context reference

The entry's `process_context` field references the Cell
Charter at `contexts/v1-alpha/dea_pc-cd-op.yaml`. The Cell
Charter's `processes` array references this entry back,
forming a bidirectional reference (PC-008).

## The ECF Conformance Gate

The entry declares an `ecfConformance` block
(CR-ECF-CG-001..004; enforced by
`scripts/check_ecf_conformance.py`):

```yaml
ecfConformance:
  framework: EnterpriseConceptFramework
  contractVersion: '1.0.0'
  profile: dea:ecf@1.0.0
  status: conformant-with-extension
  affiliation: inherits-catalog
  canonicalReferences:
    - kind: coordinate
      domain: CustomerAndDemand
      stage: Operate
      identifier: ecf:customerAndDemand.operate
  extensions:
    - name: process_intent
      doesNotRedefine: true
      rationaleRef: change-requests/CR-BP-SPEC-BP-01.md
    # ... process_type, process_specialization, process_audience
```

The entry **inherits the catalog's conformance posture**
(`affiliation: inherits-catalog`); the canonical references
resolve to the ECF Domain and Stage of the Process Context.
Extensions declare `doesNotRedefine: true` so that the
catalog's classification axes are NOT claimed as new ECF
vocabulary.

## Validators exercised (all PASS)

| Validator | Result |
|---|---|
| `check_process_identity.py` (BP-ARC-ID-001..005) | PASS |
| `check_process_specialization.py` (BP-SPEC-01-001..007) | PASS |
| `check_process_context.py` (PC-001..PC-008) | PASS |
| `check_legacy_migration.py` (BP-MIG-001..005) | PASS |
| `check_ecf_conformance.py` | PASS |
| `validate_consumer.py` against `dea-architecture-framework@v0.6.0` | PASS |
| Process Contribution Report workflow | Generated `dea_bp_manage-customer-relationship.report.md` with status=PASS |

## Files for this entry

| Path | Purpose |
|---|---|
| [`entities/v1-alpha/dea_bp_manage-customer-relationship.yaml`](../../entities/v1-alpha/dea_bp_manage-customer-relationship.yaml) | The canonical BP entry |
| [`contexts/v1-alpha/dea_pc-cd-op.yaml`](../../contexts/v1-alpha/dea_pc-cd-op.yaml) | The Cell Charter (Process Context) |
| [`contributions/processes/dea_bp_manage-customer-relationship.yaml`](../../contributions/processes/dea_bp_manage-customer-relationship.yaml) | The contribution record |
| [`change-requests/CR-BP-03C-sample-process-contribution.md`](../../change-requests/CR-BP-03C-sample-process-contribution.md) | The CR that landed the entry |

## See also

- [`docs/architecture.md`](../architecture.md) — the architectural narrative
- [`docs/classification.md`](../classification.md) — the 4-axis classification
- [`docs/identity.md`](../identity.md) — the process-identity contract
- [`docs/relandscape.md`](../relandscape.md) — the contribution-driven re-landscape
- [`README.md`](../../README.md) — the architectural statement
