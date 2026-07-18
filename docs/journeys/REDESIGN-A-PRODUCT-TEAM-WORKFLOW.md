# Starter Journey: Redesign a Product-Team Workflow

Use this journey to improve one recurring product-team decision or productive motion through responsible human-AI collaboration.

## At a Glance

| | |
|---|---|
| **Use when** | Recurring work is slow, inconsistent, context-poor, or being changed through AI assistance |
| **Decision at stake** | Should the team repair, assist, redesign, contain, or stop this workflow change? |
| **Core participants** | Decision owner, people doing and affected by the work, Product Manager, product operations, technical partners, and proportionate governance partners |
| **Typical shape** | 4–7+ facilitated hours across multiple sessions, followed by a bounded pilot over real calendar time |
| **Primary result** | Observed baseline, redesigned decision cycle, explicit responsibilities, pilot evidence, and an adoption decision |
| **Execution layer** | [Redesign a Product-Team Workflow command](../../commands/aipom-redesign-workflow.md) |

The workshop time does not include the real-use pilot. A workflow is not proven because participants liked the design in the room.

## When This Journey Fits

Choose this path when the unit of change is recurring work performed by a product team, such as research synthesis, opportunity selection, experiment review, roadmap decisions, launch preparation, escalation routing, or portfolio analysis.

It is especially useful when:

- AI is being added to produce existing artifacts faster without examining the decision cycle
- Context, handoffs, rework, delays, or unclear authority degrade a recurring decision
- Hidden review labor offsets apparent automation gains
- Teams use different informal workflows and want to test a repeatable practice
- A promising local motion may deserve a playbook after representative use

Do not begin with a vendor feature or an idealized process diagram. Begin with observed cases and the decision or outcome that must improve.

## The Decision at Stake

Frame the work around one recurring decision:

> Based on observed work, should we repair the current cycle, assist a bounded step, redesign the full cycle, or contain the proposed AI use—and how will we know whether the change improves the decision without creating unacceptable burden or risk?

Define what is inside and outside the workflow boundary before assigning tasks to people or AI.

## Who Should Participate

Include:

- The person accountable for the recurring decision
- People who perform the work, receive its outputs, and handle exceptions
- The Product Manager and Product Operations where present
- Relevant design, research, engineering, data, and operations partners
- People affected by the decision or workflow consequences
- Legal, privacy, security, safety, risk, or AI governance partners proportionate to the proposed data, behavior, and authority
- A new-user reviewer before declaring the workflow reusable

Do not design the future workflow only with managers or only with tool enthusiasts. The people carrying the work and review burden must be represented.

## Evidence to Prepare

Bring evidence from actual cases:

- Three or more representative examples, including an exception or failure where possible
- Triggers, inputs, sources, decisions, handoffs, delays, rework, and outcomes
- Cycle time, quality, burden, error, escalation, and affected-user evidence
- Existing tools, prompts, context packages, and informal workarounds
- Decision rights, approvals, autonomy, controls, fallback, and incident history
- Known context, data, behavior, evaluation, or capability constraints

If observations are unavailable, begin by collecting them. A documented ideal is not a trustworthy baseline.

## Suggested Engagement Shape

### Before the sessions

1. Name one recurring decision and its accountable owner.
2. Collect representative cases and establish a provisional baseline.
3. Identify participants who perform, review, receive, and are affected by the work.
4. Flag any proposed data access, automated action, or consequence that requires specialist review.

### Session 1: Observe and diagnose the current motion

- Map the trigger, evidence, context, synthesis, deliberation, decision, action, feedback, and revision.
- Surface hidden labor, missing perspectives, failure modes, delays, and rework.
- Separate workflow problems from tool limitations and organizational policy gaps.
- Agree which outcome and countermeasures the redesign must improve.

### Session 2: Design human-AI responsibilities

- Allocate AI preparation, analysis, recommendation, execution, and monitoring separately.
- Assign human review, judgment, approval, accountability, escalation, and stop authority.
- Define authoritative context, provenance, acceptable behavior, evaluation, fallback, and recovery.
- Choose the smallest redesign capable of changing the decision outcome.

### Between sessions: Run a bounded pilot

- Compare the redesign with the observed baseline using representative cases.
- Record outcomes, cycle time, rework, review burden, exceptions, failures, and user effects.
- Preserve manual fallback and stop authority.
- Revise the design when the evidence changes.

### Session 3: Decide and hand off

- Review pilot evidence and disagreement.
- Decide adopt, revise, contain, or stop.
- Assign the workflow owner, measures, review cadence, escalation, and retirement triggers.
- Build a reusable playbook only when representative use supports standardization.

## Smallest Useful Version

Run a 60–90 minute observed-case review when the team is not ready for a full redesign:

1. Select one recurring decision and one representative case.
2. Map its actual trigger, inputs, handoffs, judgment, authority, and outcome.
3. Identify the most consequential friction or hidden burden.
4. Choose one observation or low-exposure test and a review date.

This is a diagnostic and learning motion. It does not justify automating the workflow or publishing a standard playbook.

## What the Journey Produces

- Observed current-state productive-motion map
- Baseline, friction, failure, and hidden-burden diagnosis
- Human-AI work contract with explicit authority and fallback
- Redesigned decision cycle and bounded pilot plan
- Measures, countermeasures, evidence, and adoption decision
- Owner, review cadence, escalation, and unresolved questions
- Reusable workflow playbook only when evidence earns it

The useful result is an improved, testable decision cycle—not faster production of the same artifacts.

## Decision Authority and Escalation

- The named decision owner retains accountability for the workflow outcome.
- AI may prepare, analyze, recommend, monitor, or perform bounded actions only within explicit authority.
- Required human review must have capacity, criteria, and stop authority.
- Legal, privacy, security, safety, risk, and governance decisions remain with accountable specialists.
- Unclear authority or insufficient recovery evidence requires lower autonomy, narrower scope, or containment.
- Do not standardize a redesign that has not been tested in representative use.

## What Usually Follows

- **Adopt:** assign stewardship, onboard qualified users, and monitor outcome plus burden.
- **Revise:** change the workflow, context, behavior, evaluation, or responsibilities and pilot again.
- **Contain:** limit data, actions, users, or autonomy while resolving a critical gap.
- **Stop:** restore the fallback and retain the evidence that explains the decision.

When a tested motion is stable enough to travel, use the workflow playbook and workflow-to-skill methods to preserve its judgment, evidence, controls, exceptions, ownership, and improvement cadence.

## Facilitation and Agent Handoff

Use the [Redesign a Product-Team Workflow command](../../commands/aipom-redesign-workflow.md) for the canonical sequence, context handoff, stop rules, and completion requirements. The integrated redesign uses the [AIPOM Decision Cycle Redesign](../../skills/aipom-decision-cycle-redesign/SKILL.md) and should produce a [Workflow Playbook](../../skills/aipom-workflow-playbook-builder/SKILL.md) only after representative pilot evidence exists.

From the repository root, `./create-starter-pack.sh --pack team-lead-workflow` generates the corresponding working project. Inside a generated project, begin with `$aipom-start` in Codex or `/aipom-start` in Claude Code.
