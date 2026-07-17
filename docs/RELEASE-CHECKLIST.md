# v0.5 Release Checklist

Use this checklist for the explicitly synthetic-data `v0.5` public preview.

## Before Tagging

- [ ] `VERSION` is `0.5` and the changelog date is finalized.
- [ ] `./scripts/test-library.sh` passes from a clean checkout.
- [ ] `./scripts/build-release.sh` passes from a clean checkout.
- [ ] Both versioned archives pass `unzip -t`.
- [ ] `shasum -a 256 -c dist/SHA256SUMS` passes.
- [ ] All 41 skills, templates, and examples are present.
- [ ] Catalogs match canonical metadata.
- [ ] Synthetic forward-test findings are resolved and external field validation is labeled as a post-release evidence target.
- [ ] Source freshness and legal or regulatory caveats are reviewed.
- [ ] No confidential client or personal material is present.
- [ ] License and attribution are visible in source and packages.
- [ ] Contribution and issue governance is ready for public users.

## Draft Release

- [ ] Create tag `v0.5` only after explicit approval.
- [ ] Create a draft GitHub Release from that tag.
- [ ] Attach both versioned archives and `SHA256SUMS`.
- [ ] Use the finalized changelog entry as release notes.
- [ ] Verify the attached asset hashes.
- [ ] Review the repository as an anonymous new user.

## Publish

- [x] Obtain explicit approval to publish the synthetic-data `v0.5` preview.
- [x] Obtain explicit approval to change repository visibility.
- [ ] Publish the release and then switch visibility in the agreed sequence.
- [ ] Verify public links, installation steps, license, and archive downloads.
- [ ] Record the next source-review and field-feedback dates.
