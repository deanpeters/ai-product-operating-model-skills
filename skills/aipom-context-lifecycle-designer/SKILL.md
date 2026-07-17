---
name: aipom-context-lifecycle-designer
description: Design how AI context is created, retrieved, refreshed, versioned, reconciled, retained, expired, excluded, and retired for a recurring purpose.
type: component
category: context-knowledge-and-data
phase: 3
status: active
operating_level: [organization, product-team, initiative]
audience: [Product Operations, Product Manager, Engineering, Data, Knowledge Management, Privacy, Security, AI Governance]
best_for: [Operating reusable context packages, Preventing stale or conflicting context, Defining retention correction and expiry behavior]
evidence_required: [Authoritative source map and context package, Retrieval and failure evidence, Permissions retention and correction rules, Owners and change triggers]
produces: [Context lifecycle design, State transition and conflict rules, Ownership monitoring and test plan]
assessment_questions: [CTX-01, CTX-02, CTX-04, CTX-05]
maturity_move: {from: repeatable, to: operationalized}
estimated_time: 60-120 min
group_size: 4-10
depends_on: [authoritative-source-map, aipom-context-package-builder]
combine_with: [aipom-data-readiness-audit, aipom-workflow-playbook-builder, aipom-production-evidence-review]
sources: []
---

# AIPOM Context Lifecycle Designer

## What Is It

Design the operating lifecycle for purpose-specific AI context from creation through retrieval, use, feedback, correction, refresh, versioning, reconciliation, retention, expiry, exclusion, and retirement.

## Why Use It

A trustworthy context package at launch becomes dangerous when sources change, corrections do not propagate, or old decisions persist without expiry. Lifecycle design makes context state and failure behavior operational.

## When to Use It

Use when a context package supports recurring or production work, especially when sources, permissions, policies, or decisions change. This does not replace data retention, privacy, legal, or records-management authority.

## What It Produces

- Context objects, states, transitions, and owners
- Retrieval, provenance, refresh, reconciliation, and expiry rules
- Correction, exclusion, deletion, fallback, and escalation behavior
- Monitoring, tests, change control, and review cadence

## Who Should Participate

Include context consumers, source owners and stewards, workflow and technical owners, knowledge or data specialists, and privacy, security, legal, or governance partners as needed.

## Evidence to Bring

Bring source maps, context packages, retrieval logs, stale or conflicting cases, permission and retention rules, correction events, incidents, change histories, and operating ownership.

## How to Do It

1. Define the purpose, consumer, decision, consequence, and context boundary.
2. Inventory context objects, authoritative sources, derivations, versions, and owners.
3. Define states such as draft, approved, active, disputed, stale, expired, restricted, and retired.
4. Specify creation, approval, retrieval, refresh, reconciliation, correction, exclusion, expiry, and deletion transitions.
5. Define provenance, timestamps, confidence, conflict, and missing-context signals shown at use.
6. Set retention and access rules with accountable specialists.
7. Design fallback and escalation when context is missing, stale, disputed, or inaccessible.
8. Define monitoring for retrieval quality, staleness, conflict, correction propagation, and unauthorized use.
9. Test representative state changes and assign review triggers.

## Key Concepts

- Context state should change system behavior.
- Correction must propagate to derived artifacts.
- Newest is not always authoritative.
- Retention and retrieval serve different decisions.

## Organizational Applications

Use for product knowledge, policy retrieval, research evidence, customer context, decision histories, workflow playbooks, and agent memory.

## Common Pitfalls

- Designing retrieval without expiry
- Treating timestamps as trust
- Updating sources without derived context
- Retaining everything because it may be useful
- Omitting disputed and restricted states
- Assigning stewardship without monitoring or correction duties

## Combine With

Use `aipom-data-readiness-audit` for data fitness, `aipom-workflow-playbook-builder` to embed context behavior in work, and `aipom-production-evidence-review` to inspect lifecycle performance.

## Assets and Templates

- [Context lifecycle template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

This skill is an original AIPOM synthesis of context engineering, knowledge governance, data lifecycle, and operational reliability practice.
