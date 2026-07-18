# Starter Packs Product Contract

Starter Packs are branded, job-led mini-playbooks that turn the canonical AIPOM library into a self-contained working project for a specific persona and consequential decision.

They are intended for people who want to use their existing Codex, Claude Code, or compatible coding-agent environment without first learning the 41-skill catalog or configuring a separate graphical application.

## Product Promise

A user should be able to choose a Starter Pack, generate a working folder, add the context and evidence they already have, launch their preferred coding agent, and begin a guided AIPOM workflow with explicit evidence, assumptions, decisions, authority, and next actions.

Starter Packs are an access and orchestration layer. They do not create new canonical methods, relax evidence standards, transfer human authority, or prove that the underlying practice works in the user's organization.

## Why Persona Plus Job

A persona alone is too broad. Product Managers appear in all 41 canonical skills, and Product Operations and Team Leads also participate across much of the library. A useful Starter Pack therefore combines a recognizable person with a bounded job:

| Starter Pack | Persona | Bounded job | Primary result |
|---|---|---|---|
| Head of Product — Set AI Product Direction | Head of Product, including CPO and SVP of Product | Turn AI ambition into product choices, non-goals, and portfolio implications | Product thesis and owned first commitments |
| CTO — Establish the AI Technical Readiness Bar | CTO and equivalent senior technology leaders | Define consequence-aware evidence and operating expectations | Technical readiness classes, evidence bar, and review rules |
| Product Operations — Establish an Operating-Model Baseline | Product Operations | Assess inconsistent organizational AI product practice and choose the next interventions | Evidence-based profile and owned roadmap |
| Product Manager — Evaluate an AI Initiative | Product Manager | Decide whether one AI opportunity or initiative should proceed at a defined scope | Proceed, constrain, remediate, pause, or stop recommendation |
| Team Lead — Redesign an AI-Assisted Workflow | Team Lead | Observe, redesign, and test one recurring product-team motion | Bounded workflow adoption decision |

Additional Starter Packs require a distinct user, decision, and completion result. Do not create broad role bundles or multiply packs merely to cover every audience label.

## How Package Contents Differ

The five packages do not contain the same skills. They share a consistent working-project shell so users can move between packs without relearning the mechanics, while each manifest selects the canonical methods required for its particular decision.

The generated [Skills by Starter Pack](../catalog/skills-by-starter-pack.md) page is the current inverse view of every primary and dependency relationship. Do not maintain a second package-membership list in skill frontmatter.

| Starter Pack | Primary skills | Total with dependencies | Why this selection fits |
|---|---|---:|---|
| Head of Product — Set AI Product Direction | Strategy Thesis Advisor; Portfolio Posture Advisor | 2 | Direction-setting requires explicit product choices and a portfolio response without dragging the leader through initiative-level execution methods |
| CTO — Establish the AI Technical Readiness Bar | Platform Dependency Audit; Context Readiness; Data Readiness; Evaluation Strategy; Risk, Control, and Incident Playbook | 14 | A defensible technical bar must connect dependencies, information fitness, evaluation, accountability, controls, and recovery |
| Product Operations — Establish an Operating-Model Baseline | Operating-Model Assessment; Operating-Model Roadmap; seven category advisors | 10 | Organization-level diagnosis needs coverage across all seven operating-model categories and a route from findings to owned change |
| Product Manager — Evaluate an AI Initiative | Opportunity Framing; Outcome Value Map; Bet Charter; Initiative Readiness Review | 18 | An initiative decision must integrate value, economics, technical readiness, evidence, governance, authority, and stop conditions |
| Team Lead — Redesign an AI-Assisted Workflow | Workflow Opportunity Advisor; Productive Motion Map; Human-AI Work Contract; Decision-Cycle Redesign; Workflow Playbook | 6 | Workflow change begins with observed work, makes human and AI responsibilities explicit, and earns reuse through a bounded pilot |

“Total with dependencies” includes the primary skills plus recursively required `depends_on` skills. It does not include optional `combine_with` recommendations. The manifest remains the machine-readable source of truth when package contents change.

## Canonical and Generated Boundaries

The repository maintains one canonical copy of each skill:

```text
skills/                          canonical methods, templates, and examples
starter-packs/manifests/         canonical Starter Pack recipes
starter-packs/schema/            canonical manifest contract
starter-packs/templates/         shared working-project templates
starter-packs/adapters/          shared native-agent adapter templates
scripts/create-starter-pack.py   canonical generator
create-starter-pack.sh           macOS and Linux wrapper
create-starter-pack.ps1          Windows PowerShell wrapper
dist/starter-packs/              optional generated output; never canonical
```

The repository will not contain five maintained copies of the same skill. The generator copies required canonical skills into a temporary build and then atomically moves the completed project to a user-selected working directory. Those copies are generated dependencies, not editable sources.

## Manifest Contract

Every manifest defines:

- Stable pack ID and independent pack version
- Persona and bounded scenario
- Trigger, operating level, and decision
- Persona guide, journey, and command entry points
- Explicitly selected canonical skills
- Required dependency behavior
- Supporting assessment and standards content
- Mutable workspace directories and ledgers
- Supported coding-agent platforms
- Completion result, required outputs, and authority boundary
- License and attribution requirement

Required `depends_on` relationships are resolved recursively. `combine_with` relationships are useful recommendations but do not become package dependencies unless the manifest selects them explicitly.

## Generated Experience

A generated project contains:

```text
working-project/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── LICENSE
├── PACK-LOCK.yaml
├── CONTEXT-LEDGER.md
├── DECISION-LOG.md
├── context/
├── evidence/
├── outputs/
├── .agents/skills/aipom-start/  when Codex is selected
├── .claude/skills/aipom-start/  when Claude Code is selected
└── library/
    ├── skills/
    ├── assessments/
    ├── commands/
    └── docs/
```

`AGENTS.md` is the primary cross-agent project contract. `CLAUDE.md` directs Claude Code to that contract. Codex discovers `$aipom-start` under `.agents/skills/`; Claude Code discovers `/aipom-start` under `.claude/skills/`. Both generated adapters come from one shared template and orchestrate the packaged journey and command without duplicating canonical skill content.

## Generator Entry Points

The Python generator is the implementation source of truth:

```bash
python3 scripts/create-starter-pack.py --help
```

Run without arguments for a plain-language wizard, or use arguments for automation:

```bash
python3 scripts/create-starter-pack.py --list
python3 scripts/create-starter-pack.py --describe product-manager-initiative
python3 scripts/create-starter-pack.py \
  --pack product-manager-initiative \
  --platform both \
  --output dist/starter-packs/product-manager-initiative \
  --non-interactive
```

The generator supports pack selection, platform intent, output directory, listing, description, dry-run, non-interactive mode, help, and version. It refuses any existing destination rather than risking an overwrite.

The thin platform wrappers expose the same wizard, arguments, and help:

```bash
./create-starter-pack.sh --help
```

```powershell
.\create-starter-pack.ps1 --help
```

Prebuilt ZIPs may be published for convenience, but they will be generated from the same manifests and canonical sources. ZIPs are immutable release artifacts, not maintained documents.

## Safety and Evidence Contract

The generator and generated projects:

- Refuse to overwrite a nonempty destination silently
- Never copy credentials or local secrets
- Never modify canonical skill sources
- Preserve the CC BY-NC-SA 4.0 license and attribution
- Keep user context, evidence, outputs, and ledgers separate from generated dependencies
- Preserve guided, context-dump, and best-guess behavior
- Keep evidence, assumptions, disagreement, and missing information visible
- Preserve critical-gap and evidence-ceiling rules
- Distinguish AI recommendations from accountable human decisions
- Route legal, privacy, security, safety, risk, finance, governance, technical, operational, and domain decisions to the appropriate authority

## Starter Pack Product Phase Status

These product phases describe the Starter Pack access and packaging system. They are not the [library build phases](../ROADMAP.md).

### Phase 0 — Product contract: complete

The Starter Packs name, purpose, initial audience-and-job combinations, canonical boundaries, dependency rules, safety contract, and planned cross-platform direction are defined.

### Phase 1 — Manifest system: complete

The schema, five manifests, and repository-integrated validation are implemented. The manifests validate against canonical skills, files, dependency graphs, supported platforms, and licensing requirements.

### Phase 2 — Core Python generator: complete

The generator supports an interactive wizard and argument-driven use, resolves required skill dependencies, performs dry runs, refuses existing destinations, builds atomically, preserves source checksums, the base Git revision, and worktree status in `PACK-LOCK.yaml`, and validates the generated project's internal links.

### Phase 3 — Shared working-project shell: complete

Shared templates produce a readable `README.md`, primary `AGENTS.md` contract, thin `CLAUDE.md` pointer, context and decision ledgers, separated context/evidence/output workspaces, canonical license, and generated `library/` dependencies. When generated from a clean checkout, references omitted from a bounded pack point to the exact upstream Git revision instead of becoming dead links; dirty working-tree generation is labeled in the lockfile.

### Phase 4 — Native agent adapters: complete

The selected platform controls native discovery output. Codex receives `.agents/skills/aipom-start/SKILL.md` plus `agents/openai.yaml`; Claude Code receives `.claude/skills/aipom-start/SKILL.md`. Selecting `both` produces both adapters. The adapter reads the shared project contract, inspects supplied context and evidence, selects the appropriate entry mode, and begins the packaged journey.

### Phase 5 — Cross-platform wrappers: complete

`create-starter-pack.sh` supports macOS and Linux, preferring `python3` and falling back to `python`. `create-starter-pack.ps1` supports Windows PowerShell and prefers the Python launcher before `python3` or `python`. Both forward all arguments unchanged to the canonical Python generator and provide a clear missing-Python error.

### Phase 6 — Release packaging: complete

Release automation generates all five working projects, creates deterministic ZIP files and SHA-256 checksums, includes the required Starter Pack sources in the canonical release, verifies reproducible archive bytes, extracts every archive cleanly, validates internal links, and confirms native Codex and Claude Code discovery files.

### Phase 7 — Cold-start use: synthetic gate complete; human use pending

The automated clean-room gate passes all five extracted persona packages and verifies recognition, start instructions, workspaces, outputs, authority boundaries, dependency closure, lockfile integrity, internal links, and native Codex and Claude Code discovery. Representative-user starts remain pending. See the [Starter Pack synthetic cold-start report](validation/starter-pack-cold-start-report.md).
