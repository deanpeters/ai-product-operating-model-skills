# Starter Journey: Evaluate an AI Initiative

Use this journey to decide whether a specific AI opportunity should be explored, funded, launched, scaled, constrained, remediated, paused, or stopped.

## At a Glance

| | |
|---|---|
| **Use when** | A material decision is pending for one AI opportunity or initiative |
| **Decision at stake** | What motion, if any, is justified at the proposed scope and consequence? |
| **Core participants** | Accountable decision owner, Product Manager, technical and operational owners, affected-user representation, and proportionate specialists |
| **Typical shape** | 4–8+ facilitated hours across 2–4 sessions, plus evidence preparation; depth varies with consequence |
| **Primary result** | Proceed, proceed with constraints, remediate and re-review, pause, or stop recommendation |
| **Execution layer** | [Evaluate an AI Initiative command](../../commands/aipom-evaluate-initiative.md) |

The range is deliberately broad. A low-exposure discovery decision should not require the same review as production autonomy, sensitive-data use, or a high-consequence launch.

## When This Journey Fits

Choose this path when a named decision is pending for one opportunity, pilot, product feature, internal AI system, agentic workflow, vendor-dependent capability, or deployed initiative.

It is especially useful before:

- Funding discovery or validation
- Moving from prototype to pilot
- Launching or scaling to more users
- Increasing autonomy or action authority
- Introducing sensitive data, a new vendor, or a new jurisdiction
- Returning to operation after an incident or material change

Do not use this journey to manufacture approval for a preferred solution. Begin with the customer or operational problem, alternatives, consequence, and evidence.

## The Decision at Stake

State the decision in scope-specific terms:

> Given the proposed users, environment, data, behavior, authority, exposure, and evidence, should this initiative proceed now—and under what constraints, conditions, ownership, expiry, and review trigger?

A general statement that an initiative is “ready” is not sufficient. Readiness changes with scope, population, autonomy, data, jurisdiction, and consequence.

## Who Should Participate

Include:

- One accountable owner for the material decision
- The Product Manager and relevant product, design, research, engineering, data, and operations owners
- Finance or portfolio leadership when investment or economics are material
- Affected-user, customer, worker, or domain representation appropriate to the use case
- Legal, privacy, security, safety, risk, compliance, or AI governance specialists proportionate to consequence
- The people responsible for operation, monitoring, support, escalation, rollback, and incident response

Workshop participation does not imply specialist approval. Record each required decision and who has authority to make it.

## Evidence to Prepare

Useful evidence includes:

- Customer or workflow problem evidence and credible alternatives
- Opportunity frame, outcome logic, baseline, and value assumptions
- Bet owner, scope, non-goals, next test, and stop conditions
- Economics, total costs, dependencies, and vendor exposure
- Architecture, context, sources, data rights, quality, and lifecycle evidence
- Behavior contract, representative evaluations, thresholds, and production signals
- Human-AI responsibilities, autonomy boundaries, accountability, controls, fallback, and recovery
- Adoption, operator capacity, support, incident, and affected-user evidence

Bring partial evidence rather than delaying until every artifact exists. Missing evidence should reduce confidence, permitted scope, or authority; it should not be silently converted into a positive readiness claim.

## Suggested Engagement Shape

### Before the sessions

1. Name the exact decision, accountable owner, proposed scope, and consequence.
2. Collect existing artifacts into a single evidence and assumption ledger.
3. Identify specialist decisions required and invite the relevant authorities.
4. Separate the material decision from any lower-exposure learning motion that could continue safely.

### Session 1: Frame the opportunity and value

- Confirm the problem, affected people, current alternatives, and non-goals.
- Expose the causal path from AI-enabled behavior to customer, operational, and economic outcomes.
- Establish the bet owner, next evidence-producing test, constraints, and stop conditions.
- Stop if the initiative is solution-first and the underlying opportunity remains unsupported.

### Session 2: Examine readiness and critical gaps

- Review economics and platform dependencies.
- Examine workflow, context, data, behavior, evaluation, and production evidence.
- Make human authority, accountability, controls, escalation, rollback, and incident response explicit.
- Preserve disagreements and specialist decisions; do not combine everything into one compensating score.

### Session 3: Make and record the decision

- Identify critical gaps and state which actions they constrain.
- Choose proceed, proceed with constraints, remediate and re-review, pause, or stop.
- Record the permitted interim motion, conditions, owners, expiry, measures, and next review trigger.
- Confirm who makes the final accountable and specialist decisions after the session.

High-consequence initiatives may require additional specialist reviews or evidence collection between sessions. The AIPOM journey coordinates those decisions; it does not impersonate them.

## Smallest Useful Version

For an early, low-exposure opportunity, run a 60–90 minute decision-framing review:

1. Define the problem, affected people, alternatives, and proposed AI role.
2. Name the decision owner, consequence, evidence, and assumptions.
3. Select the smallest evidence-producing test with explicit non-goals and stop conditions.
4. Record which material decisions remain out of scope.

This can justify further discovery. It cannot establish launch, scale, sensitive-data, or autonomy readiness.

## What the Journey Produces

- Opportunity and scope definition
- Outcome and causal-value map
- Bet ownership, constraints, next test, and stop conditions
- Evidence, confidence, assumption, and disagreement ledger
- Proportionate readiness profiles and critical gaps
- Recommendation and permitted interim motion
- Required specialist decisions
- Conditions, owners, expiry, measures, and next review trigger

The useful result is a bounded decision with explicit evidence conditions—not a polished business case that hides uncertainty.

## Decision Authority and Escalation

The facilitation team may synthesize evidence and recommend a path. It does not authorize investment, accept risk, approve data use, certify compliance, or make decisions reserved for accountable specialists.

- The named business or product authority owns the overall investment or product decision.
- Legal, privacy, security, safety, risk, finance, and governance authorities own decisions within their remit.
- A critical control gap cannot be offset by expected value or strong model performance.
- Missing specialist approval remains a constraint, not implied consent.
- Conditions require an owner, expiry, monitoring, and a re-review trigger.

## What Usually Follows

- **Proceed:** execute the scoped motion and begin production evidence review when operation starts.
- **Proceed with constraints:** monitor the limits and return before expiry or material change.
- **Remediate and re-review:** assign prerequisites and do not perform the blocked action.
- **Pause:** preserve learning and evidence while ownership, capacity, or external conditions change.
- **Stop:** record why, protect useful learning, and retire dependent work deliberately.

Repeat the review after material changes to model, data, vendor, workflow, population, autonomy, jurisdiction, incident history, or intended use.

## Facilitation and Agent Handoff

Use the [Evaluate an AI Initiative command](../../commands/aipom-evaluate-initiative.md) for the canonical sequence, context handoff, stop rules, and completion requirements. The full path culminates in the [AIPOM Initiative Readiness Review](../../skills/aipom-initiative-readiness-review/SKILL.md); earlier decisions should use only the proportionate components needed to support the decision.

From the repository root, `./create-starter-pack.sh --pack product-manager-initiative` generates the corresponding working project. Inside a generated project, begin with `$aipom-start` in Codex or `/aipom-start` in Claude Code.
