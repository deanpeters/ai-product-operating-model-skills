# Current-State Handoff

Use this document when a coworker or a new coding agent picks up the repository without the conversation that produced it.

Last updated: 2026-07-17

## Cold Start

Read these files in order:

1. [README](../README.md) — public purpose, audiences, and entry points
2. [This handoff](HANDOFF.md) — current source state and next work
3. [Repository Working Agreement](../AGENTS.md) — non-negotiable project rules
4. [Active Post-Release Roadmap](POST-RELEASE-ROADMAP.md) — release direction
5. [Skill Specification](SKILL-SPEC.md) — only when changing canonical skills or metadata

Then run:

```bash
git status --short
git log -5 --oneline --decorate
./scripts/test-library.sh
```

Do not begin by generating new skills. The planned 41-skill catalog is complete.

## Repository and Release State

- Public repository: <https://github.com/deanpeters/ai-product-operating-model-skills>
- Active branch: `main`
- Current tagged release: `v0.5`, published as a synthetic-data public preview
- License: CC BY-NC-SA 4.0
- Canonical library: 41 active skills across seven categories and four build phases
- Assessment: 35 stable questions with evidence and maturity-scoring rules
- Public entry routes: three practitioner journeys and six executive adoption packages
- Primary execution personas: Product Operations, Product Manager, and Team Lead
- Platform packaging: canonical platform-neutral archive plus a generated Codex-compatible archive

The tagged `v0.5` assets are the original launch snapshot. Public `main` also contains the post-launch executive, practitioner, persona, and documentation experience layers. Do not assume the tagged archives contain every improvement now visible on `main`.

## What Exists Now

### Public front doors

- [README](../README.md) welcomes people by role, working style, and problem.
- [Target Personas](TARGET-PERSONAS.md) defines execution roles and authority boundaries.
- [Starting Paths](STARTING-PATHS.md) compares organization, initiative, and workflow journeys.
- [Executive Field Guide](EXECUTIVE-FIELD-GUIDE.md) explains the leadership case.
- [Documentation Guide](README.md) routes readers through the rest of the repository.

### Practitioner execution layer

- [Product Operations flow](personas/PRODUCT-OPERATIONS.md)
- [Product Manager flow](personas/PRODUCT-MANAGER.md)
- [Team Lead flow](personas/TEAM-LEAD.md)
- [Assess an Organization](journeys/ASSESS-AN-ORGANIZATION.md)
- [Evaluate an AI Initiative](journeys/EVALUATE-AN-AI-INITIATIVE.md)
- [Redesign a Product-Team Workflow](journeys/REDESIGN-A-PRODUCT-TEAM-WORKFLOW.md)

### Executive engagement layer

The [Executive Adoption Packages](adoption-packages/README.md) organize existing skills around alignment, investment, readiness, workflow pilots, governance, and quarterly portfolio decisions. They are navigation and engagement layers, not additional canonical skills.

### Canonical method layer

- `skills/` is the source of truth for methods, metadata, templates, and examples.
- `assessments/` is the source of truth for questions, evidence scoring, and maturity logic.
- Shared standards live in `docs/SKILL-SPEC.md`, `docs/ADAPTIVE-FACILITATION.md`, and `docs/EVIDENCE-STANDARD.md`.
- `commands/` contains the compact facilitation and agent execution layer for the three starting paths.
- `catalog/` is generated from skill metadata. Do not edit it manually.
- `dist/` is generated release output and is ignored by Git.

## Recent Changes to Understand

The public experience was deliberately reorganized after the original `v0.5` launch:

1. The README now begins with recognizable people, problems, and benefits rather than repository architecture.
2. Leaders have an executive field guide and six adoption packages.
3. Practitioners have three detailed journey guides above the command layer.
4. Product Operations, Product Managers, and Team Leads have plain-English role flows.
5. Relevant canonical skills now include those execution personas in audience metadata and selected participation guidance.
6. The generated catalog includes a skills-by-persona view.
7. `scripts/test-library.sh` compares generated catalogs before and after generation, so uncommitted but correctly regenerated catalogs can validate.

Current audience coverage is intentionally selective:

- Product Manager: 41 of 41 skills
- Product Operations: 37 of 41 skills; specialist-only data, evaluation-set, and platform builders remain excluded
- Team Lead: 32 of 41 skills; executive strategy, portfolio allocation, economic-case, platform-audit, and assurance-pack methods remain excluded

Audience inclusion means the role performs, coordinates, decides, facilitates, or acts on the method. It does not transfer specialist or executive authority.

## Validation and Release Commands

Run the complete source and generated-catalog suite:

```bash
./scripts/test-library.sh
```

Build both release archives and checksums:

```bash
./scripts/build-release.sh
```

Useful focused checks:

```bash
python3 scripts/validate-skills.py
python3 scripts/check-links.py
python3 scripts/validate-release.py
python3 scripts/generate-catalog.py
git diff --check
```

If skill metadata changes, regenerate the catalog and include the generated diff. Never hand-edit `catalog/skills-index.yaml`, the generated catalog pages, or files under `dist/`.

## Evidence Boundary

`v0.5` is structurally validated and synthetically forward-tested. It is not field-proven, compliance-certified, or evidence of organizational adoption or impact.

The repository includes a complete [human-validation kit](validation/README.md), but the planned external sessions are still pending. All public examples are synthetic. Consequential decisions require accountable business, product, technical, operational, legal, privacy, security, safety, risk, finance, governance, or domain specialists as appropriate.

## Recommended Next Work

### 1. Test the new practitioner front door

Ask at least one Product Operations practitioner, Product Manager, and Team Lead to begin cold from the README and their persona page. Observe whether each person can:

- Recognize what is in the library for them
- Choose a starting journey without catalog knowledge
- Explain what evidence and participation the work requires
- Identify their authority and the decisions that remain with others
- State the first useful action in their own words

Capture terminology friction and missing tactical steps. Update role flows and relevant skills rather than adding more top-level strategy material.

### 2. Run the prepared human pilots

Use the [Validation Hub](validation/README.md) to run the executive/portfolio, product/initiative, and governance/operations sessions. Record only sanitized, non-confidential findings in the public findings register.

### 3. Decide the next tagged release contract

The current `VERSION` and release validator support `0.x` versions such as `0.5` and `0.6`, not patch forms such as `0.5.1`. Either:

- Use `v0.6` for the next tagged evidence and usability release, or
- Explicitly expand the versioning, changelog, packaging, and validation contract before creating a patch tag.

Do not overwrite the existing `v0.5` tag or silently replace its historical assets.

### 4. Continue the active post-release roadmap

After field and persona findings, improve facilitation, examples, cross-platform behavior, adoption evidence, and stable contracts. Do not add skills merely to increase the catalog count.

## Known Limitations

- Human field validation remains pending.
- The role flows and executive packages have not yet been tested with representative external users.
- Examples are synthetic.
- Only Codex has a generated platform-specific package today.
- Audience metadata shows intended participation, not proven usability or adoption.
- External URL availability is not checked in CI.
- The tagged `v0.5` release assets predate the latest public-experience improvements on `main`.

## Change Guardrails

- Preserve the CC BY-NC-SA 4.0 license and attribution.
- Never add Productside client-confidential material, personal data, raw session notes, recordings, credentials, privileged advice, or security-sensitive information.
- Do not claim field effectiveness, adoption, impact, certification, or compliance without evidence.
- Do not let strong value or maturity scores hide critical safety, legal, privacy, security, accountability, evaluation, rollback, or incident gaps.
- Keep human decision authority explicit.
- Use canonical source files and regenerate derived files.
- Update this handoff whenever current state, active next work, versioning, or validation behavior changes materially.

## Definition of a Good Handoff

A new coworker or coding agent should be able to clone the repository, read the five cold-start files, run validation, explain the current evidence boundary, locate the canonical sources, and select the next task without needing the conversation that created the repository.
