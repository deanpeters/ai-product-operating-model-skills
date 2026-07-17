---
name: aipom-outcome-value-map
description: Map how AI behavior may change user behavior, product outcomes, economic value, and risk while exposing causal assumptions and countermeasures.
type: component
category: strategy-and-economic-outcomes
phase: 2
status: active
operating_level: [portfolio, product-team, initiative]
audience: [CPO, Product Manager, Design, Engineering, Research, Finance, AI Governance]
best_for: [Connecting AI behavior to meaningful value, Challenging activity metrics, Choosing measures and causal tests]
evidence_required: [Opportunity frame, Current outcome baselines, Behavior or workflow evidence, Economic and risk assumptions]
produces: [Outcome and value chain, Causal assumption ledger, Measures and countermeasures]
assessment_questions: [STR-02, STR-03, STR-04, WFL-05]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 45-75 min
group_size: 3-8
depends_on: [aipom-opportunity-framing]
combine_with: [aipom-bet-charter, aipom-economic-case-builder, aipom-evaluation-strategy-advisor]
sources: []
---

# AIPOM Outcome Value Map

## What Is It

Trace the causal path from an AI behavior through human or workflow behavior to product, customer, operational, economic, safety, and risk outcomes. Mark the assumptions and countermeasures that keep a desirable metric from hiding a worse result.

## Why Use It

Teams frequently jump from “the model can do this” to revenue or savings without showing who changes behavior, why, or at what cost. The map turns that leap into testable links.

## When to Use It

Use after framing an opportunity and before committing to a bet, evaluation strategy, or economic case. Revisit when evidence breaks a causal link or reveals a harmful countereffect.

## What It Produces

- AI behavior and quality conditions
- User, operator, or decision behavior changes
- Product and customer outcomes
- Economic, operational, safety, and risk consequences
- Causal assumptions, measures, countermeasures, and next tests

## Who Should Participate

Include the Product Manager, affected-user or workflow representatives, design, technical and data partners, finance or operations, and governance partners where outcomes carry material consequences.

## Evidence to Bring

Bring the opportunity frame, baselines, behavioral research, workflow evidence, economics, evaluation results, incidents, and comparable alternatives. Estimated links remain assumptions until tested.

## How to Do It

1. State the intended outcome and the decision the map supports.
2. Define the AI behavior required, including acceptable quality and prohibited failure.
3. Map how users or operators must notice, trust, interpret, and act differently.
4. Connect those behaviors to product, customer, or operational outcomes.
5. Connect outcomes to revenue, margin, cost, risk, safety, or strategic value.
6. Add costs, review burden, displaced work, and negative externalities.
7. Mark every causal link as evidenced, inferred, assumed, or contradicted.
8. Select leading measures, lagging measures, and countermeasures.
9. Prioritize the causal assumption whose failure most changes the decision.

## Key Concepts

- Model performance is an input, not a business outcome.
- Human response is often the weakest causal link.
- Countermeasures reveal local optimization and hidden harm.
- Value includes avoided loss and risk, but not without evidence.

## Organizational Applications

Use to improve initiative proposals, align product and finance, design evaluations, reject vanity metrics, and explain why a technically strong system may still create weak value.

## Common Pitfalls

- Drawing arrows without assumptions or evidence
- Treating adoption as value
- Omitting human review cost and rework
- Counting benefits while externalizing risk
- Using one metric for model, workflow, and business performance
- Refusing to revise the map when evidence changes

## Combine With

Use `aipom-bet-charter` to own the hypothesis, `aipom-evaluation-strategy-advisor` to test behavior and workflow links, and `aipom-economic-case-builder` for a fuller financial decision.

## Assets and Templates

- [Outcome value map template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

This skill is an original AIPOM synthesis of causal outcome mapping and evidence-based product investment practice.
