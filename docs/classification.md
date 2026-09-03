# Process Classification

**CR-BP-03 §2.2, §7.**

This document captures the **4-axis classification** that
CR-BP-03 introduces. Each axis answers a different question;
conflating them is the historical source of much process-catalog
confusion.

## The four axes

| Axis | Field | Vocabulary | Question it answers |
|---|---|---|---|
| **Intent** | `process_intent` (existing; preserved) | operational / support / management | **What is the process doing?** Describes the nature of the work. |
| **Type** | `process_type` (new; CR-BP-03) | strategic / management / core / support / standardization | **Where does the process sit in the enterprise process landscape?** The 5-component classification (Mintzberg). |
| **Specialization** | `process_specialization` (new; CR-BP-03) | list of parent process ids | **What is this process a specialization of?** Inheritance / pattern-based refinement. |
| **Audience** | `process_audience` (existing; preserved; confirmed to be the ECF domain) | governance-existence / supply-resources / people-organization / customer-demand / product-offering / operations-delivery / finance-value | **Which ECF domain does the process serve?** |

## Axis 1: Intent (existing; preserved)

`process_intent` describes **what the process is doing** — the
nature of the work. The vocabulary is preserved from CR-BP-01:

- `operational` — the process performs direct work (delivers a
  service, processes a transaction, runs an operation).
- `support` — the process provides internal support (HR, IT,
  facilities) to enable other processes.
- `management` — the process plans, monitors, or controls other
  processes or resources.

## Axis 2: Type (new; CR-BP-03)

`process_type` describes **where the process sits in the
enterprise process landscape** — the 5-component classification
(Mintzberg). The vocabulary is at
[`classifications/process-types.yaml`](../../classifications/process-types.yaml):

| ID | Name | Primary Organizational Component | Primary Purpose |
|---|---|---|---|
| `strategic` | Strategic Process | Strategic Apex | Direction, vision, goals, strategic decisions |
| `management` | Management Process | Middle Line | Plan, monitor, control resource allocation to achieve strategic goals |
| `core` | Core Process | Operating Core | Direct value creation; products / services to external customers |
| `support` | Support Process | Support Staff | Internal-to-enterprise services that keep the organization running |
| `standardization` | Standardization Process | Technostructure | Cross-cutting overlay for compliance, consistency, continuous improvement, quality |

`process_type` defaults to `core` when the entry is a Business
Process. The classification is a **catalog-controlled
vocabulary**, not a new ontology (CR-BP-03 §3). The semantic
entity remains `dea:BusinessProcess` regardless of `process_type`.

## Axis 3: Specialization (new; CR-BP-03)

`process_specialization` describes **what this process is a
specialization of** — the inheritance / pattern-based refinement
hierarchy. The vocabulary is at
[`classifications/process-specializations.yaml`](../../classifications/process-specializations.yaml).

Example:

```yaml
# A specialization refines a parent process for a specific pattern.
- id: dea:bp-manage-customer
  process_type: management
  # ...

- id: dea:bp-manage-enterprise-customer
  process_type: management
  process_specialization:
    - dea:bp-manage-customer
  specialization_pattern: by-customer-segment
  # ...
```

`process_specialization` is a list of parent process ids (multi-
inheritance is permitted). `specialization_pattern` is an optional
free-text label (e.g. "by-customer-segment", "by-region",
"by-product-line", "by-tier", "by-compliance-regime").

This is **not** a new metamodel relationship; it is a
**catalog-level annotation** that records the specialization
hierarchy for navigation and governance. The authoritative
`dea:specializes` relationship in the metamodel continues to
govern the kernel + specialization discipline (CR-MM-PROC-01).

## Axis 4: Audience (existing; preserved)

`process_audience` describes **which ECF domain the process
serves**. Confirmed to be the ECF domain per the user's
clarification. The vocabulary is the 7-value ECF domain enum:

- `governance-existence`
- `supply-resources`
- `people-organization`
- `customer-demand`
- `product-offering`
- `operations-delivery`
- `finance-value`

`process_audience` is a **single-axis audience classification**.
It is **not** a full ECF coordinate (Domain × Lifecycle Stage) —
that lives in Process Context (CR-BP-02).

## How the four axes interact

A single Business Process can have any combination of the four
axes. Consider:

- A `core` process that is also `operational` in intent and
  serves the `customer-demand` audience and is a specialization
  of `Manage Customer` is normal and expected.
- A `support` process that is `management` in intent (e.g.
  "Manage Internal Tooling") is a coherent combination.

Without the four distinct axes, these combinations would be
ambiguous. With them, each axis captures a different concern.

## Classification ≠ ontology

CR-BP-03 explicitly forbids the addition of
`dea:entity-strategic-process`,
`dea:entity-management-process`, etc. to the root model. The
five-value `process_type` is a **catalog-controlled vocabulary**;
the semantic entity remains `dea:BusinessProcess`.

## See also

- [`docs/architecture.md`](architecture.md) — the structural architecture
- [`docs/identity.md`](identity.md) — how a process is identified
- [`docs/relandscape.md`](relandscape.md) — how reclassification is surfaced
- [`classifications/process-types.yaml`](../../classifications/process-types.yaml)
- [`classifications/process-specializations.yaml`](../../classifications/process-specializations.yaml)
- [`change-requests/CR-BP-03-business-process-architecture.md`](../../change-requests/CR-BP-03-business-process-architecture.md) §2.2, §7
