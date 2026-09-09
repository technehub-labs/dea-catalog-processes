# Versioning Policy

## Status: Draft (CR-BP-24)

The catalog is **pre-1.0** and **untagged by deliberate decision** until the
Phase 20 governance approval gate of CR-BP-15 closes. CR-BP-24 introduces
this document so the `CHANGELOG.md` reference resolves and the versioning
discipline is stated before the first cut.

## Format

This repository follows
[Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) for the
`CHANGELOG.md` format. Versioning is SemVer once a tag is cut:

| Stage | When | Bump |
|---|---|---|
| `0.x.y` | Pre-release; landing series in flight | minor on tranche closure; patch on documentation-only fix |
| `1.0.0` | Phase 20 governance approval closes CR-BP-15 | major |
| `1.x.y` | Post-1.0 catalogue evolution | minor on a canonical admission wave; major on a Domain rename; patch on a documentation / governance-artifact reconciliation |

## What triggers a version bump

Version bumps are **release-cut events**, not per-CR events. The CR
programme may land many Change Requests between two release cuts; the
CHANGELOG `[Unreleased]` section accumulates them and the release cut
fixes the version at that snapshot. The first release cut is the
event that closes CR-BP-15 Phase 20.

## Why no tag today

The repository has no git tags as of 2026-09-08. That is intentional:

1. The catalogue is at the `0.x` stage. A `0.x` tag would advertise a
   release-grade artifact and the catalogue is explicitly an
   architecture-inception product (see `README.md` Current Status).
2. Phase 20 governance approval (CR-BP-15 §22; CR-BP-16 §22) is a
   human decision gate. Cutting a tag before that gate closes would
   publish a version whose canonical status has not been governance-
   approved.
3. The ECF Domain enum is at v2.5.0 in the `dea-metaframework` repo
   (the source of truth). The Process Catalog carries the same
   vocabulary and should not be tagged independently of upstream.

## Cutting the first tag

When Phase 20 closes:

1. Update `CHANGELOG.md` to move the `[Unreleased]` section to a
   dated `v0.1.0` section.
2. Cut the tag with `git tag -s v0.1.0 -m "v0.1.0" <sha>` and
   `git push --tags`.
3. Open a `gh release create v0.1.0` using the CHANGELOG section as
   the release notes.

This is a release-cut event, not a per-CR event. The release-cut CR
itself is **not** within the scope of CR-BP-24; that is its own
deliberate act after Phase 20 closes.
