# Synthetic Worked Example: Appeal-Summary Assistant

**Synthetic example.** The organization, evidence, and decisions below are fictional.

## Decision Contract

A health-benefits administrator is deciding whether an AI assistant that drafts appeal summaries deserves further validation. Human reviewers would retain every appeal decision. The current manual workflow is the baseline; a rules-based document assembly option remains a non-AI alternative.

The Product Manager and engineering owner are named, but no accountable business decision owner has accepted the benefit-risk decision. The required role is therefore recorded as **unassigned**, not silently assigned to the Product Manager.

## Comparable Record

| Dimension | AI-assisted drafting | Current manual workflow | Evidence and limitation |
|---|---|---|---|
| Outcome value | Could reduce summary preparation time | Averages 18 minutes per appeal | A 200-case retrospective test averaged 8 minutes, but covered one employer plan |
| Evidence | Promising but narrow | Established operating baseline | AI test excluded handwritten and non-English records |
| AI fit | Bounded drafting task with human review | Human synthesis from source records | Human approval does not guarantee subtle omissions will be detected |
| Feasibility | Basic retrospective feasibility demonstrated | Already operational | Production workflow, unsupported records, and monitoring are untested |
| Responsibility | Three material omissions occurred | Existing human quality controls apply | No omission threshold or severity rule was set before the test |
| Readiness | Not ready for live operation | Current process remains available | No business owner, monitoring plan, incident playbook, or rollback exercise |
| Reversibility | Manual fallback exists | Fully human | Fallback has not been exercised from a live AI workflow |

Finance forecasts $900,000 in annual savings across all plans. That figure remains an assumption because eligible volume, review burden, exception handling, vendor cost, monitoring, remediation, and cross-plan performance were not demonstrated.

## Critical-Gap Check

| Gap | Consequence | Can it be bounded? | Required authority |
|---|---|---|---|
| No accountable business owner | No one owns pilot entry or stopping | Yes, before live use | Appeals operations executive |
| Narrow evaluation population | Performance outside one plan is unknown | Yes, through testing or explicit exclusions | Product and domain owners |
| No prospective omission threshold | The observed omissions cannot produce a pass decision | Yes | Domain, evaluation, and governance authorities |
| Vendor retains prompts for 30 days | Data handling may be unacceptable | Specialist decision required | Privacy, security, legal, and procurement |
| Human review untested under workload | Oversight may be ceremonial under pressure | Yes, through representative simulation | Operations and research |

## Recommendation

**Posture: Validate.** The problem is meaningful, the AI role is bounded, and the time signal justifies a learning investment. The use case is not rejected because the gaps appear testable; it is not approved for a live pilot because triage is not a readiness decision.

Run a prospective shadow test across the intended population. Include relevant plans, languages, and document types, or define reliable routing exclusions. Set material-omission severity and acceptance thresholds before testing. Compare AI-assisted and manual review for time, omissions, downstream rework, reviewer detection, and total operating cost under realistic workload.

The next decision is triggered when the representative evaluation, specialist data decisions, owner assignment, and operational-control rehearsal are complete. If those conditions are met, route the initiative to `aipom-initiative-readiness-review`. Until an authorized owner sets a calendar date, the review date remains unresolved rather than invented.

## Ledger

- **Evidence used:** 200-case retrospective test and current 18-minute baseline, treated as reported evidence.
- **Assumptions:** enterprise savings, reviewer effectiveness, and cross-plan performance.
- **Specialist decisions:** privacy, security, legal, procurement, and domain acceptability remain reserved.
- **Next action:** Product Manager prepares the validation plan; appeals leadership assigns the accountable business owner.
