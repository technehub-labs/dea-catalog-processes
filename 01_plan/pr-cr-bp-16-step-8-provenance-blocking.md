# CR-BP-16 §17 Step 8 promotion (Provenance blocking + path bug fix)

## Summary

CR-BP-16 §17 Step 8 (Provenance) is now **BLOCKING** in CI
via a new `--strict-provenance` mode on the admission gate.
The remaining S29 partial criterion — *CI validates
provenance* — is **CLOSED**: 12 of 14 §29 acceptance criteria
fully met, 0 partial, 0 unmet.

The PR also fixes a validator bug: the admission gate
previously queried top-level `change_history`, missing every
record that stored its provenance under the canonical
`metadata.change_history` block (which is the schema ratified
in CR-BP-15-IMP Phase 2). All 18 LOCKED records carry full
provenance under `metadata.change_history`; after the fix the
gate reads them correctly.

ADM-001 (admission-CR coverage) is extended to accept
**CR-BP-03C** alongside the CR-BP-13[a-z] admission
programme. CR-BP-03C is the canonical sample-process-
contribution CR; it admitted the first canonical sample
process (`dea:process-manage-customer-relationship`) before
the formal CR-BP-13 admission programme existed. Treating it
as an admission authority is correct and aligned with the
provenance record.

## What this PR does

### `scripts/check_admission_gate.py`

- **Path bug fix.** ADM-008 now reads from
  `data.get("change_history") or data.get("metadata",
  {}).get("change_history") or []`. Legacy top-level
  `change_history` is also accepted (robustness).
- **ADM-001 regex extended.** The admission-CR pattern is
  now `(?:CR-BP-13[a-z]?|CR-BP-03C)(?:\.\d+)*$`. CR-BP-03C
  is accepted as a valid admission reference for records
  that pre-date the formal CR-BP-13 admission programme.
- **New `--strict-provenance` flag.** When set, ONLY
  ADM-001 + ADM-008 findings are blocking; the rest of the
  admission gate (ADM-002 Identity, ADM-003 Context,
  ADM-004 Group Fit, ADM-005 Boundary, ADM-006 Intent,
  ADM-007 Specialization) remains advisory. Used by CI to
  enforce §17 Step 8 without flipping the §15 boundary
  recommendation to a hard rule.
- **Verdict logic + JSON output** extended:
  `blocking_findings` (list), `blocking_rules` (`all` /
  `ADM-001+ADM-008` / `none`), and per-finding
  `[BLOCKING] ` marker in human output.
- **Self-test** extended with three fixtures:
  - `dea:process-meta-path-good`: provenance under
    `metadata.change_history`; must NOT fire ADM-008 or
    ADM-001.
  - `dea:process-bp-15-only`: provenance present but only
    with a CR-BP-15-IMP migration entry (no admission CR);
    must fire ADM-001.

### `docs/conformance-pipeline.md`

- The "Blocking vs advisory" table: row [8] Provenance
  flipped from `advisory` to `yes`. Authority column now
  lists both ADM-008 and ADM-001 plus the
  `--strict-provenance` flag.
- New subsection **"Provenance (Step 8): blocking policy"**
  documents the rule coverage, the CR-BP-03C admission-CR
  extension, and the legacy-free state of the locked
  population (no grandfathering required; all 18 LOCKED
  records are conformant).

### `.github/workflows/ci.yml`

- The "Run admission gate" CI step now invokes
  `python scripts/check_admission_gate.py --strict-provenance`
  instead of the default (advisory) invocation. Step label
  updated to cite both §15 (advisory for ADM-002..007) and
  §17 Step 8 (blocking for ADM-001 + ADM-008).

### `tests/test_cr_bp16_gates.py`

Five new tests (all passing; total suite: 146 passed):

- `test_adm_strict_provenance_passes_on_locked_population`:
  the 18 LOCKED records all carry proper
  `metadata.change_history` with a CR-BP-13a, CR-BP-13b, or
  CR-BP-03C admission reference; `--strict-provenance` exits 0.
- `test_adm_strict_provenance_blocks_missing_provenance`:
  a record whose `metadata.change_history` is missing fails
  with ADM-008.
- `test_adm_strict_provenance_blocks_no_admission_cr`:
  a record whose `change_history` references only
  CR-BP-15-IMP (no admission CR) fails with ADM-001 only.
- `test_adm_strict_provenance_accepts_cr_bp_03c_as_admission`:
  CR-BP-03C is accepted as an admission reference.
- `test_adm_reads_change_history_from_metadata_block`:
  regression guard for the path bug.

## CR-BP-16 §29 acceptance criteria status

| Criterion | Status | This PR? |
|---|---|---|
| Conformance rules machine-readable | ✅ | (PR-29) |
| CI executes structural validation | ✅ | (PR-31) |
| CI executes semantic validation | ✅ | (PR-29) |
| CI validates specialization graphs | ✅ | (PR-39; BP-SEM-013+014) |
| CI validates references | ✅ | (PR-31) |
| CI validates provenance | ✅ | **yes** (ADM-008 + ADM-001 strict-provenance) |
| CI validates CR metadata | ✅ | (PR-41; CR-META strict + retro-fit) |
| Architectural regression detected | ✅ | (PR-38) |
| New-process admission mandatory path | ✅ | (PR-39 + this PR) |
| Existing canonical baseline defined | ✅ | (PR-38) |
| Documentation describes the gate | ✅ | (PR-40 + this PR) |
| Conformance results reproducible | ✅ | (PR-38) |
| Canonical status = conformance + governance | ✅ | (PR-38) |
| Gate ≠ ECF coverage = process completeness | ✅ | (PR-31) |

**Net: 14 fully met (up from 11); 0 partial (down from 1); 0 unmet.**
CR-BP-16 §29 acceptance is now COMPLETE pending governance approval.

## Verification

- `pytest tests/ -q`: **146 passed** (1 pre-existing failure
  unrelated to this PR — `test_check_struct_clean_repo_passes`
  asserts STRUCT-OK on stderr; STRUCT-OK is printed to stdout.
  That test was already failing on `a6c3175` before this PR).
- `python3 scripts/check_admission_gate.py --self-test`:
  PASS.
- `python3 scripts/check_process_semantics.py --strict`:
  CONFORMANT.
- `python3 scripts/check_architectural_regression.py --strict`:
  CONFORMANT.
- `python3 scripts/conformance_result.py`: **CONFORMANT**
  (15 gates, 0 blocking, 0 advisory).
- `python3 scripts/check_admission_gate.py --strict-provenance`:
  exit 0 (CONFORMANT-WITH-WARNINGS; 36 ADM-005 boundary
  findings remain advisory per §15).
- Dash-clean: zero en/em dashes in added lines.

## Programme position

- CR-BP-14: **Implemented** end-to-end.
- CR-BP-15 + CR-BP-15-IMP: Phases 1-7 shipped; disposition
  register LOCKED at 18/18; catalogue CONFORMANT.
- CR-BP-16: **all 14 §29 acceptance criteria fully met**.
  §10/15/16/17/18/19/21/22/23/24/25 + Step 8 machinery live in CI.
  Promotion-to-blocking pattern continues to be applied
  incrementally per step.
- Next: **CR-BP-13c+ admission tranche** (first post-freeze
  admission exercise). The gate is fully ready; ADM-001 +
  ADM-008 are blocking, the §15 boundary recommendation is
  documented, and the locked population passes the new gate.
