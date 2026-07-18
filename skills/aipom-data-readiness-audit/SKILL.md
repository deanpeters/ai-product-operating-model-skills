---
name: aipom-data-readiness-audit
description: Assess whether data is fit for a specific AI product decision across provenance, quality, access, representativeness, consent, privacy, freshness, and operations.
type: component
category: context-knowledge-and-data
phase: 2
status: active
operating_level: [organization, product-team, initiative]
audience: [CTO, Product Manager, Team Lead, Data, Engineering, Research, Privacy, Security, AI Governance]
best_for: [Deciding whether an AI use case may proceed, Finding consequential data gaps before build, Defining bounded remediation rather than generic cleanup]
evidence_required: [Named use and behavior requirements, Data samples lineage and owners, Quality and coverage evidence, Consent privacy access and operational controls]
produces: [Purpose-specific data readiness profile, Critical gaps and constrained decisions, Remediation and evidence plan]
assessment_questions: [CTX-03, CTX-05, EVAL-03, GOV-04]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 60-120 min
group_size: 4-10
depends_on: [authoritative-source-map, aipom-behavior-contract-builder]
combine_with: [aipom-context-package-builder, aipom-golden-dataset-builder, aipom-initiative-readiness-review]
sources: [https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10]
---

# AIPOM Data Readiness Audit

## What Is It

Assess whether named data is fit for a specific AI behavior and decision. Examine provenance, quality, coverage, representativeness, consent, privacy, access, freshness, change, and operational stewardship without collapsing critical gaps into an average score.

## Why Use It

“We have the data” says nothing about whether it is lawful, representative, current, usable, or capable of supporting the intended behavior. Readiness is purpose-specific and must constrain the next decision.

## When to Use It

Use before training, retrieval, evaluation, launch, or expanded use when data materially shapes behavior. This is not a legal, privacy, or security approval and should route those decisions to accountable specialists.

## What It Produces

- Data-use boundary and readiness profile
- Evidence, assumptions, and critical gaps
- Allowed, constrained, prohibited, or deferred uses
- Remediation actions, owners, tests, and review date

## Who Should Participate

Include the Product Manager, data owner and steward, engineering, domain experts, affected-user representation, and privacy, security, legal, or governance partners proportionate to the use.

## Evidence to Bring

Bring behavior requirements, source maps, samples, lineage, collection purpose, consent or permission records, quality reports, subgroup coverage, freshness, transformations, access controls, incidents, and maintenance ownership.

## How to Do It

1. Define the exact behavior, decision, population, environment, and consequence.
2. Inventory data sources, derivations, owners, permissions, and intended uses.
3. Examine completeness, accuracy, consistency, timeliness, duplication, and label quality.
4. Examine representativeness, affected groups, historical bias, missingness, and edge cases.
5. Verify provenance, collection context, consent, privacy, security, access, retention, and deletion obligations with accountable partners.
6. Assess drift, refresh, lineage, versioning, correction, and operational stewardship.
7. Identify critical gaps and specify which decisions they constrain.
8. Choose allowed, constrained, prohibited, or deferred use; avoid compensating averages.
9. Define remediation, evidence tests, owners, and re-audit triggers.

## Key Concepts

- Readiness is fitness for a named purpose, not a reusable score.
- Missingness may encode who the system fails to see.
- Permission to access is not automatically permission for every AI use.
- Operational ownership matters after the first audit.

## Organizational Applications

Use for retrieval, evaluation datasets, model adaptation, decision support, personalization, automation, and vendor data transfers.

## Common Pitfalls

- Auditing a dataset without the intended behavior
- Using one readiness average
- Treating volume as representativeness
- Assuming historical labels are ground truth
- Omitting consent, deletion, or downstream use
- Writing remediation with no owner or decision consequence

## Combine With

Use `authoritative-source-map` for trust and ownership, `aipom-golden-dataset-builder` for representative evaluation sets, and `aipom-initiative-readiness-review` for cross-category launch decisions.

## Assets and Templates

- [Data readiness audit template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

- NIST, [AI Risk Management Framework 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10), January 26, 2023. Supports lifecycle data quality, representativeness, privacy, documentation, and risk-management considerations. Accessed July 16, 2026.

Completing this audit does not establish legal, privacy, security, or regulatory compliance.
