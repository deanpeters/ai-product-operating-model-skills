---
name: aipom-economic-case-builder
description: Build an evidence-aware economic case for an AI investment across value, full lifecycle cost, uncertainty, alternatives, risk, and decision thresholds.
type: component
category: strategy-and-economic-outcomes
phase: 3
status: active
operating_level: [portfolio, initiative]
audience: [CPO, VP Product, Product Operations, Product Manager, Finance, Engineering, Operations, AI Governance]
best_for: [Funding validation or scale, Comparing AI with non-AI alternatives, Revising a case when evidence changes]
evidence_required: [Outcome value map and baselines, Cost and capacity evidence, Adoption and evaluation evidence, Dependency risk and alternative estimates]
produces: [AI economic case, Scenario and sensitivity model, Funding decision rules]
assessment_questions: [STR-02, STR-03, STR-04, POR-02, POR-03]
maturity_move: {from: repeatable, to: operationalized}
estimated_time: 60-120 min
group_size: 3-8
depends_on: [aipom-outcome-value-map, aipom-bet-charter]
combine_with: [aipom-platform-dependency-audit, aipom-investment-stage-gates, aipom-initiative-readiness-review]
sources: []
---

# AIPOM Economic Case Builder

## What Is It

Build a decision-ready economic case connecting AI behavior and adoption to customer, operational, financial, safety, or risk value. Include full lifecycle cost, uncertainty, alternatives, dependencies, and explicit funding thresholds.

## Why Use It

AI cases often count optimistic labor savings while omitting review, evaluation, data, inference, integration, governance, failure, switching, and change costs. A useful case exposes the causal and economic assumptions that must earn further investment.

## When to Use It

Use before material validation, procurement, scale, or renewal decisions. Early cases should use ranges and learning milestones; do not demand false precision from discovery-stage evidence.

## What It Produces

- Value logic and baseline
- Full lifecycle cost model
- Base, downside, and upside scenarios
- Sensitivity, break-even, and dependency analysis
- Continue, revise, pause, or stop decision rules

## Who Should Participate

Include the investment owner, Product Manager, finance, engineering or platform owners, operations, and governance partners where failure or compliance costs matter.

## Evidence to Bring

Bring outcome maps, baselines, experiments, adoption evidence, review burden, model and infrastructure costs, staffing, evaluation and control costs, incident estimates, contracts, alternatives, and uncertainty ranges.

## How to Do It

1. Name the funding decision, horizon, scope, and accountable owner.
2. Restate the causal value chain and mark evidenced versus assumed links.
3. Quantify the current baseline and credible non-AI alternatives.
4. Model value through customer, revenue, margin, cost, capacity, safety, or avoided risk outcomes.
5. Include build, buy, data, integration, inference, evaluation, review, monitoring, governance, change, failure, and exit costs.
6. Create downside, base, and upside scenarios with explicit adoption and quality assumptions.
7. Run sensitivity and break-even analysis on the few variables that change the decision.
8. Identify concentration, portability, and tail-risk exposure that arithmetic may hide.
9. Define evidence milestones and continue, revise, pause, or stop thresholds.

## Key Concepts

- Saved minutes are not savings unless capacity or outcomes change.
- Ranges are more honest than unsupported point forecasts.
- Avoided risk needs probability, consequence, and attribution assumptions.
- Economic evidence should evolve at each investment gate.

## Organizational Applications

Use for pilot funding, vendor selection, scale decisions, renewal, build-versus-buy, workflow redesign, and portfolio reallocation.

## Common Pitfalls

- Counting gross time saved as cash benefit
- Omitting review and control cost
- Assuming full adoption at launch
- Ignoring non-AI alternatives and switching cost
- Letting expected value hide intolerable downside
- Preserving the original forecast after evidence changes

## Combine With

Use `aipom-platform-dependency-audit` for concentration and exit exposure, `aipom-investment-stage-gates` for funding decisions, and `aipom-initiative-readiness-review` for cross-category constraints.

## Assets and Templates

- [Economic case template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

This skill is an original AIPOM synthesis of scenario-based product economics, total-cost analysis, and evidence-based investment practice.
