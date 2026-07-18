---
name: aipom-evaluation-strategy-advisor
description: Recommend the product, model, workflow, human, and production evaluations needed for an AI decision, based on behavior, consequences, evidence gaps, and lifecycle stage.
type: interactive
category: evaluation-and-evidence
phase: 1
status: active
operating_level: [product-team, initiative]
audience: [CTO, Product Operations, Product Manager, Team Lead, Design, Engineering, Data, Research, AI Governance]
best_for: [Designing evaluation before launch, Fixing metric-heavy but decision-light testing, Choosing the next evidence investment]
evidence_required: [Product decision and behavior contract, Users and failure consequences, Existing evaluation results, Production and workflow evidence]
produces: [Evaluation strategy, Coverage and evidence gaps, Decision rules and ownership]
assessment_questions: [EVAL-01, EVAL-02, EVAL-03, EVAL-04, EVAL-05]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 45-75 min
group_size: 3-8
depends_on: [aipom-behavior-contract-builder]
combine_with: [aipom-golden-dataset-builder, aipom-eval-scorecard-builder, aipom-production-evidence-review]
sources:
  - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
---

# AIPOM Evaluation Strategy Advisor

## What Is It

Choose the evaluations needed to make a specific AI product decision. Connect behavior and consequence to product, model, workflow, human, and production evidence rather than defaulting to one benchmark.

## Why Use It

A model metric can improve while the product decision, workflow, or user outcome gets worse. This advisor makes evaluation coverage and decision rules explicit across the system lifecycle.

## When to Use It

Use before major build, launch, expanded autonomy, production review, or after behavior changes and incidents.

## What It Produces

- Decision-centered evaluation strategy
- Coverage across behavior, users, workflows, and lifecycle
- Measures, judges, sampling, thresholds, and limitations
- Owners and ship/continue/pause/rollback rules

## Who Should Participate

Include the Product Manager, evaluation and technical owners, design or research, operators, affected-user representatives, and governance specialists as consequences require.

## Evidence to Bring

Bring the behavior contract, intended-use evidence, real cases, baselines, failures, workflow measures, model results, complaints, monitoring, and current decisions.

## How to Do It

1. Define the decision evaluation must enable.
2. Extract users, behaviors, consequences, lifecycle stage, and existing evidence.
3. Map evidence needs across product outcome, system behavior, workflow, human review, and production.
4. Identify representative normal, edge, subgroup, adversarial, and severe-failure coverage.
5. Choose quantitative and qualitative measures, judges, calibration, sampling, and cadence.
6. Set thresholds and critical-failure overrides tied to decisions.
7. Name owners, uncertainty, monitoring, and the next evidence gap.

## Facilitation Protocol

Support guided, context-dump, and best-guess modes. Ask about the decision before the metric. Present numbered evaluation strategies with coverage and tradeoffs. In best-guess mode label unverified thresholds.

## Decision Logic

- Prioritize product evaluation when user and outcome value are uncertain.
- Prioritize behavior evaluation when acceptable output and failure boundaries are unclear.
- Prioritize workflow/human evaluation when review quality, burden, or authority is uncertain.
- Prioritize production evaluation when drift, scale, or real-world interaction dominates.
- Require layered evaluation for consequential systems; no average offsets a critical failure.

## Completion Criteria

Finish with the decision, evaluation layers, cases, measures, thresholds, owners, gaps, critical overrides, and next evidence action.

## Key Concepts

- Evaluation exists to change a decision.
- Representative coverage matters more than convenient volume.
- Human judges require calibration and limitations.
- Production evidence complements rather than replaces pre-launch evaluation.

## Organizational Applications

Use for generated content, recommendations, classifiers, assistants, agents, and AI-assisted internal workflows.

## Common Pitfalls

- Beginning with available metrics
- Using vendor benchmarks as product evidence
- Omitting humans and workflows
- Testing only average cases
- Setting thresholds without consequences or owners
- Monitoring without a decision rule

## Combine With

Use the behavior contract as input, then build representative datasets and scorecards; use production review after launch.

## Assets and Templates

- [Evaluation strategy template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

- NIST, [AI Risk Management Framework 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10), January 26, 2023. Supports mapped, measured, managed, and governed AI risk across the lifecycle. Accessed July 16, 2026.
