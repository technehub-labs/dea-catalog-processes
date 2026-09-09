# Versioning Policy

## Status: Active (CR-BP-29, 2026-09-09)

`v0.2.0` is the second tagged release of `dea-catalog-processes`,
cut at the snapshot produced by CR-BP-28 (register v4 re-derivation
against ECF v2.5.0) on 2026-09-09. The catalogue at `v0.2.0` is
functionally identical to `v0.1.0`: 196/196 records at CR-BP-16
conformance level L4; 0 findings; register audit 35 / 0 / 14. The
0.1.0 -> 0.2.0 bump is the register-version stamp (v3 -> v4 in
`l1-register.yaml` / `l1-candidate-universe.yaml`), not a content
change. Downstream consumers of the L1 register itself should pin
to `v0.2.0` for register-v4 fidelity. The catalogue content
(196 records, 35 landed L1 groups, 14 backlog-deferred cells,
dispositions 107 RETAIN / 18 RECLASSIFY / 1 MOVE) is unchanged
from `v0.1.0`.

This document is the operative versioning discipline for the
`0.x` evolution. It was originally authored by CR-BP-24 (programme
closure reconciliation, 2026-09-08) to state the deliberate-untagged
policy until Phase 20 closed. CR-BP-26 (first release cut,
2026-09-09) transitioned it to the post-release state. CR-BP-29
(second release cut, 2026-09-09) updates the bump table.

## Format

This repository follows
[Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) for
the `CHANGELOG.md` format. Versioning is SemVer once a tag is cut.

| Stage | When | Bump |
|---|---|---|
| `0.1.0` | **cut** 2026-09-09 (CR-BP-26). First release; lands the seven-domain programme + ECF v2.5.0 + Phase 20 closure. | n/a (initial) |
| `0.2.0` | **cut** 2026-09-09 (CR-BP-29). Register v3 -> v4 re-derivation against ECF v2.5.0 (CR-BP-28); content unchanged from v0.1.0; register-version stamp only. | minor (register-version stamp) |
| `0.x.y` (x >= 3) | `0.x` evolution: new admission waves, new conformance rules, documentation reconciliations | minor on a canonical admission wave or a Domain rename; patch on a documentation / governance-artifact reconciliation |
| `1.0.0` | The catalogue is stable in a stronger sense than "Phase 20 closed for one programme": the upstream ECF is also at a stable point and a sustained conformance pass is observed | major |

## What triggers a version bump

Version bumps are **release-cut events**, not per-CR events. The
CR programme may land many Change Requests between two release cuts;
the CHANGELOG `[Unreleased]` section accumulates them and the
release cut fixes the version at that snapshot.

## Pre-release history (now closed)

The repository had no git tags before `v0.1.0`. That was intentional:

1. The catalogue was at the pre-release stage: governance approval
   for the landing-programme scope was open (CR-BP-15 Phase 20).
2. Phase 20 governance approval (CR-BP-15 §22; CR-BP-16 §22) **closed
   on 2026-09-09 by CR-BP-25** (see
   `docs/governance/phase-20-review-crbp15.md`).
3. The upstream ECF vocabulary was at `v2.5.0` (`dea-metaframework`,
   the source of truth); the catalogue is now tagged to reflect that
   snapshot and the discipline of pinning to a known ECF version.

## Cutting the next tag

When the next release is due:

1. Move the `[Unreleased]` section to a dated `[vN.M.P]` section in
   `CHANGELOG.md`.
2. Update `CITATION.cff` (`version`, `date-released`, `url`).
3. Merge the carrier PR to `main`.
4. `git tag -s vN.M.P -m "vN.M.P" <merge-commit-sha>` on `main`.
5. `git push --tags` to `origin`.
6. `gh release create vN.M.P --repo technehub-labs/dea-catalog-processes
   --title "vN.M.P" --notes-file <CHANGELOG-vN.M.P-section.md>`.
