# CR-BP-16 §16 enforcement promotion (CR-META strict mode + 5 CRs retro-fitted)

## Summary

The CR-META-001..006 gate is now **blocking** in CI for new and
modified CRs (mtime >= 2026-09-06 cutoff). Legacy CRs (mtime
< cutoff) remain advisory. Five CRs were retro-fitted to the
§21 metadata format: CR-BP-03C, CR-BP-12, CR-BP-14, CR-BP-15,
and CR-BP-16. CR-BP-13A was already §21-compliant and serves
as the canonical reference. CR-BP-16 §29 acceptance criteria
now: **11 fully met (up from 10)**, 1 partial, 0 unmet.

## What this PR does
### `scripts/check_cr_metadata.py` (extended)

- New `--cutoff-date` flag (default 2026-09-06 = CR-BP-16
  acceptance). CRs last modified on or after the cutoff are
  classified as "new"; CRs modified earlier are "legacy".
- New `--strict` mode: blocks the gate when any NEW CR fails
  any rule. Legacy CRs are reported as advisory and do not
  block.
- **CR-META-001 normalisation**: `Proposed (2026-09-03)` is
  accepted as a valid `Proposed` Status (parens stripped).
- **CR-META-002 normalisation**: `L1 (Process Catalog)` is
  accepted as a valid `L1` Layer (parens stripped).
- **Filename pattern** extended to admit `CR-BP-NN` with
  uppercase letter suffix (legacy `CR-BP-03C`).
- **Metadata line pattern** admits both `**Key**: value`
  (canonical) and `**Key:** value` (legacy / GitHub-issues).
- **JSON output** includes `new_findings` + `legacy_findings`
  arrays + `cutoff_date`.
- **Cutoff probe uses `git log -1 --format=%ct`** instead of
  filesystem mtime (fresh-clone reproducer pitfall; filesystem
  mtime is reset on every `git checkout`).
- Self-test extended with cutoff-aware good and bad fixtures.

### CR retro-fits

- `change-requests/CR-BP-03C-sample-process-contribution.md`:
  added `**Layer**: L1` + `**Owner**: TechNeHub Labs`.
- `change-requests/CR-BP-12-process-group-profile.md`:
  bolded existing metadata + added Layer/Owner.
- `change-requests/CR-BP-14-process-semantic-reconciliation.md`:
  added full §21 metadata block (Status, Layer, Owner, Type,
  Scope, Depends On).
- `change-requests/CR-BP-15-process-catalog-reconciliation.md`:
  added full §21 metadata block.
- `change-requests/CR-BP-16-process-catalog-conformance-gate.md`:
  added §21 metadata for both CR-BP-16 and CR-BP-15-IMP
  blocks.

### Infrastructure

- `reconciliation/baseline/v1.yaml`: refreshed SHA-256 for
  the 3 CRs whose content changed.
- `reconciliation/inventory.yaml`: regenerated to reflect
  the touched CRs.
- `.github/workflows/ci.yml`: CR-META step now runs
  `python scripts/check_cr_metadata.py --strict`.
- `docs/conformance-pipeline.md`: new "CR Validation (Step 9)
  cutoff policy" subsection documents the policy.
- `tests/test_cr_bp16_gates.py` (extended, 5 new tests):
  - `test_cr_meta_strict_passes_when_no_new_failures`
  - `test_cr_meta_strict_fails_on_new_bad_fixture`
  - `test_cr_meta_strict_passes_on_legacy_bad_fixture`
  - `test_cr_meta_accepts_layer_with_parenthetical_qualifier`
  - `test_cr_meta_accepts_status_with_date_qualifier`

## Acceptance criteria

CR-BP-16 §29 acceptance criteria: **11 fully met** (up from 10);
1 partial (provenance schema validation); 0 unmet.

## Verification

- `pytest tests/ -q`: **142 passed**.
- BP-SEM `--strict`: CONFORMANT.
- BP-AR `--strict`: CONFORMANT.
- Conformance Result on the branch: **CONFORMANT** (15 gates,
  0 blocking, 0 advisory).
- CR-META on the branch: ADVISORY-LEGACY (24 legacy findings,
  0 new findings); --strict returns 0.
- Fresh-clone regenerator repro: PASSES.
- Dash-clean on added non-CR content.

## Programme position

- CR-BP-14: **Implemented** end-to-end.
- CR-BP-15 + CR-BP-15-IMP: **Phases 1-7 shipped**; register
  LOCKED at 18/18; catalogue CONFORMANT.
- CR-BP-16: §10/15/16/17/18/19/21/22/23/24/25 machinery live
  in CI. **§16 enforcement promoted from advisory to blocking**
  (with cutoff grandfathering) as of this PR. **11 of 14 §29
  acceptance criteria fully met**; 1 partial; 0 unmet.
- Next: **CR-BP-13c+ admission tranche** (first post-freeze
  admission exercise): the gate machinery is fully ready.
  Awaiting user direction.
