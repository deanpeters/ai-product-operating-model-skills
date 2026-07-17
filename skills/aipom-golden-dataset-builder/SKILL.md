---
name: aipom-golden-dataset-builder
description: Build a governed, representative AI evaluation set with provenance, expected behavior, edge cases, affected groups, adjudication, versioning, and limits.
type: component
category: evaluation-and-evidence
phase: 3
status: active
operating_level: [product-team, initiative]
audience: [Product Manager, Team Lead, Research, Data, Engineering, Domain Experts, Privacy, AI Governance]
best_for: [Creating repeatable pre-release evaluation, Improving unrepresentative test cases, Governing expected answers and expert disagreement]
evidence_required: [Behavior contract and real-use evidence, Data readiness and provenance, Failure incidents and affected perspectives, Expert adjudication capacity]
produces: [Versioned evaluation set, Coverage and provenance record, Adjudication and maintenance rules]
assessment_questions: [EVAL-02, EVAL-03, EVAL-04, CTX-03]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 90-180 min plus maintenance
group_size: 4-10
depends_on: [aipom-behavior-contract-builder, aipom-data-readiness-audit]
combine_with: [aipom-eval-scorecard-builder, aipom-evaluation-strategy-advisor, aipom-production-evidence-review]
sources: [https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence]
---

# AIPOM Golden Dataset Builder

## What Is It

Build a governed set of representative evaluation cases with inputs, context, expected behavior, acceptable variation, prohibited outcomes, provenance, coverage, adjudication, and lifecycle rules. “Golden” means reviewed reference evidence, not infallible truth.

## Why Use It

Convenient happy-path examples create stable scores and false confidence. A useful set represents real use, edge cases, affected groups, adversarial conditions, uncertainty, and consequential failure modes.

## When to Use It

Use after defining behavior and data readiness, before repeatable evaluation or launch decisions. Use production evidence to revise the set without contaminating protected holdouts.

## What It Produces

- Versioned case set and case schema
- Provenance, permission, coverage, and limitation record
- Expected behavior, acceptable variation, and prohibited outcomes
- Adjudication, access, holdout, refresh, and retirement rules

## Who Should Participate

Include product, evaluation and data specialists, domain experts, affected-user representation, engineering, and privacy or governance partners proportionate to the data and consequences.

## Evidence to Bring

Bring behavior contracts, real-use samples, incidents, edge and adversarial cases, affected-group evidence, source lineage, permissions, evaluation goals, expert guidance, and known disagreements.

## How to Do It

1. Define the decision, behavior, population, environment, and consequence the set evaluates.
2. Create a case schema for input, context, provenance, expected behavior, acceptable variation, prohibited outcomes, rationale, and tags.
3. Sample representative normal use and deliberately add edge, subgroup, adversarial, ambiguous, and failure cases.
4. Verify provenance, permission, privacy, security, and intended-use boundaries.
5. Have qualified reviewers independently label or rubric cases and preserve meaningful disagreement.
6. Adjudicate only where a reference judgment is defensible; mark ambiguous cases explicitly.
7. Analyze coverage and missingness rather than relying on case count.
8. Separate development, calibration, and protected holdout use.
9. Version changes, prevent leakage, and define refresh, challenge, and retirement triggers.

## Key Concepts

- Representative does not mean statistically large by itself.
- Expert disagreement may be part of the expected behavior.
- A holdout loses value when repeatedly optimized against.
- Dataset quality includes governance and lifecycle, not just labels.

## Organizational Applications

Use for retrieval, classification, summarization, recommendation, decision support, agents, safety testing, and workflow evaluation.

## Common Pitfalls

- Calling historical outputs ground truth
- Sampling only easy or successful cases
- Omitting affected groups and real failure modes
- Forcing consensus on ambiguous judgments
- Reusing a holdout for iteration
- Updating cases without version and decision history

## Combine With

Use `aipom-eval-scorecard-builder` for scoring and decision rules, `aipom-evaluation-strategy-advisor` for coverage, and `aipom-production-evidence-review` to add emerging cases responsibly.

## Assets and Templates

- [Evaluation-set template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

- NIST, [Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile, NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence), July 26, 2024, updated April 8, 2026. Supports representative testing, provenance, measurement, and lifecycle risk practices. Accessed July 17, 2026.
