# v1-alpha Catalog Entries

This directory will hold Process catalog entries once Phase 2 content population begins.

Each entry should be a YAML file following the schema in `../../schemas/entity.schema.json`. Example shape:

```yaml
id: dea:process-order-management
type: Process
name: Order Management
process_intent: operational
process_audience: customer-demand
description: End-to-end order capture, fulfilment, and settlement.
version: 1.0.0
stakeholders:
  - dea:stakeholder-end-customer
actors:
  - dea:actor-fulfilment-team
  - dea:actor-order-mgmt-system
```

See [DEA Metamodel process schema](https://github.com/technehub-labs/dea-metamodel/blob/main/schemas/entities/process.json) and [process-type-taxonomy.md](https://github.com/technehub-labs/dea-metamodel/blob/main/docs/process-type-taxonomy.md) for full canonical definitions and worked examples.
