---
name: aipom-portfolio-quarterly-review
description: Run a recurring AI portfolio review that reallocates capital and capacity using strategy, outcomes, economics, readiness, production evidence, dependencies, and learning.
type: workflow
category: cross-category
phase: 4
status: active
operating_level: [organization, portfolio]
audience: [CPO, CTO, VP Product, Product Operations, Product Manager, Finance, Engineering, Risk, AI Governance]
best_for: [Quarterly AI investment decisions, Stopping zombie pilots and premature scale, Rebalancing initiatives and shared capabilities]
evidence_required: [Strategy and portfolio inventory, Initiative economics readiness and production evidence, Dependencies incidents and control status, Capacity reuse adoption and prior decision records]
produces: [Portfolio decision record, Initiative and shared-capability allocations, Updated strategy assumptions and next review agenda]
assessment_questions: [STR-01, STR-02, STR-03, STR-04, STR-05, POR-01, POR-02, POR-03, POR-04, POR-05, EVAL-05, GOV-03, CAP-03, CAP-04]
maturity_move: {from: operationalized, to: compounding}
estimated_time: 2-4 hours quarterly plus preparation
group_size: 5-12 decision group
depends_on: [aipom-portfolio-posture-advisor, aipom-investment-stage-gates]
combine_with: [aipom-production-evidence-review, aipom-strategy-narrative-builder, aipom-operating-model-retrospective]
sources: []
---

# AIPOM Portfolio Quarterly Review

## What Is It

Run a recurring evidence-based portfolio decision that continues, changes, scales, constrains, pauses, stops, or retires AI investments and funds the shared operating capabilities they depend on.

## Why Use It

Portfolio meetings become status theater when initiative owners report activity without comparable decisions. A quarterly review connects strategy, value, economics, readiness, production evidence, dependencies, controls, capability, and capacity to explicit allocation.

## When to Use It

Use quarterly or at a cadence appropriate to investment and risk. Run off-cycle reviews after material incidents, dependency changes, strategic shifts, or evidence that invalidates a major bet.

## What It Produces

- Portfolio context, evidence quality, and change ledger
- Initiative decisions and funding or capacity allocations
- Shared capability, dependency, and safeguard investments
- Retired assumptions, stopped work, exceptions, and owners
- Strategy updates, communication actions, and next review agenda

## Who Should Participate

Include accountable portfolio authorities, product and technology leaders, Product Operations, finance, shared-platform owners, and governance partners. Initiative owners provide evidence; they do not unilaterally set criteria or approve exceptions.

## Evidence to Bring

Bring strategy choices, initiative inventory, bet charters, economics, stage decisions, readiness and production reviews, outcomes, costs, incidents, dependencies, adoption, reusable capabilities, capacity, exceptions, and prior decision follow-through.

## How to Do It

1. Load the prior decision ledger, commitments, exceptions, and material changes.
2. Confirm current strategy, constraints, capacity, and the decisions required this cycle. Define capacity in usable units and state whether continuing existing work consumes the same allocation slots as new investment.
3. Normalize initiative evidence by stage, consequence, and decision—not one universal score.
4. Review outcome and economic evidence, production behavior, readiness, dependencies, controls, adoption, and owner confidence.
5. Apply critical-gap and exception-expiry logic before relative comparison.
6. Decide continue, change, validate, scale, constrain, pause, stop, or retire for each material initiative.
7. Allocate investment to shared context, evaluation, governance, platform, capability, and reuse conditions that unlock several bets.
8. Examine concentration, duplication, zombie pilots, premature scale, and unowned mandatory work.
9. Update strategy assumptions, narrative, allocations, owners, communication, and next evidence requirements.
10. Record decisions, dissent, exceptions, allocation assumptions, and follow-through for the next review.

## Facilitation Protocol

Use context-dump mode for pre-read synthesis and guided mode for contested decisions. Ask only questions that change allocation, constraint, or ownership. In best-guess mode recommend bounded learning or containment rather than confident scale. Preserve dissent and conflicts of interest.

## Decision Logic

1. **Explore or validate:** important uncertainty with a bounded learning path.
2. **Continue:** evidence supports the current stage and next test.
3. **Scale:** representative outcomes, economics, controls, capacity, and production evidence support expansion.
4. **Constrain or pause:** critical gaps or external conditions limit responsible operation.
5. **Stop or retire:** value fails, criteria repeatedly miss, ownership disappears, or a better alternative wins.
6. **Fund shared capability:** one operating condition unlocks or protects several strategically relevant bets.

Do not let sunk cost, executive sponsorship, or aggregate portfolio scores override failed criteria or critical gaps.

An exception must name the authority granting it, the constrained scope, safeguards, expiry, and evidence required for renewal. If capacity units, exception authority, or decision dates are missing, expose them as allocation assumptions or unresolved governance conditions rather than silently resolving them.

## Completion Criteria

Finish with evidence quality, initiative decisions, allocations, shared capabilities, stopped work, exceptions and expiry, dissent, accountable owners, strategy changes, communication actions, and next review evidence.

## Key Concepts

- Portfolio review allocates scarce capital and attention.
- Learning investments and scaling investments require different evidence.
- Stopped work is a sign of functioning governance.
- Shared capabilities compete for funding with visible features.

## Organizational Applications

Use for enterprise AI portfolios, business-unit investments, innovation funds, internal workflow programs, platform strategies, and vendor rationalization.

## Common Pitfalls

- Running initiative status presentations
- Comparing discovery and production with one score
- Funding visibility instead of evidence
- Ignoring shared dependencies and mandatory controls
- Renewing exceptions automatically
- Recording decisions without reallocating capacity

## Combine With

Use `aipom-production-evidence-review` for operational evidence, `aipom-strategy-narrative-builder` to communicate changed choices, and `aipom-operating-model-retrospective` to improve the review system.

## Assets and Templates

- [Quarterly review template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

This workflow is an original AIPOM synthesis of evidence-based portfolio governance, staged investment, strategy review, and organizational learning.
