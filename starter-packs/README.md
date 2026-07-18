# AIPOM Starter Packs

Starter Packs are small, job-led AIPOM playbooks that generate self-contained working projects for people using Codex, Claude Code, or another compatible coding agent.

The intended experience is simple: choose a recognizable job, generate a working folder, place available context and evidence inside it, launch the preferred coding agent, and begin a guided AIPOM workflow.

## Current Status

Starter Pack product phases 0 through 6 are complete. These are separate from the [library build phases](../ROADMAP.md):

- The Starter Packs product and source contract is documented.
- A machine-readable manifest schema exists.
- Five pack manifests exist across leadership and execution roles.
- Manifest structure, repository paths, canonical skill references, and recursive dependencies validate.
- The Python generator supports both an interactive wizard and command-line arguments.
- Shared templates create a platform-neutral working project with agent guidance, ledgers, workspace folders, canonical dependencies, licensing, and a reproducible lockfile.
- Native `$aipom-start` and `/aipom-start` project skills make generated packs discoverable in Codex and Claude Code.
- Bash and PowerShell wrappers provide the same wizard, help, and arguments without requiring users to call the Python file directly.
- Release automation builds deterministic ZIPs for all five packs, publishes SHA-256 checksums, verifies reproducible archive bytes, extracts each archive cleanly, checks internal links, and confirms both native agent layouts.

Generated working folders and ZIPs remain disposable build outputs under ignored `dist/`. Do not hand-build or commit them as canonical sources.

## Current Starter Packs

Each Starter Pack contains a different, job-specific selection of canonical AIPOM skills. The project shell is shared—agent instructions, context and evidence folders, working ledgers, licensing, and native agent entry points—but the workflow, skills, dependencies, outputs, and authority boundaries differ.

| Starter Pack | Primary skills | Total with dependencies | Why this pack exists |
|---|---|---:|---|
| `head-of-product-direction` | Strategy Thesis Advisor; Portfolio Posture Advisor | 2 | Help a Head of Product, CPO, or SVP of Product set direction, non-goals, portfolio posture, and first commitments |
| `cto-technical-readiness` | Platform Dependency Audit; Context Readiness; Data Readiness; Evaluation Strategy; Risk, Control, and Incident Playbook | 14 | Help a CTO establish the technical evidence, dependency, control, exception, and recovery bar |
| `product-operations-assessment` | Operating-Model Assessment; Operating-Model Roadmap; seven category advisors | 10 | Help Product Operations diagnose organizational conditions and establish an owned improvement roadmap |
| `product-manager-initiative` | Opportunity Framing; Outcome Value Map; Bet Charter; Initiative Readiness Review | 18 | Help a Product Manager decide whether one initiative should proceed, change, pause, or stop |
| `team-lead-workflow` | Workflow Opportunity Advisor; Productive Motion Map; Human-AI Work Contract; Decision-Cycle Redesign; Workflow Playbook | 6 | Help a Team Lead redesign and test one recurring team workflow |

The total includes skills selected directly by the manifest plus any required `depends_on` skills. Dependencies are included because the decision needs them, not to make every pack look comprehensive.

These are persona-and-job combinations. They are not comprehensive role bundles. A broad role bundle would include much of the library and would not provide a useful starting decision.

## Source Contract

- `skills/` remains the only canonical source for skill content.
- `starter-packs/manifests/` defines which canonical materials each Starter Pack needs.
- `catalog/skills-by-starter-pack.md` and `catalog/starter-packs-index.yaml` are generated inverse views; they are never edited directly.
- `starter-packs/schema/starter-pack.schema.yaml` defines the manifest contract.
- Required `depends_on` skills will be included recursively.
- `combine_with` relationships remain advisory and are not automatically included.
- Generated working projects and ZIPs will be written under ignored `dist/` or to a user-selected directory.
- Generated copies are disposable build outputs and must never be edited as canonical content.

## Generate a Working Project

Run without arguments for the guided wizard:

```bash
./create-starter-pack.sh
```

On Windows PowerShell:

```powershell
.\create-starter-pack.ps1
```

Or provide arguments:

```bash
python3 scripts/create-starter-pack.py \
  --pack product-manager-initiative \
  --platform both \
  --output dist/starter-packs/product-manager-initiative \
  --non-interactive
```

Discover available packs and options with:

```bash
./create-starter-pack.sh --list
./create-starter-pack.sh --help
```

The destination must not already exist. Generated projects include exact source and dependency information in `PACK-LOCK.yaml`.

## Validate Starter Packs

Install the development requirements, then run:

```bash
python3 scripts/validate-starter-packs.py
```

The complete repository suite also runs this validation:

```bash
./scripts/test-library.sh
```

Build and verify all five downloadable archives:

```bash
python3 scripts/build-starter-pack-release.py
```

Run the synthetic clean-room cold-start gate against the extracted archives:

```bash
python3 scripts/test-starter-pack-cold-start.py
```

The complete release command also builds these archives and includes them in `dist/SHA256SUMS`:

```bash
./scripts/build-release.sh
```

## Current Evidence Boundary

Product Phase 7 is in progress. The automated synthetic clean-room gate passes all five packs; representative-persona cold starts remain pending. See the [cold-start report](../docs/validation/starter-pack-cold-start-report.md).

See [Starter Packs Product Contract](../docs/STARTER-PACKS.md) for the complete design and phase boundary.
