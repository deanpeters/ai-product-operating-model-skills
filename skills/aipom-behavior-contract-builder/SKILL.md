---
name: aipom-behavior-contract-builder
description: Define expected, acceptable, and prohibited AI behavior with representative cases, thresholds, escalation, and consequences. Use before evaluation, launch, or autonomy decisions.
type: component
category: evaluation-and-evidence
phase: 1
status: active
operating_level: [product-team, initiative]
audience: [Product Operations, Product Manager, Team Lead, Design, Engineering, Data, Research, AI Governance]
best_for:
  - Defining acceptable behavior before evaluation or launch
  - Resolving disagreement about what good enough means
  - Establishing limits before granting AI authority
evidence_required:
  - Intended users, use cases, and affected people
  - Product outcomes and known failure consequences
  - Representative examples and constraints
  - Existing evaluation evidence where available
produces:
  - AI behavior contract
  - Representative behavior cases
  - Escalation and decision thresholds
assessment_questions: [EVAL-01, EVAL-02, EVAL-03, GOV-02]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 45-75 min
group_size: 3-8
depends_on: []
combine_with: [aipom-autonomy-boundary-designer, aipom-golden-dataset-builder, aipom-eval-scorecard-builder]
sources:
  - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
---

# AIPOM Behavior Contract Builder

## What Is It

Define how an AI product should behave, the range of acceptable variation, what it must refuse or escalate, and what happens when behavior falls outside the contract. The contract connects product intent to evaluation and operating decisions.

## Why Use It

Teams cannot evaluate “helpful,” “safe,” or “accurate” consistently without observable expectations and consequences. A contract makes disagreement inspectable before it becomes a launch dispute or incident. Writing it does not prove conformance; representative evaluations and production evidence do.

## When to Use It

Use before building an evaluation set, setting autonomy boundaries, launching a probabilistic feature, or revising behavior after incidents or user evidence. It is not a legal compliance determination or a substitute for specialist review.

## What It Produces

- Purpose and scope
- Expected, acceptable, escalated, and prohibited behaviors
- Representative normal, edge, adversarial, and failure cases
- Thresholds tied to ship, continue, pause, rollback, or retire decisions
- Owners, evidence gaps, and review triggers

## Who Should Participate

Include the Product Manager, technical and evaluation owners, design or research, workflow operators, and the person accountable for affected outcomes. Add legal, privacy, security, safety, accessibility, or domain specialists in proportion to consequences.

## Evidence to Bring

Bring user research, intended-use statements, real inputs, known failures, policies, evaluation results, complaints, incidents, and affected-user perspectives. Label hypothetical cases and unsupported thresholds as assumptions.

## How to Do It

1. **Set scope.** Name the system version, users, affected people, contexts, and decision the contract must support.
2. **Define purpose.** State the user outcome and boundaries; avoid capability marketing.
3. **Describe behaviors.** Use observable input-condition-output-consequence statements.
4. **Classify behavior.** Mark each as expected, acceptable variation, escalate/refuse, or prohibited.
5. **Add cases.** Cover frequent use, difficult ambiguity, affected groups, misuse, adversarial inputs, and consequential failure.
6. **Set evidence rules.** Name measures, human judgment, sampling, thresholds, and limitations. Avoid fake precision.
7. **Connect decisions.** Specify which evidence triggers ship, continuation, correction, pause, rollback, or retirement.
8. **Assign ownership.** Name who interprets evidence, decides, remains accountable, and approves changes.

AI may organize cases and draft language. Humans decide acceptable consequences, thresholds, and authority.

## Key Concepts

- **Behavior, not intention:** describe what users can observe.
- **Acceptable range:** probabilistic systems require bounded variation, not one ideal answer.
- **Consequence-aware evaluation:** weight failures by who is affected and what follows.
- **Contract evolution:** version behavior when evidence or context changes.

## Organizational Applications

Use for assistants, recommendations, classifiers, generated content, decision support, and agents. Reuse the contract across design reviews, evaluation datasets, autonomy decisions, production monitoring, and incident learning.

## Common Pitfalls

- Using adjectives without observable cases
- Testing only happy paths
- Treating an average score as permission to ignore severe failures
- Setting thresholds without evidence or a decision
- Omitting affected people, refusals, escalation, or owners
- Treating the document as proof of reliable behavior

## Combine With

Use `aipom-autonomy-boundary-designer` to decide authority, `aipom-golden-dataset-builder` to operationalize representative cases, and `aipom-eval-scorecard-builder` to define measurement and decision rules.

## Assets and Templates

- [Behavior contract template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

- NIST, [AI Risk Management Framework 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10), January 26, 2023. Supports lifecycle risk mapping, measurement, management, and accountable governance. Accessed July 16, 2026. NIST notes that the framework is being revised.
