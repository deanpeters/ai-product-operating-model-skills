---
name: aipom-operating-model-assessment
description: Assess AI product operating-model maturity across seven categories using evidence, disagreement, and critical-gap logic. Use to identify consequential gaps and next interventions.
type: workflow
category: cross-category
phase: 1
status: active

operating_level:
  - organization
  - portfolio
  - product-team

audience:
  - CPO
  - CTO
  - VP Product
  - Product Operations
  - Product Manager
  - Design
  - Engineering
  - Data
  - Research
  - Legal
  - Privacy
  - Security
  - Risk
  - AI Governance

best_for:
  - Establishing an evidence-based baseline before operating-model design
  - Identifying the weakest consequential organizational conditions
  - Comparing leadership intent with product-team and governance practice
  - Preparing an AI product operating-model roadmap

evidence_required:
  - Existing strategy, portfolio, workflow, context, evaluation, governance, and capability artifacts
  - Examples showing whether documented practices are actually used
  - Decision records, evaluation results, adoption evidence, and outcome measures where available
  - Perspectives from leadership, practitioners, governance partners, and affected users where relevant

produces:
  - Seven-category maturity profile
  - Evidence and confidence ledger
  - Disagreement and critical-gap report
  - Prioritized intervention recommendations
  - Named owners and next evidence-producing actions

assessment_questions:
  - STR-01
  - STR-02
  - STR-03
  - STR-04
  - STR-05
  - POR-01
  - POR-02
  - POR-03
  - POR-04
  - POR-05
  - WFL-01
  - WFL-02
  - WFL-03
  - WFL-04
  - WFL-05
  - CTX-01
  - CTX-02
  - CTX-03
  - CTX-04
  - CTX-05
  - EVAL-01
  - EVAL-02
  - EVAL-03
  - EVAL-04
  - EVAL-05
  - GOV-01
  - GOV-02
  - GOV-03
  - GOV-04
  - GOV-05
  - CAP-01
  - CAP-02
  - CAP-03
  - CAP-04
  - CAP-05

maturity_move:
  from: absent
  to: emerging

estimated_time: 2-4 hours across one or more sessions
group_size: 4-20

depends_on: []

combine_with:
  - aipom-operating-model-roadmap
  - aipom-strategy-thesis-advisor
  - aipom-portfolio-posture-advisor
  - aipom-workflow-opportunity-advisor
  - aipom-context-readiness-advisor
  - aipom-evaluation-strategy-advisor
  - responsible-aipom-governance-advisor
  - aipom-capability-maturity-advisor

sources:
  - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
  - https://oecd.ai/en/accountability/
---

# AIPOM Operating Model Assessment

## What Is It

Use this workflow to assess how an organization currently chooses, builds, evaluates, governs, and learns from AI-powered products and AI-assisted product work across seven connected categories.

The workflow uses the canonical [35-question assessment](../../assessments/aipom-operating-model-assessment.md), [evidence rubric](../../assessments/evidence-rubric.md), and [scoring model](../../assessments/scoring-model.md). Do not copy, rewrite, or improvise replacement questions inside the workflow.

The assessment changes the organization from unexamined maturity claims toward an evidence-based profile with consequential gaps, named owners, and next interventions. The score is navigation; the changed decision and organizational motion are the point.

## Why Use It

Organizations commonly confuse AI activity with capability and documentation with adoption. A single radar chart can also hide different operating levels, weak evidence, serious disagreement, or a missing non-negotiable control.

This workflow helps leaders and teams:

- Distinguish discussed, documented, used, and outcome-improving practices
- Compare leadership intent with practitioner and governance experience
- Separate organization maturity from initiative readiness
- Identify the weakest consequential condition rather than the lowest arithmetic score
- Prevent strong low-risk scores from offsetting critical gaps
- Route findings to concrete skills, owners, and evidence-producing actions
- Establish a baseline that can be revisited without rewarding performative activity

## When to Use It

Use the assessment before an operating-model design sprint or roadmap, during strategic planning, after rapid growth in AI initiatives, when governance and product teams disagree about readiness, or when leaders need to determine why pilots are not becoming reliable capability.

Do not use the organization assessment as a launch approval for one initiative. Use an initiative-readiness review for that decision while keeping the two profiles separate.

## What It Produces

The assessment report includes:

1. Scope, operating levels, and participants
2. Evidence inventory and limitations
3. Scores and confidence for all 35 questions
4. Seven category profiles
5. Material disagreements and missing perspectives
6. Critical gaps that constrain action
7. Weakest consequential conditions
8. Prioritized intervention recommendations
9. Named decision and action owners
10. Next evidence-producing actions and unresolved questions

## Who Should Participate

Build a cross-functional evidence group rather than relying on a single executive workshop.

Include appropriate representatives from:

- Product and technology leadership
- Product Managers and product teams
- Product Operations
- Design, research, data, and engineering
- Legal, privacy, security, safety, risk, compliance, or AI governance
- Business or operational owners
- Affected users, customers, or workforce representatives when relevant

Record which perspectives are missing. Do not treat attendance as evidence of maturity.

## Evidence to Bring

Invite artifacts and examples across all seven categories:

- Strategy documents and decisions they changed
- Portfolio inventories, charters, stage gates, and stop decisions
- Workflow maps, human-AI responsibility agreements, and before-and-after measures
- Source maps, context packages, data assessments, and lifecycle controls
- Behavior contracts, evaluation sets, scorecards, and production reviews
- Accountability records, autonomy boundaries, control tests, and incidents
- Competency maps, applied learning evidence, reuse records, and outcome measures

Evidence is an invitation, not a gate. When evidence is missing, record the gap, lower confidence, and recommend how to obtain useful evidence. Use `Not assessed` when the available context cannot distinguish absent practice from unobserved practice. Use `1 — Absent` only when inquiry or explicitly attributed reports support absence in the stated scope. Unsupported claims can never score above `2 — Emerging`.

## How to Do It

### 1. Set scope before scoring

Name the organization, business unit, geography, product area, time period, and operating levels being assessed. Record the decision the assessment must enable.

Do not combine materially different scopes into one score. Create separate profiles when enterprise policy, portfolio practice, team behavior, or initiative readiness differ.

### 2. Establish the participant and evidence map

Identify represented and missing perspectives. Inventory supplied artifacts and classify claims as discussed, documented, used, or impact-demonstrated.

Create an initial evidence ledger with source, owner, date, relevance, limitations, confidence, and decision implication.

### 3. Select the assessment path

Use all 35 canonical questions for a complete baseline. For a phased assessment, work category by category but preserve one shared context ledger and do not claim full-library coverage until all categories are complete.

### 4. Evaluate each question

For every canonical question:

1. State the claim being assessed.
2. Review evidence and counterevidence.
3. Identify scope and representativeness.
4. Record disagreement.
5. Assign evidence strength.
6. Decide whether a score is supportable; otherwise record `Not assessed` and the evidence needed.
7. Select the highest maturity score fully supported.
8. Assign confidence and explain the limiting factor.
9. Flag any critical gap.
10. Name the next evidence-producing action.

Do not ask participants to self-score an unfamiliar concept without explaining the maturity anchors and examining evidence.

### 5. Build category profiles

Show all five question scores, evidence confidence, disagreement, and critical gaps. If a category summary is needed, use the median and display the underlying distribution.

Do not use a category average to conceal an important weakness.

### 6. Apply critical-gap logic

Report missing legal, privacy, security, safety, accountability, oversight, evaluation, or rollback conditions separately. State which actions they constrain, such as launch, scale, sensitive-data use, or increased autonomy.

### 7. Find the weakest consequential conditions

Prioritize conditions based on their effect on decisions and outcomes, not merely their numeric rank. Look for dependencies: a weak source system may undermine evaluation; unclear accountability may prevent a safe autonomy decision; a missing strategy may create a portfolio of unrelated pilots.

### 8. Recommend interventions

For each priority condition, recommend a specific AIPOM skill or foundational method, explain why it fits, identify the owner, and state the evidence the intervention should produce.

Limit the first improvement horizon to a coherent set of motions the organization can own. Do not prescribe all 41 skills.

### 9. Confirm the human decision and handoff

The accountable leader decides which findings and interventions to adopt. Record accepted decisions, deferred decisions, disagreements, owners, dates, unresolved questions, and the trigger for reassessment.

## Facilitation Protocol

### Guided mode

Ask one consequential question at a time. Begin with scope and the decision to be enabled, then move through the canonical questions while reusing the evidence ledger. Explain the maturity anchors before requesting judgment.

### Context-dump mode

Read all supplied materials first. Pre-populate claims, evidence, possible scores, confidence, and gaps. Ask only about ambiguities or missing information that could change the profile or recommendation.

### Best-guess mode

Produce a provisional profile using labeled assumptions. Cap unsupported scores at `2 — Emerging`, leave genuinely unobservable conditions `Not assessed`, use low confidence, identify missing perspectives, and propose the smallest evidence-gathering actions needed before consequential decisions.

### Multi-session handling

At the end of each session, preserve:

- Categories and questions completed
- Evidence reviewed
- Provisional scores and confidence
- Disagreements
- Critical gaps
- Open questions
- Next required input

Resume from this ledger without repeating completed questions.

At meaningful routing decisions, present numbered intervention options, explain fit, recommend a default when evidence supports it, and accept combined or custom selections.

## Decision Logic

- If the requested scope mixes organization maturity and initiative readiness, separate the profiles.
- If only executive opinions are available, treat them as claims and run best-guess mode with low confidence.
- If a practice is documented but use is not demonstrated, do not score it above `2 — Emerging`.
- If current examples show repeatable use in part of the scope, consider `3 — Repeatable` while stating the boundary.
- If organization-wide use is claimed without representative evidence, lower the score or confidence.
- If evidence demonstrates measured improvement and reuse, consider `5 — Compounding` only within the supported scope.
- If respondents disagree, preserve the distribution and investigate operating level, scope, recency, incentives, or missing perspectives.
- If a critical gap exists, state the constrained decision before discussing averages.
- If several gaps share a root cause, recommend the root intervention before treating symptoms.
- If the organization has little evidence across categories, prioritize a small assessment-to-action loop rather than a comprehensive transformation program.

Do not calculate an overall score when scopes differ materially. If stakeholders require one and scopes align, use the median of category medians, label it as a navigation aid, and display all category profiles and critical gaps beside it.

## Completion Criteria

Complete the workflow only when it contains:

- Defined scope and operating levels
- All intended canonical questions assessed
- Evidence and assumptions
- Score, confidence, and rationale for each question
- Seven category profiles for a complete assessment
- Preserved disagreements and missing perspectives
- Critical gaps and constrained decisions
- Weakest consequential conditions
- Prioritized interventions with fit rationale
- Named owners and next evidence-producing actions
- Unresolved questions and reassessment trigger

Do not finish with only scores, a radar chart, or generic recommendations.

## Key Concepts

### Evidence Before Score

The score summarizes the strongest claim the evidence supports. Confidence does not replace evidence.

### Profile Before Average

The distribution across categories and questions is more useful than a single number because operating models fail through consequential weak links.

### Consequence Before Arithmetic

The priority condition is the weakness that most constrains responsible value, not automatically the numerically lowest item.

### Disagreement Is Data

Different perspectives may reveal policy-practice gaps, uneven adoption, scope differences, or competing risk tolerances.

### Assessment-to-Action Loop

An assessment is useful only when it changes a decision, routes work to an intervention, assigns ownership, and produces new evidence.

## Organizational Applications

- Establish an enterprise or business-unit baseline
- Diagnose why pilots do not become repeatable capability
- Prepare an operating-model roadmap or design sprint
- Compare documented governance with product-team practice
- Identify capability and context dependencies across a portfolio
- Reassess progress after a defined improvement horizon
- Support leadership discussion without manufacturing false consensus

## Common Pitfalls

- Using executive self-ratings as evidence
- Averaging away a critical gap
- Mixing organization maturity with initiative readiness
- Treating a policy, template, workshop, or license as adoption
- Asking all questions mechanically despite supplied context
- Hiding disagreement to create a cleaner chart
- Recommending every skill instead of the next coherent motions
- Confusing completed assessment output with changed organizational practice
- Reassessing activity measures rather than decision or outcome evidence

## Combine With

- `aipom-operating-model-roadmap` to sequence findings into 30-, 90-, 180-, and 365-day interventions
- The seven category advisors to deepen the most consequential category diagnosis
- `aipom-autonomy-boundary-designer` when unclear AI authority is a priority governance gap
- `aipom-strategy-thesis-advisor` when portfolio incoherence begins with a missing strategic thesis
- Foundational problem-framing, system-mapping, stakeholder-mapping, and premortem skills when those methods already solve the underlying problem

## Assets and Templates

- [Assessment report template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example and critique](examples/weak-example.md)
- [Canonical assessment questions](../../assessments/aipom-operating-model-assessment.md)
- [Evidence rubric](../../assessments/evidence-rubric.md)
- [Scoring model](../../assessments/scoring-model.md)

## Sources

- National Institute of Standards and Technology, [Artificial Intelligence Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10), published January 26, 2023. Supports lifecycle-based, organizational AI risk management; governance; measurement; and documented accountability. Accessed July 16, 2026. NIST notes that AI RMF 1.0 is being revised.
- OECD.AI, [Advancing Accountability in AI](https://oecd.ai/en/accountability/). Supports role- and context-aware accountability and iterative risk governance across the AI lifecycle. Accessed July 16, 2026.
