# v0.5 Release Checklist

> **Historical launch record:** Every gate below was completed for the published `v0.5` snapshot. Use [HANDOFF.md](HANDOFF.md) and [POST-RELEASE-ROADMAP.md](POST-RELEASE-ROADMAP.md) for current work.

Use this checklist for the explicitly synthetic-data `v0.5` public preview.

## Before Tagging

- [x] `VERSION` is `0.5` and the changelog date is finalized.
- [x] `./scripts/test-library.sh` passes from a clean checkout.
- [x] `./scripts/build-release.sh` passes from a clean checkout.
- [x] Both versioned archives pass `unzip -t`.
- [x] `shasum -a 256 -c dist/SHA256SUMS` passes.
- [x] All 41 skills, templates, and examples are present.
- [x] Catalogs match canonical metadata.
- [x] Synthetic forward-test findings are resolved and external field validation is labeled as a post-release evidence target.
- [x] Source freshness and legal or regulatory caveats are reviewed.
- [x] No confidential client or personal content is present; all historical Dean author and committer records use the approved AIPOM routing alias.
- [x] License and attribution are visible in source and packages.
- [x] Contribution and issue governance is ready for public users.

## Draft Release

- [x] Create tag `v0.5` only after explicit approval.
- [x] Create a draft GitHub Release from that tag.
- [x] Attach both versioned archives and `SHA256SUMS`.
- [x] Use the finalized changelog entry as release notes.
- [x] Verify the attached asset hashes.
- [x] Review the repository as an anonymous new user.

## Publish

- [x] Obtain explicit approval to publish the synthetic-data `v0.5` preview.
- [x] Obtain explicit approval to change repository visibility.
- [x] Publish the release and then switch visibility in the agreed sequence.
- [x] Verify public links, installation steps, license, and archive downloads.
- [x] Record the active post-release feedback and evidence roadmap.
