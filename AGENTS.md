# Repository Guidelines

## Repository Mission

AI Product Operating Model Skills (AIPOM) is a structured library of tools for assessing, designing, and improving how organizations manage AI-powered products and AI-assisted product work.

The library helps organizations establish repeatable practices across seven connected areas:

1.  Strategy and Economic Outcomes
2.  Portfolio and Investment Choices
3.  Product-Team Workflows
4.  Context, Knowledge, and Data
5.  Evaluation and Evidence
6.  Governance and Accountability
7.  Capability, Adoption, and Reuse

These are organizational operating-model skills, not generic AI prompts, software engineering recipes, tool tutorials, or isolated product-management templates.

The intended users include:

-   CPOs and CTOs
-   Product and technology executives
-   Product Operations leaders
-   Product Managers
-   Design, engineering, data, and research leaders
-   Legal, privacy, security, risk, and AI governance partners
-   Consultants, trainers, and facilitators helping organizations improve AI product practice

## Operating Philosophy

### Functional and Pedagogic in Equal Measure

Every skill must serve two purposes:

1.  Help the user complete useful organizational work.
2.  Help the user understand the reasoning, evidence, tradeoffs, and failure modes behind that work.

A user should finish a skill with more than a completed artifact. They should understand how to evaluate, adapt, defend, and repeat the method.

The visible skill teaches a human facilitator how to run the method.

The embedded instructions teach an AI agent how to facilitate it responsibly.

Never optimize one audience at the expense of the other.

### Skills Change Conditions

Assessment questions diagnose organizational conditions.

Skills help change those conditions.

Do not create a skill that merely restates an assessment question or fills out a decorative canvas. Every skill must identify:

-   The condition it is designed to change
-   The evidence needed to understand that condition
-   The decisions the activity supports
-   The artifact or recommendation it produces
-   The next organizational motion it enables
-   The maturity movement it is intended to create

The output is not the outcome.

### Evidence Over Aspiration

This library distinguishes among four claims:

1.  A practice is discussed.
2.  A practice is documented.
3.  A practice is consistently used.
4.  A practice demonstrably improves decisions or outcomes.

Do not treat policies, templates, workshops, licenses, training attendance, or executive statements as proof of organizational maturity by themselves.

Where evidence matters, request or inspect:

-   Existing artifacts
-   Named owners
-   Examples of actual use
-   Decision records
-   Evaluation results
-   Adoption evidence
-   Customer or end-user evidence
-   Business or operational measures
-   Examples of decisions changed by the practice

When evidence is unavailable:

-   State what is missing.
-   Label assumptions clearly.
-   Do not quietly convert confidence into fact.
-   Do not award a maturity score above `2 - Emerging`.

### Outcomes Over Outputs

AI activity is not evidence of AI capability.

Do not measure success through:

-   Prompts submitted
-   Tokens consumed
-   Licenses purchased
-   Logins
-   Tools deployed
-   Pilots launched
-   Documents generated
-   Features labeled “AI”

Prefer evidence such as:

-   Shorter learning cycles
-   Better decisions
-   Reduced rework
-   Improved customer outcomes
-   Increased revenue
-   Protected margin
-   Reduced churn
-   Lower operating cost
-   Lower risk
-   Improved safety or compliance
-   Faster time-to-decision
-   Reuse of effective organizational practices

### Human Accountability Remains Human

AI may assist, accelerate, augment, analyze, simulate, draft, recommend, and perform bounded actions.

AI does not absorb human accountability.

Skills involving agents, automation, governance, evaluation, or decision support must make explicit:

-   What AI may do independently
-   What requires human review
-   Who decides
-   Who is accountable
-   What triggers escalation
-   What the system must never do
-   How failures are detected and corrected

## Scope Boundaries

This repository is specifically for AI Product Management operating-model work.

It is not:

-   A general Product Manager skills library
-   A collection of vendor-specific prompting tricks
-   A model-training or machine-learning engineering handbook
-   A substitute for legal, security, privacy, or regulatory review
-   A collection of generic innovation canvases with “AI” added to the title
-   A repository for Productside client-confidential material
-   A place to duplicate skills that already exist elsewhere without a clear operating-model extension

Use existing foundational skills from Product Manager Skills and MITRE ITK Skills when they already solve the underlying problem.

Examples include:

-   Problem framing
-   Positioning
-   Business health diagnosis
-   Feature investment analysis
-   Context engineering
-   Agent orchestration
-   System mapping
-   Stakeholder mapping
-   Premortems
-   Culture-building activities

The AI Product Operating Model Skills library should extend these methods into organizational AI product practice rather than manufacture weaker copies.

## The Seven Categories

Every category-specific skill must belong to one of the seven primary categories. Workflow skills that genuinely coordinate three or more categories may use `cross-category`; do not use it merely because a skill has secondary relationships.

### `strategy-and-economic-outcomes`

Determines where AI creates meaningful value, which outcomes should change, and how AI investments support broader product and business strategy.

### `portfolio-and-investment-choices`

Supports decisions about which AI opportunities should be explored, validated, funded, scaled, paused, pivoted, or retired.

### `product-team-workflows`

Redesigns repeatable product-team motions around decisions, collaboration, evidence, context, and human-AI responsibilities.

### `context-knowledge-and-data`

Establishes trusted sources, usable context, data readiness, ownership, retrieval, persistence, refresh, and lifecycle practices.

### `evaluation-and-evidence`

Defines acceptable AI behavior, evaluation methods, evidence standards, production monitoring, and evidence-based product decisions.

### `governance-and-accountability`

Translates responsible-AI principles into named ownership, controls, autonomy boundaries, escalation, incident response, and trust evidence.

### `capability-adoption-and-reuse`

Builds role-based capability, applied learning systems, adoption measures, reusable skills, stewardship, and continuous improvement.

Do not create an eighth category merely because a new skill crosses boundaries. Select the primary category and use metadata to identify secondary relationships.

## Skill Types

All skills belong to one of three types.

### Component Skills

Focused methods that produce one primary operating artifact, usually within 30 to 90 minutes.

Examples:

-   AI Bet Charter
-   Human-AI Work Contract
-   Authoritative Source Map
-   AI Behavior Contract
-   Autonomy Boundary Matrix

A component skill should be independently useful but capable of being orchestrated by larger workflows.

### Interactive Advisors

Adaptive diagnostic skills that gather context, identify the most important condition, recommend an appropriate path, and explain why.

Interactive advisors must:

-   Recognize information already supplied
-   Avoid asking questions already answered
-   Ask only for missing information
-   Adapt subsequent questions based on previous answers
-   Offer guided, context-dump, and best-guess modes
-   Present numbered recommendations at meaningful decision points
-   Accept numbered selections, combined selections, and custom responses
-   Explain why each recommendation fits
-   End with a usable diagnosis, recommendation, or artifact

An interactive advisor is not a fixed questionnaire wearing a conversational hat.

### Workflow Skills

End-to-end processes that coordinate multiple advisors and components across several decisions, artifacts, or sessions.

Examples:

-   AI Operating Model Assessment
-   AI Operating Model Design Sprint
-   AI Initiative Readiness Review
-   AI Portfolio Quarterly Review
-   AI Operating Model Roadmap

Workflow skills must preserve:

-   Supplied context
-   Evidence
-   Assumptions
-   Decisions
-   Ownership
-   Unresolved questions
-   Outputs from component skills
-   Recommended next actions

Do not make the user re-enter information already produced earlier in the workflow.

## Project Structure

Use the following repository structure:

```
.
├── AGENTS.md
├── README.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── LICENSE
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md
│       ├── template.md
│       ├── examples/
│       │   ├── worked-example.md
│       │   └── weak-example.md
│       └── assets/
├── commands/
│   └── <workflow-command>.md
├── assessments/
│   ├── aipom-operating-model-assessment.md
│   ├── evidence-rubric.md
│   └── scoring-model.md
├── catalog/
│   ├── INDEX.md
│   ├── skills-index.yaml
│   ├── skills-by-category.md
│   ├── skills-by-type.md
│   └── skills-by-phase.md
├── docs/
│   ├── SKILL-SPEC.md
│   ├── ADAPTIVE-FACILITATION.md
│   ├── EVIDENCE-STANDARD.md
│   ├── OPERATING-MODEL.md
│   ├── CONTRIBUTION-WORKFLOW.md
│   └── research/
├── scripts/
│   ├── validate-skills.py
│   ├── check-links.py
│   ├── generate-catalog.py
│   ├── build-release.sh
│   └── test-library.sh
└── dist/
```

### Canonical Sources

-   `skills/` is the source of truth for skill content.
-   `assessments/` is the source of truth for assessment questions and maturity scoring.
-   `docs/` is the source of truth for shared behavioral and structural standards.
-   `catalog/` contains generated navigation files.
-   `dist/` contains generated release artifacts.

Do not edit generated catalog or distribution files directly.

## Skill Folder and Naming Rules

Each skill lives at:

```
skills/<skill-name>/SKILL.md
```

Naming requirements:

-   Use lowercase kebab-case.
-   The folder name must exactly match the frontmatter `name`.
-   Use descriptive names based on the job performed.
-   Prefer names such as `aipom-autonomy-boundary-designer`.
-   Avoid vague names such as `aipom-helper`, `strategy-tool`, or `maturity-framework`.
-   Do not rename an existing skill without updating all references.
-   Keep skill names concise enough to remain usable across agent platforms.
-   Keep frontmatter descriptions clear, concrete, and free of promotional language.

Use “Product Manager” rather than “PM” in user-facing prose unless quoting or preserving an established term.

## Required Skill Frontmatter

Every `SKILL.md` must include valid YAML frontmatter.

Minimum structure:

```
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
 - CTO
 - VP Product
 - Product Operations
 - AI Governance

best_for:
 - Preparing an agentic product for launch
 - Resolving disagreement about human approval
 - Reviewing a system with unclear authority boundaries

evidence_required:
 - Proposed AI or agent actions
 - User and organizational consequences
 - Existing approval and escalation policies
 - Evaluation results where available

produces:
 - Autonomy boundary matrix
 - Escalation policy
 - Named accountable owners

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

See `docs/SKILL-SPEC.md` for the complete schema and allowed values.

### `evidence_required`

This field identifies the evidence that should inform the activity.

Evidence is an invitation, not a gate. Users may arrive with partial or no evidence. The skill should help identify what is missing and distinguish demonstrated practice from assumption.

### `maturity_move`

This field states the organizational condition the skill is designed to change.

Good:

>   Move autonomy governance from undocumented individual judgment to a repeatable, reviewable, and testable organizational practice.

Weak:

>   Complete an autonomy canvas.

### `assessment_questions`

Use stable assessment IDs.

Do not repeat or fork assessment questions inside individual skills. Link the skill to the relevant questions in `assessments/aipom-operating-model-assessment.md`.

## Required Skill Sections

Every `SKILL.md` should follow this human-readable structure:

1.  `# Skill Name`
2.  `## What Is It`
3.  `## Why Use It`
4.  `## When to Use It`
5.  `## What It Produces`
6.  `## Who Should Participate`
7.  `## Evidence to Bring`
8.  `## How to Do It`
9.  `## Key Concepts`
10. `## Organizational Applications`
11. `## Common Pitfalls`
12. `## Combine With`
13. `## Assets and Templates`
14. `## Sources`

Interactive and workflow skills must also include:

-   `## Facilitation Protocol`
-   `## Decision Logic`
-   `## Completion Criteria`

The detailed requirements for each section live in `docs/SKILL-SPEC.md`.

Do not turn `AGENTS.md` into a duplicate of that specification.

## Adaptive Facilitation Behavior

Use `docs/ADAPTIVE-FACILITATION.md` as the source of truth.

Unless a skill explicitly requires another pattern, interactive and workflow skills should support three entry modes:

1.  **Guided mode:** Ask one question at a time.
2.  **Context-dump mode:** Accept supplied material, extract what is already known, and ask only for meaningful gaps.
3.  **Best-guess mode:** Make reasonable assumptions, label them, and continue.

### Context Handling

Anything supplied with the request counts as context already given.

This includes:

-   Text following the skill invocation
-   Uploaded documents
-   Existing artifacts
-   Assessment results
-   Outputs from prior skills
-   Pasted notes
-   Links or repository files the agent can inspect

Do not ask the user to repeat information already available.

### Questions

-   Ask plain-language questions.
-   Ask one question at a time in guided mode.
-   Use small batches only when the questions are tightly connected and low effort.
-   Do not interrogate the user merely because the template contains empty fields.
-   Ask only for information that can change the recommendation or artifact.
-   Explain unfamiliar concepts before asking the user to score them.
-   Accept uncertainty as a valid answer.

### Decision Points

At meaningful decision points:

-   Present numbered options.
-   Explain when each option fits.
-   Recommend a default when evidence supports one.
-   Accept selections such as `1`, `1 and 3`, or custom text.
-   Synthesize combined choices rather than forcing the user to restart.

### Completion

A skill is complete when it has produced:

-   The promised artifact or recommendation
-   The evidence used
-   The assumptions made
-   The decisions reached
-   The unresolved questions
-   The named next action
-   Related skills that logically follow

Do not finish with a generic invitation to “explore further.”

## Maturity Scoring Standard

The default organizational maturity scale is:

| Score | Label           | Meaning                                                                           |
|-------|-----------------|-----------------------------------------------------------------------------------|
| 1     | Absent          | No consistent practice or accountable ownership                                   |
| 2     | Emerging        | Isolated experiments, individuals, or informal practices                          |
| 3     | Repeatable      | The practice works in some teams and can be reproduced                            |
| 4     | Operationalized | The practice is standardized, governed, and used across the organization          |
| 5     | Compounding     | The practice is measured, improved, reused, and demonstrably strengthens outcomes |

Rules:

-   No evidence means no score above 2.
-   Do not average away a critical governance, safety, legal, or accountability gap.
-   Use category profiles before calculating an overall score.
-   Preserve disagreement among respondents rather than manufacturing false consensus.
-   Distinguish organization-level maturity from initiative readiness.
-   Distinguish documented practice from adopted practice.
-   Distinguish adoption from demonstrated impact.
-   Identify the weakest consequential condition, not merely the lowest arithmetic score.
-   Recommend next motions, not just labels.

See `assessments/scoring-model.md` and `assessments/evidence-rubric.md`.

## Writing Style

Use the editorial voice of a professional facilitation toolkit.

Write with:

-   Calm authority
-   Clear definitions
-   Practical instructions
-   Explicit purpose
-   Concrete organizational application
-   Respect for the user’s judgment
-   Clear tradeoffs
-   Named failure modes
-   Short paragraphs and useful tables

Avoid:

-   Vendor marketing language
-   “Revolutionary,” “game-changing,” and similar claims
-   Generic AI enthusiasm
-   Buzzword fog
-   Fake precision
-   Unexplained jargon
-   Infantilizing nontechnical users
-   Empty motivational copy
-   Treating Product Managers as ticket writers or feature coordinators
-   Presenting frameworks as universal laws
-   Adding “AI” to an existing tool without changing its application
-   Excessive punctuation, decorative emojis, or theatrical formatting

Use examples to show reasoning, not merely finished output.

Anti-patterns are load-bearing. Do not remove them to shorten a skill.

## Common Repository Anti-Patterns

Do not introduce any of the following:

### Assessment-as-Answer

A radar chart or maturity score is not an operating-model intervention.

Every assessment must connect findings to specific skills and next actions.

### Questionnaire Disguised as Advisor

An interactive skill must interpret context and recommend a path.

It must not merely ask every question in a template and print the answers back.

### Artifact-as-Maturity

Completing a policy, charter, workshop, or template does not prove the practice is used.

### Tool-First Design

Do not begin with ChatGPT, Claude, Copilot, Gemini, Cursor, or another vendor.

Begin with the decision, workflow, outcome, evidence, or organizational condition.

### One Giant Skill

Do not create a monolithic skill that attempts to assess, redesign, govern, train, and measure the entire organization.

Use workflow skills to orchestrate smaller component and advisor skills.

### Duplicated Foundation

Do not recreate problem framing, stakeholder mapping, system mapping, premortems, context engineering, or orchestration methods when an existing library already provides a credible foundation.

### False Organizational Consensus

Do not flatten conflicting leadership, product-team, governance, and practitioner perspectives into a single confident score.

Surface the disagreement and explain why it matters.

### Risk by Arithmetic

Do not let high scores in low-risk areas compensate for a missing non-negotiable control.

### Phase Inflation

Do not add later-phase skills merely to increase the catalog count.

Each phase must produce a coherent, usable release.

## Four-Phase Build Discipline

The planned library contains 41 skills across four phases.

`ROADMAP.md` is the source of truth for phase membership and progress.

### Phase 1: Assess and Establish the Foundation

Build the minimum viable operating-model system:

-   Organization assessment
-   Operating-model roadmap
-   Seven category advisors
-   Foundational charters and contracts
-   Workflow-to-skill conversion

Phase 1 should work as a complete assessment-to-action loop.

### Phase 2: Make Core Practices Repeatable

Build the components needed to turn findings into repeatable practices:

-   Opportunity framing
-   Outcome mapping
-   Use-case triage
-   Investment gates
-   Productive-motion mapping
-   Workflow playbooks
-   Source and data readiness
-   Accountability
-   Role competencies

### Phase 3: Build Evidence and Control Systems

Add deeper economic, evaluation, context-lifecycle, dependency, and incident-control infrastructure.

### Phase 4: Scale, Assure, and Institutionalize

Add recurring portfolio review, production evidence review, trust assurance, learning systems, adoption measurement, and operating-model retrospectives.

### Phase Rules

-   Work within the current active phase unless explicitly instructed otherwise.
-   Do not create empty placeholders for later phases.
-   Do not mark a skill complete until its content, examples, metadata, templates, links, and validation pass.
-   Prefer a smaller complete phase over a large partially built catalog.
-   Update `ROADMAP.md` when phase status changes.
-   Do not silently move skills between phases.

## Research and Source Standards

Use primary or authoritative sources whenever a skill depends on:

-   Laws or regulations
-   Industry standards
-   Government guidance
-   Published frameworks
-   Named methodologies
-   Technical specifications
-   Current product or platform capabilities

Record:

-   Source title
-   Publishing organization
-   URL
-   Publication or update date when available
-   Access date for time-sensitive material
-   Which claim or method the source supports

For legal, regulatory, privacy, safety, and security material:

-   Do not present the skill as legal advice.
-   State jurisdiction and sector assumptions.
-   Separate requirements from recommended practices.
-   Flag information likely to change.
-   Do not claim that completing a skill establishes compliance.

Do not invent citations, statistics, case studies, or framework provenance.

Synthetic examples must be labeled as synthetic.

## Build and Validation Commands

This is a Markdown-first repository with lightweight Python and shell validation.

Use:

```
rg --files
```

List repository files.

```
rg "skill-name"
```

Find references before adding, renaming, or removing a skill.

```
python3 scripts/validate-skills.py
```

Validate frontmatter, required sections, allowed metadata, skill-folder names, and maturity mappings.

```
python3 scripts/check-links.py
```

Check internal links and cross-skill references.

```
python3 scripts/generate-catalog.py
```

Regenerate catalog indexes from canonical skill metadata.

```
./scripts/test-library.sh
```

Run the complete validation suite.

```
./scripts/build-release.sh
```

Build release artifacts after validation succeeds.

If a referenced script does not yet exist:

-   Do not pretend it ran.
-   Validate manually where practical.
-   Report the missing automation.
-   Create the script only when it is in scope for the task.

## Skill Development Workflow

Before creating or changing a skill:

1.  Read this `AGENTS.md`.
2.  Read `README.md`.
3.  Read `ROADMAP.md`.
4.  Read `docs/SKILL-SPEC.md`.
5.  Read `docs/ADAPTIVE-FACILITATION.md` for interactive or workflow skills.
6.  Inspect at least one comparable existing skill.
7.  Search for overlapping skills in this repository and referenced libraries.
8.  Confirm the skill’s category, type, phase, operating level, and maturity move.
9.  Identify which assessment questions it addresses.

When implementing:

1.  Create or update `skills/<skill-name>/SKILL.md`.
2.  Add `template.md` when the skill produces a repeatable artifact.
3.  Add at least one worked example.
4.  Add at least one weak or failed example when useful.
5.  Include explicit common pitfalls.
6.  Add sources for external frameworks or current requirements.
7.  Add cross-skill relationships.
8.  Run validation.
9.  Regenerate catalogs.
10. Review the diff for accidental generated-file edits or unrelated changes.

A new skill is not complete because `SKILL.md` exists.

## Skill Quality Checklist

A skill is release-ready only when:

-   The purpose and trigger conditions are clear.
-   The skill changes a named organizational condition.
-   The promised output is specific.
-   The evidence requirements are defined.
-   Users may arrive with partial or no evidence.
-   The operating level is explicit.
-   The skill distinguishes facts, evidence, assumptions, and recommendations.
-   The facilitation behavior adapts to supplied context.
-   The skill avoids questions already answered.
-   Examples demonstrate reasoning.
-   At least one meaningful anti-pattern is included.
-   Human decision authority and accountability are explicit where relevant.
-   Maturity claims follow the evidence standard.
-   Related skills and dependencies resolve.
-   Internal links pass.
-   Catalog metadata validates.
-   The skill can be used by both a human facilitator and an AI agent.
-   The user should understand more when finished than when they started.

## Generated Files

Do not edit these directly:

-   `catalog/skills-index.yaml`
-   `catalog/skills-by-category.md`
-   `catalog/skills-by-type.md`
-   `catalog/skills-by-phase.md`
-   Files under `dist/`

Update canonical sources and regenerate them through repository scripts.

## Compatibility

Skills should remain readable and useful without a specific agent platform.

Avoid:

-   Runtime-specific placeholders that appear as unexplained text elsewhere
-   Tool calls embedded as mandatory syntax
-   Assumptions about one model provider
-   Instructions dependent on one proprietary interface
-   Hidden context that a human facilitator cannot inspect

Agent integrations may adapt the canonical skills for:

-   Codex
-   ChatGPT
-   Claude
-   Claude Code
-   Cursor
-   Gemini
-   Copilot
-   Other systems capable of loading structured instructions

The canonical `SKILL.md` remains platform-neutral.

Platform-specific packaging belongs in build scripts or distribution directories.

## Codex Working Guidance

When asked to perform work in this repository:

-   Inspect relevant repository guidance and existing patterns before improvising.
-   Prefer the most specific existing skill or specification.
-   Make the smallest coherent change that fulfills the request.
-   Preserve existing naming, metadata, and editorial conventions.
-   Do not broaden the task into an unrelated refactor.
-   Reuse supplied context.
-   Do not ask for information already available in the repository.
-   Use repository scripts and source-of-truth files before relying on opinion.
-   Validate all changed skills and cross-links.
-   Run the complete test suite when practical.
-   Report tests not run and why.
-   Do not claim a script passed unless it was actually executed.
-   Do not modify generated artifacts by hand.
-   Do not publish, commit, push, or open a pull request unless explicitly instructed.

This repository contains organizational methods and documentation, not conventional application code. Review for conceptual correctness, evidence quality, facilitation behavior, and cross-skill coherence, not merely syntax.

## Commit and Pull Request Guidelines

Use imperative commit subjects.

Examples:

```
Add AI autonomy boundary designer
Strengthen evidence rubric for maturity scoring
Connect portfolio advisor to stage-gate skills
```

Pull requests should include:

-   A concise summary
-   The skill type and category
-   The roadmap phase
-   The organizational condition changed
-   The assessment questions addressed
-   New or changed artifacts
-   Validation performed
-   Known limitations or unresolved questions
-   Relevant issues or sources

Avoid commit messages such as:

```
Updates
More AI stuff
Fix docs
```

## Release Checklist

Before preparing a release:

-   Confirm all active-phase skills are complete.
-   Run `./scripts/test-library.sh`.
-   Regenerate catalogs.
-   Rebuild release artifacts.
-   Verify skill counts in `README.md`.
-   Verify phase counts in `ROADMAP.md`.
-   Spot-check category, type, and phase indexes.
-   Confirm all cross-skill links resolve.
-   Confirm examples and templates are included.
-   Confirm sources are accurate.
-   Confirm no confidential client material is present.
-   Confirm generated artifacts match canonical sources.
-   Summarize notable maturity moves enabled by the release.

## Final Governing Principle

This repository is not trying to help organizations look more mature at AI Product Management.

It is trying to help them operate more maturely.

When choosing between:

-   A polished score and an uncomfortable finding
-   A completed artifact and a changed practice
-   More AI activity and a better decision
-   Faster output and stronger evidence
-   Automation and accountable judgment

Choose the second.
