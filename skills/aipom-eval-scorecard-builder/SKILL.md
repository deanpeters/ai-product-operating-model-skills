---
name: aipom-eval-scorecard-builder
description: Define calibrated AI evaluation metrics, rubrics, judges, thresholds, sampling, uncertainty, ownership, and decision rules tied to behavior and consequences.
type: component
category: evaluation-and-evidence
phase: 3
status: active
operating_level: [product-team, initiative]
audience: [Product Manager, Research, Data, Engineering, Domain Experts, AI Governance]
best_for: [Turning a behavior contract into repeatable evaluation, Calibrating human or automated judges, Making launch and rollback thresholds explicit]
evidence_required: [Behavior contract and evaluation strategy, Governed representative cases, Failure consequences and baselines, Judge calibration evidence]
produces: [Evaluation scorecard, Calibration and sampling plan, Decision threshold and exception rules]
assessment_questions: [EVAL-01, EVAL-02, EVAL-03, EVAL-04, EVAL-05]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 60-120 min
group_size: 4-10
depends_on: [aipom-behavior-contract-builder, aipom-golden-dataset-builder]
combine_with: [aipom-evaluation-strategy-advisor, aipom-production-evidence-review, aipom-risk-control-incident-playbook]
sources: [https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence]
---

# AIPOM Eval Scorecard Builder

## What Is It

Define how AI behavior will be measured and converted into product decisions: metrics, rubrics, judges, calibration, thresholds, sampling, uncertainty, subgroup views, critical failures, ownership, and action rules.

## Why Use It

Metric collections fail when they lack representative cases, calibrated judgment, consequences, or decision thresholds. A scorecard makes clear what a passing score permits—and what a critical failure blocks regardless of averages.

## When to Use It

Use after behavior and representative cases are defined, before validation, launch, scale, or recurring production review. Recalibrate when behavior, population, context, judges, or consequences change.

## What It Produces

- Metric and rubric definitions
- Judge, calibration, sampling, and uncertainty plan
- Thresholds, critical-failure rules, and subgroup views
- Continue, revise, constrain, rollback, or stop decision rules

## Who Should Participate

Include product and evaluation owners, domain experts, data and engineering, affected-user perspectives, and governance partners where consequences are material.

## Evidence to Bring

Bring behavior contracts, evaluation strategy, governed cases, baselines, incidents, consequences, subgroup needs, reviewer guidance, judge comparisons, and candidate thresholds.

## How to Do It

1. Define the product decision and behavior dimensions being evaluated.
2. Select metrics and rubrics that distinguish quality, safety, workflow, human, and outcome evidence.
3. Define unit, denominator, direction, aggregation, subgroup, and uncertainty for every measure.
4. Choose human, automated, model-based, or hybrid judges according to consequence and explainability needs.
5. Calibrate judges against qualified reference decisions and measure disagreement.
6. Define sampling across representative, edge, adversarial, subgroup, and production cases.
7. Set evidence-based thresholds and non-compensable critical failures.
8. Map results to continue, revise, constrain, rollback, or stop actions.
9. Assign measurement, review, decision, exception, and recalibration ownership.

## Key Concepts

- A metric without a decision rule is observation, not governance.
- Aggregate performance can hide subgroup or critical failures.
- Model judges require calibration and monitoring.
- Thresholds express consequence and tolerance, not universal truth.

## Organizational Applications

Use for pre-release evaluation, regression tests, vendor comparison, human-review quality, workflow adoption, production monitoring, and rollback decisions.

## Common Pitfalls

- Choosing metrics because tools expose them
- Using averages to hide critical failures
- Treating model judges as objective
- Setting thresholds after seeing desired results
- Omitting sampling and uncertainty
- Assigning measurement without decision authority

## Combine With

Use `aipom-evaluation-strategy-advisor` for coverage, `aipom-production-evidence-review` for recurring decisions, and `aipom-risk-control-incident-playbook` for threshold-triggered response.

## Assets and Templates

- [Eval scorecard template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

- NIST, [Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile, NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence), July 26, 2024, updated April 8, 2026. Supports documented measurement, representative evaluation, monitoring, and risk-based decision practices. Accessed July 17, 2026.
