# Worked examples

This directory holds **worked examples** that demonstrate
the canonical pattern for catalog entries. Each example
walks the full CR-BP-03 / CR-BP-03A / CR-BP-02 machinery
end-to-end.

## Available examples

| Example | Purpose |
|---|---|
| [`manage-customer-relationship.md`](manage-customer-relationship.md) | The canonical Business Process entry (CR-BP-03C). Exercises every part of the machinery: 4-axis classification, identity contract, relationships, L0/L1/L2 hierarchy, Process Context reference, ECF Conformance Gate. **Future contributors should treat this as the reference example.** |

## Why this directory exists

The `docs/` directory holds **architectural narrative**
(`architecture.md`, `classification.md`, `identity.md`,
`relandscape.md`, `conformance.md`). The narrative explains
the **why**; the examples demonstrate the **how**.

A reader who wants to contribute a new Business Process
entry should:

1. Read [`docs/architecture.md`](../architecture.md) to
   understand the structural decomposition.
2. Read [`docs/classification.md`](../classification.md) to
   understand the 4-axis classification.
3. Read [`docs/identity.md`](../identity.md) to understand
   the process-identity contract.
4. **Pattern-match against `manage-customer-relationship.md`**
   to see a real entry that exercises every part of the
   machinery.
5. Copy the
   [`PROCESS-CONTRIBUTION-TEMPLATE.yaml`](../../contributions/processes/PROCESS-CONTRIBUTION-TEMPLATE.yaml),
   fill it in, and submit as a PR.

## See also

- [`README.md`](../../README.md) — the architectural statement
- [`docs/`](../) — architectural narrative
- [`contributions/processes/`](../../contributions/processes/) — the contribution template + record
