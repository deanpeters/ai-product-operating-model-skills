# Worked Example: Customer-Support Resolution Agent

**Synthetic example.** The organization, evidence, and decisions below are fictional.

## Situation

A subscription-software company is testing an AI agent that classifies support requests, drafts responses, sends routine instructions, issues small service credits, and proposes account changes. The pilot has operated in shadow mode for four weeks.

The decision is whether to permit any production actions without case-by-case approval.

## Evidence Reviewed

| Evidence | What it supports | Limitation |
|---|---|---|
| 600 shadow-mode cases | Classification accuracy is acceptable for common request types | One product line and only four weeks |
| 80 edge and adversarial cases | The agent refuses several unsupported requests | Weak coverage of account-access requests |
| Current support approval policy | Supervisors may approve credits up to $100 | Written policy does not prove consistent operation |
| Operator interviews | Agents can review drafts in under two minutes | Peak-hour workload was not observed |
| Tool and audit-log test | Actions are logged and service credits can be reversed | Account-access changes have no tested rollback |

Evidence demonstrates a bounded pilot, not repeatable organizational practice. The maturity claim remains `2 — Emerging`.

## Assumptions

| Assumption | Consequence if wrong | Evidence needed |
|---|---|---|
| Peak-hour reviewers remain available | Approval queues could create unsafe shortcuts | Peak-volume simulation |
| Routine instructions remain stable | Agent could send obsolete recovery steps | Source freshness and expiry test |

## Boundary Matrix

| Atomic action | Consequence and reversibility | Boundary | Controls and rationale |
|---|---|---|---|
| Classify a request for routing | Low direct consequence; routing is reversible | Independent within constraints | Monitor sampling, confidence threshold, and fallback queue |
| Draft a response | No external effect until sent | Independent within constraints | Cite approved sources and label uncertainty for reviewer |
| Send routine setup instructions | Moderate customer impact; correction is possible | Human approval required | Evidence is too narrow for direct sending; reviewer sees source and draft |
| Issue a service credit up to $25 | Financial action but reversible and bounded | Human approval required | Supervisor approval, transaction log, daily aggregate limit |
| Change account access | Security and customer-rights implications; rollback untested | Human execution only | AI may summarize the request but cannot invoke the access tool |
| Alter contract terms or close an account | High consequence and potentially difficult to reverse | Prohibited | Outside intended purpose and delegated authority |

## Escalation and Stop Policy

| Trigger | Immediate behavior | Recipient | Resume owner |
|---|---|---|---|
| Missing approved source | Do not draft or send; route to human | Knowledge owner | Support operations director |
| Confidence below threshold or novel intent | Route without action | Queue supervisor | Product Manager |
| Audit logging unavailable | Disable all tool actions | Engineering on-call | Accountable service owner |
| Material complaint or unauthorized action | Suspend production agent | Incident lead and privacy/security partners | Support operations director after review |

## Human Oversight Decision

Reviewers demonstrated competence and authority during ordinary-volume observation, but peak-volume capacity remains untested. The system therefore cannot send messages or issue credits independently.

## Next Action

The Product Manager will run a two-week bounded pilot with human approval for all external actions, including a peak-volume simulation and expanded access-request evaluation set. The support operations director remains accountable for the production decision.

## Unresolved Questions

- Can the knowledge source expire instructions automatically?
- What customer notice is required when AI drafts or sends a response?
- Does the daily aggregate credit limit need a team-level control?
