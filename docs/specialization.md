# Process Specialization

**CR-BP-03 §3; CR-BP-14 §12; CR-BP-12.**

Specialization expresses semantic refinement of one Business Process by
another. A specialized process inherits the semantic pattern of its
parent while introducing a materially distinguishing scope, subject,
regime or context.

## Definition

A Process Specialization expresses semantic refinement of another
process. It answers: what more general process does this process
refine?

```text
Manage Customer Relationship                # general
        │
        ├── Manage Enterprise Customer Relationship        # specialization
        ├── Manage Consumer Customer Relationship         # specialization
        └── Manage Partner Customer Relationship          # specialization
```

## What specialization is

Specialization is **semantic refinement**. The specialized process
introduces a materially distinguishing property along an approved
basis. Approved bases (CR-BP-14 §12.2) include:

- `by-customer-segment`
- `by-geography`
- `by-product`
- `by-service`
- `by-channel`
- `by-regulatory-regime`
- `by-operating-model`
- `by-lifecycle-condition`
- `by-organizational-context`

A free-text label is also admitted when accompanied by a
`specialization_basis` field.

## What specialization is not

Specialization is **not** decomposition. A specialized process is a
*kind of* its parent, not a *part of* it. Structural decomposition
(parts within a process architecture) uses the `composes`
relationship and belongs to a different concern.

Specialization is **not** organizational hierarchy, capability
refinement or context. The catalog rejects specialization
relationships that merely rename the parent without introducing a
meaningful semantic distinction (BP-SEM-006).

## Canonical form

The canonical specialization annotation is:

```yaml
process_specialization:
  - dea:process-manage-customer-relationship
specialization_pattern: by-customer-segment   # approved basis or free-text + basis
```

Multi-inheritance is permitted; the array lists every parent. Every
specialization reference MUST resolve to a canonical Business Process
(BP-SEM-005). Where evidence establishes legitimate non-canonical
parent references (planned parents), the validator emits a warning
rather than an error.

## Identity independence

Changes to specialization SHALL NOT automatically create a new process
identity (BP-SEM-009). A specialization that adds no new semantic
property is rejected as a redundant alias; a specialization that
introduces a new coherent unit of work may require a new identity.

## See also

- [`docs/semantic-contract.md`](semantic-contract.md): Specialization
  tells us what more general process it refines (CR-BP-14 §29)
- [`docs/architecture.md`](architecture.md): structural composition vs
  specialization
- [`classifications/process-specializations.yaml`](../classifications/process-specializations.yaml):
  the controlled vocabulary of specialization patterns
- [`scripts/check_process_specialization.py`](../scripts/check_process_specialization.py):
  BP-SPEC-01-001..007 (the kernel + specialization discipline)
- [`scripts/check_process_semantics.py`](../scripts/check_process_semantics.py):
  BP-SEM-005, BP-SEM-006, BP-SEM-009 (the semantic validator)
- [`change-requests/CR-BP-03-business-process-architecture.md`](../change-requests/CR-BP-03-business-process-architecture.md) §3
- [`change-requests/CR-BP-14-process-semantic-reconciliation.md`](../change-requests/CR-BP-14-process-semantic-reconciliation.md) §12