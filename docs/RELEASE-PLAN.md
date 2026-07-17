# AIPOM v0.5 Release Plan

The 41-skill build roadmap is complete. This plan governs the path from complete private repository to the first public preview release, `v0.5`.

Do not create the `v0.5` tag, publish a GitHub Release, or make the repository public until the field-validation and public-release gates are complete.

## Stage 1: Release Readiness

**Status: complete**

- Version contract and changelog
- Automated validation and packaging in GitHub Actions
- Versioned canonical and Codex archives
- Stable archive aliases and SHA-256 checksums
- Release metadata, completeness, and source-traceability checks
- Clean-clone validation path
- Release checklist and readiness record

**Gate:** A clean checkout can validate and build the same release candidate without local context.

## Stage 2: Entry Paths

**Status: complete**

- Assess an organization
- Evaluate an AI initiative
- Redesign a product-team workflow
- Context-led routing and handoff rules
- Beginner-readable starting-point documentation

**Gate:** A new user can select a path, invoke the right skills, preserve context, and reach a useful decision without reading all 41 skills first.

## Stage 3: Representative Field Validation

**Status: synthetic forward-testing complete; external field validation pending**

Test six representative skills across executive or portfolio leaders, product teams, and governance partners:

- `aipom-operating-model-assessment`
- `aipom-strategy-thesis-advisor`
- `aipom-use-case-triage`
- `aipom-autonomy-boundary-designer`
- `aipom-initiative-readiness-review`
- `aipom-portfolio-quarterly-review`

Capture time, unnecessary questions, missing context, terminology friction, artifact usefulness, decisions changed, facilitation failures, and whether another facilitator can repeat the method.

The first isolated synthetic cycle exercised all six representative skills across executive, product-team, governance, and portfolio scenarios. Findings and changes are recorded in the [v0.5 forward-test report](validation/v0.5-forward-test-report.md). This does not close the external field-evidence gate.

**Gate:** Representative users complete useful work and the resulting evidence has been incorporated into the library.

## Stage 4: Example and Facilitation Hardening

**Status: initial synthetic hardening complete; field-derived hardening pending**

- Convert permitted field findings into anonymized examples
- Add edge cases for disagreement, partial evidence, and interrupted workflows
- Tighten questions, decision logic, templates, and handoffs
- Record which skills demonstrably changed decisions
- Re-run the full release suite

**Gate:** Priority field issues are resolved without introducing client-confidential content or unsupported maturity claims.

## Stage 5: Public Release Preparation

**Status: planned**

- Final confidentiality, license, attribution, and source-freshness review
- Public contribution and issue governance
- Release notes and packaged assets
- `v0.5` tag and draft GitHub Release
- Final private-repository review
- Repository visibility change only after explicit approval

**Gate:** The draft release contains verified assets and documentation, and the repository is safe and understandable for public use.

## Stop Rule

The next work should improve evidence, examples, usability, interoperability, and measured reuse. Do not create additional skills merely to increase the catalog beyond 41.
