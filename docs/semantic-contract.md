# The Semantic Contract of the Business Process Catalog

**Source:** CR-BP-14 (Process Semantic Reconciliation), distilled for
readers and contributors. Where this document and a Change Request
disagree, the Change Request governs.

This document answers one question: **what does a Business Process
record in this catalog mean?** It is the orientation layer for the
catalog; the normative text lives in
[`change-requests/CR-BP-14-process-semantic-reconciliation.md`](../change-requests/CR-BP-14-process-semantic-reconciliation.md).

## One kernel, many specializations

The OpenDEA Process discipline is a kernel + specializations model. The
OpenDEA Process kernel (`dea:Process`) is defined in the metamodel;
`dea:BusinessProcess` is its first Core specialization. This catalog is
the canonical home of that specialization. It does not redefine the
kernel, and it does not create new ontology entities: every
classification vocabulary here is catalog-controlled.

> The Business Process Catalog is a specialization catalog of the
> OpenDEA Process kernel.

## The architecture in one picture

```text
Enterprise Concept Framework (ECF)
        │  Domain × Lifecycle Stage
        ▼
Process Context                  where responsibility is examined
        ▼
L0  Process Scope                what responsibility is organized
        ▼
L1  Process Group                how related responsibilities are grouped
        ▼
L2  Business Process             what work is performed
        │
        ├─ Process Intent        why the work exists (purpose)
        ├─ Process Classification how the work is positioned (landscape)
        ▼
Process Specialization           what more general process it refines
        ▼
Process Relationships            what it serves, realizes, depends on
```

Decomposition (L0-L4) and characterization (Intent, Classification,
Specialization, Context, Relationships) are separate concerns. No one
of these concepts substitutes for another.

## The dimensions of a Business Process

Every canonical Business Process is characterized along six
independent dimensions:

| Dimension | Question it answers |
|---|---|
| Identity | What coherent process is this? |
| Intent | What kind of purposeful work does it perform? |
| Classification | Where is it positioned in the process landscape? |
| Specialization | What general process does it refine? |
| Context | Within what enterprise context is it defined or used? |
| Relationships | What enterprise concepts does it interact with or serve? |

### Identity

A Business Process is a bounded unit of work that transforms defined
inputs into outputs, contributes distinctly to an enterprise objective,
stands as a coherent unit of work, and carries identifiable
responsibility for its means of execution. Identity is established by
the identity contract: Verb + Object + optional Scope + Trigger +
Outcome + Evidence (see [`docs/identity.md`](identity.md)).

Identity is independent of classification, intent, context, audience
and organizational ownership. Classification and context may change
without creating a new process identity; only a material change to the
unit of work itself does that.

### Intent: why the work exists

Process Intent describes the purposeful nature of the work. The
controlled vocabulary
([`classifications/process-intents.yaml`](../classifications/process-intents.yaml))
is purpose-oriented:

| Intent | The work... |
|---|---|
| `govern` | establishes, directs, assures or enforces direction, policy, authority or compliance |
| `manage` | plans, coordinates, monitors, controls or optimizes an enterprise responsibility |
| `operate` | performs recurring work that produces or maintains an operational result |
| `deliver` | produces, provisions or transfers an intended product, service, experience or outcome |
| `support` | enables other enterprise responsibilities through internal services or resources |
| `develop` | creates, improves or evolves an enterprise asset, offering, capability or outcome |
| `transform` | changes an existing enterprise state, capability, model or operating condition |

### Classification: where the work is positioned

Process Classification describes the position of the process in the
enterprise process landscape. The five-value vocabulary
([`classifications/process-types.yaml`](../classifications/process-types.yaml))
is retained: `strategic`, `management`, `core`, `support`,
`standardization`.

### Intent is not Classification

Intent is the nature and purpose of the work; Classification is its
architectural position. Neither is inferred from the other. Identical
tokens across the two vocabularies (`support`; `management` vs
`manage`) are a lexical coincidence, not a semantic equivalence. A
`core` process may have intent `manage` (`Manage Customer
Relationship`); a `strategic` process may have intent `govern`
(`Govern Enterprise Risk`).

### Specialization: what the process refines

Process Specialization expresses semantic refinement of a more general
process. A specialization names its parent, its basis (customer
segment, geography, product, service, channel, regulatory regime,
operating model, lifecycle condition, organizational context) and its
distinguishing semantic property. A specialization that merely renames
its parent is rejected.

Specialization is not decomposition: a child process is a *kind of*
its parent, not a *part of* it.

### Context: where the responsibility is examined

A Process Context is an ECF Domain × Lifecycle Stage intersection. It
is a semantic boundary for discovery and evaluation; it is not a
process, group, function, capability, classification or intent. An ECF
intersection never generates a process automatically: the ECF provides
context; the Process Architecture provides process structure.

A process may participate in multiple contexts where evidence
establishes legitimate cross-context responsibility. The legacy
`process_audience` field is a migration alias and is never a
substitute for Process Context.

### Relationships: how the process connects

Relationships express how a process interacts with enterprise context
and concepts: `serves` and `contributes-to` toward ECF coordinates,
`realizes` toward capabilities, `composes` for structural composition,
`specializes` toward parent processes.

## Naming

Business Process names follow `<Verb> <Object> [<Scope>]`: an
imperative verb, the principal object, and an optional meaningful
scope. Names avoid organizational department names, lifecycle-stage
names, ECF cell names, and classification vocabulary used as a
substitute for process meaning. The ECF matrix is never a mechanical
process-name generator.

## The separations that are always true

| Distinction | Rule |
|---|---|
| Intent ≠ Classification | Purpose is not position; never inferred from each other |
| Audience ≠ Context | Audience is a legacy alias; Context is Domain × Lifecycle |
| Specialization ≠ Decomposition | Kind-of is not part-of |
| Context ≠ Process | An ECF cell never generates a process |
| Process Group ≠ Business Function ≠ Capability | Grouping processes is not grouping capabilities or organizational ownership |
| Catalog ≠ Kernel | This catalog specializes the Process kernel; it never redefines it |

## See also

- [`docs/architecture.md`](architecture.md): structural architecture
- [`docs/identity.md`](identity.md): the identity contract
- [`docs/classification.md`](classification.md): classification narrative
- [`docs/governance/reconciliation-programme.md`](governance/reconciliation-programme.md):
  the governance loop that keeps this contract true over time
- [`change-requests/CR-BP-14-process-semantic-reconciliation.md`](../change-requests/CR-BP-14-process-semantic-reconciliation.md):
  the normative text
