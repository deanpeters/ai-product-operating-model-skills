# Starter Journey: Establish the AI Technical Readiness Bar

Use this journey when a CTO needs a consequence-aware standard for the technical evidence and operating conditions required before AI products launch, scale, change materially, or receive greater authority.

## At a Glance

| | |
|---|---|
| **Use when** | Teams use inconsistent readiness claims or technical review happens too late and without shared evidence expectations |
| **Decision at stake** | What technical evidence and operating capability are required for each class of launch, scale, data, dependency, and autonomy decision? |
| **Core participants** | CTO, architecture and engineering, data, operations, Product Managers, Product Operations, security, privacy, risk, governance, and affected domain owners |
| **Typical shape** | 5–9 facilitated hours across preparation and 2–4 sessions; exercises may add time |
| **Primary result** | Consequence-aware technical readiness bar with evidence, ownership, exception, expiry, and review rules |
| **Execution layer** | [Establish the AI Technical Readiness Bar command](../../commands/aipom-establish-technical-readiness-bar.md) |

## When This Journey Fits

Choose this path when “production ready” means different things across teams, pilots are approaching scale without tested dependencies or recovery, evaluation is reduced to model metrics, or technical specialists repeatedly reconstruct launch expectations from scratch.

Do not turn the result into a universal checklist. Requirements must vary with intended behavior, affected people, scale, data, environment, autonomy, and failure consequence.

## The Decision at Stake

State the technical leadership decision:

> For each material consequence class, what must be demonstrated about dependencies, context, data, behavior, evaluation, monitoring, control, fallback, rollback, incident response, and ownership before the proposed action is technically supportable?

The bar informs accountable decisions. It does not replace product, investment, legal, privacy, security, safety, risk, or governance approval.

## Who Should Participate

Include:

- The CTO or equivalent accountable technical executive
- Architecture, engineering, platform, data, evaluation, operations, reliability, and support owners
- Product Managers, Product Operations, and Team Leads who integrate or operate the work
- Security, privacy, legal, safety, risk, compliance, procurement, and AI governance specialists proportionate to scope
- Domain and affected-user representation where technical failure changes real-world outcomes

Name who owns the standard, who supplies evidence, who reviews each area, and who may approve an exception.

## Evidence to Prepare

Bring architecture and data flows, vendor and model dependencies, contracts and service terms, source ownership, data provenance and permissions, behavior contracts, evaluation results, monitoring, incidents, runbooks, rollback tests, portability tests, support capacity, and examples of past launch decisions.

Documents and diagrams are partial evidence until operation, failure, portability, and recovery have been tested at a representative level.

## Suggested Engagement Shape

### Before the sessions

1. Define the decision classes and consequences the readiness bar must distinguish.
2. Collect existing architecture, dependency, context, data, evaluation, operations, and incident material.
3. Identify immediate critical gaps that should constrain an active initiative before the standard is complete.

### Session 1: Define consequence classes and dependencies

- Define scale, data, environment, autonomy, and failure-consequence tiers.
- Map material model, vendor, infrastructure, integration, talent, contractual, and operating dependencies.
- Define required portability, degradation, outage, switching, and exit evidence.

### Session 2: Define information and evaluation evidence

- Establish purpose-specific context and data ownership, provenance, permission, quality, refresh, and lifecycle expectations.
- Define acceptable behavior and the product, model, workflow, human, and production evaluations needed for each decision class.
- State thresholds, limitations, reviewers, and actions triggered by failure.

### Session 3: Define operation and recovery

- Connect monitoring signals to authorized containment, fallback, rollback, and stop actions.
- Assign incident command, technical action, product decisions, specialist review, communications, and evidence preservation.
- Require representative exercises where consequence warrants them.

### Session 4: Establish the operating standard

- Assemble required evidence by consequence class.
- Name owners, reviewers, decision authority, exceptions, expiry, and re-review triggers.
- Define how the bar changes after incidents, material system changes, new evidence, or recurring failure.

## Smallest Useful Version

For one imminent decision, run a 90-minute scoped technical-bar review:

1. Define the exact launch, scale, data, vendor, or autonomy decision.
2. Identify the three most consequential dependency, evaluation, or recovery claims.
3. Examine the evidence supporting those claims.
4. Constrain the action, assign remediation, and set a re-review date where evidence is insufficient.

Call this an initiative-specific technical review, not an organization-wide readiness standard.

## What the Journey Produces

- Technical decision and consequence classes
- Dependency, concentration, portability, and exit evidence requirements
- Context and data readiness expectations
- Behavior and evaluation coverage requirements
- Monitoring, control, fallback, rollback, incident, and recovery expectations
- Owners, reviewers, exception authority, expiry, and review triggers
- Critical gaps and permitted interim motions

## Decision Authority and Escalation

The CTO owns accountable technical decisions within the organization's governance model. Product leaders own product direction, finance and portfolio authorities own reserved investment decisions, and legal, privacy, security, safety, risk, and governance specialists retain their decisions.

No aggregate score may compensate for a critical gap. An unmet non-negotiable bar constrains the corresponding action until the accountable authority records a permitted, time-bounded exception.

## Facilitation and Agent Handoff

Use the [Establish the AI Technical Readiness Bar command](../../commands/aipom-establish-technical-readiness-bar.md) for the canonical sequence, context handoff, stop rules, and completion requirements. Apply the packaged dependency, context, data, evaluation, and incident methods in proportion to the decision classes being established.

From the repository root, `./create-starter-pack.sh --pack cto-technical-readiness` generates the corresponding working project. Inside a generated project, begin with `$aipom-start` in Codex or `/aipom-start` in Claude Code.
