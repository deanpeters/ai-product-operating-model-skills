# AI Product Operating Model Skills

> **v0.5 public preview:** This library is structurally validated and synthetically forward-tested. It has not yet been validated through representative organizational field sessions, and demonstrated adoption or impact has not been established. All worked examples are synthetic. Review consequential decisions with accountable domain specialists. See [Evidence Status](docs/EVIDENCE-STATUS.md).

AI Product Operating Model Skills (AIPOM) is a platform-neutral library for assessing, designing, and improving how organizations choose, build, evaluate, govern, and learn from AI-powered products and AI-assisted product work.

The library is built for CPOs, CTOs, product and technology leaders, Product Operations, Product Managers, cross-functional delivery leaders, governance partners, consultants, trainers, and facilitators.

The goal is not more AI activity or more completed canvases. The goal is better organizational decisions and repeatable practices.

## Start Here

- [Choose a starting path](docs/STARTING-PATHS.md): assess an organization, evaluate an AI initiative, or redesign a product-team workflow.
- [Operating model](docs/OPERATING-MODEL.md): the product concept, seven categories, operating levels, and intended outcomes.
- [Roadmap](ROADMAP.md): canonical phase membership and completion status for all 41 active skills.
- [Skill specification](docs/SKILL-SPEC.md): required metadata, sections, naming, and completion rules.
- [Adaptive facilitation](docs/ADAPTIVE-FACILITATION.md): how advisors and workflows recognize context and guide decisions.
- [Evidence standard](docs/EVIDENCE-STANDARD.md): how claims, evidence, assumptions, and maturity scores are handled.
- [v0.5 release plan](docs/RELEASE-PLAN.md): private-preview readiness, field-validation, and public-release gates.
- [Public preview contract](docs/PUBLIC-PREVIEW.md): what v0.5 is ready for, what it does not claim, and how feedback will shape v0.6.
- [Contribution guide](CONTRIBUTING.md): the shortest path from an idea to a validated contribution.

Repository-wide instructions for human and AI contributors live in [AGENTS.md](AGENTS.md).

## Current State

All four build phases are complete. The library now provides 41 active, validated skills spanning assessment, action, repeatable practice, evidence, readiness, control, assurance, learning, and continuous improvement:

- Assess the operating model across 35 evidence-based questions
- Diagnose the most consequential gap in each of seven categories
- Establish foundational bets, behavior, authority, human-AI work, and context
- Sequence owned 30-, 90-, 180-, and 365-day interventions
- Convert proven workflows into reusable organizational skills
- Frame opportunities and causal value before funding AI bets
- Triage use cases and apply evidence-based investment gates
- Map, assign, document, and measure repeatable human-AI workflows
- Establish authoritative sources, data readiness, accountability, and role competencies
- Build full-cost economic cases and expose platform dependency risk
- Govern context lifecycles, evaluation sets, scorecards, and incident response
- Review initiative readiness without averaging away critical gaps
- Prototype and test bounded operating-model changes before scaling
- Review production evidence and communicate current trust assurance
- Build applied learning systems and measure adoption impact
- Reallocate the AI portfolio and improve the operating model through recurring evidence

The planned 41-skill catalog is complete. Future releases should deepen field evidence, examples, facilitation quality, interoperability, and measured reuse rather than add skills for catalog size.

`v0.5` is the first public preview. Its release basis is complete structural validation, synthetic forward-testing, explicit evidence limitations, and public feedback infrastructure—not a claim of field-proven effectiveness. See [release readiness](docs/RELEASE-READINESS.md) and the [release checklist](docs/RELEASE-CHECKLIST.md).

The first synthetic forward-test and facilitation-hardening cycle is complete across six representative skills. See the [v0.5 forward-test report](docs/validation/v0.5-forward-test-report.md). The [validation hub](docs/validation/README.md) contains the external pilot plan, participant brief, facilitator runbook, capture form, calibration scenarios, and findings register. External human validation and public-use feedback will build the evidence base for `v0.6`.

## Three Starting Paths

You do not need to read all 41 skills before doing useful work:

1. [Assess an organization](commands/aipom-assess-organization.md) to produce an evidence-based maturity profile and owned operating-model roadmap.
2. [Evaluate an AI initiative](commands/aipom-evaluate-initiative.md) to reach a proceed, constrain, remediate, pause, or stop decision.
3. [Redesign a product-team workflow](commands/aipom-redesign-workflow.md) to test a responsible human-AI decision cycle before standardizing it.

Canonical packages preserve the full AIPOM organizational metadata. The release build also generates Codex-compatible packages with platform-specific metadata and bundled references.

No skill is counted as complete until its content, metadata, templates, examples, links, and validation pass. See [ROADMAP.md](ROADMAP.md) for live status.

## The Seven Categories

1. **Strategy and Economic Outcomes** — where AI creates value and which outcomes should change.
2. **Portfolio and Investment Choices** — which opportunities to explore, fund, scale, pause, pivot, or retire.
3. **Product-Team Workflows** — how decisions, evidence, context, collaboration, and human-AI responsibilities should work.
4. **Context, Knowledge, and Data** — which sources and data can be trusted, used, refreshed, retained, or excluded.
5. **Evaluation and Evidence** — acceptable behavior, representative evaluations, monitoring, and evidence-based decisions.
6. **Governance and Accountability** — ownership, autonomy boundaries, controls, escalation, incident response, and trust evidence.
7. **Capability, Adoption, and Reuse** — role capability, applied learning, stewardship, reuse, adoption, and continuous improvement.

These categories are connected. They are not seven organizational terrariums.

## Operating Levels

| Level | Focus |
|---|---|
| Organization | Enterprise strategy, governance, capability, and operating systems |
| Portfolio | Investment allocation, dependencies, evidence, and coherence across initiatives |
| Product team | Repeatable workflows, decision rights, context, and collaboration |
| Initiative | Readiness, economics, evidence, controls, and accountability for one AI bet |

An initiative canvas is not an enterprise operating model. An organizational policy is not proof that product teams use it.

## Skill Types

- **Component:** a focused method that produces one primary operating artifact, usually in 30–90 minutes.
- **Interactive advisor:** an adaptive diagnostic that interprets supplied context and recommends an appropriate next move.
- **Workflow:** an end-to-end process that coordinates several advisors and components while preserving evidence, assumptions, decisions, ownership, and unresolved questions.

Every skill is both functional and pedagogic: it helps complete organizational work and teaches the reasoning, tradeoffs, evidence, and failure modes behind that work.

## Evidence Before Maturity

AIPOM distinguishes four claims:

1. A practice is discussed.
2. A practice is documented.
3. A practice is consistently used.
4. A practice demonstrably improves decisions or outcomes.

A policy, workshop, license, training course, or generated artifact is not proof of organizational maturity by itself. If evidence is absent, a maturity score cannot exceed `2 — Emerging`.

The default maturity scale is:

| Score | Label | Meaning |
|---:|---|---|
| 1 | Absent | No consistent practice or accountable ownership |
| 2 | Emerging | Isolated experiments, individuals, or informal practices |
| 3 | Repeatable | The practice works in some teams and can be reproduced |
| 4 | Operationalized | The practice is standardized, governed, and used across the organization |
| 5 | Compounding | The practice is measured, improved, reused, and demonstrably strengthens outcomes |

See [assessments/scoring-model.md](assessments/scoring-model.md) for the complete rules.

## Repository Structure

```text
.
├── AGENTS.md
├── README.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── VERSION
├── CITATION.cff
├── SECURITY.md
├── LICENSE
├── assessments/       # Canonical questions, evidence rubric, and scoring
├── catalog/           # Generated navigation; do not edit directly
├── commands/          # Workflow entry points
├── docs/              # Canonical shared standards
├── scripts/           # Validation, generation, testing, and packaging
├── skills/            # Canonical skill content
└── dist/              # Generated release artifacts
```

## Development

Install the one development dependency:

```bash
python3 -m pip install -r requirements-dev.txt
```

Run the full verification suite:

```bash
./scripts/test-library.sh
```

Regenerate catalogs after changing canonical skill metadata:

```bash
python3 scripts/generate-catalog.py
```

Build a release after validation succeeds:

```bash
./scripts/build-release.sh
```

The build produces:

- `dist/aipom-skills-v0.5.zip`, the versioned canonical platform-neutral library
- `dist/aipom-codex-skills-v0.5.zip`, the versioned Codex-compatible skill packages
- Stable aliases without version suffixes for local consumers
- `dist/SHA256SUMS`, checksums for the versioned release archives

Generated catalog and distribution files must not be edited directly.

## Scope Boundaries

AIPOM is not a prompt library, vendor comparison, AI tool tutorial, machine-learning engineering handbook, generic Product Manager toolkit, legal opinion, or collection of maturity charts without interventions.

The library should use credible foundational methods from existing Product Manager and organizational-toolkit libraries rather than recreate weaker copies with “AI” added to their names.

Examples must be public, appropriately licensed, anonymized, or clearly labeled as synthetic. Productside client-confidential material does not belong here.

## License

This work is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/). See [LICENSE](LICENSE) for the legal code.
