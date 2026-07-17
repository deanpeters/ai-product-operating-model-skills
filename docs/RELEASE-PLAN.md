# AIPOM v0.5 Release Plan

The 41-skill build roadmap is complete. This plan governs the first public preview release, `v0.5`, and the evidence-building path that follows it.

`v0.5` is explicitly a synthetic-data public preview. External human field validation is not a release blocker for this pre-1.0 version; it becomes a primary input to `v0.6`. The release must state that boundary prominently and must not claim field-proven effectiveness, adoption, impact, or compliance.

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

**Status: complete for the v0.5 synthetic-preview gate; external evidence program moves to v0.6**

Test six representative skills across executive or portfolio leaders, product teams, and governance partners:

- `aipom-operating-model-assessment`
- `aipom-strategy-thesis-advisor`
- `aipom-use-case-triage`
- `aipom-autonomy-boundary-designer`
- `aipom-initiative-readiness-review`
- `aipom-portfolio-quarterly-review`

Capture time, unnecessary questions, missing context, terminology friction, artifact usefulness, decisions changed, facilitation failures, and whether another facilitator can repeat the method.

The first isolated synthetic cycle exercised all six representative skills across executive, product-team, governance, and portfolio scenarios. Findings and changes are recorded in the [v0.5 forward-test report](validation/v0.5-forward-test-report.md).

The [external validation hub](validation/README.md) is ready for three human pilots covering leadership and portfolio, product and initiative, and governance and operations. Those sessions, independent-facilitator calibrations, and public-use feedback will inform `v0.6`.

**v0.5 gate:** All six representative skills pass isolated synthetic scenarios; findings are incorporated; evidence limitations are public; and feedback mechanisms are ready.

**v0.6 evidence target:** Representative users complete useful work, independent facilitators reproduce consequential decisions, and permitted findings are incorporated.

## Stage 4: Example and Facilitation Hardening

**Status: complete for v0.5 synthetic evidence; field-derived hardening moves to v0.6**

- Convert permitted field findings into anonymized examples
- Add edge cases for disagreement, partial evidence, and interrupted workflows
- Tighten questions, decision logic, templates, and handoffs
- Record which skills demonstrably changed decisions
- Re-run the full release suite

**v0.5 gate:** Priority synthetic findings are resolved, representative examples teach the reasoning path, and the full release suite passes.

**v0.6 evidence target:** Priority field and public-use findings are resolved without introducing confidential content or unsupported maturity claims.

## Stage 5: Public Release Preparation

**Status: in progress**

- Final confidentiality, license, attribution, and source-freshness review
- Public contribution and issue governance
- Release notes and packaged assets
- `v0.5` tag and draft GitHub Release
- Final private-repository review
- Repository visibility change only after explicit approval

**Gate:** The draft release contains verified assets and documentation, and the repository is safe and understandable for public use.

## Stop Rule

The next work should improve evidence, examples, usability, interoperability, and measured reuse. Do not create additional skills merely to increase the catalog beyond 41.
