# v0.5 Release Readiness

## Current Decision

`v0.5` is approved as the first public preview using synthetic examples and synthetic forward-testing. It is suitable for public learning, evaluation, adaptation, and feedback. It is not presented as field-proven, production-certified, compliance-establishing, or evidence of demonstrated adoption or impact.

## Completed Foundations

- All 41 roadmap skills are active and validated.
- Every skill has a template, worked example, and weak example.
- Canonical assessment, evidence, facilitation, and scoring standards exist.
- Canonical and Codex-compatible packages build locally.
- Release metadata and source traceability are validated automatically.
- GitHub Actions validates and packages clean checkouts with read-only repository permissions and immutable action SHAs.
- Three guided entry paths give users a practical front door.
- A privacy-aware external field-validation kit covers all six representative skills and independent-facilitator calibration.

## Release Candidate Outputs

Running `./scripts/build-release.sh` produces:

- `dist/aipom-skills-v0.5.zip`
- `dist/aipom-codex-skills-v0.5.zip`
- Stable aliases without the version suffix
- `dist/SHA256SUMS`

These are release candidates, not published assets.

## Public Preview Status

- Source-freshness, confidentiality, license, and attribution review passed.
- Public contribution, feedback, safety, and vulnerability-reporting paths are active.
- The `v0.5` prerelease is published with verified canonical and Codex archives plus checksums.
- Repository visibility is public; Discussions, secret scanning, and push protection are enabled.

External field validation is now a post-release evidence program for `v0.6`, not a blocker for the explicitly pre-1.0 `v0.5` preview.

## Known Limitations

- Most examples are synthetic rather than field-derived.
- The canonical package is platform-neutral; only Codex packaging is currently generated as a platform-specific distribution.
- External URL availability is not checked in CI because network access is not deterministic. Source presence and traceability are checked locally.
- A complete catalog is not evidence that organizations have adopted or benefited from the practices.
- Synthetic forward-tests demonstrate internal behavioral coherence, not real session duration, human usability, adoption, decision impact, or independent facilitator repeatability.
