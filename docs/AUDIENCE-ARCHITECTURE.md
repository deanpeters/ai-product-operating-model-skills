# AIPOM Audience and Navigation Architecture

## Purpose

AIPOM serves people who need to understand the operating-model problem, make a consequential decision, facilitate organizational work, or maintain the library. They should not have to enter through the same explanation.

This document defines the public navigation model. It is an experience layer over the canonical assessment, skills, standards, and catalogs. It does not create a second operating model or a second source of truth.

## Three Public Doors

### Lead Change

**Primary readers:** CPOs, CTOs, product and technology executives, Product Operations leaders, governance leaders, and transformation sponsors.

**Question:** Why does the organization need an AI product operating model, which decisions should improve, and where should leadership begin?

**Primary route:** [Executive Field Guide](EXECUTIVE-FIELD-GUIDE.md), followed by an appropriate [executive adoption package](adoption-packages/README.md) or [starting path](STARTING-PATHS.md).

This door should emphasize organizational consequences, decision quality, ownership, evidence, and a bounded first move. It should not require readers to understand repository structure or skill metadata.

### Do the Work

**Primary readers:** Product Managers, product teams, cross-functional partners, facilitators, consultants, trainers, and practitioners responsible for an initiative or recurring workflow.

**Question:** What decision or condition needs attention, what evidence should we bring, and what useful result will the work produce?

**Primary route:** [Starting Paths](STARTING-PATHS.md), then a practitioner journey guide, guided command, and the skills it orchestrates.

This door should be situation-led and action-oriented. It should explain participants, preparation, effort, outputs, decision authority, and what happens next before exposing the full catalog.

### Build the Library

**Primary readers:** Skill authors, maintainers, reviewers, agent integrators, and contributors.

**Question:** How is AIPOM structured, governed, validated, extended, and released?

**Primary route:** [Contribution Guide](../CONTRIBUTING.md), [Skill Specification](SKILL-SPEC.md), and [repository operating contract](../AGENTS.md).

This door should contain schemas, naming, canonical-source rules, authoring requirements, validation commands, and release mechanics. Contributor detail should remain available without dominating the executive or practitioner experience.

## Audience Routing

| Reader need | Lead with | Then offer | Avoid leading with |
|---|---|---|---|
| Understand the executive case | Organizational problem and decisions improved | Operating levels, evidence expectations, first 90 days | Folder structure, metadata, build phases |
| Select an intervention | Situation, decision, consequence, and evidence | A bounded starting path | The complete 41-skill catalog |
| Facilitate a session | Participants, preparation, sequence, authority, and completion | Canonical skills and facilitation standards | Executive positioning or repository internals |
| Evaluate the framework | Claims, limitations, evidence status, and sources | Validation reports and public-preview contract | Promotional claims or implied field proof |
| Contribute or integrate | Canonical sources and validation rules | Catalog, packaging, and release workflow | Simplified public summaries as specifications |

## Progressive Disclosure

Public documentation should move from purpose to action to implementation:

1. **Recognize the problem.** Explain why disconnected AI activity is an operating-model issue.
2. **Name the decision.** Help the reader identify the consequential decision or condition that needs to change.
3. **Choose a bounded path.** Route the reader to an organizational assessment, initiative evaluation, or workflow redesign.
4. **Do the work.** Use canonical commands and skills while preserving evidence, assumptions, decisions, and ownership.
5. **Inspect the system.** Offer the complete catalog, standards, schemas, and repository mechanics when needed.

The seven categories remain the diagnostic architecture. They should not be the only navigation available to someone arriving with an urgent decision.

## Content Ownership

| Content | Canonical source |
|---|---|
| Executive explanation and adoption route | `docs/EXECUTIVE-FIELD-GUIDE.md` |
| Sponsor-ready engagement packages | `docs/adoption-packages/` |
| Product concept, categories, levels, and intended outcomes | `docs/OPERATING-MODEL.md` |
| Situation-led entry routes | `docs/STARTING-PATHS.md`, `docs/journeys/`, and `commands/` |
| Assessment questions and scoring | `assessments/` |
| Skill content and relationships | `skills/` |
| Shared skill and facilitation requirements | `docs/SKILL-SPEC.md` and `docs/ADAPTIVE-FACILITATION.md` |
| Generated skill navigation | `catalog/` |
| Contributor operating contract | `AGENTS.md` and `CONTRIBUTING.md` |
| Release evidence and limitations | `docs/EVIDENCE-STATUS.md` and `docs/PUBLIC-PREVIEW.md` |

Summaries may appear in the README and other guides, but changes to a definition, rule, skill, score, or release claim must be made in its canonical source.

## Editorial Rules

- Begin with the reader's decision or organizational problem, not the catalog.
- Describe outcomes and changed conditions before artifacts.
- Use “Product Manager” rather than “PM” unless preserving an established term.
- Explain unfamiliar operating-model language before using it as navigation.
- Keep executive summaries brief enough to support a decision about where to begin.
- Make practitioner routes explicit about preparation, participants, authority, and completion.
- Keep evidence limitations visible without making repository validation the main value proposition.
- Never imply that completing a path proves adoption, maturity, compliance, or impact.
- Link summaries to canonical material rather than duplicating specifications.

## Test for Future Front-Door Changes

A navigation or positioning change is useful when a new reader can answer:

1. What organizational problem does AIPOM address?
2. Which decision or practice can it help me improve?
3. Where should someone in my role begin?
4. What evidence, participation, and authority will the work require?
5. What will I be able to decide or do when the work is complete?
6. What does the current public preview claim—and not claim?

If answering those questions requires reading the complete catalog or contributor contract, the front door is carrying the wrong information.
