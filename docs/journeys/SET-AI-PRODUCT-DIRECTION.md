# Starter Journey: Set AI Product Direction

Use this journey when a Head of Product needs to turn broad or fragmented AI ambition into product choices, portfolio implications, and an owned near-term direction.

## At a Glance

| | |
|---|---|
| **Use when** | AI ambition is broad, competing, vendor-led, or disconnected from product and portfolio choices |
| **Decision at stake** | Where will AI contribute to product strategy, what will the organization avoid, and what moves first? |
| **Core participants** | Head of Product, CTO, portfolio or finance authority, Product Operations, customer or domain representation, and proportionate governance partners |
| **Typical shape** | 3–5 facilitated hours across 2–3 sessions plus evidence preparation |
| **Primary result** | Evidence-aware product thesis, choices and non-goals, portfolio implications, and owned first commitments |
| **Execution layer** | [Set AI Product Direction command](../../commands/aipom-set-product-direction.md) |

## When This Journey Fits

Choose this path when leaders use the same AI language but appear to mean different things, initiatives are accumulating without shared product logic, vendor capabilities are driving priorities, or teams cannot explain what should receive attention and what should not.

Do not use this journey to approve a particular initiative, certify organizational maturity, or create a polished strategy narrative before the choices exist.

## The Decision at Stake

State the leadership decision explicitly:

> Given customer and business evidence, current capabilities, constraints, and portfolio commitments, where should AI contribute to product strategy now, what will we not pursue, and which owned learning or investment motions happen next?

The result must guide allocation and product decisions. “Use AI where it adds value” is not a strategic choice.

## Who Should Participate

Include:

- The Head of Product or equivalent accountable product authority
- The CTO or accountable technology authority
- Portfolio, finance, or business authority proportionate to the commitments
- Product Operations and representative Product Managers or Team Leads who understand actual operating conditions
- Customer, user, research, design, data, and domain perspectives relevant to the proposed focus
- Legal, privacy, security, safety, risk, or AI governance partners where direction creates material constraints

Participation does not transfer decision authority. Preserve disagreements and record who decides each unresolved issue.

## Evidence to Prepare

Bring existing product and business strategy, customer and market evidence, portfolio inventory, spend and capacity, initiative outcomes, stop decisions, dependencies, incidents, governance constraints, and examples of what teams are actually doing.

Missing evidence is a strategic assumption, not permission to make the thesis sound more certain.

## Suggested Engagement Shape

### Before the sessions

1. Name the accountable decision owner, scope, horizon, and decisions the direction must guide.
2. Assemble existing evidence, stated ambitions, active bets, constraints, and disagreements.
3. Separate product choices from initiative readiness and technical or specialist approvals.

### Session 1: Make the product thesis explicit

- Define the customer, product, economic, and operating conditions that matter.
- Identify where AI may change those conditions and where it is inappropriate or unsupported.
- State choices, non-goals, causal assumptions, boundaries, and evidence gaps.
- Identify the next bounded learning bets rather than promising broad transformation.

### Session 2: Test the portfolio implications

- Classify current work as exploration, validation, scaling, enabling capability, mandatory risk work, containment, or stop candidates.
- Expose concentration, duplication, premature scaling, vendor momentum, and zombie pilots.
- Decide what receives attention now, what remains constrained, and what should stop or return to learning.

### Session 3: Commit and communicate

- Record the first commitments, owners, capacity implications, and evidence milestones.
- Name unresolved technical, financial, governance, and specialist decisions.
- Define the events and evidence that will trigger review or revision.
- Communicate choices without turning uncertainty into slogans.

## Smallest Useful Version

For an early leadership conversation, run a 60–90 minute direction-framing review:

1. Name one customer or business condition and one decision leadership must make.
2. State one plausible AI role, one non-goal, and the evidence behind each.
3. Identify the current portfolio contradiction that matters most.
4. Assign one evidence-producing action and a review date.

Call this a provisional direction, not a complete product strategy.

## What the Journey Produces

- Product and portfolio decision scope
- AI product strategy thesis
- Choices, non-goals, boundaries, and assumptions
- Portfolio posture and contradiction diagnosis
- First learning, investment, containment, and stop motions
- Owners, evidence milestones, unresolved decisions, and review trigger

## Decision Authority and Escalation

The Head of Product owns product direction within the organization's authority model. The CTO owns technical decisions; finance or portfolio authorities own reserved investment decisions; and legal, privacy, security, safety, risk, and governance specialists retain their authority.

A strong strategic fit cannot offset a critical readiness or control gap. This journey determines direction, not initiative approval.

## Facilitation and Agent Handoff

Use the [Set AI Product Direction command](../../commands/aipom-set-product-direction.md) for the canonical sequence, context handoff, stop rules, and completion requirements. The journey uses the [strategy thesis advisor](../../skills/aipom-strategy-thesis-advisor/SKILL.md) and [portfolio posture advisor](../../skills/aipom-portfolio-posture-advisor/SKILL.md) as its core methods.

From the repository root, `./create-starter-pack.sh --pack head-of-product-direction` generates the corresponding working project. Inside a generated project, begin with `$aipom-start` in Codex or `/aipom-start` in Claude Code.
