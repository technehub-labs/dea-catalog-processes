# Processes

> Business or operational processes that deliver value. Classified by intent (operational/support/management) and audience (ECF domain).

**Layer:** L1 · **Entity:** `BP` · **Metamodel:** [v3.0.0-alpha](https://github.com/technehub-labs/dea-metamodel)

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=Process)

## Status

This is a **scaffold** repository — created during the Process taxonomy rollout. Content population is planned for a subsequent phase.

## Entity Definition

| Field | Value |
|-------|-------|
| Entity ID | `dea:entity-business-process` |
| Class Alias | `BP` |
| Layer | L1 |
| Metamodel Version | v3.0.0-alpha |

## Classification

Processes are classified by **two orthogonal axes**:

### Axis 1 — `process_intent` (what role?)

| Value | Definition |
|---|---|
| `operational` | Executes recurring, day-to-day work |
| `support` | Enables other processes |
| `management` | Decides, plans, allocates, or governs |

### Axis 2 — `process_audience` (whose work most advanced?)

The seven Enterprise Concept Framework (ECF) domains, axiom-derived:
`governance-existence | supply-resources | people-organization | customer-demand | product-offering | operations-delivery | finance-value`

Plus two multi-valued typed references:

| Field | Reference | Catalog |
|---|---|---|
| `stakeholders[]` | External/affected parties | [`dea-catalog-stakeholders`](https://github.com/technehub-labs/dea-catalog-stakeholders) |
| `actors[]` | Performers (humans, teams, systems, AI agents) | [`dea-catalog-actors`](https://github.com/technehub-labs/dea-catalog-actors) |

See [`technehub-labs/dea-metamodel/docs/process-type-taxonomy.md`](https://github.com/technehub-labs/dea-metamodel/blob/main/docs/process-type-taxonomy.md) for full rationale, tie-breaker rules, and worked examples.

## Catalog Structure

```
dea-catalog-processes/
├── metamodel-pointer.yaml   ← entity mapping (do not edit manually)
├── entities/
│   └── v1-alpha/          ← catalog entries go here
│       └── README.md
├── schemas/                ← JSON Schema for this entity type
│   └── entity.schema.json
└── .github/
    └── workflows/
        └── ci.yml         ← validates entries against schema
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) and the [DEA Metamodel](https://github.com/technehub-labs/dea-metamodel) for guidance.
