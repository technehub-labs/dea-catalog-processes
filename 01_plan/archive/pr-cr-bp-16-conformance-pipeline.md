# CR-BP-16 conformance pipeline (S17/S18/S19/S25) + unified Conformance Result

## Summary

CR-BP-16 §17 (CI Conformance Pipeline), §18 (unified Conformance
Result), §19 (blocking-conditions mapping), and §25 (continuous-
conformance triggers) are now live. Every PR receives a single
CONFORMANCE RESULT verdict that aggregates all 10 pipeline steps.
The catalogue remains **38/38 Level 4 (Canonically Conformant)**,
**0 BP-SEM findings**, **0 BP-AR findings**.

This PR ships:
- the missing visitor-facing pipeline doc (closes D7);
- a unified Conformance Result aggregator (the canonical
  pre-merge verdict source);
- CI step that emits the aggregated verdict.

## What this PR does

### `docs/conformance-pipeline.md` (new, 153 lines)

Documents the 10-step pipeline (Schema, Structure, References,
Semantics, Hierarchy, Specialization Graph, MECE, Provenance,
CR Validation, Conformance Result), the blocking-vs-advisory
matrix, the §19 blocking-conditions mapping (13 conditions),
and the §25 continuous-conformance triggers (7 re-evaluation
events). This is the D7 visitor-facing doc that was missing
from the programme plan.

### `scripts/conformance_result.py` (new, 162 lines)

Runs all 15 gates (10 blocking + 5 advisory) and produces a
single CONFORMANCE RESULT verdict:

- `CONFORMANT`: all mandatory gates pass.
- `CONFORMANT-WITH-WARNINGS`: all blocking gates pass, only
  advisory findings remain.
- `NON-CONFORMANT`: at least one mandatory gate fails.

`--json` mode emits a structured report (per-gate returncode +
verdict line, blocking failures list, advisory failures list).
`--strict` treats advisory failures as blocking.

### `.github/workflows/ci.yml`

New "Aggregate Conformance Result (CR-BP-16 §17/S18)" step runs
after the per-gate steps. The aggregated verdict is the canonical
pre-merge source.

### `docs/conformance.md`

See Also block updated to link to `docs/conformance-pipeline.md`.

### `tests/test_conformance_result.py` (new, 7 tests)

- `test_conformance_result_runs_on_live`: verdict CONFORMANT.
- `test_conformance_result_json_shape`: JSON shape correct;
  every [1]..[10] step covered.
- `test_conformance_result_strict_propagates_failure`: --strict
  surfaces failures.
- `test_pipeline_doc_exists`: doc present.
- `test_pipeline_doc_covers_all_10_steps`: every step in doc.
- `test_pipeline_doc_covers_13_blocking_conditions`: all 13
  §19 conditions present.
- `test_pipeline_doc_covers_continuous_conformance`: all 7
  §25 triggers present.

## CR-BP-16 §29 acceptance criteria status

| Criterion | Status | This PR? |
|---|---|---|
| Conformance rules machine-readable | ✅ | (PR-29) |
| CI executes structural validation | ✅ | (PR-31) |
| CI executes semantic validation | ✅ | (PR-29) |
| CI validates specialization graphs | ✅ | (PR-37 + PR-39) |
| CI validates references | ✅ | (PR-31) |
| CI validates provenance | ⚠️ partial | (PR-39 ADM-008) |
| CI validates CR metadata | ✅ | (PR-39) |
| Architectural regression detected | ✅ | (PR-38) |
| New-process admission mandatory path | ⚠️ partial | (PR-39) |
| Existing canonical baseline defined | ✅ | (PR-38) |
| Documentation describes the gate | ✅ | **yes** (this PR) |
| Conformance results reproducible | ✅ | (PR-38) |
| Canonical status = conformance + governance | ✅ | (PR-38) |
| Gate ≠ ECF coverage = process completeness | ✅ | (PR-31) |

**Net: 10 fully met (up from 9); 2 partial; 0 unmet.**

## Verification

- `pytest tests/ -q`: **137 passed** (130 prior + 7 new for
  Conformance Result + pipeline doc).
- BP-SEM `--strict`: CONFORMANT.
- BP-AR `--strict`: CONFORMANT.
- Conformance Result on the branch: **CONFORMANT** (15 gates
  evaluated, 0 blocking failures, 0 advisory failures).
- Fresh-clone regenerator repro: PASSES.
- Dash-clean: zero en/em dashes in added lines.

## Programme position

- CR-BP-14: **Implemented** end-to-end.
- CR-BP-15 + CR-BP-15-IMP: **Phases 1-7 shipped**; the disposition
  register is LOCKED at 18/18; the catalogue is CONFORMANT.
- CR-BP-16: §10/15/16/17/18/19/21/22/23/24/25 machinery now live
  in CI. The §26 reconciliation-compatibility section is satisfied
  by the disposition register + conformance report. **10 of 14 §29
  acceptance criteria fully met**; 2 partial (provenance schema
  validation, mandatory enforcement of CR-META on new CRs) and 0
  unmet. CR-BP-16 is functionally **Implemented** as of this PR.
- Next: **CR-BP-13c+ admission tranche** (the next post-freeze
  admission exercise): the gate machinery is fully ready. Awaiting
  user direction.