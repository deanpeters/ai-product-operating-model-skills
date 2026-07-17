---
name: aipom-use-case-triage
description: Compare AI opportunities across outcome value, evidence, feasibility, responsibility, readiness, and reversibility to recommend explore, validate, defer, or reject.
type: interactive
category: portfolio-and-investment-choices
phase: 2
status: active
operating_level: [portfolio, product-team, initiative]
audience: [CPO, VP Product, Product Operations, Product Manager, Team Lead, Engineering, Finance, AI Governance]
best_for: [Comparing an intake of AI ideas, Preventing enthusiasm-only prioritization, Choosing bounded discovery investments]
evidence_required: [Comparable opportunity frames, Outcome and value assumptions, Feasibility and readiness evidence, Consequences and constraints]
produces: [Comparable triage record, Posture recommendation for each use case, Portfolio-level gaps and next tests]
assessment_questions: [POR-01, POR-02, POR-03, STR-04]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 45-90 min
group_size: 3-10
depends_on: [aipom-opportunity-framing, aipom-outcome-value-map]
combine_with: [aipom-bet-charter, aipom-investment-stage-gates, aipom-portfolio-posture-advisor]
sources: []
---

# AIPOM Use-Case Triage

## What Is It

An adaptive comparison method for deciding which AI opportunities deserve exploration, validation, deferral, or rejection. It preserves evidence quality and critical constraints instead of disguising judgment in a single weighted score.

## Why Use It

Idea funnels reward confident storytelling and false precision. Triage makes alternatives comparable while preventing strong value claims from averaging away unsafe behavior, unavailable data, or missing ownership.

## When to Use It

Use for intake, portfolio shaping, innovation funds, or before creating detailed bet charters. Do not use it to decide scale; later-stage evidence belongs in investment gates.

## What It Produces

- Comparable opportunity records and confidence notes
- Explore, validate, defer, or reject recommendation per use case
- Non-negotiable constraints and portfolio dependencies
- Next test, owner, decision rule, and review date

## Who Should Participate

Include the portfolio decision owner, Product Operations, product and technology representatives, finance, and governance partners. Invite opportunity owners to clarify evidence, not set their own criteria.

## Evidence to Bring

Bring opportunity frames, outcome maps, alternatives, user evidence, feasibility signals, data and context readiness, evaluation needs, governance consequences, adoption constraints, costs, and reversibility.

## How to Do It

1. Extract supplied context and normalize each opportunity to a comparable scope. For a single proposal, compare it with the current workflow, a non-AI alternative, or the decision to do nothing.
2. Confirm the portfolio decision, constraints, capacity, and non-negotiables.
3. Examine outcome value, evidence strength, AI fit, feasibility, responsibility, readiness, and reversibility.
4. Record missing perspectives, disagreements, and evidence confidence.
5. Apply critical constraints before comparing relative attractiveness.
6. Present posture options and recommend a default with reasons.
7. Define the smallest evidence-producing action for opportunities that proceed.
8. Record the owner, decision rule, exceptions, and next review.

Triage determines the next investment posture; it does not establish launch or scale readiness. Route a selected opportunity to a bet charter, investment gate, or initiative-readiness review appropriate to the next decision.

## Facilitation Protocol

Support guided, context-dump, and best-guess modes. In guided mode ask first which decision and capacity constraint govern the comparison. In context-dump mode extract existing answers before asking gaps. In best-guess mode label assumptions and avoid turning incomplete information into numeric certainty.

## Decision Logic

1. **Explore:** meaningful condition, credible AI fit, high uncertainty, bounded consequence, and a cheap learning path.
2. **Validate:** promising evidence but material behavior, value, feasibility, adoption, or responsibility questions remain.
3. **Defer:** attractive opportunity lacks a prerequisite, owner, capacity, or decision window.
4. **Reject:** weak condition or AI fit, unacceptable consequence, unavailable critical input, or a clearly superior alternative.

Use dimensions as structured judgment, not a compensating arithmetic score. No value score overrides a non-negotiable safety, legal, privacy, security, or accountability gap.

## Completion Criteria

Finish with the evidence used, assumptions, alternatives, posture for every use case, critical constraints, disagreements, owners, next tests, and review decisions. If a named owner or review date is unavailable, identify the required role, mark assignment unresolved, and use an evidence-completion trigger rather than inventing details.

## Key Concepts

- Comparable does not mean falsely precise.
- Evidence quality changes confidence, not just rank.
- Reversibility determines how cheaply uncertainty can be explored.
- A prerequisite gap may justify defer rather than reject.

## Organizational Applications

Use for product intake, innovation councils, annual planning, vendor proposals, and reducing duplicate or strategically incoherent pilots.

## Common Pitfalls

- Scoring proposals before framing them consistently
- Letting presenters define favorable criteria
- Averaging away critical constraints
- Confusing a demo with feasibility evidence
- Ranking opportunities without capacity or next decisions
- Treating defer as a polite yes

## Combine With

Use `aipom-bet-charter` for selected opportunities, `aipom-investment-stage-gates` for continuation decisions, and `aipom-portfolio-posture-advisor` for portfolio balance.

## Assets and Templates

- [Triage record template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

This advisor is an original AIPOM synthesis of evidence-based opportunity, portfolio, and responsible-investment practice.
