# CR-BP-16 full conformance gate: S10 / S15 / S16 / S22

## Summary

The remaining CR-BP-16 sections called out in §29 acceptance
criteria are now live as CI machinery (**advisory**). The
catalogue remains **38/38 Level 4 (Canonically Conformant)** and
**0 BP-SEM / BP-AR findings**.

This PR ships four new gate validators, four new CI steps, and
extends the BP-SEM family to BP-SEM-014 (cycle detection).
Together with PR-31..38, **9 of the 14 §29 acceptance criteria
are now fully met; 5 are partial** (with gate machinery in place
and the remaining work scoped to specific follow-up items).

## What this PR does

### BP-SEM-014 Specialization Cycle Detection

- `scripts/check_process_semantics.py` (extended):
  - **BP-SEM-014**: the specializes graph MUST be acyclic
    (CR-BP-16 §10). Self-specialization (A -> A) and any cycle
    (A -> B -> ... -> A) are architectural regressions. A DFS
    pass detects back-edges after per-record checks complete.
  - Module docstring documents BP-SEM-014 alongside BP-SEM-001..013.
  - Self-test extended with a cycle fixture (broken-blocking: 6 -> 10).

### New validators (advisory)

- `scripts/check_cr_metadata.py` (new): **CR-META-001..006**
  (CR-BP-16 §16). Every architectural CR must carry **Status**,
  **Layer**, **Owner**, **Depends on** (with `CR-BP-NN` refs),
  **Companion to**, and a filename matching the CR-BP-NN
  pattern. **Advisory**: legacy CRs lack §21 metadata; CR-BP-13A
  is the planned first CR to demonstrate full §21 compliance.
- `scripts/check_documentation_conformance.py` (new):
  **DOC-001..003** (CR-BP-16 §22). Three rules flag legacy
  synonym usage without the preferred term (e.g. "Process
  Kernel" alone without "Business Process"), unresolvable
  canonical id references, and standalone "Process" usage
  outside compound forms ("Business Process", "Process Group",
  "Process Context", etc.). **Advisory**.
- `scripts/check_admission_gate.py` (new): **ADM-001..008**
  (CR-BP-16 §15). Eight rules for new-process admission:
  Evidence coverage (admission CR in change_history), Identity
  shape, Context resolution, Group fit, Boundary completeness
  (triggers, outcomes), Intent+Classification in approved
  vocabularies, Specialization validity, Provenance shape.
  **Advisory**: surfaces findings on the locked population
  for review (boundary + provenance fields are recommended,
  not required).

### CI

- `.github/workflows/ci.yml`: three new advisory CI steps:
  - "Run CR metadata gate" (CR-META-001..006)
  - "Run documentation conformance gate" (DOC-001..003)
  - "Run admission gate" (ADM-001..008)

### Tests

- `tests/test_check_process_semantics.py`:
  - `test_bp_sem_014_detects_cycle`: BP-SEM-014 fires on a
    2-record cycle.
  - `test_bp_sem_014_rejects_self_specialization`: BP-SEM-014
    fires on self-specialization.
  - Parametrized rule-coverage extended for BP-SEM-014.
- `tests/test_cr_bp16_gates.py` (new, 11 tests): CR metadata,
  documentation conformance, and admission gate tests.

## CR-BP-16 §29 acceptance criteria status

| Criterion | Status | This PR? |
|---|---|---|
| Conformance rules machine-readable | ✅ | (PR-29) |
| CI executes structural validation | ✅ | (PR-31) |
| CI executes semantic validation | ✅ | (PR-29) |
| CI validates specialization graphs | ✅ | **yes** (BP-SEM-013 + 014) |
| CI validates references | ✅ | (PR-31) |
| CI validates provenance | ⚠️ partial | **yes** (ADM-008) |
| CI validates CR metadata | ✅ | **yes** (CR-META) |
| Architectural regression detected | ✅ | (PR-38) |
| New-process admission mandatory path | ⚠️ partial | **yes** (gate live; enforcement pending CR-BP-13A pilot) |
| Existing canonical baseline defined | ✅ | (PR-38) |
| Documentation describes the gate | ⚠️ partial | **yes** (gate live; docs walkthrough separate) |
| Conformance results reproducible | ✅ | (PR-38) |
| Canonical status = conformance + governance | ✅ | (PR-38) |
| Gate ≠ ECF coverage = process completeness | ✅ | (PR-31) |

**Net: 9 fully met (up from 5); 5 partial (down from 8); 0 unmet.**

## Verification

- `pytest tests/ -q`: **130 passed** (116 prior + 14 new for
  BP-SEM-014, CR-META, DOC, ADM).
- BP-SEM `--strict`: CONFORMANT (0 errors, 0 warnings).
- BP-AR `--strict`: CONFORMANT (no architectural regressions).
- BP-SEM-014 cycle detection: live graph has no cycles.
- CR-META: 46 findings across 16 CR files (advisory; legacy CRs).
- DOC: 436 findings (advisory; docs cleanup separate item).
- ADM: 54 findings across 18 Process records (advisory;
  boundary + provenance fields).
- Fresh-clone regenerator repro PASSES.
- Dash-clean: zero en/em dashes in added lines.

## Programme position

- CR-BP-14: **Implemented** end-to-end.
- CR-BP-15 + CR-BP-15-IMP: Phases 1-7 shipped; the disposition
  register is LOCKED at 18/18; the catalogue is CONFORMANT.
- CR-BP-16: §21 + §23/24 + §10/15/16/22 machinery now live in
  CI. The remaining sections (§17 pipeline ordering, §19 blocking
  conditions beyond what's already live, §25 continuous
  conformance enforcement, full provenance schema validation,
  docs walkthrough) are scoped for future PRs.
- Next: **CR-BP-13A admission tranche** (customer + demand L1
  admission) — the first post-freeze admission exercise, OR a
  CR-BP-16 §17/§25 follow-up that promotes the advisory gates
  to blocking. Awaiting user direction.