---
name: aipom-initiative-readiness-review
description: Review one AI initiative across value, economics, dependencies, workflow, context, evaluation, governance, controls, capability, and recovery before a material decision.
type: workflow
category: cross-category
phase: 3
status: active
operating_level: [portfolio, product-team, initiative]
audience: [CPO, CTO, Product Operations, Product Manager, Team Lead, Engineering, Finance, Operations, Legal, Privacy, Security, Risk, AI Governance]
best_for: [Launch or scale decisions, Increasing autonomy or sensitive-data use, Resolving conflicting readiness claims]
evidence_required: [Bet outcome and economic evidence, Architecture context data and evaluation artifacts, Accountability controls and incident readiness, Adoption capability and operating evidence]
produces: [Initiative readiness profile, Critical gaps and constrained decisions, Proceed constrain remediate pause or stop recommendation]
assessment_questions: [STR-02, STR-03, STR-04, POR-02, POR-03, POR-04, WFL-03, WFL-04, WFL-05, CTX-01, CTX-02, CTX-03, CTX-04, CTX-05, EVAL-01, EVAL-02, EVAL-03, EVAL-04, EVAL-05, GOV-01, GOV-02, GOV-03, GOV-04, GOV-05, CAP-01, CAP-02, CAP-03]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 2-4 hours across preparation and review
group_size: 5-14
depends_on: [aipom-bet-charter, aipom-economic-case-builder, aipom-platform-dependency-audit, aipom-evaluation-strategy-advisor, aipom-accountability-charter, aipom-risk-control-incident-playbook]
combine_with: [aipom-investment-stage-gates, aipom-operating-model-design-sprint, aipom-production-evidence-review]
sources:
  - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
  - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
---

# AIPOM Initiative Readiness Review

## What Is It

Integrate evidence for one AI initiative before a material decision such as validation, limited operation, launch, scale, sensitive-data use, or increased autonomy. Keep initiative readiness separate from organization-wide maturity.

## Why Use It

Strong model results or a completed governance checklist can conceal weak economics, context, workflow, recovery, or accountability. This review applies profiles and critical-gap logic rather than a compensating average.

## When to Use It

Use at material investment gates and after significant model, data, workflow, vendor, autonomy, incident, or jurisdiction changes. It supports accountable decisions; it is not legal, safety, security, privacy, or regulatory certification.

## What It Produces

- Scope, decision, evidence, and confidence ledger
- Readiness profiles across value, dependencies, workflow, context/data, evaluation, governance/controls, and capability/operation
- Critical gaps, disagreements, and constrained decisions
- Proceed, proceed with constraints, remediate and re-review, pause, or stop recommendation
- Owners, evidence conditions, expiry, and next review

## Who Should Participate

Include the accountable decision owner, Team Lead, Product Manager, Product Operations where present, technical and operational owners, finance, affected-user or domain representation, and legal, privacy, security, risk, or governance specialists proportionate to consequence.

## Evidence to Bring

Bring bet and outcome evidence, economics, dependencies, workflow measures, context and data readiness, behavior contract, evaluation set and scorecard, accountability, autonomy boundaries, controls, incidents, adoption, capability, and rollback evidence.

## How to Do It

1. Define the exact decision, scope, population, environment, autonomy, jurisdictions, and consequence.
2. Separate the decision under review from any lower-exposure interim motion that may continue while prerequisites are remediated.
3. Load supplied artifacts into a context ledger; ask only for decision-changing gaps.
4. Profile strategic value and economics, including alternatives and uncertainty.
5. Profile platform, data, context, workflow, and operating dependencies.
6. Profile behavior, evaluation coverage, thresholds, production signals, and uncertainty.
7. Profile accountability, authority, controls, escalation, rollback, incident response, and specialist decisions.
8. Profile user adoption, operator capacity, role competence, support, and change readiness.
9. Preserve disagreements and distinguish evidence, assumptions, and required approvals.
10. Identify critical gaps and state which actions they constrain before any summary.
11. Recommend a decision, permitted interim motion, conditions, owners, expiry, and next review trigger.

## Facilitation Protocol

Support guided, context-dump, and best-guess modes. In guided mode begin with the material decision and consequence. In context-dump mode prepopulate the review from artifacts. In best-guess mode reduce confidence and authority, label missing specialist decisions, and never infer readiness from document completion.

## Decision Logic

1. **Proceed:** representative evidence supports the scoped decision and no critical gap remains.
2. **Proceed with constraints:** value is supported and residual gaps can be bounded through limits, monitoring, fallback, and expiry.
3. **Remediate and re-review:** a resolvable prerequisite blocks the decision.
4. **Pause:** evidence, ownership, capacity, or external conditions cannot currently support a responsible decision.
5. **Stop:** weak value, unacceptable consequence, failed criteria, or a superior alternative invalidates the initiative.

Do not average away a critical legal, privacy, security, safety, accountability, evaluation, rollback, or incident-response gap. Required specialists make decisions within their authority; the review does not impersonate them.

Record unresolved specialist decisions in a decision register. Missing specialist approval remains a constraint, not implied consent. When a named owner or date is unavailable, name the required role, mark it unassigned, and use an evidence or decision trigger until the accountable authority sets the calendar.

## Completion Criteria

Finish with defined scope, evidence and confidence, category profiles, disagreements, critical gaps, constrained actions, recommendation, permitted interim motion, accountable decision, specialist decision register, conditions, owners, expiry, unresolved questions, and re-review trigger.

## Key Concepts

- Initiative readiness is not organization maturity.
- Readiness is decision- and scope-specific.
- A constraint must have an owner and expiry.
- Completed artifacts are inputs, not proof of operation.

## Organizational Applications

Use for pilot entry, limited launch, scale, sensitive-data use, agent authority, vendor changes, post-incident return, and market expansion.

## Common Pitfalls

- Producing one overall readiness score
- Reviewing documents instead of evidence of use
- Allowing strong value to compensate for critical control gaps
- Conflating specialist review with product approval
- Setting conditions without monitoring or expiry
- Reusing an old review after material change

## Combine With

Use `aipom-investment-stage-gates` for recurring portfolio decisions, `aipom-operating-model-design-sprint` when multiple readiness gaps reflect organizational design, and `aipom-production-evidence-review` after operation.

## Assets and Templates

- [Readiness review template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

- NIST, [AI Risk Management Framework 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10), January 26, 2023. Supports lifecycle governance, mapping, measurement, and management of AI risks. Accessed July 17, 2026; NIST states that version 1.0 is under revision.
- NIST, [AI RMF Generative AI Profile, NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence), July 26, 2024, updated April 8, 2026. Supports risk-based evaluation and management for generative AI. Accessed July 17, 2026.

This workflow does not establish compliance or replace decisions assigned to accountable specialists.
