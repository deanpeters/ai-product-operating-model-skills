---
name: aipom-platform-dependency-audit
description: Assess model, vendor, data, infrastructure, integration, talent, switching, and portability dependencies that can change an AI investment decision.
type: component
category: portfolio-and-investment-choices
phase: 3
status: active
operating_level: [organization, portfolio, initiative]
audience: [CTO, VP Product, Product Manager, Engineering, Procurement, Finance, Security, AI Governance]
best_for: [Material vendor or platform commitments, Preparing scale or renewal decisions, Finding concentration and exit exposure]
evidence_required: [Architecture and data flows, Contracts pricing and service terms, Model and evaluation evidence, Portability tests and operating ownership]
produces: [Dependency and concentration map, Scenario and exit analysis, Mitigation and decision recommendations]
assessment_questions: [POR-04, POR-05, STR-04, GOV-03]
maturity_move: {from: emerging, to: repeatable}
estimated_time: 60-120 min
group_size: 4-10
depends_on: [aipom-bet-charter]
combine_with: [aipom-economic-case-builder, aipom-investment-stage-gates, aipom-initiative-readiness-review]
sources: [https://airc.nist.gov/airmf-resources/airmf/5-sec-core/]
---

# AIPOM Platform Dependency Audit

## What Is It

Map and test the external and internal dependencies that shape value, reliability, control, and exit: models, vendors, data, infrastructure, integrations, talent, contracts, pricing, evaluation, and operational knowledge.

## Why Use It

A technically successful pilot can become economically or operationally fragile when one provider changes price, behavior, access, terms, region, or service. Dependency is not automatically bad; unmanaged dependency is the problem.

## When to Use It

Use before material procurement, scale, renewal, architecture lock-in, sensitive-data transfer, or increased autonomy. Scope the audit to the decision rather than producing a generic vendor inventory.

## What It Produces

- Dependency, ownership, and concentration map
- Change, outage, degradation, and exit scenarios
- Portability evidence and switching cost
- Accept, mitigate, diversify, constrain, renegotiate, or exit recommendation

## Who Should Participate

Include the investment owner, architecture and engineering, product, procurement, finance, security, data, operations, and governance partners.

## Evidence to Bring

Bring architecture, data flows, contracts, service terms, pricing, usage, evaluations, incidents, operational runbooks, portability tests, skills, and migration estimates. Contract language without tested operations is partial evidence.

## How to Do It

1. Name the investment decision and critical capabilities.
2. Map upstream, runtime, downstream, organizational, and contractual dependencies.
3. Record owner, substitutability, concentration, data movement, and failure consequence.
4. Test price, model change, outage, quality regression, access loss, policy change, and provider-exit scenarios.
5. Examine portability of prompts, context, data, evaluations, integrations, logs, and operating knowledge.
6. Estimate switching time, cost, downtime, retraining, revalidation, and control changes.
7. Identify dependencies that constrain scale, autonomy, geography, or data use.
8. Recommend accept, mitigate, diversify, constrain, renegotiate, or exit actions.
9. Assign owners, evidence tests, monitoring, and decision triggers.

## Key Concepts

- Portability is demonstrated through tests, not architecture diagrams.
- Multi-vendor designs can add complexity without reducing critical concentration.
- Organizational expertise is a dependency.
- Dependency exposure belongs in economics and stage gates.

## Organizational Applications

Use for foundation-model providers, cloud and vector infrastructure, data vendors, orchestration platforms, evaluation services, and internal shared platforms.

## Common Pitfalls

- Treating vendor availability as portability
- Mapping technology but not contracts or skills
- Ignoring model behavior changes
- Assuming multi-cloud eliminates concentration
- Omitting re-evaluation and migration cost
- Creating mitigations with no trigger or owner

## Combine With

Use `aipom-economic-case-builder` to price exposure, `aipom-investment-stage-gates` to constrain funding, and `aipom-initiative-readiness-review` to integrate critical gaps.

## Assets and Templates

- [Dependency audit template](template.md)
- [Synthetic worked example](examples/worked-example.md)
- [Weak example](examples/weak-example.md)

## Sources

- NIST AI Resource Center, [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). Manage 3 addresses monitoring third-party AI resources and applying documented controls. Accessed July 17, 2026. NIST notes that AI RMF 1.0 is under revision.
