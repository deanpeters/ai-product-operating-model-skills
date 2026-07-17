---
name: authoritative-source-map
description: Define which sources are authoritative for a purpose, who owns them, who may use them, how conflicts resolve, and when trust expires.
type: component
category: context-knowledge-and-data
phase: 2
status: active
operating_level: [organization, product-team, initiative]
audience: [Product Operations, Product Manager, Data, Knowledge Management, Privacy, Security, AI Governance]
best_for: [Resolving conflicting organizational sources, Preparing trusted context for AI-assisted work, Assigning source ownership and refresh]
evidence_required: [Actual source inventory, Ownership and permission records, Conflict and failure examples, Refresh and usage evidence]
produces: [Purpose-specific authoritative source map, Conflict and trust rules, Ownership and remediation actions]
assessment_questions: [CTX-01, CTX-02, CTX-05]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 45-90 min
group_size: 3-10
depends_on: [aipom-context-readiness-advisor]
combine_with: [aipom-context-package-builder, aipom-data-readiness-audit, aipom-context-lifecycle-designer]
sources: []
---

# Authoritative Source Map

## What Is It

Define the trust role of each source for a named decision or workflow: authoritative, supporting, derived, disputed, restricted, or excluded. Assign ownership, audiences, permissions, refresh, expiry, and conflict resolution.

## Why Use It

Retrieval can make conflicting or stale information easier to find without making it trustworthy. A purpose-specific map prevents “single source of truth” slogans from hiding scope, ownership, and exceptions.

## When to Use It

Use when teams repeatedly reconcile sources, context packages lack provenance, or AI behavior changes with retrieval order. Map sources for a defined purpose rather than declaring one enterprise source universally authoritative.

## What It Produces

- Source inventory and trust role by purpose
- Owner, steward, audience, permission, freshness, and expiry
- Conflict, fallback, and exclusion rules
- Remediation actions and review cadence

## Who Should Participate

Include source owners and users, the workflow or decision owner, data or knowledge stewards, and privacy, security, legal, or governance partners where restrictions apply.

## Evidence to Bring

Bring real source samples, metadata, lineage, permissions, update histories, consumer use, conflicts, failures, and ownership records. A source title is not evidence of authority.

## How to Do It

1. Define the decision, workflow, audience, and consequence the map serves.
2. Inventory sources actually used, including shadow and derived sources.
3. Classify each source’s trust role for that purpose.
4. Record owner, steward, origin, audience, access, sensitivity, refresh, and expiry.
5. Identify overlap, contradiction, missing coverage, and derived transformations.
6. Define precedence, reconciliation, escalation, fallback, and exclusion rules.
7. Test the rules against representative conflicts and stale-source cases.
8. Assign remediation actions, review cadence, and evidence of use.

## Key Concepts

- Authority is purpose-specific, not a permanent property of a file.
- Ownership includes correction and conflict resolution.
- Access does not imply permission to reuse in AI context.
- Expired trust should change system behavior.

## Organizational Applications

Use for policy retrieval, product decisions, customer facts, research repositories, operating metrics, support knowledge, and context-package governance.

## Common Pitfalls

- Calling everything authoritative
- Mapping only official repositories while ignoring actual use
- Naming an owner with no correction duty
- Omitting derived sources and transformations
- Assuming freshness from a recent access date
- Defining precedence without testing conflicts

## Combine With

Use `aipom-context-package-builder` to assemble bounded context, `aipom-data-readiness-audit` for data fitness, and `aipom-context-lifecycle-designer` for persistence and expiry.

## Assets and Templates

- [Authoritative source map template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

This skill is an original AIPOM synthesis of information governance, knowledge stewardship, provenance, and context-engineering practice.
