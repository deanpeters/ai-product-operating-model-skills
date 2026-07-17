---
name: aipom-autonomy-boundary-designer
description: Define evidence-based boundaries for what an AI system may do independently, with human approval, or never. Use before launch, scaling, or increasing AI authority.
type: component
category: governance-and-accountability
phase: 1
status: active

operating_level:
  - organization
  - product-team
  - initiative

audience:
  - Product Manager
  - Product Operations
  - Engineering
  - Design
  - Legal
  - Privacy
  - Security
  - Risk
  - AI Governance

best_for:
  - Preparing an AI or agentic product for launch
  - Increasing the authority of an existing AI system
  - Resolving disagreement about human approval
  - Reviewing a workflow with vague human-in-the-loop claims

evidence_required:
  - Inventory of proposed AI actions
  - Consequences for users and the organization
  - Existing approval and escalation policies
  - Evaluation or production evidence where available
  - Relevant legal, privacy, security, safety, and contractual constraints

produces:
  - Autonomy boundary matrix
  - Escalation and stop policy
  - Named decision and accountability owners
  - Evidence plan for safely changing autonomy

assessment_questions:
  - GOV-01
  - GOV-02
  - GOV-03
  - WFL-03
  - EVAL-02

maturity_move:
  from: emerging
  to: repeatable

estimated_time: 45-60 min
group_size: 3-8

depends_on:
  - aipom-behavior-contract-builder

combine_with:
  - human-aipom-work-contract
  - aipom-accountability-charter
  - aipom-risk-control-incident-playbook

sources:
  - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
  - https://oecd.ai/en/dashboards/ai-principles/P9
  - https://eur-lex.europa.eu/eli/reg/2024/1689/oj
---

# AIPOM Autonomy Boundary Designer

## What Is It

Use this skill to decide, action by action, what an AI system may do independently, what requires human approval, and what it must never do. Base each boundary on consequences, reversibility, detectability, evidence, and applicable constraints—not on what the technology can technically perform.

The skill changes autonomy governance from undocumented individual judgment into a reviewable operating practice with named owners, escalation triggers, and a path for changing authority when evidence improves or deteriorates.

## Why Use It

“Human in the loop” is not a control unless the loop identifies the action being reviewed, the reviewer, the evidence available, the time allowed, the authority to intervene, and what happens when review fails.

Explicit boundaries help a product team:

- Prevent capability from silently becoming authority
- Match human review to consequence and uncertainty
- Avoid ceremonial approvals that add delay without reducing risk
- Design monitoring, rollback, and escalation around real actions
- Explain authority to users, operators, governance partners, and auditors
- Increase or reduce autonomy through evidence rather than optimism

Completing the matrix does not prove the controls are used. Test the workflow and retain evidence of actual operation.

## When to Use It

Use this skill when an AI system will recommend, communicate, transact, modify records, trigger tools, allocate resources, affect access, or otherwise act on behalf of a person or organization.

Use it before launch, after a consequential incident, when expanding the system’s tools or permissions, when moving from recommendation to execution, or when evaluation evidence changes.

Do not use it as a substitute for legal, privacy, security, safety, accessibility, labor, or sector-specific review.

## What It Produces

The completed artifact contains:

1. Scope and action inventory
2. Action-level autonomy decisions
3. Rationale and supporting evidence
4. Required controls and human review
5. Escalation and stop triggers
6. Named decision, review, and accountability owners
7. Exceptions and unresolved questions
8. Evidence needed to increase, retain, or reduce autonomy

## Who Should Participate

Include the Product Manager, technical owner, workflow operator, and the person accountable for the affected outcome. Add design, research, data, legal, privacy, security, safety, risk, compliance, or domain specialists in proportion to the consequences.

Someone who performs the proposed human review should participate. Do not design oversight solely from management assumptions about how operators work.

## Evidence to Bring

Bring whatever is available; missing evidence is a finding, not a reason to cancel the activity.

Useful evidence includes:

- A concrete list of system actions and tools
- Intended users, affected people, and operating contexts
- Known failure modes and consequences
- Evaluation cases, thresholds, and production observations
- Current permissions, logs, approval flows, rollback mechanisms, and incident history
- Applicable policies, contracts, laws, standards, and sector requirements
- Operator workload, competence, authority, and response-time constraints

Label unsupported claims as assumptions. No evidence of reliable control operation means no maturity claim above `2 — Emerging`.

## How to Do It

### 1. Fix the scope

Name the system, version, environment, users, affected people, jurisdiction or sector assumptions, and decision being made. Separate design-time, test, and production authority.

### 2. Inventory atomic actions

Write actions as verbs with objects: “draft a reply,” “send a reply,” “change an account limit,” or “delete a record.” Split bundled actions because different steps often require different authority.

### 3. Examine consequences

For each action, discuss:

- Potential benefit and harm
- Who is affected and whether they can contest the outcome
- Reversibility and cost of correction
- Detectability and time before harm compounds
- Scale, frequency, and cumulative effects
- Uncertainty, novelty, and evidence quality
- Sensitive data, rights, safety, financial, contractual, or regulatory implications

Do not collapse these dimensions into a decorative risk score. Use them to explain the boundary.

### 4. Set the boundary

Choose one state for each action:

- **Independent within constraints:** the system may act without case-by-case approval while required controls operate.
- **Human approval required:** an authorized person must review the action and relevant evidence before execution.
- **Human execution only:** AI may prepare information, but a human performs the consequential action.
- **Prohibited:** the system must not propose or execute the action in the defined scope.

When evidence is weak or consequences are difficult to reverse, choose the more restrictive boundary.

### 5. Make oversight operational

For every non-prohibited action, name preventive controls, monitoring, logs, thresholds, reviewer competence, response time, fallback behavior, rollback, and the accountable owner.

Confirm the reviewer can understand the evidence, challenge the system, refuse the action, and stop operation. If not, the review is ceremonial.

### 6. Define escalation and stop rules

Specify events that suspend independent action or the whole system, such as threshold breaches, missing logs, novel cases, control failure, material complaints, data drift, security events, or unavailable reviewers.

Name who receives the escalation, who decides whether to resume, and what evidence is required.

### 7. Define the change path

State the evidence required to increase autonomy and the signals that reduce it. Use shadow operation, bounded pilots, representative evaluation, monitored production sampling, and incident learning as appropriate.

### 8. Confirm the decision

Record disagreements, unresolved legal or policy questions, the final human decision owner, the accountable executive or operational owner, and the next test. Do not let the AI facilitator make the authority decision.

## Key Concepts

### Capability Is Not Authority

Technical ability does not grant organizational permission. Authority is delegated by accountable humans within constraints.

### Evidence-Proportionate Autonomy

The scope of independent action should grow only when evidence demonstrates acceptable behavior and effective controls in representative conditions.

### Meaningful Human Oversight

Oversight requires competence, information, time, authority, and a practical ability to intervene. A click-through approval does not satisfy those conditions.

### Least Necessary Authority

Grant only the tools, data, permissions, duration, and action scope necessary for the intended outcome.

### Reversible Before Irreversible

Prefer bounded, observable, and reversible actions while learning. Separate drafting from sending and recommendation from execution.

## Organizational Applications

- Define agent tool permissions before launch
- Review an AI assistant moving from drafting to direct communication
- Set approval rules for refunds, pricing, access, scheduling, or record changes
- Clarify authority across vendors, internal teams, and human operators
- Revisit boundaries after incidents, model changes, or new evidence
- Create a common autonomy pattern across a portfolio without pretending every use case has the same risk

## Common Pitfalls

- Writing one boundary for the entire system instead of action-level decisions
- Treating “human in the loop” as sufficient detail
- Using a numeric risk average to offset a non-negotiable control
- Assigning review to people without time, context, competence, or authority
- Ignoring cumulative harm from frequent low-impact actions
- Assuming logs, rollback, or escalation work without testing them
- Expanding autonomy after a successful demo rather than representative evidence
- Treating completion of the matrix as proof of operational maturity

## Combine With

- `aipom-behavior-contract-builder` to define acceptable and prohibited behavior before assigning authority
- `human-aipom-work-contract` to integrate boundaries into the daily workflow
- `aipom-accountability-charter` to formalize decision rights and escalation
- `aipom-risk-control-incident-playbook` to operationalize detection, rollback, response, and learning

## Assets and Templates

- [Autonomy boundary template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example and critique](examples/weak-example.md)

## Sources

- National Institute of Standards and Technology, [Artificial Intelligence Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10), published January 26, 2023. Supports lifecycle risk management, roles, accountability, and human-AI oversight considerations. Accessed July 16, 2026. NIST notes that AI RMF 1.0 is being revised.
- OECD.AI, [Accountability (OECD AI Principle 1.5)](https://oecd.ai/en/dashboards/ai-principles/P9). Supports role-based accountability, traceability, and ongoing risk management. Accessed July 16, 2026.
- European Union, [Regulation (EU) 2024/1689, Article 14](https://eur-lex.europa.eu/eli/reg/2024/1689/oj). Supports risk-proportionate human oversight for high-risk AI systems. Accessed July 16, 2026. Apply only with appropriate jurisdictional and legal review; this skill is not legal advice and does not establish compliance.

