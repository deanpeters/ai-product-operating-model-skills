---
name: workflow-to-skill-converter
description: Convert a proven, improved workflow into a governed, reusable skill with context, decisions, examples, guardrails, evaluations, ownership, and maintenance rules.
type: component
category: capability-adoption-and-reuse
phase: 1
status: active
operating_level: [organization, product-team]
audience: [Product Operations, Product Manager, Design, Engineering, Enablement]
best_for:
  - Bottling a workflow that works repeatedly
  - Turning local practice into inspectable organizational capability
  - Preparing a human and agent-readable facilitation method
evidence_required:
  - Current and improved workflow evidence
  - Examples of repeated use and outcomes
  - Context, decisions, guardrails, and failure modes
  - Named steward and intended users
produces:
  - Canonical reusable skill bundle
  - Evidence and readiness decision
  - Stewardship and improvement plan
assessment_questions: [CAP-04, WFL-04, WFL-05, CTX-02]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 60-120 min
group_size: 2-6
depends_on: [human-aipom-work-contract]
combine_with: [aipom-workflow-playbook-builder, aipom-adoption-impact-scorecard]
sources: []
---

# Workflow to Skill Converter

## What Is It

Convert a workflow with demonstrated usefulness into a reusable skill that a human facilitator and an AI agent can run, inspect, evaluate, and improve. This is not a prompt-polishing exercise.

## Why Use It

Local workflows disappear, drift, or spread without their judgment and failure modes. A skill can preserve the productive motion—but packaging an unproven workflow merely scales confusion.

## When to Use It

Use after the workflow has a clear outcome, repeated examples, known decisions, and an owner. If the workflow is still unclear or ineffective, map and redesign it first.

## What It Produces

- Reuse-readiness decision
- Canonical `SKILL.md`, template, and examples
- Context, guardrails, evaluations, and stop rules
- Stewardship, versioning, adoption, and improvement plan

## Who Should Participate

Include workflow practitioners, the outcome owner, Product Operations or enablement, an agent-instruction author, and governance partners where consequences require them.

## Evidence to Bring

Bring observed workflow examples, before-and-after evidence, decisions and exceptions, context inputs, failures, user feedback, and proof that the practice can be repeated.

## How to Do It

1. Confirm the workflow changes a useful decision or outcome.
2. Assess reuse readiness: repeated use, stable core, known variation, owner, and evidence.
3. Extract triggers, inputs, decisions, steps, outputs, handoffs, and completion criteria.
4. Preserve judgment: options, tradeoffs, uncertainty, escalation, and stop rules.
5. Separate essential instructions from templates, examples, references, and assets.
6. Write trigger-rich metadata and concise imperative instructions.
7. Add a worked and weak example that demonstrate reasoning.
8. Define evaluation scenarios and forward-test without leaking expected answers.
9. Assign stewardship, version, review cadence, adoption measures, and retirement rules.

## Key Concepts

- **Proven before packaged:** reusable output requires evidence of a useful motion.
- **Judgment preservation:** encode decisions, not just steps.
- **Progressive disclosure:** keep core instructions lean; load details when needed.
- **Stewardship:** every reusable skill needs an owner and retirement path.

## Organizational Applications

Use for discovery, synthesis, portfolio review, evidence review, governance, context assembly, and other recurring product-team motions.

## Common Pitfalls

- Converting a blank template or one-off prompt
- Scaling a broken workflow
- Removing anti-patterns to shorten instructions
- Embedding confidential context
- Omitting evaluation, ownership, and retirement
- Measuring downloads instead of changed work or outcomes

## Combine With

Use `human-aipom-work-contract` to define collaboration, `aipom-workflow-playbook-builder` for a deeper operating playbook, and `aipom-adoption-impact-scorecard` to measure changed practice.

## Assets and Templates

- [Conversion template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

This skill is an original AIPOM synthesis informed by the repository’s canonical skill specification and contribution workflow.
