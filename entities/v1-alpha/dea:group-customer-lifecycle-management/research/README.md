# Research register: dea:group-customer-lifecycle-management

This directory holds research artifacts that produced and govern this
Process Group's first-class canonical record.

## Provenance

| File | Origin | Moved by | Date |
|---|---|---|---|
| `l1-register.yaml` | `docs/research/l1-register.yaml` (CR-BP-11) | CR-CATALOG-STRUCT-02 migration | 2026-09-05 |
| `l1-candidate-universe.yaml` | `docs/research/l1-candidate-universe.yaml` (CR-BP-11) | CR-CATALOG-STRUCT-02 migration | 2026-09-05 |
| `L1-REGISTER-v0.1.md` | `docs/research/L1-REGISTER-v0.1.md` (CR-BP-11) | CR-CATALOG-STRUCT-02 migration | 2026-09-05 |

## Governing CR

- **CR-BP-11** (merged): the 49-coordinate L1 disposition register that
  produced this Process Group as one of 38 accepted coordinate outcomes
  (38 accepted, 11 deferred; 102 candidates surveyed).
- **CR-BP-12** (merged): the Process Group profile/schema/validator
  promotion that first established this entity as a catalog-owned
  first-class record (rather than a metadata label on
  `dea:process-manage-customer-relationship`).
- **CR-BP-13** (proposed, this PR): research ratification. Promotes the
  38 accepted dispositions to `ratified-accepted` and the 11 deferred
  dispositions to `backlog-deferred` with rationale (Activate/Retire
  are transition stages, not stable Process Group operating scopes).
  Adds a top-level `ratification: { version: 1, cr: CR-BP-13,
  ratified_at: '2026-09-05' }` block to `l1-register.yaml` and
  `l1-candidate-universe.yaml`. Idempotent (re-running the ratification
  tool is a no-op).

## Ratification evidence

The research register was ratified on 2026-09-05. Disposition counts:

| Disposition | Coordinates | L1 candidates |
|---|---:|---:|
| `ratified-accepted` | 38 | 86 |
| `backlog-deferred` | 11 | 16 |
| **Total** | **49** | **102** |

The 11 backlog-deferred coordinates all sit on the Activate or Retire
lifecycle stages. They are transition stages, not stable Process Group
operating scopes; CR-BP-13 §4 records the rationale. The backlog can be
revisited if a discrete Activate/Retire process identity is later
identified (separate CR).

## Why this entity owns this research

The research register is about **L1 Process Groups**: the 49-coordinate
Domain x Lifecycle matrix and the disposition of each coordinate. L1
entities own L1 evidence. The L2 process that this L1 group composes
(`dea:process-manage-customer-relationship`) has its own research
subtree (currently empty; will be populated when per-process evidence
accumulates).
