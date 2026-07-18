# Skill Contribution Workflow

Use this workflow to move from an idea or source document to a validated AIPOM skill.

## 1. Preflight

- Confirm the proposal improves an existing skill or addresses a documented operating-model gap that warrants an explicit roadmap amendment.
- Search this repository and referenced skill libraries for overlap.
- Identify the operating-model extension beyond any foundational method.
- Confirm one primary category, skill type, operating levels, and assessment IDs.
- State the organizational condition and intended maturity movement.

Stop if the proposal is a generic Product Manager method, vendor tutorial, decorative canvas, duplicate foundation, assessment question disguised as an intervention, or catalog growth without a demonstrated gap.

## 2. Define the Contract

Before drafting prose, write down:

- Trigger conditions
- Evidence inputs
- Decisions supported
- Primary artifact or recommendation
- Human decision authority and accountability
- Next organizational motion
- Completion criteria
- Relevant failure modes

## 3. Draft the Canonical Skill

Create:

```text
skills/<skill-name>/SKILL.md
```

Follow [SKILL-SPEC.md](SKILL-SPEC.md). For interactive advisors and workflows, also follow [ADAPTIVE-FACILITATION.md](ADAPTIVE-FACILITATION.md).

## 4. Add the Artifact and Examples

- Add `template.md` for a repeatable output.
- Add `examples/worked-example.md` for every active skill.
- Add `examples/weak-example.md` when it teaches an important evidence, reasoning, or facilitation failure.
- Mark synthetic examples clearly.
- Use examples to demonstrate reasoning, not merely polished output.

## 5. Source Claims

Use primary or authoritative sources for laws, standards, named methods, specifications, and current platform capabilities. Record what each source supports.

Do not present a skill as legal advice or claim it establishes compliance.

## 6. Validate

Run:

```bash
python3 scripts/validate-skills.py
python3 scripts/check-links.py
python3 scripts/generate-catalog.py
./scripts/test-library.sh
```

Fix canonical source files and regenerate catalogs. Do not hand-edit generated files.

## 7. Review Conceptual Quality

Confirm that the skill:

- Changes a condition rather than merely produces an output
- Treats evidence as an invitation rather than an entry gate
- Distinguishes facts, evidence, assumptions, and recommendations
- Does not ask for context already supplied
- Preserves disagreement when it matters
- Makes accountability explicit
- Produces a named next action
- Teaches the user how to adapt and defend the method

## 8. Update Status

Update `ROADMAP.md` only when the definition of done is met. Regenerate catalogs and run the full test suite again.

Do not mark a skill active based on prose alone.

## Starter Pack Changes

A Starter Pack change begins with a persona-and-job decision, not a desire to expose more skills.

1. Update the canonical manifest under `starter-packs/manifests/`.
2. Change shared templates or adapters only when the generated working-project contract changes for more than one pack.
3. Keep package membership out of skill frontmatter.
4. Run `python3 scripts/validate-starter-packs.py` to resolve recursive dependencies and validate repository paths.
5. Regenerate the catalog and inspect `catalog/skills-by-starter-pack.md` for unintended primary or dependency changes.
6. Generate the affected pack into a clean temporary directory and run the complete repository suite.

Do not edit generated pack folders, `PACK-LOCK.yaml`, catalog files, or files under `dist/` as canonical sources.
