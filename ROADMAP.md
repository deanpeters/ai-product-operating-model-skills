# AIPOM Roadmap

This file is the source of truth for phase membership, skill names, progress, and release gates.

All build phases are complete, and the synthetic-data [`v0.5` public preview](https://github.com/deanpeters/ai-product-operating-model-skills/releases/tag/v0.5) is published. Post-release evidence, interoperability, adoption, and stabilization work is tracked in [docs/POST-RELEASE-ROADMAP.md](docs/POST-RELEASE-ROADMAP.md).

## Status Vocabulary

- `planned` — named and sequenced, but not started
- `drafting` — canonical content is being developed
- `review` — content exists and is undergoing conceptual or facilitation review
- `active` — complete and validated for the current release

A skill is not `active` merely because `SKILL.md` exists. Its metadata, content, template where applicable, worked example, weak example where useful, links, and validation must pass.

## Phase 0: Repository Foundation

**Objective:** Establish the canonical contracts and tooling required to build the library coherently.

| Deliverable | Status |
|---|---|
| Root repository contract and front door | active |
| CC BY-NC-SA 4.0 license | active |
| Skill, facilitation, evidence, and operating-model standards | active |
| Canonical 35-question assessment | active |
| Evidence rubric and scoring model | active |
| Validation and link-checking scripts | active |
| Catalog generator and release tooling | active |

**Exit gate:** The repository structure, contracts, assessment, and tooling validate before Phase 1 skill generation begins.

## Phase 1: Assess and Establish the Foundation

**Objective:** Create the minimum viable assessment-to-action operating-model system.

| Category | Skill | Type | Status |
|---|---|---|---|
| Cross-category | `aipom-operating-model-assessment` | workflow | active |
| Cross-category | `aipom-operating-model-roadmap` | workflow | active |
| Strategy | `aipom-strategy-thesis-advisor` | interactive | active |
| Portfolio | `aipom-portfolio-posture-advisor` | interactive | active |
| Workflows | `aipom-workflow-opportunity-advisor` | interactive | active |
| Context | `aipom-context-readiness-advisor` | interactive | active |
| Evaluation | `aipom-evaluation-strategy-advisor` | interactive | active |
| Governance | `responsible-aipom-governance-advisor` | interactive | active |
| Capability | `aipom-capability-maturity-advisor` | interactive | active |
| Portfolio | `aipom-bet-charter` | component | active |
| Workflows | `human-aipom-work-contract` | component | active |
| Context | `aipom-context-package-builder` | component | active |
| Evaluation | `aipom-behavior-contract-builder` | component | active |
| Governance | `aipom-autonomy-boundary-designer` | component | active |
| Capability | `workflow-to-skill-converter` | component | active |

**Total:** 15 skills.

**Phase status: complete.** All 15 Phase 1 skills are active and validated as a coherent assessment-to-action loop.

**Pattern gate: complete.** The component, interactive-advisor, and workflow exemplars established the behavior and artifact patterns used by subsequent Phase 1 skills.

**Exit gate:** A leadership team can assess the operating model, identify the weakest consequential conditions, select an intervention, produce a useful artifact, assign a next action, build a roadmap, and capture effective practice for reuse.

## Phase 2: Make Core Practices Repeatable

**Objective:** Convert assessment findings into repeatable organizational practices.

| Category | Skill | Type | Status |
|---|---|---|---|
| Strategy | `aipom-opportunity-framing` | component | active |
| Strategy | `aipom-outcome-value-map` | component | active |
| Portfolio | `aipom-use-case-triage` | interactive | active |
| Portfolio | `aipom-investment-stage-gates` | component | active |
| Workflows | `aipom-productive-motion-map` | component | active |
| Workflows | `aipom-workflow-playbook-builder` | component | active |
| Context | `authoritative-source-map` | component | active |
| Context | `aipom-data-readiness-audit` | component | active |
| Governance | `aipom-accountability-charter` | component | active |
| Capability | `role-based-aipom-competency-map` | component | active |

**Total:** 10 skills.

**Phase status: complete.** All 10 Phase 2 skills are active and validated as a coherent finding-to-repeatable-practice layer.

**Exit gate:** A Phase 1 finding can be converted into a repeatable practice with evidence requirements, named ownership, decision rules, and an observable maturity move.

## Phase 3: Build Evidence and Control Systems

**Objective:** Add economic, evaluation, context-lifecycle, dependency, and incident-control infrastructure.

| Category | Skill | Type | Status |
|---|---|---|---|
| Strategy | `aipom-economic-case-builder` | component | active |
| Portfolio | `aipom-platform-dependency-audit` | component | active |
| Workflows | `aipom-decision-cycle-redesign` | workflow | active |
| Context | `aipom-context-lifecycle-designer` | component | active |
| Evaluation | `aipom-golden-dataset-builder` | component | active |
| Evaluation | `aipom-eval-scorecard-builder` | component | active |
| Governance | `aipom-risk-control-incident-playbook` | component | active |
| Cross-category | `aipom-initiative-readiness-review` | workflow | active |
| Cross-category | `aipom-operating-model-design-sprint` | workflow | active |

**Total:** 9 skills.

**Phase status: complete.** All 9 Phase 3 skills are active and validated as an integrated evidence, readiness, and control system.

**Exit gate:** An organization can evaluate an AI initiative across economics, dependencies, behavior, context, controls, accountability, and readiness without averaging away a critical gap.

## Phase 4: Scale, Assure, and Institutionalize

**Objective:** Establish recurring mechanisms for review, trust, capability, adoption, and continuous improvement.

| Category | Skill | Type | Status |
|---|---|---|---|
| Strategy | `aipom-strategy-narrative-builder` | component | active |
| Evaluation | `aipom-production-evidence-review` | workflow | active |
| Governance | `aipom-trust-assurance-pack-builder` | component | active |
| Capability | `aipom-learning-system-designer` | workflow | active |
| Capability | `aipom-adoption-impact-scorecard` | component | active |
| Cross-category | `aipom-portfolio-quarterly-review` | workflow | active |
| Cross-category | `aipom-operating-model-retrospective` | workflow | active |

**Total:** 7 skills.

**Phase status: complete.** All 7 Phase 4 skills are active and validated as the recurring assurance, learning, portfolio, and improvement layer.

**Exit gate:** The organization can repeatedly review investments, monitor production evidence, communicate trust evidence, grow role capability, measure changed outcomes, reuse effective practices, and retire performative AI activity.

## Library Totals

| Phase | Skills |
|---|---:|
| Phase 1 | 15 |
| Phase 2 | 10 |
| Phase 3 | 9 |
| Phase 4 | 7 |
| **Total** | **41** |

**Library status: complete.** All 41 planned skills across all four phases are active. Future work should improve evidence, examples, facilitation, interoperability, and field use rather than inflate the catalog.
