# Starter Journey: Assess an Organization

Use this journey to move from scattered views of organizational AI capability to an evidence-based profile and an owned improvement roadmap.

## At a Glance

| | |
|---|---|
| **Use when** | The issue spans several teams, initiatives, or operating-model conditions |
| **Decision at stake** | Which consequential conditions should leadership contain, investigate, establish, or scale next? |
| **Core participants** | Accountable executive, Product Operations, product and technology leaders, practitioners, and governance partners |
| **Typical shape** | 4–7 facilitated hours across 2–4 sessions, plus evidence preparation |
| **Primary result** | Seven-category profile, critical gaps, prioritized interventions, owners, and a dated roadmap |
| **Execution layer** | [Assess an Organization command](../../commands/aipom-assess-organization.md) |

The range is a planning guide, not a promised duration. Scope, evidence availability, disagreement, and the number of operating levels represented will change the effort.

## When This Journey Fits

Choose this path when leaders need to understand how the organization currently chooses, funds, builds, evaluates, governs, and learns from AI product work—and the problem cannot be reduced to one initiative or one recurring workflow.

It is especially useful when:

- Different leaders give conflicting accounts of readiness or maturity
- Pilots and tools are multiplying without shared investment discipline
- Policies exist but evidence of product-team use is unclear
- Governance, evaluation, context, or capability gaps affect several initiatives
- Leadership needs a sequenced operating-model roadmap rather than a catalog of improvements

Do not use an organization assessment merely to approve a specific launch. Use the [initiative journey](EVALUATE-AN-AI-INITIATIVE.md) for a scoped launch, scale, funding, sensitive-data, or autonomy decision.

## The Decision at Stake

The assessment should help leadership decide:

> Which organizational conditions are consequential enough to address now, what should be constrained while evidence is weak, and which owned interventions belong in the next 30, 90, 180, and 365 days?

Agree on the organizational scope and decision horizon before collecting scores. The assessment is not complete merely because all questions have answers.

## Who Should Participate

Include enough perspectives to compare intent, documented practice, and actual use:

- One accountable executive sponsor
- Product Operations or another operating-model steward
- Product, design, engineering, data, research, and operations representation proportionate to scope
- Legal, privacy, security, safety, risk, or AI governance partners where relevant
- People who perform or are affected by the practices being assessed
- Owners expected to deliver the first 90 days of the roadmap

One person may represent more than one role in a smaller organization. Do not infer organizational consensus from an executive-only session or a single product team.

## Evidence to Prepare

Bring what already exists; do not create polished documents just to enter the assessment.

Useful evidence includes:

- AI or product strategy and investment decisions
- Portfolio reviews, bet records, stage gates, and stop decisions
- Examples of real product-team workflows and decision records
- Context, source, data, evaluation, monitoring, and incident artifacts
- Policies plus examples showing whether and how teams use them
- Ownership, approval, escalation, and recovery records
- Training, adoption, reuse, outcome, and operational measures
- Perspectives from leadership, practitioners, governance partners, and affected users

Missing evidence is a finding. Label it; do not replace it with confidence or workshop consensus.

## Suggested Engagement Shape

### Before the sessions

1. Name the sponsor, scope, operating levels, and decisions the assessment must support.
2. Ask participants for existing artifacts and examples of actual use.
3. Pre-populate an evidence ledger with claims, sources, confidence, gaps, and disagreements.
4. Identify any immediate legal, privacy, security, safety, accountability, or rollback concern that may require containment before the assessment finishes.

### Session 1: Establish the evidence-based profile

- Confirm scope and explain the difference between discussed, documented, consistently used, and demonstrably effective practice.
- Work through the canonical assessment without asking for information already supplied.
- Preserve differences among leadership, practitioner, and governance perspectives.
- Profile each category and operating level; do not force one overall average.

### Session 2: Interpret consequential conditions

- Identify critical gaps before ranking general improvement opportunities.
- Separate missing evidence from weak practice and specialist decisions still required.
- Route only consequential conditions to the relevant category advisors.
- Agree what must be contained, learned, established, or scaled.

### Session 3: Build the roadmap

- Select the smallest interventions capable of changing the priority conditions.
- Sequence dependencies across 30, 90, 180, and 365 days.
- Name owners, evidence milestones, decision gates, review cadence, and deferred work.
- Check the plan against real capacity; fewer owned motions are better than parallel transformation theater.

Sessions may be combined or split. The assessment and roadmap should preserve one context ledger so participants do not have to repeat evidence.

## Smallest Useful Version

When time or evidence is limited, run a 60–90 minute scoping and critical-condition review:

1. Define the scope and one leadership decision.
2. Gather two or more perspectives and the evidence already available.
3. Identify the most consequential known gap, disagreement, or missing evidence.
4. Assign one containment or evidence-producing action and a review date.

Call this a scoped diagnostic, not a full organization assessment. Do not publish a seven-category maturity profile unless the intended canonical questions and perspectives have been covered.

## What the Journey Produces

- Assessment scope and evidence ledger
- Seven-category profiles for a full assessment
- Confidence, disagreement, and critical-gap record
- Prioritized conditions and constrained decisions
- Selected interventions and dependencies
- Owned 30-, 90-, 180-, and 365-day roadmap
- Unresolved questions, specialist decisions, and next review date

The useful result is leadership agreement about what to do, constrain, investigate, or defer—not the radar chart.

## Decision Authority and Escalation

The assessment team may synthesize evidence and recommend interventions. It does not approve funding, accept risk, authorize data use, certify compliance, or override accountable specialists.

- The executive sponsor owns the operating-model decision and roadmap commitment.
- Functional leaders own capacity and implementation commitments.
- Legal, privacy, security, safety, risk, and governance specialists retain decisions assigned to their authority.
- Critical gaps must remain visible even when other categories are strong.
- Unsupported maturity cannot exceed `2 — Emerging`.

## What Usually Follows

Within ten working days:

- Confirm roadmap ownership, the first evidence milestone, and review cadence
- Distribute the evidence and disagreement record, not only the summary profile
- Begin the smallest 30-day containment or learning motions
- Route priority conditions to focused AIPOM skills rather than running every category advisor

At the first review, ask what decision, behavior, evidence quality, or outcome changed. Completed artifacts alone do not establish progress.

## Facilitation and Agent Handoff

Use the [Assess an Organization command](../../commands/aipom-assess-organization.md) for the canonical sequence, context handoff, stop rules, and completion requirements. The command orchestrates the [AIPOM Operating Model Assessment](../../skills/aipom-operating-model-assessment/SKILL.md) and [AIPOM Operating Model Roadmap](../../skills/aipom-operating-model-roadmap/SKILL.md).

From the repository root, `./create-starter-pack.sh --pack product-operations-assessment` generates the corresponding working project. Inside a generated project, begin with `$aipom-start` in Codex or `/aipom-start` in Claude Code.
