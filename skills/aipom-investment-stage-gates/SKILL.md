---
name: aipom-investment-stage-gates
description: Define evidence-based entry, continuation, pivot, scale, pause, and stop decisions for AI investments without turning gates into document approval theater.
type: component
category: portfolio-and-investment-choices
phase: 2
status: active
operating_level: [organization, portfolio, initiative]
audience: [CPO, CTO, VP Product, Product Operations, Product Manager, Finance, Engineering, AI Governance]
best_for: [Creating consistent AI funding decisions, Ending zombie pilots, Separating learning capital from scaling capital]
evidence_required: [Bet charters and initiative inventory, Outcome and evaluation evidence, Cost and dependency evidence, Control incidents and adoption evidence]
produces: [Investment gate model, Stage-specific evidence requirements, Decision and exception record]
assessment_questions: [POR-02, POR-03, POR-05, STR-04]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 60-90 min
group_size: 4-10
depends_on: [aipom-bet-charter, aipom-use-case-triage]
combine_with: [aipom-portfolio-posture-advisor, aipom-economic-case-builder, aipom-initiative-readiness-review]
sources: []
---

# AIPOM Investment Stage Gates

## What Is It

Create a small set of recurring investment decisions for AI bets, with evidence proportionate to each stage and explicit continue, pivot, scale, pause, stop, and exception paths.

## Why Use It

Without gates, pilots persist because no one owns the stopping decision. With bureaucratic gates, teams optimize documents instead of learning. A useful gate names the decision, minimum evidence, accountable authority, and consequence of not meeting the bar.

## When to Use It

Use after triage and bet chartering, before multiple initiatives compete for continuing or scaling capital. Tailor rigor to consequence and reversibility rather than imposing one checklist on every experiment.

## What It Produces

- Stages and decisions from exploration through retirement
- Minimum evidence and critical controls at each gate
- Decision authority, timing, exception, and appeal rules
- Standard decision record and portfolio learning loop

## Who Should Participate

Include portfolio and funding authorities, Product Operations, product and technology leaders, finance, and governance partners. Initiative owners supply evidence but should not approve their own exceptions.

## Evidence to Bring

Bring real initiative histories, decisions, costs, evaluations, incidents, dependencies, adoption evidence, and stopped or stalled pilots. Design around actual uncertainty, not hypothetical perfection.

## How to Do It

1. Define the stages and the investment decision at each boundary.
2. Separate exploration evidence from validation and scale evidence.
3. Specify required outcome, behavior, feasibility, economic, adoption, and responsibility evidence.
4. Identify critical gaps that block progression regardless of other strengths.
5. Assign decision authority, contributors, reviewers, and escalation.
6. Define continue, pivot, scale, pause, stop, and retire criteria.
7. Create time-bounded exceptions with an owner, rationale, compensating control, and expiry.
8. Set review cadence and capture what portfolio criteria should change from experience.
9. Test the model against past initiatives and revise ambiguous gates.

## Key Concepts

- Gates fund the next uncertainty, not the original story.
- Scale requires representative evidence and operating controls.
- Critical gaps are not averaged away.
- An expired exception becomes a decision, not permanent ambiguity.

## Organizational Applications

Use for innovation funds, quarterly planning, platform investments, vendor-backed pilots, and retirement of low-learning initiatives.

## Common Pitfalls

- Requiring the same evidence at every stage
- Approving documents instead of examining use
- Hiding stop decisions behind endless pilots
- Treating sunk cost as evidence
- Allowing initiative owners to approve exceptions
- Scaling before production, workflow, and responsibility evidence exists

## Combine With

Use `aipom-portfolio-posture-advisor` to diagnose portfolio balance, `aipom-economic-case-builder` for material scale economics, and `aipom-initiative-readiness-review` before consequential launch or expansion.

## Assets and Templates

- [Stage-gate design template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

This skill is an original AIPOM synthesis of evidence-based staged investment and portfolio decision practice.
