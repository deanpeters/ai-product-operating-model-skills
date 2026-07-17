---
name: aipom-risk-control-incident-playbook
description: Design preventive controls, detection, triage, containment, rollback, communication, investigation, remediation, learning, and reporting for AI incidents.
type: component
category: governance-and-accountability
phase: 3
status: active
operating_level: [organization, product-team, initiative]
audience: [Product Operations, Product Manager, Team Lead, Engineering, Operations, Security, Privacy, Legal, Risk, AI Governance]
best_for: [Preparing an AI product for operation, Repairing weak rollback or escalation, Coordinating product and governance incident duties]
evidence_required: [Behavior and autonomy boundaries, Evaluation thresholds and production signals, Existing incident and escalation systems, Applicable reporting and preservation duties]
produces: [AI risk-control map, Incident response playbook, Exercise and learning plan]
assessment_questions: [GOV-02, GOV-03, GOV-04, GOV-05, EVAL-05]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 90-180 min plus exercise
group_size: 5-12
depends_on: [aipom-accountability-charter, aipom-autonomy-boundary-designer, aipom-eval-scorecard-builder]
combine_with: [aipom-production-evidence-review, aipom-trust-assurance-pack-builder, aipom-initiative-readiness-review]
sources:
  - https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
  - https://eur-lex.europa.eu/eli/reg/2024/1689/oj
  - https://oecd.ai/en/site/incidents/
---

# AIPOM Risk-Control Incident Playbook

## What Is It

Connect material AI risks to preventive controls, detection, triage, containment, fallback, rollback, communication, evidence preservation, investigation, remediation, learning, and external reporting where applicable.

## Why Use It

Policies do not stop incidents, and generic software response may miss probabilistic behavior, model or context changes, human overreliance, affected groups, vendor dependencies, and regulatory reporting duties.

## When to Use It

Use before operation or expanded autonomy, and revise after material change, near miss, incident, or exercise. Engage accountable legal and regulatory specialists; this playbook does not determine compliance or reporting obligations.

## What It Produces

- Risk-to-control and detection map
- Severity, triage, containment, rollback, and escalation rules
- Roles, decision authority, communications, evidence preservation, and reporting routes
- Exercise, remediation, learning, and verification plan

## Who Should Participate

Include the Team Lead, Product Manager, Product Operations where present, product and technical owners, operations, security, privacy, legal, risk, communications, domain experts, affected-user representation, and the accountable executive.

## Evidence to Bring

Bring behavior contracts, autonomy boundaries, scorecards, monitoring, data and context flows, dependencies, incident systems, policies, prior failures, reporting duties, contacts, and tested rollback mechanisms.

## How to Do It

1. Define system scope, consequences, affected parties, jurisdictions, and accountable owner.
2. Map hazards and failure modes to preventive, detective, corrective, and recovery controls.
3. Define signals, severity, confidence, triage, and thresholds for containment or stop.
4. Assign incident command, technical action, product decision, communications, specialist review, and accountability.
5. Specify safe state, fallback, rollback, access restriction, and vendor escalation.
6. Define internal and external communications, affected-party support, and required reporting routes with specialists.
7. Preserve logs, versions, inputs, outputs, context, decisions, and chain of custody without destroying evidence through premature changes.
8. Define investigation, root and contributing factors, remediation, verification, and reopen criteria.
9. Feed learning into behavior, evaluation, context, controls, training, and portfolio decisions.
10. Run tabletop and technical exercises; record observed gaps and owners.

## Key Concepts

- Detection must map to an authorized action.
- Safe state differs by product and consequence.
- Near misses are operating evidence.
- Investigation should preserve evidence and avoid scapegoating operators.

## Organizational Applications

Use for harmful outputs, unauthorized actions, privacy or security events, evaluation regression, context corruption, vendor failure, automation bias, and affected-group harm.

## Common Pitfalls

- Copying a generic incident plan without AI behavior
- Defining severity with no affected-party view
- Naming rollback that has never been tested
- Changing the system before preserving evidence
- Making legal or communications review the incident commander
- Closing incidents without verifying remediation

## Combine With

Use `aipom-production-evidence-review` for recurring signals, `aipom-trust-assurance-pack-builder` for current trust evidence, and `aipom-initiative-readiness-review` to block launch when recovery is unready.

## Assets and Templates

- [Risk-control incident template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

- NIST AI Resource Center, [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). Manage 4 covers monitoring, incident response, recovery, communication, and change management. Accessed July 17, 2026; NIST notes AI RMF 1.0 is under revision.
- European Union, [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj), especially Articles 9, 72, and 73 on lifecycle risk management, post-market monitoring, and serious-incident reporting for systems in scope. Accessed July 17, 2026.
- OECD.AI, [AI Incidents](https://oecd.ai/en/site/incidents/). Supports consistent incident concepts and learning from reported risks and incidents. Accessed July 17, 2026.

Requirements vary by role, system, sector, and jurisdiction. Completing this skill does not establish compliance or replace specialist judgment.
