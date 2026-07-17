---
name: aipom-workflow-playbook-builder
description: Turn a tested human-AI workflow into an inspectable playbook with context, roles, decisions, examples, controls, measures, fallback, and improvement ownership.
type: component
category: product-team-workflows
phase: 2
status: active
operating_level: [product-team, initiative]
audience: [Product Operations, Product Manager, Design, Engineering, Operations, AI Governance]
best_for: [Making a tested workflow repeatable, Onboarding another team without losing judgment, Governing an AI-assisted operating motion]
evidence_required: [Observed motion map, Human-AI work contract, Behavior and evaluation evidence, Pilot outcomes exceptions and incidents]
produces: [Reusable workflow playbook, Run and exception guidance, Ownership and improvement cadence]
assessment_questions: [WFL-03, WFL-04, WFL-05, CAP-04]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 60-120 min
group_size: 3-8
depends_on: [aipom-productive-motion-map, human-aipom-work-contract]
combine_with: [workflow-to-skill-converter, aipom-context-package-builder, aipom-behavior-contract-builder]
sources: []
---

# AIPOM Workflow Playbook Builder

## What Is It

Capture a tested human-AI productive motion so another qualified team can run, inspect, adapt, and improve it without losing its evidence, judgment, controls, or exception behavior.

## Why Use It

Informal workflows drift, depend on a few experts, and preserve happy paths while forgetting failure recovery. A playbook makes the operating practice visible; observed use and improved outcomes—not the document—establish maturity.

## When to Use It

Use after the workflow has been mapped, responsibilities are explicit, and a bounded pilot has produced evidence. Do not standardize an untested redesign or package one team’s workaround as universal practice.

## What It Produces

- Purpose, trigger, scope, prerequisites, and outcome
- Roles, decisions, context, steps, and handoffs
- Examples, behavior boundaries, controls, escalation, and fallback
- Measures, review cadence, owner, version, and retirement rules

## Who Should Participate

Include practitioners, workflow and decision owners, product and technical partners, a new-user reviewer, and governance partners proportionate to consequence.

## Evidence to Bring

Bring motion maps, work contracts, context packages, evaluations, run records, before-and-after measures, exceptions, incidents, user feedback, and revision decisions.

## How to Do It

1. Confirm that the workflow is sufficiently tested to reuse and name remaining limits.
2. State purpose, trigger, outcome, scope, prerequisites, and non-goals.
3. Define roles, decision rights, accountability, and required competence.
4. Specify authoritative inputs, context assembly, provenance, and exclusions.
5. Write the smallest usable happy path with visible handoffs and review.
6. Add representative examples, weak examples, exceptions, escalation, fallback, and stop rules.
7. Connect behavior and evaluation requirements to decision points.
8. Define outcome, cycle, rework, burden, safety, and adoption measures.
9. Assign an owner, review cadence, versioning, change, and retirement process.
10. Forward-test with a qualified user who did not design it.

## Key Concepts

- Reusable means judgment and failure behavior travel with the steps.
- A playbook is a governed operating artifact, not proof of adoption.
- Minimum viable guidance should be runnable without hiding prerequisites.
- Exceptions are first-class design inputs.

## Organizational Applications

Use to scale research synthesis, support preparation, product reviews, launch checks, portfolio analysis, and other recurring AI-assisted decisions.

## Common Pitfalls

- Publishing before testing actual use
- Describing tools without the decision or outcome
- Hiding context and competence prerequisites
- Documenting only the happy path
- Omitting ownership, measures, and retirement
- Copying across teams without checking local consequence

## Combine With

Use `workflow-to-skill-converter` when the playbook should become an agent-facilitated skill, `aipom-context-package-builder` for reusable inputs, and `aipom-behavior-contract-builder` for testable behavior.

## Assets and Templates

- [Workflow playbook template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

This skill is an original AIPOM synthesis of workflow standardization, human-AI operating design, and continuous-improvement practice.
