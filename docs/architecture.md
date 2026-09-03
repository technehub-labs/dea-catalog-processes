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

In the schema, structural composition is captured in the
`relationships` array (canonical; CR-BP-03 §6; CR-BP-03A §3.1).
Each relationship entry conforms to the metamodel's
`relationship-instance.json` shape with full provenance.

## Capability realization

Capability realization is captured in the `relationships` array
as relationship instances of type `realizes`. Each entry
conforms to the metamodel's `relationship-instance.json` shape.

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

## The `relationships` shape (CR-BP-03A §3.1)

The `relationships` field is an **array of relationship
instances**, NOT a structured object. Each entry is a typed
relationship with full CR-002 provenance, CR-6 lifecycle, and
effective_from/to temporal validity:

```yaml
relationships:
  - source_id: dea:bp:manage-customer
    target_id: dea:bp:manage-enterprise-customer
    relationship_type: composes
    status: active
    rationale: "L2 Business Process structurally composes another L2."
    provenance:
      type: manual
      asserted_by: <contributor>
      asserted_at: <YYYY-MM-DD>
  - source_id: dea:bp:manage-customer
    target_id: dea:capability:manage-customer
    relationship_type: realizes
    status: active
    rationale: "Business Process realizes Business Capability."
    provenance:
      type: manual
      asserted_by: <contributor>
      asserted_at: <YYYY-MM-DD>
```

The catalog primarily uses `composes` (structural composition)
and `realizes` (capability realization). Other types
(`specializes`, `aggregates`, `depends-on`, etc.) are admitted
when the contributor can defend the choice.

The metamodel's `relationship-instance.json` is authoritative
on the relationship shape. The catalog profiles the source_id
and target_id to the catalog's process id namespace
(`dea:bp:...`).

## Legacy field migration (CR-BP-03A §3.2, §3.3)

Three legacy fields are addressed by CR-BP-03A:

1. **`parent_process`** — REMOVED. This was a catalog invention
   from CR-BP-01 (the wrong-premise implementation, since
   reverted). The metamodel's `process.json` does not declare
   it. The migration validator
   (`scripts/check_legacy_migration.py`; BP-MIG-001) surfaces
   any entry that declares it and emits a migration
   recommendation.
2. **`child_processes`** — REMOVED. Same as `parent_process`.
   The migration validator (BP-MIG-002) surfaces any entry that
   declares it.
3. **`capabilities_delivered`** — Soft-deprecated. The metamodel
   still declares this as a simple array of strings (a
   backward-compat shim). CR-BP-03A keeps the field in the
   schema but marks it as soft-deprecated. The canonical form
   is `relationships[relationship_type=realizes]` with full
   provenance. The migration validator (BP-MIG-003) surfaces
   any entry that declares it and emits a migration
   recommendation.

The migration is **contribution-driven**: the contributor
updates the proposed_entry to use the canonical form, re-runs
CI, and the reviewer approves. The catalog does not
auto-rewrite.

## See also

- [`README.md`](../../README.md) — the architectural statement
- [`docs/classification.md`](classification.md) — the 4-axis classification
- [`docs/identity.md`](identity.md) — the process-identity contract
- [`docs/relandscape.md`](relandscape.md) — the contribution-driven re-landscape mechanism
- [`change-requests/CR-BP-03-business-process-architecture.md`](../../change-requests/CR-BP-03-business-process-architecture.md)
- [`change-requests/CR-BP-03A-legacy-migration.md`](../../change-requests/CR-BP-03A-legacy-migration.md)
