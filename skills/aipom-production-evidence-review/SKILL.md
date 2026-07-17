---
name: aipom-production-evidence-review
description: Run a recurring review of AI behavior, workflow, human, outcome, control, incident, and affected-party evidence to continue, change, constrain, roll back, or retire.
type: workflow
category: evaluation-and-evidence
phase: 4
status: active
operating_level: [portfolio, product-team, initiative]
audience: [Product Operations, Product Manager, Team Lead, Engineering, Operations, Research, Data, Risk, AI Governance]
best_for: [Recurring production governance, Responding to drift or emerging harm, Deciding whether AI behavior should continue or change]
evidence_required: [Production monitoring and evaluation results, Workflow outcome and human-review evidence, Incidents feedback appeals and affected-party evidence, Versions changes controls and dependencies]
produces: [Production evidence review record, Continue change constrain rollback or retire decision, Monitoring and remediation actions]
assessment_questions: [EVAL-01, EVAL-02, EVAL-03, EVAL-04, EVAL-05, GOV-03, GOV-05]
maturity_move: {from: operationalized, to: compounding}
estimated_time: 60-120 min recurring
group_size: 5-12
depends_on: [aipom-eval-scorecard-builder, aipom-risk-control-incident-playbook]
combine_with: [aipom-golden-dataset-builder, aipom-trust-assurance-pack-builder, aipom-portfolio-quarterly-review]
sources:
  - https://www.nist.gov/news-events/news/2026/03/new-report-challenges-monitoring-deployed-ai-systems
  - https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
  - https://eur-lex.europa.eu/eli/reg/2024/1689/oj
---

# AIPOM Production Evidence Review

## What Is It

Run a recurring, decision-oriented review of how an AI product behaves in real use, including product and model performance, workflow outcomes, human interaction, affected-party evidence, controls, incidents, dependencies, and change history.

## Why Use It

Pre-release evaluation cannot represent every production condition. Dashboards also fail when no one interprets interacting signals, examines blind spots, or owns the authority to constrain and change behavior.

## When to Use It

Use on a risk-proportionate cadence and after material changes, threshold breaches, incidents, appeals, drift, or new affected-party evidence. Accountable specialists determine applicable legal or regulatory monitoring duties.

## What It Produces

- Scope, versions, changes, and evidence ledger
- Behavior, workflow, human, outcome, control, incident, and equity profile
- Blind spots, disagreements, and critical signals
- Continue, change, constrain, roll back, pause, or retire decision
- Remediation, monitoring, communication, and review actions

## Who Should Participate

Include the accountable product or operational owner, Team Lead, Product Manager, Product Operations where present, engineering and operations, evaluation or research, affected-user representation, and governance partners proportionate to consequence.

## Evidence to Bring

Bring scorecards, monitoring, logs, samples, workflow and outcome measures, review burden, subgroup views, drift, feedback, appeals, overrides, incidents, near misses, dependency changes, model and context versions, and remediation status.

## How to Do It

1. Define the decision window, deployed scope, versions, changes, population, and accountable owner.
2. Load monitoring and qualitative evidence; identify missing or unreliable signals.
3. Compare current behavior with contracts, scorecards, baselines, and launch conditions.
4. Review workflow outcomes, human reliance, review burden, overrides, and fallback use.
5. Review customer, affected-party, subgroup, appeal, complaint, incident, and near-miss evidence.
6. Examine context, data, model, vendor, integration, and environment changes.
7. Apply critical-failure and constrained-decision logic before aggregate trends.
8. Decide continue, change, constrain, roll back, pause, or retire.
9. Assign remediation, communication, monitoring, verification, and next review.
10. Feed new cases and lessons into evaluation, context, controls, playbooks, and portfolio decisions.

## Facilitation Protocol

Support context-dump mode for evidence preparation and guided mode for unresolved decision points. Ask one consequential question at a time. In best-guess mode, label blind spots, reduce authority or exposure, and do not interpret missing monitoring as stable behavior.

## Decision Logic

1. **Continue:** evidence remains within behavior, outcome, burden, and risk boundaries.
2. **Change:** a remediable behavior, context, workflow, or threshold issue requires revision.
3. **Constrain:** reduce population, action, autonomy, data, geography, or volume while evidence improves.
4. **Roll back or pause:** critical thresholds, controls, or recovery conditions fail.
5. **Retire:** value no longer justifies cost or risk, repeated remediation fails, or a better alternative exists.

No aggregate improvement offsets a critical harm or control failure. Preserve evidence gaps and material disagreement.

## Completion Criteria

Finish with deployed scope and versions, evidence and confidence, blind spots, critical signals, decision and authority, remediation owners, communications, verification, next review, and learning propagated to related artifacts.

## Key Concepts

- Monitoring is an evidence system, not a dashboard.
- Absence of detected harm is not evidence of absence.
- Human behavior and workload are production signals.
- Every signal needs an owner and possible action.

## Organizational Applications

Use for AI features, agents, decision support, retrieval, recommendations, internal workflows, regulated systems, and third-party models.

## Common Pitfalls

- Reviewing only model metrics
- Treating missing data as green
- Ignoring human overrides and burden
- Letting aggregate gains hide affected-group harm
- Recording actions without authority or verification
- Updating production without evaluation and assurance artifacts

## Combine With

Use `aipom-golden-dataset-builder` to incorporate emerging cases, `aipom-trust-assurance-pack-builder` to refresh stakeholder evidence, and `aipom-portfolio-quarterly-review` for investment consequences.

## Assets and Templates

- [Production review template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

- NIST, [Challenges to the Monitoring of Deployed AI Systems](https://www.nist.gov/news-events/news/2026/03/new-report-challenges-monitoring-deployed-ai-systems), March 9, 2026, updated March 18, 2026. Supports risk-proportionate post-deployment monitoring across technical, human, and organizational signals. Accessed July 17, 2026.
- NIST AI Resource Center, [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). Measure 2.4 and Manage 4 address production monitoring, feedback, response, recovery, and continual improvement. Accessed July 17, 2026; NIST notes AI RMF 1.0 is under revision.
- European Union, [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj), particularly Article 72 for post-market monitoring obligations applicable to high-risk systems in scope. Accessed July 17, 2026.

This workflow does not determine compliance or replace accountable legal, safety, privacy, security, or regulatory decisions.
