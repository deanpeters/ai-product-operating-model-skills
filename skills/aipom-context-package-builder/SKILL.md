---
name: aipom-context-package-builder
description: Assemble a bounded, reusable context package with purpose, authoritative sources, constraints, decisions, examples, exclusions, and refresh rules. Use for recurring AI-assisted work.
type: component
category: context-knowledge-and-data
phase: 1
status: active
operating_level: [organization, product-team, initiative]
audience: [Product Operations, Product Manager, Team Lead, Engineering, Data, Research, Knowledge Management]
best_for:
  - Grounding a recurring AI-assisted workflow
  - Reducing stale, conflicting, or excessive context
  - Creating an inspectable handoff across people and agents
evidence_required:
  - Workflow purpose and decisions supported
  - Candidate source artifacts and owners
  - Constraints, terminology, examples, and prior decisions
  - Access, privacy, retention, and freshness requirements
produces:
  - Bounded context package
  - Source and conflict ledger
  - Refresh, exclusion, and ownership rules
assessment_questions: [CTX-01, CTX-02, CTX-04, CTX-05, WFL-04]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 45-90 min
group_size: 2-6
depends_on: []
combine_with: [authoritative-source-map, aipom-context-readiness-advisor, aipom-context-lifecycle-designer]
sources: []
---

# AIPOM Context Package Builder

## What Is It

Build the smallest inspectable context package that enables a specific human-AI workflow or decision. Include purpose, trusted sources, constraints, definitions, decisions, examples, exclusions, conflicts, ownership, and refresh rules.

## Why Use It

More context is not automatically better. Stuffed, stale, conflicting, or unowned context increases error and hides provenance. A bounded package makes context a maintained product input rather than an accidental prompt dump.

## When to Use It

Use for recurring workflows, agent handoffs, evaluations, or decisions that require stable organizational context. Diagnose source readiness first when ownership or trust is broadly unclear.

## What It Produces

- Purpose and decision contract
- Authoritative source inventory and conflict rules
- Constraints, glossary, decisions, examples, and exclusions
- Access, refresh, expiry, version, and owner metadata
- Gaps and next maintenance action

## Who Should Participate

Include the workflow owner, source owners, intended users, technical implementer, and privacy, security, legal, records, or domain specialists as needed.

## Evidence to Bring

Bring the real source files, dates, owners, prior decisions, examples, access rules, user evidence, and known conflicts. Links without owners or freshness signals are leads, not authoritative context.

## How to Do It

1. State the workflow, decision, audience, and failure consequence.
2. Define what the package must enable and must not be used for.
3. Inventory sources; name owner, authority, audience, access, and freshness.
4. Resolve or preserve conflicts with an explicit precedence rule.
5. Extract only necessary constraints, definitions, decisions, and examples.
6. Add exclusions: sensitive, irrelevant, expired, speculative, or unlicensed material.
7. Define retrieval cues, version, refresh, expiry, and change notification.
8. Test the package on representative and failure cases.
9. Assign stewardship and record unresolved gaps.

## Key Concepts

- **Purpose-bounded context:** relevance depends on the decision.
- **Authority and provenance:** users can trace why a source is trusted.
- **Exclusion is design:** what stays out is as important as what enters.
- **Lifecycle:** context decays and must be refreshed or retired.

## Organizational Applications

Use for product strategy, customer synthesis, portfolio reviews, support, evaluation, governance evidence, and reusable skills.

## Common Pitfalls

- Copying everything into one file
- Treating recency as authority
- Hiding conflicting decisions
- Including sensitive material without a purpose or permission
- Omitting expiry and ownership
- Testing retrieval without testing decision quality

## Combine With

Use `authoritative-source-map` for wider source systems, `aipom-context-readiness-advisor` for diagnosis, and `aipom-context-lifecycle-designer` for persistence and refresh controls.

## Assets and Templates

- [Context package template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

This skill is an original AIPOM synthesis of context-engineering and organizational knowledge practices.
