# OpenDEA Business Process Catalog

## Purpose

The OpenDEA Business Process Catalog establishes the canonical, structured and machine-consumable foundation for representing, organizing and evolving business processes within the OpenDEA ecosystem.

The repository is not intended to be a simple collection of process names or a conventional process reference library. It provides the foundation for a rigorous **Business Process Architecture** that enables the systematic identification, classification, decomposition, validation and reuse of business process knowledge.

The catalog is designed to support enterprise transformation, digital transformation, operational transformation, process modelling, workflow design, automation, autonomous operations and AI-enabled or agentic operations.

The Business Process Catalog is a foundational OpenDEA repository. Process elements defined here are expected to establish canonical references that can be used by other OpenDEA repositories and models rather than independently recreating or redefining the same business process concepts.

The governing principle is:

> **One canonical definition. One stable identity. Many valid relationships.**

---

# Architectural Position

The Business Process Catalog is grounded in the OpenDEA conceptual architecture.

The OpenDEA Enterprise Concepts Framework (ECF) provides the primary organizing structure for understanding the enterprise. The ECF establishes a matrix formed by the intersection of Enterprise Domains and Lifecycle Stages.

The Business Process Catalog uses this structure as its contextual foundation.

```text
Enterprise Domain × Lifecycle Stage
                │
                ▼
          Process Scope / Context
                │
                ▼
       Process Architecture
                │
                ▼
        Process Decomposition
```

An ECF intersection does not automatically represent a business process.

Instead, each intersection defines the **Process Context** within which the relevant business processes are identified, analysed and validated.

This distinction is fundamental to the architecture of the catalog.

> **The ECF provides the contextual coordinate. The Business Process Architecture provides the process structure.**

---

# Enterprise Concepts Framework

The Enterprise Concepts Framework provides a holistic and structured representation of the enterprise through the intersection of:

* Enterprise Domains
* Lifecycle Stages

Each intersection represents a distinct enterprise context.

```text
ECF Cell

Domain
   ×
Lifecycle Stage
   │
   ▼
Enterprise Context
```

Within the Business Process Catalog, an ECF cell is interpreted as a **Process Context**.

A Process Context defines the conceptual boundary within which one or more business process elements may be identified.

The Process Context is therefore not automatically equivalent to:

* a Business Process;
* a Business Function;
* a Business Capability;
* a Process Group; or
* a process decomposition level.

The Process Context provides the semantic and architectural boundary for determining which business processes belong within the Domain and Lifecycle intersection.

---

# Canonical Process Context

Each Process Context is defined by a unique combination of:

```text
Domain
Lifecycle Stage
```

Conceptually:

```text
Process Context
├── Domain
├── Lifecycle Stage
├── Scope
├── Included Concerns
├── Excluded Concerns
├── Adjacent Contexts
└── Process Elements
```

Every Process Context should establish:

* what enterprise concerns belong within the context;
* what outcomes or transformations must be addressed;
* what concerns are explicitly outside the context;
* which adjacent ECF contexts may have closely related responsibilities; and
* the criteria used to determine the placement of process elements.

This provides the basis for maintaining clear boundaries throughout the catalog.

---

# Business Process Architecture

The Business Process Catalog establishes a structured decomposition architecture.

The intended topology is:

```text
Process Context
       │
       ▼
L0 ── Process Scope
       │
       ▼
L1 ── Process Group
       │
       ▼
L2 ── Business Process
       │
       ▼
L3 ── Activity
       │
       ▼
L4 ── Task
```

The precise normative semantics of these levels will be aligned with the OpenDEA Metamodel.

The current architecture treats the levels as follows.

## L0: Process Scope / Process Context

L0 establishes the highest-level scope within which a coherent set of related process concerns is organized.

L0 provides the conceptual entry point for process decomposition within a Process Context.

An L0 element must:

* represent a coherent and stable enterprise responsibility;
* have a clear semantic boundary;
* contribute uniquely to the coverage of its Process Context;
* avoid overlap with sibling L0 elements; and
* provide a meaningful basis for decomposition.

An ECF Process Context may contain one or more L0 elements.

An L0 element is not assumed to be synonymous with an ECF Domain or Lifecycle Stage.

---

## L1: Process Group

L1 represents a coherent grouping of related processes within an L0 Process Scope.

A Process Group organizes related process responsibilities that share a meaningful functional or operational relationship.

An L1 element must:

* have a clear purpose within its parent L0;
* establish a non-overlapping boundary relative to sibling groups;
* provide a meaningful grouping for lower-level processes; and
* support systematic decomposition.

The precise relationship between Process Group, Business Function and other OpenDEA concepts will be governed by the normative OpenDEA Metamodel.

The Business Process Catalog must not independently redefine Business Function.

---

## L2: Business Process

L2 represents the first level at which an element is treated as an independently meaningful Business Process.

An L2 Business Process must satisfy the normative criteria established for a Business Process.

The intended validation criteria include:

1. **Input and Output Transformation**
   The process transforms defined inputs into defined outputs.

2. **Objective Contribution**
   The process makes a distinct contribution toward a defined business or enterprise objective.

3. **Standalone Executability**
   The process can be understood and executed as a coherent unit of work.

4. **Resource Responsibility**
   The process has identifiable responsibility for the resources, capabilities, roles or means required for its execution.

An element that does not satisfy the required criteria should not be classified as an L2 Business Process.

It may instead represent:

* a Process Group;
* an Activity;
* a Task;
* a Business Function;
* a Capability; or
* another OpenDEA concept.

---

## L3: Activity

L3 represents a cohesive grouping of work that contributes to an L2 Business Process but does not independently satisfy the criteria required for an L2 Business Process.

An Activity provides logical structure within a Business Process.

Activities should be evaluated according to their:

* cohesion;
* contribution to the parent process;
* boundary clarity;
* independence from sibling activities; and
* appropriateness as a grouping of tasks.

The formal cohesion model and scoring criteria will be defined as part of the repository validation architecture.

---

## L4: Task

L4 represents the lowest defined level of business process decomposition within the catalog.

A Task is an actionable unit of work that contributes to the completion of an Activity.

A Task should satisfy the intended atomicity criteria:

1. **Indivisibility**
   The task represents a sufficiently atomic unit of work within the Business Process Architecture.

2. **Single Responsibility**
   The task has a clear primary execution responsibility.

3. **Bounded Execution**
   The task represents a bounded unit of work.

4. **Verifiable Completion**
   Completion of the task can be determined.

Work below the approved decomposition boundary is treated as implementation detail, system behaviour, workflow logic or work instruction unless explicitly modelled by another OpenDEA framework.

The normative decomposition stopping rule will be established through OpenDEA governance.

---

# Process Discovery Method

Business processes are not created by mechanically combining Domain and Lifecycle terminology.

The catalog does not treat the ECF matrix as a process name generator.

Instead, process elements are derived through structured semantic analysis.

The governing principle is:

> **Processes are discovered from the meaning of the enterprise context, not constructed through word combinations.**

For each Process Context, the following method is applied.

## 1. Establish the Context

Determine the meaning of:

```text
Domain
+
Lifecycle Stage
=
Process Context
```

The analysis must establish what the intersection means from an enterprise perspective.

---

## 2. Define the Cell Charter

Each Process Context should establish a Cell Charter describing:

* the enterprise concern;
* the lifecycle concern;
* the combined semantic meaning;
* expected outcomes;
* relevant transformations;
* inclusions;
* exclusions; and
* adjacent boundaries.

The Cell Charter establishes the basis for process identification.

---

## 3. Identify Coverage Concerns

Before identifying processes, determine the complete set of concerns that must be addressed within the Process Context.

These concerns represent semantic coverage requirements.

They are not automatically process elements.

This prevents the premature acceptance of the first plausible process name.

---

## 4. Identify Candidate Processes

Candidate processes should be derived from:

* recognised business process concepts;
* established management and operational disciplines;
* enterprise architecture;
* industry practices;
* authoritative process frameworks; and
* the semantic requirements of the Process Context.

The preferred approach is to identify established and recognisable business process concepts.

Artificially constructed names should be avoided.

---

## 5. Evaluate Process Candidates

Each candidate is evaluated against:

* semantic fit;
* Process Context coverage;
* uniqueness of contribution;
* process criteria;
* boundary clarity;
* overlap with other candidates; and
* compatibility with the OpenDEA Metamodel.

A candidate must not be accepted simply because it appears linguistically appropriate.

---

## 6. Establish the Canonical Set

The accepted set of process elements must collectively address the Process Context.

The objective is to identify the smallest coherent set that provides complete coverage without unnecessary duplication.

This may result in:

* one process element;
* multiple process elements; or
* further architectural analysis where the Process Context has not yet been sufficiently understood.

---

# MECE and Holistic Coverage

The Business Process Catalog applies Mutually Exclusive and Collectively Exhaustive principles across multiple architectural scopes.

MECE is not treated as a single validation exercise.

## Process Context MECE

Within a Domain × Lifecycle Process Context:

* sibling process elements must not duplicate responsibility;
* every accepted element must provide unique coverage; and
* the complete set must collectively address the defined Cell Charter.

---

## Domain MECE

Across all Lifecycle Stages within an Enterprise Domain:

* process responsibilities must be lifecycle-specific;
* the same process should not be independently recreated across multiple stages;
* lifecycle transitions must have clear boundaries.

---

## Lifecycle MECE

Across all Enterprise Domains within a Lifecycle Stage:

* each Domain must maintain a distinct enterprise concern;
* processes must not duplicate responsibilities already owned by another Domain;
* cross-domain dependencies must be represented as relationships rather than duplicate process definitions.

---

## Enterprise Matrix MECE

Across the complete ECF matrix:

* each process element must have one canonical conceptual home;
* duplicate process definitions must be prevented;
* related processes may exist across contexts without representing the same process;
* relationships must not be confused with ownership.

The governing principle is:

> **One canonical home. Many valid relationships.**

---

## Hierarchical MECE

At every level of decomposition:

```text
Parent
 ├── Child A
 ├── Child B
 └── Child C
```

the children must:

* collectively cover the intended scope of the parent; and
* maintain clear, non-overlapping boundaries.

A decomposition must not merely restate the parent at increasing levels of detail.

Each level must introduce a meaningful structural distinction.

---

# Canonical Identity

Every canonical process element will have a stable identifier.

Names and descriptions may evolve through governed change, but identity must remain stable.

Downstream OpenDEA repositories should reference canonical process identifiers rather than reproduce independent copies of process definitions.

Conceptually:

```text
Canonical Process
        │
        ├── Capability Relationship
        ├── Function Relationship
        ├── Value Stream Relationship
        ├── Information Relationship
        ├── Policy Relationship
        ├── Organization Relationship
        ├── Role Relationship
        ├── Product Relationship
        ├── Service Relationship
        ├── Workflow Relationship
        ├── Agent Relationship
        └── System Relationship
```

The existence of a relationship does not create another canonical definition of the same process.

---

# Relationship with the OpenDEA Metamodel

The Business Process Catalog is not an independent ontology.

The normative definition of Business Process and its relationships are governed by the OpenDEA Metamodel.

The repository may define catalog structures, decomposition profiles, validation rules and controlled representations required to manage the Business Process Architecture.

Where the Business Process Architecture identifies a missing foundational concept or relationship, the change must be assessed against the OpenDEA Metamodel.

The expected evolution path is:

```text
Architectural Requirement
        │
        ▼
Conceptual Analysis
        │
        ▼
OpenDEA Metamodel Assessment
        │
        ├── Existing Semantic Support
        │         │
        │         ▼
        │    Catalog Implementation
        │
        └── Semantic Gap
                  │
                  ▼
             Change Request
                  │
                  ▼
        Metamodel Evolution
                  │
                  ▼
        Derived Schema Evolution
                  │
                  ▼
        Catalog Implementation
```

The catalog must not introduce local semantic constructs that conflict with or bypass the normative OpenDEA Metamodel.

---

# Relationship with Business Capabilities and Functions

Business Process must maintain conceptual separation from related OpenDEA concepts.

In particular:

* **Business Capability** represents what an enterprise is able to do.
* **Business Function** represents a logical grouping of responsibilities or areas of work.
* **Business Process** represents a structured transformation of inputs into outcomes.
* **Activity** represents a cohesive component of a Business Process.
* **Task** represents an actionable unit of work.

These distinctions are governed by the OpenDEA conceptual and normative metamodels.

The Business Process Catalog must therefore not absorb Business Functions, Capabilities or other concepts merely because their names resemble processes.

Where a classification ambiguity exists, the element must be analysed against the applicable semantic criteria before acceptance into the catalog.

---

# Validation Architecture

The repository is intended to evolve toward programmatic validation.

Validation will include the following categories.

## Structural Validation

Validates:

* Process Context structure;
* permitted decomposition paths;
* parent and child relationships;
* level integrity;
* orphan elements; and
* invalid hierarchy transitions.

---

## Semantic Validation

Validates whether an element satisfies the criteria associated with its declared type and level.

For example, an L2 Business Process must satisfy the normative Business Process criteria.

---

## Naming Validation

Validates naming conventions appropriate to the process level and concept type.

Naming conventions will be designed to ensure:

* semantic clarity;
* grammatical consistency;
* level consistency;
* avoidance of unnecessary synonym duplication; and
* stable terminology.

---

## Boundary Validation

Validates:

* inclusion;
* exclusion;
* adjacency;
* duplicate responsibility; and
* canonical placement.

---

## MECE Validation

Validates process completeness and non-overlap:

* within a Process Context;
* within an Enterprise Domain;
* within a Lifecycle Stage;
* across the ECF matrix; and
* within every decomposition hierarchy.

---

## Referential Integrity Validation

Validates that references from other OpenDEA repositories resolve to valid canonical process identifiers and compatible process levels.

---

# Repository Evolution

The Business Process Catalog will evolve incrementally.

The initial priority is not the rapid population of process entries.

The initial priority is the establishment of a sound conceptual, architectural and validation foundation.

The evolution sequence is:

## Phase 0 — Structural Reconnaissance

Establish the current state of:

* the OpenDEA Metaframework;
* the Enterprise Concepts Framework;
* the OpenDEA Metamodel;
* the Business Process Catalog;
* existing process definitions;
* existing relationships; and
* existing schema and validation mechanisms.

Identify structural inconsistencies, semantic gaps and required architectural decisions.

---

## Phase 1 — Canonical Process Foundation

Establish:

* Process Context semantics;
* Business Process semantics;
* Function and Process boundaries;
* decomposition semantics;
* level definitions;
* naming conventions;
* canonical identity; and
* validation principles.

---

## Phase 2 — Foundational Alignment

Assess the Process Architecture against the normative OpenDEA Metamodel.

Where necessary:

* define a Change Request;
* evolve the metamodel;
* update derived schemas;
* establish conformance rules; and
* update the catalog architecture.

---

## Phase 3 — ECF Process Matrix

Establish the authoritative Process Context matrix.

For every Domain × Lifecycle intersection, define:

* Process Context;
* Cell Charter;
* scope;
* exclusions;
* coverage concerns;
* adjacent boundaries; and
* candidate process evidence.

---

## Phase 4 — L0 Discovery

Identify the canonical L0 process scopes for each Process Context.

Each L0 candidate must be evaluated for:

* semantic validity;
* contextual fit;
* unique contribution;
* boundary clarity; and
* MECE compliance.

Process discovery proceeds systematically through the ECF matrix.

---

## Phase 5 — Controlled Decomposition

Once the L0 architecture is stable:

```text
L0
↓
L1
↓
L2
↓
L3
↓
L4
```

Each decomposition is validated before subsequent levels are introduced.

---

## Phase 6 — Programmatic Validation

Implement machine-readable validation for:

* topology;
* semantic criteria;
* naming;
* boundaries;
* MECE;
* decomposition;
* canonical identity; and
* referential integrity.

---

# Governance and Architectural Decisions

Architectural and semantic decisions that materially affect the Business Process Architecture must be recorded and governed.

Examples include:

* the definition of Process Context;
* the normative meaning of each decomposition level;
* the distinction between Function and Process;
* the decomposition stopping rule;
* canonical identity conventions;
* MECE validation criteria; and
* cross-repository process relationships.

Where a decision affects the normative OpenDEA semantic model, it must be progressed through the appropriate OpenDEA Change Request process.

The catalog must remain aligned with the normative model as it evolves.

---

# Design Principles

The Business Process Catalog is governed by the following principles.

## Context Before Classification

Understand the Domain × Lifecycle intersection before identifying processes.

## Meaning Before Naming

A process name must follow semantic analysis.

It must not be produced through terminology combination.

## Established Before Invented

Prefer established and recognisable business process concepts over artificial terminology.

## Boundary Before Decomposition

Define what a process includes and excludes before decomposing it.

## One Canonical Home

Every canonical process element has one authoritative conceptual location.

## Many Valid Relationships

A process may participate in multiple enterprise relationships without being duplicated.

## MECE by Design

Completeness and non-overlap must be considered throughout the architecture, not only during final review.

## Metamodel First

The Business Process Catalog must align with the normative OpenDEA Metamodel.

## Machine-Testable Where Possible

Semantic, structural and validation rules should progressively become machine-readable and executable.

## Controlled Evolution

The architecture may evolve, but foundational changes must be explicit, governed and traceable.

---

# Current Status

The repository is undergoing architectural inception and evolution.

The current focus is to establish the canonical Business Process Architecture before substantial catalog population.

Current work includes:

* reconciliation of existing Process definitions;
* alignment with the normative OpenDEA Metamodel;
* definition of Process Context;
* analysis of decomposition semantics;
* clarification of Business Function and Business Process boundaries;
* definition of MECE validation scopes; and
* design of the future validation architecture.

No substantial process population should be considered authoritative until the foundational architecture and normative alignment have been established.

---

# Intended Outcome

The intended outcome is an authoritative OpenDEA Business Process Architecture and Catalog that provides:

* holistic enterprise process coverage;
* rigorous Domain × Lifecycle contextual organization;
* controlled process decomposition;
* explicit semantic boundaries;
* MECE validation;
* stable canonical identity;
* machine-readable representation;
* cross-repository referential integrity; and
* a durable foundation for process modelling, workflow derivation, automation, autonomous operations, AI and agentic systems.

The Business Process Catalog is therefore intended to become a foundational component of the OpenDEA ecosystem through which business process knowledge can be consistently defined, validated, reused and evolved.

> **The objective is not to create the largest catalog of processes.**
>
> **The objective is to establish the most coherent, grounded and structurally reliable process architecture from which the enterprise process landscape can be systematically derived.**
