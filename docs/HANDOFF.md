# Current-State Handoff

Use this document when a coworker or a new coding agent picks up the repository without the conversation that produced it.

Last updated: 2026-07-20

## Cold Start

Read these files in order:

1. [README](../README.md) — public purpose, audiences, and entry points
2. [This handoff](HANDOFF.md) — current source state and next work
3. [Repository Working Agreement](../AGENTS.md) — non-negotiable project rules
4. [Active Post-Release Roadmap](POST-RELEASE-ROADMAP.md) — release direction
5. [Skill Specification](SKILL-SPEC.md) — only when changing canonical skills or metadata

Then run:

```bash
git pull --ff-only
git status --short
git log -5 --oneline --decorate
./scripts/test-library.sh
```

Do not begin by generating new skills. The planned 41-skill catalog is complete.

### Copy/paste kickoff prompt for another coding agent

```text
Read AGENTS.md, README.md, docs/HANDOFF.md, and docs/POST-RELEASE-ROADMAP.md in full. Then inspect git status and the latest five commits, run ./scripts/test-library.sh, and report: (1) the current release and evidence boundary, (2) canonical versus generated sources, (3) the highest-priority unfinished work, and (4) any blocker. Do not create new skills, edit generated files directly, rebuild a published tag, or begin the deferred Streamlit workbench unless I explicitly authorize it.
```

## Repository and Release State

- Public repository: <https://github.com/deanpeters/ai-product-operating-model-skills>
- Active branch: `main`
- Current tagged release: [`v0.6`](https://github.com/deanpeters/ai-product-operating-model-skills/releases/tag/v0.6), published as a GitHub prerelease and role-led synthetic-data public preview
- Release commit: `b5ef9752c7247ef4dc6a09d0e5b443dc7a2036af`
- Published release assets: canonical library ZIP, Codex ZIP, five Starter Pack ZIPs, and combined `SHA256SUMS`
- License: CC BY-NC-SA 4.0
- Canonical library: 41 active skills across seven categories and four build phases
- Assessment: 35 stable questions with evidence and maturity-scoring rules
- Public entry routes: five leadership and practitioner journeys plus six executive adoption packages
- Target personas: Head of Product and CTO leadership roles plus Product Operations, Product Manager, and Team Lead execution roles
- Platform packaging: canonical platform-neutral archive, generated Codex-compatible archive, repository-root Claude Code plugin, and five Starter Pack archives
- Starter Packs: product contract, five manifests, generator, shared shell, native Codex and Claude Code adapters, cross-platform wrappers, deterministic archives, checksums, extraction verification, focused tests, and product phases 0–6 complete

The tagged `v0.6` assets contain the executive, practitioner, persona, journey, and Starter Pack experience as it existed at the release commit. The long-form `INTRODUCTION.md`, README ASCII-and-badge header, dynamic-version CI repair, and release-builder inclusion of `INTRODUCTION.md` were added afterward on `main`. Do not rewrite the `v0.6` tag or replace its historical assets to pull those later changes backward. The tagged `v0.5` assets likewise remain the immutable original launch snapshot.

## Pickup Snapshot

The repository has crossed the “build the catalog and packaging” boundary. The immediate job is no longer to create more methods. It is to put the existing experience in front of representative people, observe where it fails, and make focused corrections.

| Area | Current state | Do next |
|---|---|---|
| Canonical library | 41 of 41 planned skills active | Improve only from a documented gap or observed use |
| Public release | v0.6 published with eight assets | Preserve the tag; prepare a later release only from accepted findings |
| Personas and journeys | Five role flows and five end-to-end journeys complete | Cold-test with one representative person per role |
| Starter Packs | Five distinct packs generate, package, and pass synthetic cold-start checks | Run observed human cold starts against real but safe decisions |
| Evidence | Structural and synthetic evidence complete | Gather anonymized human facilitation and decision evidence |
| Interface | Streamlit direction documented only | Do not implement until explicitly prioritized |

## What Exists Now

### Public front doors

- [README](../README.md) uses badges and an ASCII banner, then welcomes people by role, working style, and problem.
- [Introduction](../INTRODUCTION.md) is the world-facing narrative article and practical Starter Pack walkthrough.
- [Target Personas](TARGET-PERSONAS.md) defines leadership and execution roles, their Starter Packs, and authority boundaries.
- [Starting Paths](STARTING-PATHS.md) compares all five product-direction, technical-readiness, organization, initiative, and workflow journeys.
- [Executive Field Guide](EXECUTIVE-FIELD-GUIDE.md) explains the leadership case.
- [Documentation Guide](README.md) routes readers through the rest of the repository.

### Role-led execution layer

- [Head of Product flow](personas/HEAD-OF-PRODUCT.md)
- [CTO flow](personas/CTO.md)
- [Product Operations flow](personas/PRODUCT-OPERATIONS.md)
- [Product Manager flow](personas/PRODUCT-MANAGER.md)
- [Team Lead flow](personas/TEAM-LEAD.md)
- [Assess an Organization](journeys/ASSESS-AN-ORGANIZATION.md)
- [Evaluate an AI Initiative](journeys/EVALUATE-AN-AI-INITIATIVE.md)
- [Redesign a Product-Team Workflow](journeys/REDESIGN-A-PRODUCT-TEAM-WORKFLOW.md)
- [Set AI Product Direction](journeys/SET-AI-PRODUCT-DIRECTION.md)
- [Establish the AI Technical Readiness Bar](journeys/ESTABLISH-AI-TECHNICAL-READINESS-BAR.md)

### Executive engagement layer

The [Executive Adoption Packages](adoption-packages/README.md) organize existing skills around alignment, investment, readiness, workflow pilots, governance, and quarterly portfolio decisions. They are navigation and engagement layers, not additional canonical skills.

### Canonical method layer

- `skills/` is the source of truth for methods, metadata, templates, and examples.
- `assessments/` is the source of truth for questions, evidence scoring, and maturity logic.
- Shared standards live in `docs/SKILL-SPEC.md`, `docs/ADAPTIVE-FACILITATION.md`, and `docs/EVIDENCE-STANDARD.md`.
- `commands/` contains the compact facilitation and agent execution layer for the five starting paths.
- `catalog/` is generated from skill metadata. Do not edit it manually.
- `dist/` is generated release output and is ignored by Git.

## Recent Changes to Understand

The public experience was deliberately reorganized for the `v0.6` release:

1. The README now begins with recognizable people, problems, and benefits rather than repository architecture.
2. Leaders have an executive field guide and six adoption packages.
3. Leadership and execution personas have five detailed journey guides above the command layer.
4. Heads of Product, CTOs, Product Operations, Product Managers, and Team Leads have plain-English role flows.
5. Relevant canonical skills identify those roles or their established equivalent titles in audience metadata and participation guidance.
6. The generated catalog includes skills-by-persona and manifest-derived skills-by-Starter-Pack views.
7. `scripts/test-library.sh` compares generated catalogs before and after generation, so uncommitted but correctly regenerated catalogs can validate.
8. `INTRODUCTION.md` now provides a long-form public launch story, quick-start instructions, package anatomy, evidence boundaries, and a direct field-feedback invitation.
9. The README now carries a sibling-repository-style ASCII identity and badges for CI, stars, license, version, skill count, Starter Packs, and the synthetic evidence label.
10. Claude Code users can install the complete canonical library through the `aipom-skills` marketplace as the `aipom` plugin. The repository root is the plugin source, so `skills/` and `commands/` remain canonical and are not copied into a second maintained tree.
11. `.github/workflows/validate-library.yml` reads the current version from `VERSION` rather than assuming v0.5 archive names.
12. `scripts/build-release.sh` includes `INTRODUCTION.md` in future canonical release archives so the README link survives clean extraction.

Current audience coverage is intentionally selective:

- Head of Product: 21 of 41 skills through `Head of Product`, CPO, and VP Product role-family metadata; this includes equivalent SVP of Product roles
- CTO: 18 of 41 skills, including strategy, platform, context, data, evaluation, governance, and assurance methods where senior technology authority is consequential
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

This now builds the canonical library archive, Codex skill archive, all five Starter Pack archives, `dist/STARTER-PACK-SHA256SUMS`, the combined `dist/SHA256SUMS`, and `dist/STARTER-PACK-COLD-START.yaml`. It also verifies clean extraction, Starter Pack operation from the canonical archive, and the automated synthetic cold-start contract.

The complete build is the release-integrity gate, not merely a packaging convenience. A prior GitHub Actions run exposed that `README.md` linked to `INTRODUCTION.md` while the canonical ZIP omitted that file. The builder now includes it, and the complete local build passes. If CI is red, inspect the current run before assuming the skill library itself failed.

Useful focused checks:

```bash
python3 scripts/validate-skills.py
python3 scripts/check-links.py
python3 scripts/validate-release.py
python3 scripts/validate-starter-packs.py
python3 -m unittest discover -s tests -p 'test_create_starter_pack.py'
python3 scripts/generate-catalog.py
git diff --check
```

If skill metadata, dependencies, or Starter Pack manifests change, regenerate the catalog and include the generated diff. Never hand-edit `catalog/skills-index.yaml`, `catalog/starter-packs-index.yaml`, the generated catalog pages, or files under `dist/`.

## Evidence Boundary

`v0.6` is structurally validated and synthetically forward-tested, including clean-room cold-start checks for all five Starter Packs. It is not field-proven, compliance-certified, or evidence of organizational adoption or impact.

The repository includes a complete [human-validation kit](validation/README.md), but the planned external sessions are still pending. All public examples are synthetic. Consequential decisions require accountable business, product, technical, operational, legal, privacy, security, safety, risk, finance, governance, or domain specialists as appropriate.

## Recommended Next Work

### 1. Run one observed Starter Pack cold start per persona

Ask a Head of Product, CTO, Product Operations practitioner, Product Manager, and Team Lead to begin cold from either the README or the appropriate downloaded Starter Pack. Observe whether each person can:

- Recognize what is in the library for them
- Choose a starting journey without catalog knowledge
- Explain what evidence and participation the work requires
- Identify their authority and the decisions that remain with others
- State the first useful action in their own words

Capture terminology friction, setup failures, missing tactical steps, inappropriate authority, and whether the person can reach the first meaningful decision point. Update manifests, templates, role flows, or relevant canonical skills rather than adding more top-level strategy material.

### 2. Put one real but bounded decision through a pack

Prefer a low-consequence decision with real disagreement and usable evidence. The strongest initial candidate is the Product Manager initiative pack because it exercises the broadest dependency chain and ends in a proceed, constrain, remediate, pause, or stop recommendation. Do not use confidential client material in the public repository.

### 3. Run the prepared human pilots

Use the [Validation Hub](validation/README.md) to run the executive/portfolio, product/initiative, and governance/operations sessions. Record only sanitized, non-confidential findings in the public findings register.

### 4. Triage findings before changing the catalog

Prioritize authority or safety failures, then decision failures, facilitation failures, and editorial friction. Correct the smallest canonical source that owns the problem, regenerate derived artifacts, and rerun the complete suite. Do not manufacture a new skill when a template, adapter, manifest, journey, or existing skill is the actual source of the failure.

### 5. Continue the active post-release roadmap

After field and persona findings, improve facilitation, examples, cross-platform behavior, adoption evidence, and stable contracts. Do not add skills merely to increase the catalog count.

### Deferred interface direction

The [post-release roadmap](POST-RELEASE-ROADMAP.md#deferred-product-direction-scenario-guided-aipom-workbench) records a possible scenario-guided Streamlit workbench with API/BYOK, local Ollama, and provider-native subscription paths. This is a future option under consideration, not the next authorized build. Do not begin implementation until the maintainer explicitly prioritizes it after comparing other interface ideas.

### Starter Packs phase boundary

The [Starter Packs product contract](STARTER-PACKS.md) and canonical manifests under `starter-packs/` define the selected project-native direction. **Starter Pack product phases 0 through 6** are complete; these are separate from the completed library build phases in `ROADMAP.md`. `scripts/create-starter-pack.py` generates a safe working project from one manifest and the canonical library. Platform selection generates Codex `$aipom-start`, Claude Code `/aipom-start`, or both; root Bash and PowerShell wrappers forward the same interface. `scripts/build-starter-pack-release.py` builds deterministic archives and verifies reproducibility, extraction, internal links, lockfiles, and both native adapter layouts. Phase 7's [synthetic cold-start gate](validation/starter-pack-cold-start-report.md) passes all five packs; representative-persona use remains pending.

### Claude Code plugin boundary

The repository root is also a single Claude Code plugin named `aipom`, distributed through the `aipom-skills` marketplace. This provides low-friction access to all canonical skills and workflow commands inside an existing project. It does not generate context, evidence, decision, or output ledgers and does not replace Starter Packs for durable multi-session work. Keep `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, and `VERSION` synchronized through `scripts/validate-claude-plugin.py`; validate the native contract with `claude plugin validate .` before release.

## Known Limitations

- Human field validation remains pending.
- The role flows and executive packages have not yet been tested with representative external users.
- Examples are synthetic.
- The tagged `v0.5` release includes only the original canonical and Codex library archives; use `v0.6` for the five Starter Packs.
- Audience metadata shows intended participation, not proven usability or adoption.
- External URL availability is not checked in CI.
- The tagged `v0.6` release is the first snapshot of the five-persona public experience.
- The post-release `INTRODUCTION.md` and README visual header are on `main` but not inside the immutable published `v0.6` archives.
- The Claude Code plugin is implemented on `main` after the `v0.6` tag and has passed native manifest validation, but a representative clean-install usability session remains pending.
- The scenario-guided Streamlit workbench is documented only as a deferred direction; no application code or implementation commitment exists.
- Starter Packs require Python plus the development dependencies. The PowerShell wrapper is structurally covered but could not be executed on the macOS development host because PowerShell is not installed there.

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
