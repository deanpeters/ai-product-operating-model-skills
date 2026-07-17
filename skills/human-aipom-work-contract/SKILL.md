---
name: human-aipom-work-contract
description: Define AI responsibilities, human judgment, review, decision authority, escalation, and learning in a recurring workflow. Use when human-AI collaboration is vague or unreliable.
type: component
category: product-team-workflows
phase: 1
status: active
operating_level: [product-team, initiative]
audience: [Product Manager, Design, Engineering, Operations, AI Governance]
best_for:
  - Introducing AI into a consequential recurring workflow
  - Fixing vague human-in-the-loop responsibilities
  - Clarifying review, handoffs, and accountability
evidence_required:
  - Current workflow and decision points
  - Roles, inputs, outputs, and failure evidence
  - AI behavior and evaluation evidence
  - Existing authority and escalation policies
produces:
  - Human-AI work contract
  - Review and escalation rules
  - Workflow measures and learning cadence
assessment_questions: [WFL-02, WFL-03, WFL-04, WFL-05, GOV-01]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 45-75 min
group_size: 3-8
depends_on: [aipom-behavior-contract-builder]
combine_with: [aipom-autonomy-boundary-designer, aipom-productive-motion-map, aipom-workflow-playbook-builder]
sources:
  - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
---

# Human-AI Work Contract

## What Is It

Define how humans and AI collaborate in one recurring workflow: what AI may prepare or perform, where human judgment enters, who reviews, who decides, who remains accountable, and how failures improve the work.

## Why Use It

AI adoption often adds hidden review labor, ambiguous authority, and brittle handoffs. A work contract makes the operating design explicit. Its existence is not maturity; observed use and improved workflow evidence are.

## When to Use It

Use after understanding the current workflow and before production adoption or expanded autonomy. Revisit after incidents, role changes, model changes, or workload evidence.

## What It Produces

- Workflow purpose and boundaries
- Step-level human and AI responsibilities
- Decision rights, review, escalation, and fallback
- Context and evidence requirements
- Measures and learning cadence

## Who Should Participate

Include people who perform the work, the Product Manager, technical owner, decision owner, and accountable operational leader. Add affected-user and governance perspectives as consequences require.

## Evidence to Bring

Bring workflow observations, cycle time, rework, decisions, current roles, AI evaluations, operator capacity, exceptions, and incidents. Do not design solely from a process diagram.

## How to Do It

1. Define the workflow outcome, actors, scope, and current baseline.
2. Map decisions, inputs, handoffs, delays, rework, and failures.
3. Split AI drafting, recommendation, execution, and monitoring into distinct responsibilities.
4. Assign human judgment, review, approval, execution, and accountability.
5. Specify required context, provenance, uncertainty, and evidence at each handoff.
6. Define escalation, refusal, absence, overload, fallback, and stop behavior.
7. Check that reviewers have competence, time, information, and authority.
8. Measure decision quality, cycle time, rework, outcomes, and review burden.
9. Pilot, observe actual work, and revise the contract.

## Key Concepts

- **Responsibility is not accountability:** AI can perform work; humans remain accountable.
- **Review is work:** budget capacity and measure burden.
- **Decision rights:** clarify recommend, review, approve, execute, and stop.
- **Graceful degradation:** missing context or people should trigger a safe fallback.

## Organizational Applications

Use for discovery synthesis, support, portfolio analysis, content review, knowledge retrieval, decision support, and agentic workflows.

## Common Pitfalls

- Assigning “AI assists” without a task or boundary
- Adding approval to every step regardless of consequence
- Ignoring reviewer capacity and automation bias
- Omitting context provenance and escalation
- Measuring speed while hiding rework or harm
- Treating the contract as proof of adoption

## Combine With

Use `aipom-behavior-contract-builder` for behavior, `aipom-autonomy-boundary-designer` for authority, and later workflow mapping and playbook skills for deeper redesign and reuse.

## Assets and Templates

- [Work contract template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

- NIST, [AI Risk Management Framework 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10), January 26, 2023. Supports explicit human roles, responsibilities, oversight, and lifecycle risk management. Accessed July 16, 2026.
