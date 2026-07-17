# AIPOM Operating Model Assessment

This is the canonical 35-question organizational assessment. Individual skills reference these stable IDs; they must not copy or fork the questions.

## How to Use the Assessment

- Assess a named scope and operating level.
- Gather perspectives from leadership, product teams, enabling functions, and governance partners where relevant.
- Ask for evidence of actual use and changed decisions, not only documented intent.
- Record disagreement rather than forcing consensus.
- Score each question using [scoring-model.md](scoring-model.md) and [evidence-rubric.md](evidence-rubric.md).
- Treat critical safety, legal, privacy, security, or accountability gaps separately from arithmetic averages.
- Convert findings into skills and named next actions. A score is not the intervention.

## Strategy and Economic Outcomes

| ID | Assessment question | Useful evidence |
|---|---|---|
| STR-01 | Does the organization have a clear, used AI product thesis that identifies where AI can create meaningful value, where it will not invest, and why? | Strategy decisions, portfolio choices, explicit non-goals, examples of opportunities declined |
| STR-02 | Are AI initiatives connected to specific customer, user, business, operational, safety, or risk outcomes rather than AI activity alone? | Outcome maps, research, product measures, economic measures, decision records |
| STR-03 | Are the causal assumptions connecting AI behavior, user behavior, product outcomes, and economic outcomes explicit and tested? | Hypothesis maps, experiments, evaluation results, revised assumptions |
| STR-04 | Do leaders use evidence and economics to compare AI investments with non-AI alternatives? | Investment cases, alternative analyses, funding decisions, stop decisions |
| STR-05 | Is the AI product strategy revised when evidence, market conditions, technology constraints, or organizational learning change? | Strategy review cadence, version history, changed bets, retired assumptions |

## Portfolio and Investment Choices

| ID | Assessment question | Useful evidence |
|---|---|---|
| POR-01 | Is there a consistent method for triaging AI opportunities across value, evidence, feasibility, responsibility, and strategic relevance? | Triage criteria, scored examples, decisions changed by the method |
| POR-02 | Does every material AI bet have a named hypothesis, accountable owner, expected outcomes, constraints, economics, and next evidence-producing test? | Bet charters, owner records, experiment plans, review decisions |
| POR-03 | Are entry, continuation, pivot, scale, pause, and kill criteria explicit and actually used? | Stage gates, review records, paused or killed initiatives, exception records |
| POR-04 | Are model, vendor, data, infrastructure, switching-cost, and portability dependencies considered in investment decisions? | Dependency audits, contracts, architecture decisions, exit or portability plans |
| POR-05 | Does the portfolio review distinguish learning investments from scaling investments and actively address zombie pilots or premature scaling? | Portfolio inventory, funding allocations, scale decisions, retired pilots |

## Product-Team Workflows

| ID | Assessment question | Useful evidence |
|---|---|---|
| WFL-01 | Has the organization identified which product-team decisions or productive motions are worth redesigning with AI assistance? | Workflow selection criteria, baseline maps, prioritization decisions |
| WFL-02 | Are current workflows understood in terms of decisions, actors, inputs, handoffs, delays, rework, and failure points before AI is introduced? | Current-state maps, cycle-time data, rework evidence, practitioner observations |
| WFL-03 | Are AI responsibilities, human judgment, review expectations, decision authority, and accountability explicit in redesigned workflows? | Human-AI work contracts, approval records, escalation paths, observed use |
| WFL-04 | Are AI-assisted workflows reusable, inspectable, and supported by context, examples, guardrails, evaluations, and stop rules? | Workflow playbooks, reusable skill packages, evaluation results, version history |
| WFL-05 | Does the organization measure whether redesigned workflows improve decision quality, cycle time, learning, rework, or outcomes? | Before-and-after measures, decision audits, team feedback, outcome evidence |

## Context, Knowledge, and Data

| ID | Assessment question | Useful evidence |
|---|---|---|
| CTX-01 | Are authoritative sources, owners, audiences, permissions, trust status, refresh cadence, and conflicts explicit? | Source maps, ownership records, access rules, conflict-resolution examples |
| CTX-02 | Can teams assemble bounded, purpose-specific context packages with constraints, evidence, decisions, definitions, and examples? | Context packages, usage examples, quality reviews, retrieval tests |
| CTX-03 | Is data assessed for quality, provenance, access, representativeness, consent, privacy, freshness, and fitness for purpose before use? | Data readiness audits, lineage, consent records, quality reports, approvals |
| CTX-04 | Are context persistence, retrieval, refresh, expiration, versioning, conflict detection, and exclusion rules defined and used? | Lifecycle rules, version history, expiration events, retrieval and conflict tests |
| CTX-05 | Can teams detect when missing, stale, excessive, conflicting, inaccessible, or untrusted context is affecting AI-assisted decisions? | Failure reports, context evaluations, incident records, corrected decisions |

## Evaluation and Evidence

| ID | Assessment question | Useful evidence |
|---|---|---|
| EVAL-01 | Does each material AI product have an evaluation strategy covering product, model, workflow, human, and production behavior as appropriate? | Evaluation plans, coverage maps, decision records, identified gaps |
| EVAL-02 | Are expected behavior, acceptable ranges, prohibited behavior, escalation conditions, and failure consequences explicit? | Behavior contracts, policy-to-test mappings, escalation examples |
| EVAL-03 | Do evaluation datasets represent real use, edge cases, affected groups, adversarial cases, and consequential failure modes? | Dataset documentation, provenance, coverage analysis, gap reviews |
| EVAL-04 | Are metrics, rubrics, judges, thresholds, sampling, cadence, ownership, and decision rules defined and calibrated? | Scorecards, calibration studies, reviewer agreement, threshold changes |
| EVAL-05 | Is production evidence regularly used to continue, change, pause, roll back, or retire AI behavior and products? | Production reviews, monitoring results, rollback or retirement decisions |

## Governance and Accountability

| ID | Assessment question | Useful evidence |
|---|---|---|
| GOV-01 | Are owners, decision rights, approvers, contributors, reviewers, and escalation paths named for material AI decisions? | Accountability charters, approvals, escalation records, decision logs |
| GOV-02 | Is it explicit what AI may do independently, with approval, or never, based on consequences and evidence? | Autonomy matrices, approval controls, observed exceptions, review outcomes |
| GOV-03 | Are preventive controls, detection, escalation, rollback, response, remediation, and learning mechanisms operational? | Control tests, incident exercises, incident records, corrective actions |
| GOV-04 | Are legal, privacy, security, safety, risk, and product partners engaged at decision points proportionate to the initiative? | Review records, risk-based routing, resolved issues, exception handling |
| GOV-05 | Can the organization provide current, usable trust evidence about behavior, limitations, evaluations, controls, ownership, and incidents? | System cards, assurance packs, audit records, customer or regulator responses |

## Capability, Adoption, and Reuse

| ID | Assessment question | Useful evidence |
|---|---|---|
| CAP-01 | Are expected AI product competencies defined by role and proficiency level rather than as generic tool fluency? | Competency maps, role expectations, assessed proficiency, hiring or development decisions |
| CAP-02 | Do learning systems combine instruction with applied practice, coaching, peer review, feedback, and progression? | Learning paths, practice artifacts, coaching records, demonstrated progression |
| CAP-03 | Does the organization measure changed behavior, decision quality, cycle time, reuse, and outcomes rather than licenses, logins, or attendance alone? | Adoption scorecards, workflow measures, outcome evidence, decision audits |
| CAP-04 | Are effective workflows converted into governed, discoverable, reusable skills with owners and improvement mechanisms? | Skill library, stewardship records, reuse evidence, version and retirement history |
| CAP-05 | Do leaders and enabling functions reinforce responsible use through incentives, review routines, support, and visible decisions? | Leadership decisions, operating reviews, incentives, support usage, addressed barriers |

## Assessment Output

The assessment produces:

- A seven-category maturity profile
- Evidence and confidence notes for every score
- Material disagreements among respondents
- Critical gaps that constrain action regardless of averages
- The weakest consequential conditions
- Recommended AIPOM skills or foundational methods
- Named owners and next evidence-producing actions
- Unresolved questions

It should not produce a single flattering score without the evidence and actions behind it.

