---
name: aipom-productive-motion-map
description: Map a recurring product-team motion through decisions, actors, inputs, handoffs, delays, rework, and failure before assigning AI and human responsibilities.
type: component
category: product-team-workflows
phase: 2
status: active
operating_level: [product-team, initiative]
audience: [Product Operations, Product Manager, Design, Engineering, Research, Data]
best_for: [Understanding work before adding AI, Finding consequential delays and rework, Establishing a baseline for workflow redesign]
evidence_required: [Observed workflow examples, Decision and handoff records, Cycle-time and rework evidence, Practitioner and affected-user perspectives]
produces: [Current-state productive-motion map, Friction and failure diagnosis, Baseline and redesign target]
assessment_questions: [WFL-01, WFL-02, WFL-05]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 45-90 min
group_size: 3-10
depends_on: [aipom-workflow-opportunity-advisor]
combine_with: [human-aipom-work-contract, aipom-workflow-playbook-builder, aipom-decision-cycle-redesign]
sources: []
---

# AIPOM Productive Motion Map

## What Is It

Map how one recurring product-team outcome is actually produced: decisions, actors, inputs, tools, handoffs, waiting, rework, exceptions, and failures. The map establishes evidence before AI responsibilities are designed.

## Why Use It

Automating a diagrammed ideal state often makes hidden work faster and less visible. Observing the real motion reveals where judgment, context, coordination, and recovery create or destroy value.

## When to Use It

Use after choosing a workflow opportunity and before a human-AI work contract, playbook, or automation design. Map a bounded recurring motion, not an entire department.

## What It Produces

- Trigger-to-outcome current-state map
- Decision, actor, input, handoff, wait, and rework record
- Failure and exception paths
- Baseline measures and priority redesign target

## Who Should Participate

Include people who perform and receive the work, the accountable workflow owner, the Product Manager, and technical or operational partners. Leadership descriptions cannot replace practitioner observation.

## Evidence to Bring

Bring recent cases, timestamps, artifacts, decision logs, rework examples, exceptions, incidents, and participant observations. Note where the formal process differs from actual work.

## How to Do It

1. Define the trigger, desired outcome, boundary, owner, and unit of work.
2. Reconstruct several real cases rather than the intended process.
3. Map steps, decisions, actors, inputs, outputs, systems, and handoffs.
4. Mark waiting, batching, searching, translation, review, rework, and abandonment.
5. Identify context that is missing, recreated, stale, or contradictory.
6. Trace exception, escalation, and failure recovery paths.
7. Measure cycle time, touch time, review burden, rework, and outcome quality where possible.
8. Identify the constraint or decision that most shapes the outcome.
9. Choose a bounded redesign target and evidence needed before changing it.

## Key Concepts

- A productive motion is a recurring path to an outcome, not a job title.
- Waiting and review are work even when absent from the process diagram.
- Exceptions reveal the true operating model.
- Baselines prevent faster output from masquerading as better work.

## Organizational Applications

Use for discovery synthesis, roadmap decisions, support escalation, launch readiness, experiment review, research intake, and portfolio preparation.

## Common Pitfalls

- Mapping the official process instead of observed work
- Starting with AI insertion points
- Ignoring exception and recovery paths
- Measuring only touch time
- Treating every friction as automation-worthy
- Redesigning the whole system before finding the constraint

## Combine With

Use `human-aipom-work-contract` to assign responsibilities, `aipom-workflow-playbook-builder` to make the redesigned motion reusable, and `aipom-decision-cycle-redesign` for deeper cross-team change.

## Assets and Templates

- [Productive motion map template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

This skill is an original AIPOM synthesis of workflow observation, service-design, and decision-flow practices.
