# AIPOM Skill Specification

This document is the source of truth for canonical skill structure and metadata.

## Canonical Location and Naming

Every skill lives at:

```text
skills/<skill-name>/SKILL.md
```

The folder name must exactly match frontmatter `name`.

- Use lowercase kebab-case.
- Prefer the `aipom-` prefix for AIPOM-specific methods.
- Preserve clear established exceptions such as `human-aipom-work-contract`, `authoritative-source-map`, and `workflow-to-skill-converter`.
- Keep names to 64 characters or fewer.
- Do not rename a skill without updating every reference.

## Required Frontmatter

```yaml
---
name: aipom-autonomy-boundary-designer
description: Define what an AI system may do independently, with approval, or never.
type: component
category: governance-and-accountability
phase: 1
status: active

operating_level:
  - organization
  - product-team
  - initiative

audience:
  - CPO
  - Product Operations
  - Product Manager
  - Team Lead
  - AI Governance

best_for:
  - Preparing an agentic product for launch

evidence_required:
  - Proposed AI or agent actions
  - Existing approval and escalation policies

produces:
  - Autonomy boundary matrix
  - Escalation policy

assessment_questions:
  - GOV-01
  - GOV-02

maturity_move:
  from: emerging
  to: repeatable

estimated_time: 45-60 min
group_size: 3-8

depends_on:
  - aipom-behavior-contract-builder

combine_with:
  - aipom-risk-control-incident-playbook

sources: []
---
```

## Field Rules

| Field | Required | Rule |
|---|---|---|
| `name` | yes | Folder match; lowercase kebab-case; maximum 64 characters |
| `description` | yes | Concrete job performed; maximum 200 characters; no promotional language |
| `type` | yes | `component`, `interactive`, or `workflow` |
| `category` | yes | One primary category from the allowed list |
| `phase` | yes | Integer `1`–`4`, matching `ROADMAP.md` |
| `status` | yes | `planned`, `drafting`, `review`, or `active` |
| `operating_level` | yes | One or more of `organization`, `portfolio`, `product-team`, `initiative` |
| `audience` | yes | At least one role |
| `best_for` | yes | At least one observable trigger or situation |
| `evidence_required` | yes | At least one useful evidence input; evidence is an invitation, not an entry gate |
| `produces` | yes | At least one specific artifact or recommendation |
| `assessment_questions` | yes | One or more stable IDs from the canonical assessment |
| `maturity_move` | yes | `from` and `to` maturity labels; must represent changed practice, not completed output |
| `estimated_time` | yes | Human-readable duration |
| `group_size` | yes | Human-readable participant range or `individual` |
| `depends_on` | yes | List; may be empty |
| `combine_with` | yes | List; may be empty |
| `sources` | yes | List; may be empty only when no external claims or methods require sources |

Allowed categories:

- `strategy-and-economic-outcomes`
- `portfolio-and-investment-choices`
- `product-team-workflows`
- `context-knowledge-and-data`
- `evaluation-and-evidence`
- `governance-and-accountability`
- `capability-adoption-and-reuse`
- `cross-category`

Allowed maturity labels are `absent`, `emerging`, `repeatable`, `operationalized`, and `compounding`.

### Audience Roles

Use audience values to identify roles that perform, coordinate, decide, facilitate, or act on the skill. Inclusion does not transfer decision authority or imply that every listed role performs the same work.

The primary execution personas are:

- `Product Operations` — stewards operating-model coherence, cross-skill context, cadence, and reuse.
- `Product Manager` — integrates product evidence and leads opportunity, outcome, readiness, and lifecycle decisions.
- `Team Lead` — coordinates day-to-day execution, responsibilities, operating evidence, escalation, and improvement for a product or specialist team.

Add these roles selectively where the skill supports work they perform or coordinate. Do not add every persona to every skill merely to increase coverage. See [TARGET-PERSONAS.md](TARGET-PERSONAS.md) for the canonical persona model and plain-English role flows.

## Required Sections

Every `SKILL.md` uses this order:

1. `# Skill Name`
2. `## What Is It`
3. `## Why Use It`
4. `## When to Use It`
5. `## What It Produces`
6. `## Who Should Participate`
7. `## Evidence to Bring`
8. `## How to Do It`
9. `## Key Concepts`
10. `## Organizational Applications`
11. `## Common Pitfalls`
12. `## Combine With`
13. `## Assets and Templates`
14. `## Sources`

Interactive advisors and workflows also require:

- `## Facilitation Protocol`
- `## Decision Logic`
- `## Completion Criteria`

These additional sections should appear after `## How to Do It` and before `## Key Concepts`.

## Supporting Files

Use this structure when applicable:

```text
skills/<skill-name>/
├── SKILL.md
├── template.md
└── examples/
    ├── worked-example.md
    └── weak-example.md
```

- A repeatable artifact requires `template.md`.
- Every active skill requires a worked example.
- Add a weak or failed example when it materially teaches evidence quality, facilitation judgment, or a common failure mode.
- Label synthetic examples explicitly.
- Put optional reusable files in `assets/`.

## Behavioral Requirements

Every skill must:

- Distinguish evidence, facts, assumptions, interpretations, and recommendations.
- Accept partial or absent evidence without pretending the practice is demonstrated.
- Connect the output to a named next action.
- State unresolved questions.
- Make human authority and accountability explicit where relevant.
- Remain useful to a human facilitator without a specific AI platform.
- Include meaningful failure modes and anti-patterns.

Interactive advisors and workflows must follow [ADAPTIVE-FACILITATION.md](ADAPTIVE-FACILITATION.md).

## Source Requirements

Use primary or authoritative sources for laws, regulations, standards, named frameworks, technical specifications, and current product capabilities.

For each source record:

- Title
- Publishing organization
- URL
- Publication or update date when available
- Access date for time-sensitive material
- The claim or method supported

Do not claim that completing a skill establishes legal or regulatory compliance.

## Completion Standard

A skill is active only when:

- Its purpose and trigger conditions are clear.
- The changed organizational condition is explicit.
- Metadata validates.
- Required sections and supporting files exist.
- Examples demonstrate reasoning.
- Assessment IDs and cross-skill references resolve.
- Evidence and maturity claims follow repository standards.
- Human and AI facilitation paths are usable.
- The full test suite passes.
