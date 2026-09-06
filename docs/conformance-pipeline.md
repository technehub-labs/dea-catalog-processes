# Conformance Pipeline (CR-BP-16 §17)

**CR-BP-16 §17: CI Conformance Pipeline.**

The catalog SHALL establish a 10-step conformance pipeline. Every
change touches the pipeline at PR time. Each step is implemented
by a validator under `scripts/` and wired into `.github/workflows/
ci.yml`. A change SHALL pass all blocking steps to receive a
`CONFORMANT` verdict; a change that passes all blocking steps but
emits advisory findings receives `CONFORMANT-WITH-WARNINGS`; a
change that fails any blocking step is `NON-CONFORMANT`.

## Pipeline ordering

```
Pull Request
     │
     ▼
[1] Schema                  (CR-BP-03, validate-process-entries workflow)
     │
     ▼
[2] Structure               (scripts/check_struct.py; STRUCT conformance)
     │
     ▼
[3] References              (BP-SEM-008 context-reference integrity;
                              BP-SEM-009..011 relationship resolution;
                              legacy migration reference check)
     │
     ▼
[4] Semantics               (BP-SEM-001..014: intent, classification,
                              specialization, cycle detection)
     │
     ▼
[5] Hierarchy               (BP-AR-001..007: architectural regression
                              patterns across the BP/PG/PC/ECF axes)
     │
     ▼
[6] Specialization Graph    (BP-SEM-013 specializes-edge validation;
                              BP-SEM-014 cycle detection;
                              scripts/check_process_specialization.py
                              BP-SPEC-01-001..007)
     │
     ▼
[7] MECE Findings           (BP-AR-007 specialization vs decomposition;
                              scripts/check_process_context.py PC-001..008;
                              scripts/check_process_group.py PG-001..008)
     │
     ▼
[8] Provenance              (ADM-008: change_history date/cr/change;
                              scripts/check_admission_gate.py ADM-001..008)
     │
     ▼
[9] CR Validation           (CR-META-001..006: Status, Layer, Owner,
                              Depends on, Companion to, filename pattern;
                              scripts/check_cr_metadata.py)
     │
     ▼
[10] CONFORMANCE RESULT     (scripts/build_conformance_report.py
                              produces Levels 1-4 per record;
                              scripts/check_admission_gate.py produces
                              CONFORMANCE RESULT verdict)
```

## Blocking vs advisory

| Step | Blocking? | Authority |
|---|---|---|
| [1] Schema | yes | validate-process-entries workflow |
| [2] Structure | advisory | STRUCT conformance (legitimate dev paths exempted) |
| [3] References | yes | BP-SEM-008 + legacy migration |
| [4] Semantics | yes | BP-SEM-001..014 |
| [5] Hierarchy | yes | BP-AR-001..007 |
| [6] Specialization Graph | yes | BP-SEM-013 + BP-SEM-014 + BP-SPEC-01-001..007 |
| [7] MECE Findings | yes (BP-AR-007 only) | BP-AR-007 + PC-001..008 + PG-001..008 |
| [8] Provenance | advisory | ADM-008 (recommendation, not requirement) |
| [9] CR Validation | yes (new CRs only) | CR-META-001..006 (legacy CRs: advisory) |
| [10] Conformance Result | yes | conformance_report.yaml Levels 1-4 |

### CR Validation (Step 9): cutoff policy

CR Validation (CR-META-001..006) runs in `--strict` mode in CI
as of PR-13. The cutoff is **2026-09-06** (CR-BP-16 acceptance
date), passed via `--cutoff-date`.

- **Legacy CRs** (mtime before the cutoff): reported as advisory
  findings. They pre-date the §21 metadata schema. They SHOULD
  be retro-fitted as a separate programme (the `CR-META-LEGACY`
  backlog); they do not block the gate.
- **New CRs** (mtime on or after the cutoff): MUST comply. Any
  new or modified CR that fails any of CR-META-001..006 blocks
  the merge.

The conformance gate accepts two conventions for the metadata
line: `**Key**: value` (canonical; colon outside bold) and
`**Key:** value` (legacy / GitHub-issues style; colon inside
bold). Both are valid; the validator normalises the key by
stripping a trailing colon. Parenthetical qualifiers on `Layer`
(e.g. `L1 (Process Catalog)`) and `Status` (e.g. `Proposed
(2026-09-03)`) are also normalised.

## Continuous conformance (CR-BP-16 §25)

The pipeline SHALL re-evaluate when:

- a process is created;
- a process changes;
- its parent changes;
- its Context changes;
- its specialization changes;
- classification vocabularies change;
- the governing metamodel changes.

In practice the entire pipeline runs on every PR. Path filters
in `.github/workflows/ci.yml` short-circuit redundant gates:

- changes under `change-requests/` re-run the CR Validation step;
- changes under `entities/` re-run the Schema, Semantics, Hierarchy,
  Specialization Graph, MECE, and Provenance steps;
- changes under `contexts/` re-run the References and MECE steps;
- changes under `classifications/` re-run the Semantics step.

## Conformance verdicts (CR-BP-16 §18)

Each PR receives one of three verdicts, displayed in the
"Conformance Result" CI step:

- `CONFORMANT`: all mandatory gates pass.
- `CONFORMANT-WITH-WARNINGS`: all blocking gates pass and only
  advisory findings remain.
- `NON-CONFORMANT`: at least one mandatory gate fails.

## Blocking conditions (CR-BP-16 §19)

A change SHALL be blocked from canonical admission if any of the
following are detected:

- Invalid schema
- Broken reference
- Duplicate canonical id
- Invalid hierarchy
- Invalid Process Intent
- Invalid Classification
- Invalid specialization
- Specialization cycle
- Missing mandatory evidence
- Unresolved identity
- Unresolved canonical disposition
- Lost provenance
- Unauthorized ontology expansion

Each condition maps to one or more rules:

| §19 condition | Rule(s) |
|---|---|
| Invalid schema | JSON Schema validation (validate-process-entries) |
| Broken reference | BP-SEM-008, BP-SEM-009, BP-SEM-010, BP-SEM-011 |
| Duplicate canonical id | BP-SEM-004 |
| Invalid hierarchy | BP-AR-001, BP-AR-002, BP-AR-003, BP-AR-004 |
| Invalid Process Intent | BP-SEM-001, BP-SEM-002 |
| Invalid Classification | BP-SEM-005, BP-SEM-006 |
| Invalid specialization | BP-SEM-013 |
| Specialization cycle | BP-SEM-014 |
| Missing mandatory evidence | ADM-008 |
| Unresolved identity | BP-SEM-008 |
| Unresolved canonical disposition | dispositions register LOCKED check |
| Lost provenance | ADM-008 |
| Unauthorized ontology expansion | BP-AR-005, BP-AR-006 |

## See also

- [`docs/conformance.md`](conformance.md): gate summary
- [`change-requests/CR-BP-16-process-catalog-conformance-gate.md`](../change-requests/CR-BP-16-process-catalog-conformance-gate.md): full CR
- [`.github/workflows/ci.yml`](../.github/workflows/ci.yml): pipeline wiring