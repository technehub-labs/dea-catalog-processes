# Process Architecture

**CR-BP-03 §1, §4, §5, §6, §7, §8, §10.**

This document captures the Business Process architecture
established by CR-BP-03. The catalog's primary subject is the
**L2 Business Process** (`dea:BusinessProcess`); the L0/L1 levels
are conceptual and live in this document + `README.md` (they are
**not** separate top-level directories).

## Decomposition

```text
ECF Domain × Lifecycle Stage
         │
         ▼
   Process Context          (CR-BP-02; contexts/v1/)
         │
         ▼
   L0 Process Scope         (conceptual; documented here)
         │
         ▼
   L1 Process Group         (conceptual; documented here)
         │
         ▼
   L2 Business Process      (entities/v1/; dea:BusinessProcess)
         │
         ▼
   Activity                 (CR-BP-04; future)
         │
         ▼
   Workflow / Task          (CR-BP-05; future; authoritative
                             metamodel)
```

## Process Context

Established by CR-BP-02. Represents `ECF Domain × Lifecycle Stage`
and provides the semantic boundary in which processes are
discovered, organized, and validated. It is **not** itself a
Business Process. The catalog carries Process Context entries at
`contexts/v1/` (currently `v1-alpha/` until the matrix is
populated per CR-BP-02 §22).

## L0 Process Scope

The highest process-architecture scope beneath Process Context.
Establishes the bounded area of process coverage. It is a
**catalog topology construct** — not currently a new normative
metamodel entity. L0 captures "the area of work" within a context.

Example (illustrative): within the Process Context
`dea:pc-cd-op` (CustomerAndDemand × Operate), an L0 Process Scope
might be "Customer Onboarding" (covering the area of bringing new
customers into the operating relationship).

## L1 Process Group

A coherent grouping of Business Processes within a Process Scope.
A catalog topology construct. L1 captures "a coherent set of
processes that work together to deliver a coherent chunk of
value."

**Process Group is NOT equivalent to Business Function.** A
Business Function is an OpenDEA semantic concept concerned with
organizational grouping of capabilities and ownership. Process
Group is concerned with organizing processes. They answer
different questions and live at different modeling concerns.

## L2 Business Process

The first canonical semantic entity: `dea:BusinessProcess`. All
L2 process definitions must conform to the authoritative OpenDEA
metamodel. The L2 entry lives in `entities/v1/` (currently
`v1-alpha/`).

## Structural composition

Process decomposition uses the authoritative OpenDEA relationship
`dea:composes`. Structural composition means:

- part-of structure;
- containment within the process architecture;
- hierarchical decomposition;
- **no implied sequence**;
- **no implied execution**;
- **no implied organizational ownership**.

```text
L1 Process Group
       │
       ▼
L2 Business Process
       │
       └── dea:composes ──► L2 Business Process
```

In the schema, structural composition is captured in
`relationships.composes` (canonical). The legacy
`parent_process` / `child_processes` fields are preserved as
migration aliases and are not authoritative.

## Capability realization

Decomposition and realization are orthogonal. A Business Process
realizes one or more Business Capabilities via `dea:realizes`,
which lives in the schema's `relationships.realizes` (canonical).
The legacy `capabilities_delivered` field is preserved as a
migration alias.

```text
              ┌───────────────┐
              │ Business      │
              │ Capability    │
              └───────▲───────┘
                      │
                   realizes
                      │
              ┌───────┴───────┐
              │ Business      │
              │ Process       │
              └───────┬───────┘
                      │
                   composes
                      │
                      ▼
              Business Process
```

## Structural vs execution

```text
Structural architecture    Behaviour / execution
─────────────────────      ───────────────────
Context                   Business Process
   ↓                           ↓
Scope                       Activity
   ↓                           ↓
Group                       Workflow
   ↓                           ↓
Business Process             Task
```

These are different modeling dimensions. Workflow and Task
already exist in the OpenDEA metamodel and should not be
reinvented by the process catalog.

- **CR-BP-03** → structural process architecture (this document)
- **CR-BP-04** → Activity Model
- **CR-BP-05** → Execution Boundary

## See also

- [`README.md`](../../README.md) — the architectural statement
- [`docs/classification.md`](classification.md) — the 4-axis classification
- [`docs/identity.md`](identity.md) — the process-identity contract
- [`docs/relandscape.md`](relandscape.md) — the contribution-driven re-landscape mechanism
- [`change-requests/CR-BP-03-business-process-architecture.md`](../../change-requests/CR-BP-03-business-process-architecture.md)
