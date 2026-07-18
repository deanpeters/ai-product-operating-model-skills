---
name: aipom-context-readiness-advisor
description: Diagnose missing, stale, conflicting, inaccessible, excessive, sensitive, or untrusted context and recommend the next source, package, data, or lifecycle intervention.
type: interactive
category: context-knowledge-and-data
phase: 1
status: active
operating_level: [organization, product-team, initiative]
audience: [CTO, Product Operations, Product Manager, Team Lead, Engineering, Data, Knowledge Management, Privacy, Security]
best_for: [Preparing a grounded AI workflow, Diagnosing unreliable or inconsistent outputs, Choosing the next context intervention]
evidence_required: [Workflow purpose, Candidate sources and owners, Failure examples, Access and lifecycle constraints]
produces: [Context readiness diagnosis, Consequential gap and recommendation, Evidence and remediation plan]
assessment_questions: [CTX-01, CTX-02, CTX-03, CTX-04, CTX-05]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 30-60 min
group_size: 2-8
depends_on: []
combine_with: [aipom-context-package-builder, authoritative-source-map, aipom-data-readiness-audit]
sources: []
---

# AIPOM Context Readiness Advisor

## What Is It

Diagnose whether a specific AI-assisted decision or workflow has the trusted, bounded, accessible, and maintainable context it needs. Recommend the smallest intervention that addresses the consequential gap.

## Why Use It

Output failures often originate in source ownership, staleness, conflict, access, or context overload rather than model capability. This advisor prevents “add more documents” from becoming the default remedy.

## When to Use It

Use before building a context package, connecting retrieval, expanding an agent, or after groundedness and consistency failures.

## What It Produces

- Readiness diagnosis by context failure mode
- Evidence, assumptions, and affected decisions
- Priority intervention and owner
- Test and improvement evidence

## Who Should Participate

Include the workflow and source owners, intended users, technical implementer, and data, privacy, security, legal, or records partners as needed.

## Evidence to Bring

Bring real sources, owners, permissions, refresh history, retrieval traces, failure cases, conflicting decisions, exclusions, and user evidence.

## How to Do It

1. Define the decision, users, scope, and consequence of bad context.
2. Extract sources, owners, access, freshness, conflicts, and known failures.
3. Diagnose missing, stale, conflicting, inaccessible, excessive, sensitive, or untrusted context.
4. Distinguish document/context problems from underlying data fitness problems.
5. Present intervention choices and recommend the smallest useful motion.
6. Name owner, test cases, evidence expected, and review trigger.

## Facilitation Protocol

Support guided, context-dump, and best-guess modes. Inspect supplied artifacts before questioning. In best-guess mode label authority and freshness assumptions and do not claim organizational readiness from one clean example.

## Decision Logic

- Use an authoritative source map when ownership, trust, permissions, or conflict span many sources.
- Build a context package when trusted sources exist but need purpose-bounded assembly.
- Run a data readiness audit when provenance, quality, consent, or representativeness is the root issue.
- Design lifecycle controls when refresh, persistence, expiry, or versioning is failing.
- Narrow or stop the workflow when sensitive or untrusted context cannot be governed.

## Completion Criteria

Finish with the failure mode, supporting evidence, affected decision, recommended intervention, owner, representative test, assumptions, and unresolved constraints.

## Key Concepts

- Context readiness is purpose-specific.
- Authority, accessibility, and freshness are different properties.
- More context can reduce signal and increase exposure.
- Missing evidence of maintenance caps maturity claims.

## Organizational Applications

Use for assistants, retrieval, agents, product discovery, portfolio reviews, support, evaluation, and governance evidence.

## Common Pitfalls

- Blaming the model before inspecting sources
- Treating a shared drive as an authoritative system
- Ignoring conflicts and exclusions
- Solving a data problem with prompt text
- Measuring retrieval while ignoring decision quality

## Combine With

Use `aipom-context-package-builder`, `authoritative-source-map`, or `aipom-data-readiness-audit` according to the diagnosed root condition.

## Assets and Templates

- [Readiness template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

This advisor is an original AIPOM synthesis of context-engineering, knowledge, and data-readiness practices.
