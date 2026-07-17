# AIPOM Maturity Scoring Model

The assessment is designed to guide organizational improvement. Scores are compressed summaries of evidence, not the answer.

## Maturity Scale

| Score | Label | Condition |
|---:|---|---|
| 1 | Absent | No consistent practice or accountable ownership |
| 2 | Emerging | Isolated experiments, individuals, or informal practices |
| 3 | Repeatable | The practice works in some teams and can be reproduced |
| 4 | Operationalized | The practice is standardized, governed, and used across the organization |
| 5 | Compounding | The practice is measured, improved, reused, and demonstrably strengthens outcomes |

## Scoring Procedure

For each question:

1. Define the assessed scope and operating level.
2. Record claims and evidence using [evidence-rubric.md](evidence-rubric.md).
3. Identify conflicting perspectives and missing evidence.
4. Decide whether a maturity score is supportable. Use `Not assessed` when missing evidence prevents a defensible distinction between absent and emerging practice.
5. If a score is supportable, assign the highest score fully supported by the evidence.
6. Assign confidence and explain the limiting factor.
7. Flag critical gaps separately.
8. Name the next evidence-producing action or intervention.

`1 — Absent` is a finding, not a synonym for “no artifact was supplied.” Use it only when credible inquiry supports that no consistent practice or accountable ownership exists in the assessed scope. Self-reported absence may support a provisional `1` with low confidence when it is explicitly attributed and important enough to act on. If the assessment has not established whether a practice exists, record `Not assessed`, state the missing evidence, and exclude that item from category arithmetic until it can be assessed.

## Score Anchors

### 1 — Absent

- No repeatable practice is visible.
- Ownership is missing or purely implicit.
- Outcomes depend on individual improvisation.

### 2 — Emerging

- Some individuals or initiatives are experimenting.
- Practices are informal, isolated, or inconsistent.
- Documentation may exist, but use is not demonstrated.
- This is the maximum score when no evidence is available.

### 3 — Repeatable

- Current examples demonstrate the practice works in more than one relevant case.
- Inputs, ownership, method, and outputs are sufficiently clear to reproduce.
- The practice may not yet be organization-wide or consistently governed.

### 4 — Operationalized

- The practice is standardized and used across the stated organizational scope.
- Ownership, governance, measures, exceptions, and review routines are active.
- Evidence distinguishes policy from actual adoption.

### 5 — Compounding

- The practice is measured and deliberately improved.
- Evidence connects it to better decisions, outcomes, risk posture, or learning.
- Effective variants are reused; ineffective variants are changed or retired.

## Category Profiles

Report all five question scores within each category before summarizing the category.

A category summary should include:

- The score distribution
- Evidence confidence
- Material disagreements
- The weakest consequential condition
- Any critical gaps
- Recommended skills and next actions

Show `Not assessed` items beside the distribution and do not convert them to zero or `1` for the median.

If a numeric category score is needed, use the median rather than the mean and show the underlying distribution. Do not allow the summary to obscure a critical gap.

## Overall Reporting

Prefer the seven-category profile over a single overall score.

If stakeholders require an overall number:

- Calculate the median of the seven category medians.
- Label it a navigation aid, not a proof of maturity.
- Display category scores, confidence, disagreements, and critical gaps beside it.
- Do not calculate an overall score when the assessed scopes differ materially.

## Critical-Gap Override

Do not average away a consequential missing control.

A critical gap may constrain recommendations involving launch, scale, increased autonomy, sensitive-data use, or continued operation even when other scores are high.

Examples include:

- No accountable human decision owner
- No tested escalation or rollback for consequential behavior
- Unresolved legal, privacy, security, or safety requirement
- No representative evaluation for a high-impact use case
- AI authority exceeding the evidence and controls supporting it

## Disagreement

Preserve respondent distributions or named perspectives when appropriate. Do not manufacture false consensus by averaging leadership confidence with practitioner or governance evidence.

Investigate whether disagreement arises from:

- Different operating levels
- Different teams or geographies
- Policy versus actual use
- Stale evidence
- Different risk tolerances
- Missing affected-user perspectives

## Initiative Readiness

Initiative readiness is not organization maturity. A mature organization may reject an unready initiative; an isolated initiative may be relatively strong inside an immature organization.

Report the two separately.

## Required Assessment Output

Every completed assessment includes:

- Scope and operating level
- Evidence reviewed and missing
- Question and category profiles
- Confidence
- Disagreements
- Critical gaps
- Weakest consequential conditions
- Recommended interventions
- Named owners
- Next evidence-producing actions
- Unresolved questions
