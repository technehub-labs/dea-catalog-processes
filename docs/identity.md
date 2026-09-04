# Process Identity

**CR-BP-03 §8; CR-BP-04 §4.**

This document captures the **process-identity contract**: a
process is tested by name + description + trigger + outcome +
evidence, not by name alone.

## Canonical ID families (CR-BP-04 §4)

Every identifier in this catalog belongs to one of five families. The prefix, separator, and purpose of each family are fixed by CR-BP-04.

| Family | Prefix | Separator | Purpose | Lives in |
|---|---|---|---|---|
| Business Process | `dea:process` | `-` | Canonical L2 Business Process entries (and specializations) | `entities/v1-alpha/` |
| Process Context | `dea:pc` | `-` | Canonical Process Context entries (Domain x Lifecycle Stage cells) | `contexts/v1-alpha/` |
| Process Group | `dea:group` | `-` | Catalog-owned L1 labels and (BP-12) first-class records | `metadata.group` (now); `entities/v1-alpha/` (after BP-12) |
| Process Scope | `dea:scope` | `-` | Catalog-owned L0 labels (metadata only; never a first-class entity) | `metadata.scope` |
| Legacy Business Process | `dea:bp` | `:` (colon) | Legacy-migration reference only; appears in `legacy_ids` arrays and in validator self-test fixtures | `legacy_ids[]` only |

The colon-vs-dash distinction is intentional. `dea:bp:*` is a deliberately alien-looking identifier that signals "this is a foreign legacy reference" to any reader; contributors cannot confuse it with `dea:process-*`. The dash-separated `dea:bp-*` form is reserved for validator self-test fixtures and is not a valid production identifier under any schema.

A new contribution must use `dea:process-*` for canonical Business Process ids. The `dea:bp-*` (dash) form must not appear in any catalog content file.

## Why identity?

A process may be:

- **Poorly named but correctly described.** E.g. a process named
  "Strategic Customer Onboarding" might actually be a
  `core` process for onboarding customers. The name is misleading
  but the description is clear.
- **Correctly named but mis-classified.** E.g. a process named
  "Manage Customer" might be declared as `process_type: core` but
  the description and outcome_statement talk about
  direction-setting — in which case the correct classification
  is `process_type: management` or even `strategic`.
- **Poorly described.** E.g. a process with a generic name and a
  vague description cannot be reliably classified.

The identity contract addresses all three: a process must
declare its name, verb + object (the analytical form of the
name), outcome_statement, and **evidence links** so the
classification can be verified against operational artifacts,
governance docs, SME interviews, and standards.

## Identity sub-block shape

```yaml
identity:
  verb: Manage           # action verb (imperative; singular)
  object: Customer       # the noun being acted on
  scope: <optional>      # optional scope qualifier
  outcome_statement: |
    Customer relationships are maintained, escalated where
    required, and renewed or terminated per policy.
  evidence_links:
    - type: documentation
      ref: docs/processes/manage-customer.md
    - type: governance
      ref: governance/process-manage-customer.md
```

The verb + object together approximate the process name; the
outcome_statement is the description-of-record. Evidence links
provide the basis for review when the name or description is
challenged.

## Validation rules

The validator `scripts/check_process_identity.py` enforces
BP-ARC-ID-001..BP-ARC-ID-005:

| Rule | Description |
|---|---|
| BP-ARC-ID-001 | Name matches identity: the process name should be `<verb> <object>` (with optional scope). |
| BP-ARC-ID-002 | Trigger required: the entry must declare `trigger` (a non-empty string). |
| BP-ARC-ID-003 | Outcome required: the entry must declare `outcome` (a non-empty string) consistent with `identity.outcome_statement`. |
| BP-ARC-ID-004 | Type / description cross-check: `process_type` is cross-checked against `identity.outcome_statement` for consistency. E.g. a `core` process whose outcome_statement talks about direction-setting is flagged. |
| BP-ARC-ID-005 | Evidence required: `identity.evidence_links` is required (minItems: 1) when the identity sub-block is present. |

The validator is **non-blocking on auto-classification**: it
emits a re-landscape suggestion with a confidence score, but the
catalog does not auto-rewrite. The re-landscape mechanism is
contribution-driven (see [`docs/relandscape.md`](relandscape.md)).

## When the identity contract is satisfied

A process has a complete identity when:

- the name matches the verb + object (and optional scope);
- the trigger is non-empty and concrete;
- the outcome is non-empty and aligns with the
  outcome_statement;
- the process_type is consistent with the outcome_statement;
- the evidence_links are present and resolve to artifacts
  (documentation, governance, interview, artifact, standard,
  regulation).

A process with a complete identity is a **coherent process**:
it can be classified, governed, re-landscaped, and audited.

## When the identity contract is violated

A process that violates one or more of the rules is
**flagged for review** by the contribution report
(`docs/relandscape.md`). The report emits a reclassification
suggestion with a confidence score. The catalog maintainer
reviews the suggestion and either:

- accepts the contribution as-is (and lands the entry);
- requests a re-landscape (the contributor updates the
  proposed_entry and re-runs CI);
- rejects the contribution.

The catalog does **not** auto-rewrite entries; this is a
human-in-the-loop process by design.

## See also

- [`docs/architecture.md`](architecture.md) — the structural architecture
- [`docs/classification.md`](classification.md) — the 4-axis classification
- [`docs/relandscape.md`](relandscape.md) — how the identity contract is enforced via contribution-driven review
- [`schemas/identity.schema.json`](../identity.schema.json) — the schema
- [`scripts/check_process_identity.py`](../scripts/check_process_identity.py) — the validator
- [`change-requests/CR-BP-03-business-process-architecture.md`](../../change-requests/CR-BP-03-business-process-architecture.md) §8
