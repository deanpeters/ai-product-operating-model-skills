# Worked Example: Regional Home-Services Platform

**Synthetic example.** The organization, participants, artifacts, and scores below are fictional.

## Assessment Contract

A regional home-services marketplace has launched five AI pilots across customer support, technician scheduling, lead scoring, review summarization, and internal knowledge search. Leadership wants to know whether the organization is ready to scale AI investment.

Scope: the US product and operations organization, excluding the maturity of individual vendors. Initiative readiness is recorded separately.

Participants include product and technology leaders, three Product Managers, operations, data, security, privacy, customer support, and a technician representative. No end-customer representative participated, which limits customer-outcome confidence.

## Evidence Inventory

| Evidence | What it supports | Limitation |
|---|---|---|
| AI pilot inventory | Five active pilots and named technical owners | No common investment criteria or stop decisions |
| Product strategy | Customer trust and appointment completion are priorities | AI choices and non-goals are absent |
| Support-agent pilot logs | Drafting reduces average handling time in one queue | Six weeks, one queue, no decision-quality measure |
| Security review policy | Reviews are required before production access | Two pilots bypassed the documented intake path |
| Vendor evaluation reports | Model accuracy was tested on vendor samples | Samples are not representative of local users or failures |
| Training attendance | 62 staff attended AI training | No evidence of changed workflow or decisions |

## Selected Question Records

### GOV-02 — Autonomy boundaries

- **Claim:** AI systems have appropriate human oversight.
- **Evidence:** Support drafts require approval; the scheduling pilot can automatically alter appointment windows; no shared action-level boundary exists.
- **Evidence strength:** 2 — Documented for one workflow, anecdotal elsewhere.
- **Disagreement:** Leadership describes all pilots as human-supervised; operators report that scheduling changes are rarely reviewed before customer notification.
- **Score:** 1 — Absent at organization level.
- **Confidence:** High; direct workflow evidence contradicts the broad claim.
- **Critical gap:** Yes for expanding scheduling autonomy.
- **Next action:** Use `aipom-autonomy-boundary-designer` before further production authority.

### EVAL-03 — Representative evaluation cases

- **Claim:** AI behavior is tested before launch.
- **Evidence:** Vendor benchmark reports and 50 hand-selected support cases; no technician, accessibility, regional-language, adversarial, or material-failure cases.
- **Evidence strength:** 1 — Anecdotal and narrow.
- **Score:** 1 — Absent.
- **Confidence:** High.
- **Critical gap:** Yes for customer-facing scale decisions.
- **Next action:** Define behavior contracts before building representative evaluation cases.

### CAP-02 — Applied learning system

- **Claim:** The workforce has been trained for AI-enabled work.
- **Evidence:** Attendance records and course materials; no practice review, coaching, progression, or demonstrated use.
- **Evidence strength:** 2 — Documented activity.
- **Score:** 2 — Emerging.
- **Confidence:** High.
- **Decision implication:** Do not report training attendance as operational capability.

## Category Profile

| Category | Question scores | Median | Confidence | Key finding |
|---|---|---:|---|---|
| Strategy and Economic Outcomes | 2, 2, 1, 1, 2 | 2 | Medium | Outcomes exist, but no AI thesis or tested economic logic |
| Portfolio and Investment Choices | 2, 2, 1, 1, 2 | 2 | High | Pilots lack common continuation and stop criteria |
| Product-Team Workflows | 2, 2, 1, 1, 1 | 1 | Medium | Local workflow experiments are not reusable or measured consistently |
| Context, Knowledge, and Data | 1, 1, 1, 1, 1 | 1 | Medium | No authoritative-source or lifecycle practice exists |
| Evaluation and Evidence | 1, 2, 1, 1, 1 | 1 | High | Testing is narrow and not tied to product decisions |
| Governance and Accountability | 2, 1, 1, 2, 1 | 1 | High | Authority, escalation, and trust evidence are incomplete |
| Capability, Adoption, and Reuse | 2, 1, 1, 1, 2 | 1 | Medium | Training activity is visible; changed practice is not |

No overall score is reported because several evidence sources cover different scopes. The category profile is sufficient for the decision.

## Critical Gaps

1. Scheduling authority is not bounded at the action level, constraining increased autonomy.
2. Customer-facing pilots lack representative evaluation, constraining scale.
3. Two pilots bypassed the documented security intake, revealing a policy-practice gap.
4. No owner is accountable for portfolio-level continuation or stop decisions.

## Weakest Consequential Conditions

The lowest numbers are not the only reason for prioritization. The root condition is that each pilot was launched as a local experiment without a shared bet, behavior, authority, or evidence contract. That weakness produces downstream evaluation and governance gaps.

## Recommended First Motions

| Priority | Intervention | Why it fits | Owner | Evidence expected |
|---:|---|---|---|---|
| 1 | `aipom-bet-charter` for the two proposed scale candidates | Establish outcomes, owner, constraints, next test, and stop criteria | Portfolio leader | Two comparable investment charters and an explicit defer decision |
| 2 | `aipom-behavior-contract-builder` followed by `aipom-autonomy-boundary-designer` for scheduling | Define acceptable behavior before delegating action authority | Scheduling Product Manager | Behavior contract, action-level boundaries, tested stop flow |
| 3 | `aipom-context-readiness-advisor` for knowledge search | Diagnose source ownership and staleness before expansion | Knowledge operations owner | Source gaps and prioritized remediation |

## Human Decision and Next Action

The CPO decides not to scale any pilot solely on current evidence. The two most promising initiatives receive a 60-day evidence-building window. The portfolio leader owns common bet reviews, and the scheduling operations director remains accountable for customer-impacting actions.

Reassessment will occur after the 60-day reviews or immediately after a material incident or control failure.
