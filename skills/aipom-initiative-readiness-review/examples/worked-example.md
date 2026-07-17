# Synthetic Worked Example: Appeal-Summary Pilot Readiness

**Synthetic example.** The organization, initiative, and evidence below are fictional.

## Decision and Scope

Decision under review: whether an AI assistant may draft appeal summaries during a limited live pilot. Humans would retain every appeal decision. The proposed pilot would cover selected employer plans and supported document types; it would not recommend outcomes, prioritize appeals, communicate with claimants, or take autonomous action.

The Product Manager and engineering owner are named. No accountable appeals executive has accepted the pilot-entry and stop decision, so that required role remains **unassigned**.

## Evidence Profile

| Area | Evidence and confidence | Critical gap | Constrained action | Owner |
|---|---|---|---|---|
| Value and economics | Draft time fell from 18 to 8 minutes in 200 retrospective cases; moderate confidence for the tested cohort | $900,000 forecast extrapolates beyond observed scope and omits operating costs | Do not approve scale economics | Finance and business owner |
| Dependencies and operations | Manual workflow remains available | Fallback and rollback were not exercised | No live pilot until rehearsal passes | Engineering and operations |
| Workflow and adoption | Reviewers perform the underlying work | Detection of subtle omissions under representative workload is unknown | Run workload simulation | Operations and research |
| Context and data | One employer plan was tested | Handwritten and non-English records were excluded | Restrict scope or expand evaluation | Product and data owners |
| Evaluation and production evidence | Three material omissions occurred | No prospective threshold, severity logic, monitoring signal, or stop rule | Define and pass a prospective evaluation | Evaluation and domain owners |
| Accountability, controls, and recovery | Product and engineering ownership exists | No accountable business owner, incident playbook, or exercised recovery | Remediate before live use | Appeals executive, risk, and engineering |
| Capability and support | Reviewers know the manual process | Training, escalation behavior, and automation-bias controls are untested | Test operator procedures | Operations and capability owners |

## Specialist Decision Register

| Reserved decision | Required role | Status | Constraint while unresolved | Evidence needed |
|---|---|---|---|---|
| Whether 30-day prompt retention is permissible | Privacy, legal, procurement | Unresolved | No use of relevant records | Contract, data-flow, and jurisdiction review |
| Whether vendor controls are sufficient | Security | Unresolved | No production access | Security assessment and approved conditions |
| Whether omission thresholds are acceptable | Appeals domain and risk | Unresolved | No live output may influence appeals | Severity framework and prospective results |
| Whether the workflow meets plan obligations | Legal and operations | Unresolved | Limit work to authorized shadow testing | Plan-specific requirements and routing rules |

The review records these decisions; it does not impersonate the specialists or convert attendance into approval.

## Recommendation

**Remediate and re-review.** The initiative is not ready for a live pilot today. A bounded shadow validation may continue only if the data use is already authorized and its outputs cannot influence real appeals.

Live operation remains blocked until:

1. An accountable appeals executive accepts pilot-entry, continuation, and stop authority.
2. Required specialist decisions are recorded.
3. A representative prospective evaluation passes thresholds established before testing.
4. Reviewers demonstrate that they detect material omissions under realistic workload.
5. Unsupported records route reliably to manual processing.
6. Monitoring defines failure signals, cadence, owners, and escalation.
7. The incident playbook, fallback, and rollback are exercised.
8. Pilot volume, population, expiry, stop conditions, and re-review triggers are documented.

If those conditions are met, the next review may recommend **proceed with constraints**. It would not approve unrestricted launch or scale.

## Authority and Trigger

The AI facilitator recommends; an authorized appeals executive decides. Because neither the person nor decision calendar was supplied, the artifact names the required role and uses completion of the evidence package as the re-review trigger. It does not invent a name or date.

## Unresolved Questions

- Which plans, languages, and document types define the intended pilot population?
- What constitutes a material omission, and what threshold is acceptable?
- What workload conditions make review less reliable?
- What notice, recordkeeping, and appeal-process obligations apply?
- Does the full economic case remain attractive after review and control burden?
