---
name: aipom-operating-model-retrospective
description: Review whether the AI product operating model improves decisions and outcomes, identify systemic friction and performative activity, and choose the next changes.
type: workflow
category: cross-category
phase: 4
status: active
operating_level: [organization, portfolio, product-team]
audience: [CPO, CTO, Product Operations, Product Manager, Engineering, Data, Finance, People Operations, AI Governance]
best_for: [Annual or semiannual operating-model improvement, Learning after several portfolio cycles, Retiring controls practices or metrics that no longer help]
evidence_required: [Assessment roadmap and prior retrospective, Portfolio and production decisions, Workflow capability adoption and outcome evidence, Incidents exceptions burden and stakeholder feedback]
produces: [Operating-model learning report, Keep change stop and experiment decisions, Updated roadmap owners and reassessment plan]
assessment_questions: [STR-01, STR-02, STR-03, STR-04, STR-05, POR-01, POR-02, POR-03, POR-04, POR-05, WFL-01, WFL-02, WFL-03, WFL-04, WFL-05, CTX-01, CTX-02, CTX-03, CTX-04, CTX-05, EVAL-01, EVAL-02, EVAL-03, EVAL-04, EVAL-05, GOV-01, GOV-02, GOV-03, GOV-04, GOV-05, CAP-01, CAP-02, CAP-03, CAP-04, CAP-05]
maturity_move: {from: operationalized, to: compounding}
estimated_time: 2-4 hours plus evidence preparation
group_size: 6-16
depends_on: [aipom-operating-model-assessment, aipom-operating-model-roadmap]
combine_with: [aipom-portfolio-quarterly-review, aipom-adoption-impact-scorecard, aipom-operating-model-design-sprint]
sources: []
---

# AIPOM Operating Model Retrospective

## What Is It

Review how the organization’s AI product operating model actually affects decisions, outcomes, learning, accountability, workload, risk, and reuse. Decide what to keep, change, stop, contain, or experiment with next.

## Why Use It

Operating systems accumulate controls, meetings, templates, metrics, and exceptions. Without reflection, useful practices harden into ceremony while recurring failures remain untouched. The retrospective evaluates the system, not individual blame.

## When to Use It

Use semiannually, annually, after several portfolio cycles, or following material organizational change or repeated incidents. Use an initiative review for one product and the organization assessment when a fresh full baseline is required.

## What It Produces

- Scope, evidence, outcome, burden, and decision-change ledger
- Category patterns, cross-category dependencies, and recurring failure modes
- Useful, weak, harmful, duplicative, and performative practices
- Keep, change, stop, contain, or experiment decisions
- Updated roadmap, owners, measures, communication, and reassessment plan

## Who Should Participate

Include accountable leadership, Product Operations, representative product teams and practitioners, technology and data, governance partners, finance or operations, capability owners, and affected-user perspectives where relevant.

## Evidence to Bring

Bring prior assessment and roadmap, portfolio decisions, stage gates, production reviews, incidents, exceptions, workflow and outcome measures, context and evaluation evidence, capability and adoption scorecards, reuse, burden, stakeholder feedback, and examples of retired work.

## How to Do It

1. Define the period, scope, decisions, outcomes, and participants; record missing perspectives.
2. Load prior commitments, assumptions, owners, and evidence into a shared ledger.
3. Examine which practices changed decisions and outcomes, not merely which artifacts exist.
4. Review critical failures, near misses, disagreements, exceptions, and repeated workarounds.
5. Examine burden, delay, duplicated controls, hidden labor, and incentives across roles.
6. Identify cross-category root causes and conditions that enabled reuse or compounding value.
7. Classify practices as keep, change, stop, contain, or experiment; explain evidence and tradeoffs.
8. Prioritize a small set of operating-model changes with owners, measures, and decision dates.
9. Update the roadmap, strategy assumptions, assessment evidence, communications, and reassessment trigger.

## Facilitation Protocol

Support context-dump mode for evidence synthesis and guided mode for interpretation and decisions. Invite practitioner and affected-party evidence before executive conclusions. In best-guess mode label missing perspectives, avoid claims of consensus, and recommend evidence-gathering rather than confident redesign.

## Decision Logic

1. **Keep:** evidence shows the practice improves decisions or outcomes at acceptable burden.
2. **Change:** the intent remains valuable but design, ownership, adoption, or measurement fails.
3. **Stop:** the practice creates ceremony, duplication, harm, or no decision value.
4. **Contain:** a critical gap requires immediate limitation before redesign.
5. **Experiment:** a plausible operating change needs a bounded test.

Do not preserve a practice because leaders sponsored it or remove a safeguard merely because it creates friction. Examine the consequence and root cause.

## Completion Criteria

Finish with scope and perspectives, evidence and confidence, decisions and outcomes changed, burden and failures, systemic patterns, keep/change/stop/contain/experiment choices, accountable owners, measures, roadmap updates, unresolved questions, and reassessment trigger.

## Key Concepts

- The operating model is a product that requires evidence and iteration.
- Friction may be waste, safeguard, or signal; diagnose before removing it.
- Compounding maturity means measured improvement and reuse.
- Retiring performative activity returns capacity to useful practice.

## Organizational Applications

Use for enterprise or business-unit reviews, post-transformation learning, governance simplification, capability investment, portfolio-system improvement, and recovery from control or process sprawl.

## Common Pitfalls

- Turning the session into executive storytelling
- Reviewing maturity scores without decisions changed
- Blaming individuals for system conditions
- Removing controls because teams dislike them
- Producing dozens of improvement actions
- Updating slides but not owners, routines, or resource allocation

## Combine With

Use `aipom-portfolio-quarterly-review` for investment cadence, `aipom-adoption-impact-scorecard` for changed practice evidence, and `aipom-operating-model-design-sprint` to test priority redesigns.

## Assets and Templates

- [Operating-model retrospective template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

This workflow is an original AIPOM synthesis of organizational retrospectives, operating-model design, evidence-based governance, and continuous improvement.
