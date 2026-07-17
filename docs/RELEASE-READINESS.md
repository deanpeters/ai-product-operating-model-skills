# v0.5 Release Readiness

## Current Decision

`v0.5` is the target first public preview. The repository remains private and no release tag exists yet.

## Completed Foundations

- All 41 roadmap skills are active and validated.
- Every skill has a template, worked example, and weak example.
- Canonical assessment, evidence, facilitation, and scoring standards exist.
- Canonical and Codex-compatible packages build locally.
- Release metadata and source traceability are validated automatically.
- GitHub Actions validates and packages clean checkouts with read-only repository permissions and immutable action SHAs.
- Three guided entry paths give users a practical front door.

## Release Candidate Outputs

Running `./scripts/build-release.sh` produces:

- `dist/aipom-skills-v0.5.zip`
- `dist/aipom-codex-skills-v0.5.zip`
- Stable aliases without the version suffix
- `dist/SHA256SUMS`

These are release candidates, not published assets.

## Remaining Gates

- Representative field validation
- Findings incorporated into priority skills and examples
- Final source-freshness, confidentiality, license, and attribution review
- Public contribution and issue governance
- Draft GitHub Release review
- Explicit approval to create the tag and change repository visibility

## Known Limitations

- Most examples are synthetic rather than field-derived.
- The canonical package is platform-neutral; only Codex packaging is currently generated as a platform-specific distribution.
- External URL availability is not checked in CI because network access is not deterministic. Source presence and traceability are checked locally.
- A complete catalog is not evidence that organizations have adopted or benefited from the practices.
