---
name: aipom-accountability-charter
description: Assign human decision rights, accountability, review, contribution, escalation, and evidence duties for a material AI product or recurring operating decision.
type: component
category: governance-and-accountability
phase: 2
status: active
operating_level: [organization, portfolio, product-team, initiative]
audience: [CPO, CTO, Product Manager, Engineering, Legal, Privacy, Security, Risk, AI Governance]
best_for: [Clarifying ownership before a consequential AI decision, Resolving committee ambiguity, Connecting accountability to evidence and escalation]
evidence_required: [Decision inventory and consequences, Existing authority and policy, Workflow and system responsibilities, Approval exception and incident examples]
produces: [AI accountability charter, Decision-rights and evidence matrix, Escalation and exception rules]
assessment_questions: [GOV-01, GOV-02, GOV-03, GOV-04]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 45-90 min
group_size: 4-10
depends_on: [responsible-aipom-governance-advisor]
combine_with: [aipom-autonomy-boundary-designer, human-aipom-work-contract, aipom-risk-control-incident-playbook]
sources:
  - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
  - https://oecd.ai/en/dashboards/ai-principles/P9
---

# AIPOM Accountability Charter

## What Is It

Assign named human decision rights and duties for a material AI product, workflow, or recurring decision. Distinguish who proposes, contributes, reviews, approves, executes, monitors, escalates, stops, and remains accountable.

## Why Use It

Committees and “human in the loop” language often spread participation while leaving authority and accountability unclear. A charter connects each consequential decision to one accountable human, required evidence, and an escalation path.

## When to Use It

Use before material funding, data use, launch, autonomy, exception, incident, or retirement decisions. Align with existing corporate authority; do not invent legal or fiduciary authority through a workshop.

## What It Produces

- Scope, decisions, consequences, and governing constraints
- Named proposal, contribution, review, approval, execution, monitoring, stop, and accountability roles
- Evidence required for each decision
- Escalation, absence, conflict, exception, and review rules

## Who Should Participate

Include the accountable business or product leader, decision operators, product and technical owners, and legal, privacy, security, safety, risk, or governance partners proportionate to the consequence.

## Evidence to Bring

Bring delegations of authority, policies, decision records, workflow contracts, autonomy boundaries, incidents, exceptions, regulatory or contractual duties, and examples where ownership failed.

## How to Do It

1. Define scope, operating level, consequence, and decisions covered.
2. Inventory decision moments across investment, data, behavior, launch, operation, incident, and retirement.
3. Name one accountable human role for each decision and verify actual authority.
4. Assign proposal, contribution, review, approval, execution, monitoring, escalation, and stop duties.
5. Specify the evidence and dissent that must reach the decision owner.
6. Define conflicts, unavailable owners, time pressure, overrides, and escalation.
7. Make exceptions time-bounded with rationale, compensating controls, owner, and expiry.
8. Test the charter against representative failure and disagreement scenarios.
9. Set review triggers and evidence that the charter is used.

## Key Concepts

- Participation does not equal accountability.
- A single accountable owner can depend on many required reviewers.
- Authority must exist in the organization, not only on the template.
- Dissent is decision evidence, not a facilitation problem to erase.

## Organizational Applications

Use for AI initiative governance, agent authority, portfolio exceptions, data approvals, production incidents, vendor adoption, and retirement decisions.

## Common Pitfalls

- Assigning accountability to a committee or “the business”
- Using role labels without verifying authority
- Making every reviewer an approver
- Omitting evidence and stop duties
- Ignoring absence, conflict, and urgent-decision paths
- Treating a signed charter as proof of use

## Combine With

Use `aipom-autonomy-boundary-designer` to define AI authority, `human-aipom-work-contract` for workflow duties, and `aipom-risk-control-incident-playbook` for operational response.

## Assets and Templates

- [Accountability charter template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

- NIST, [AI Risk Management Framework 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10), January 26, 2023. Supports explicit roles, responsibilities, authority, oversight, and lifecycle risk management. Accessed July 16, 2026.
- OECD.AI, [OECD AI Principle 1.5: Accountability](https://oecd.ai/en/dashboards/ai-principles/P9). Supports organizational accountability, traceability, and responsible stewardship. Accessed July 16, 2026.

This charter supports organizational governance; it does not establish legal or regulatory compliance.
