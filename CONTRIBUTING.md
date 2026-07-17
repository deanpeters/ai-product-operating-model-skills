# Contributing to AIPOM

AIPOM contributions should change an organizational condition, not merely add another template.

## Before You Begin

Read, in order:

1. [AGENTS.md](AGENTS.md)
2. [ROADMAP.md](ROADMAP.md)
3. [Skill specification](docs/SKILL-SPEC.md)
4. [Evidence standard](docs/EVIDENCE-STANDARD.md)
5. [Adaptive facilitation](docs/ADAPTIVE-FACILITATION.md) for interactive advisors and workflows
6. [Contribution workflow](docs/CONTRIBUTION-WORKFLOW.md)

Search for overlap before proposing a skill:

```bash
rg "relevant term|possible-skill-name" .
```

Use an existing foundational skill when it already solves the underlying problem. An AIPOM contribution must add a meaningful operating-model application.

## Contribution Standard

A contribution must identify:

- The organizational condition it changes
- The evidence needed to understand that condition
- The decision or decisions it supports
- The artifact or recommendation it produces
- The next organizational motion it enables
- The maturity movement it is intended to create
- Where human decision authority and accountability remain

Synthetic examples must be labeled. Do not contribute confidential client material.

## Validation

Install the development dependency:

```bash
python3 -m pip install -r requirements-dev.txt
```

Then run:

```bash
./scripts/test-library.sh
```

After changing skill metadata, regenerate catalogs and confirm the generated diff:

```bash
python3 scripts/generate-catalog.py
./scripts/test-library.sh
```

Do not edit files in `catalog/` or `dist/` directly.

## Change Discipline

- Keep changes focused.
- Preserve canonical names and stable assessment IDs.
- Do not move skills between phases without updating `ROADMAP.md` and explaining why.
- Use primary or authoritative sources for laws, standards, named frameworks, and time-sensitive requirements.
- Do not claim validation passed unless you ran it.

## License

By contributing, you agree that your contribution will be licensed under the repository’s [CC BY-NC-SA 4.0 license](LICENSE).

