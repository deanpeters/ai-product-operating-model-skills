# Active Post-Release Roadmap

`v0.5` puts the complete planned 41-skill catalog into public use. “Public preview” describes the maturity of the evidence base, not an incomplete catalog.

The operating principle is **release, observe, correct, and deepen**. Do not wait passively for perfect field evidence, and do not manufacture new skills merely to make the library look active.

## v0.5.x: Rapid Public Corrections

Ship patch releases when public use exposes a clear defect.

Priority order:

1. **P0 — authority or safety failure:** contain immediately and issue a patch as soon as the repair validates.
2. **P1 — decision failure:** repair in the next patch; do not defer behind editorial work.
3. **P2 — facilitation failure:** batch related fixes when they materially improve use.
4. **P3 — editorial improvement:** collect for coherent cleanup rather than constant churn.

Every patch should preserve the evidence label, update the changelog, rerun the complete suite, and publish reproducible archives and checksums.

### Current v0.5.x public-experience work

The first post-launch improvement reorganizes the public experience without changing the canonical 41-skill catalog:

- A decision-led executive field guide and first 90-day route
- Separate public doors for leaders, practitioners, and contributors
- Practitioner preparation guides above the canonical command layer
- Six executive adoption packages assembled from existing skills
- Role-led flows for Heads of Product, CTOs, Product Operations, Product Managers, and Team Leads
- A README that leads with the operating problem and bounded starting decisions

This work is intended to make the preview easier to understand, try, and critique. It does not change the `v0.5` evidence label or claim field validation.

### Immediate next work

1. Cold-test the README and persona flows with all five leadership and execution personas.
2. Run the three prepared human-validation pilots and independent-facilitator calibration.
3. Correct tactical gaps, terminology friction, unsafe recommendations, and material differences in facilitation.
4. Decide whether the next tagged snapshot is `v0.6` or whether the repository will explicitly add patch-version support. Do not overwrite `v0.5`.

See the [current-state handoff](HANDOFF.md) for restart instructions, source-of-truth boundaries, commands, and known limitations.

## Active Product Direction: Starter Packs

Starter Packs are branded, persona-and-job-led mini-playbooks that let a user generate a self-contained working project, add context and evidence, launch Codex or Claude Code, and begin a guided AIPOM workflow using the user's existing coding-agent environment.

Starter Pack product phases 0 through 6 are complete. They are separate from the library build phases recorded in `ROADMAP.md`:

- The [Starter Packs product contract](STARTER-PACKS.md) defines the product promise, canonical boundaries, safety rules, and planned cross-platform experience.
- Five manifests define Head of Product direction, CTO technical readiness, Product Operations assessment, Product Manager initiative evaluation, and Team Lead workflow redesign packs.
- A machine-readable schema and repository-integrated validator enforce manifest structure, canonical file references, recursive `depends_on` resolution, supported platforms, and licensing requirements.
- The core Python generator supports a wizard, full command-line use, safe non-overwrite behavior, atomic builds, recursive dependencies, pinned source records, and generated-link checks.
- Shared templates create platform-neutral working projects with `README.md`, `AGENTS.md`, `CLAUDE.md`, context and decision ledgers, separate workspaces, canonical library content, and `PACK-LOCK.yaml`.
- Native Codex and Claude Code project skills expose `$aipom-start` and `/aipom-start` from the same maintained adapter source.
- Bash and PowerShell wrappers forward the complete wizard and command-line interface to the Python generator.
- Release automation builds deterministic archives for all five packs, generates checksums, verifies clean extraction and internal links, and confirms both native agent layouts.

Generated ZIPs and release integration are implemented. Field testing has not been completed. Do not maintain copied pack folders manually.

### Completed Phase 6 — Release packaging

1. Generate all five packs and downloadable ZIPs through release automation. **Complete.**
2. Publish checksums and verify deterministic bytes, clean extraction, links, and native skill discovery. **Complete.**

### Phase 7 — Cold-start use: synthetic gate complete; human use pending

The automated synthetic clean-room gate passes all five packs. It verifies extracted-package recognition, start instructions, workspaces, required outputs, authority boundaries, dependency closure, lockfile integrity, links, and native agent discovery. It does not evaluate a model response or representative-user comprehension.

1. Run observed cold-start usability tests with a Head of Product, CTO, Product Operations practitioner, Product Manager, and Team Lead.
2. Correct packaging and facilitation friction found in those sessions.
3. Expand the pack catalog only after the first five expose distinct unmet jobs.

See the [Starter Pack synthetic cold-start report](validation/starter-pack-cold-start-report.md).

## Deferred Product Direction: Scenario-Guided AIPOM Workbench

**Status: future option under consideration after Starter Packs; do not build until explicitly prioritized.**

A future Streamlit interface could make the library easier to use by beginning with recognizable situations rather than asking people to navigate 41 skills. The interface should remain a scenario-guided front door to canonical AIPOM methods, not become a second source of skill content or a generic chatbot wearing AIPOM language.

Possible starting scenarios include:

- Our AI efforts are scattered and nobody sees the whole picture.
- We have an AI idea and need to decide whether it deserves exploration.
- We have a pilot and need to decide whether to launch or scale it.
- AI is changing a recurring product-team workflow.
- We need to decide what an AI system may do independently.
- A production AI system is underperforming or has caused an incident.

The intended interaction would let a user choose a scenario and role, provide existing context, work through adaptive questions, inspect a visible evidence and assumption ledger, review unresolved authority or specialist decisions, and export a durable Markdown or JSON handoff. Guided, context-dump, and best-guess entry modes should follow the existing [Adaptive Facilitation Standard](ADAPTIVE-FACILITATION.md).

### Possible AI access lanes

The workbench should support several honest access paths rather than assume one vendor or require every user to buy separate API usage:

1. **Integrated API or bring-your-own-key:** OpenAI, Anthropic, and Gemini adapters use deployment secrets, environment variables, or session-only user credentials. Provider and model choices live in non-secret configuration; credentials never do.
2. **Local model:** Ollama provides a local-first option when Streamlit and Ollama run on the same machine or trusted network.
3. **Existing AI subscription:** Provider-native AIPOM packages let people use their ChatGPT, Claude, or Gemini subscription inside that provider's own interface. Likely forms include a Custom GPT, installable Claude Skills, and a Gemini Gem. Consumer subscriptions must not be presented as API credentials for an external Streamlit application.
4. **Subscription bridge:** Streamlit may assemble a scenario-specific context packet or prompt for use in a provider-native experience and accept the resulting handoff back. This is less seamless than an API connection but avoids pretending the subscription can operate as an external model backend.

The AI may interpret supplied context, identify gaps, ask adaptive questions, synthesize evidence and disagreement, explain tradeoffs, and draft artifacts or recommendations. Application logic must still enforce evidence ceilings, critical-gap treatment, required output fields, explicit human authority, and the distinction between an AI recommendation and an accountable decision.

### Revisit before implementation

Before authorizing a build, compare this direction with other product-interface ideas and decide:

- Which user and decision deserve the first complete vertical slice
- Whether Streamlit is the right public experience or only a prototype surface
- Whether the primary route is an integrated workbench, provider-native subscription packages, or both
- Which providers and credential modes are supportable without creating unsafe secret handling or uncontrolled cost
- What information may remain session-only, what users may export, and what the application must never retain
- Which canonical content and decision rules require a machine-readable scenario schema
- What synthetic and human tests must pass before public deployment

If selected, build one complete initiative launch-or-scale scenario across the chosen access lanes before expanding to additional scenarios. Do not create 41 separate web forms or duplicate canonical skill prose inside application code.

## v0.6: Field Evidence and Facilitation

Use public feedback and the three prepared human pilots to:

- Replace synthetic-only assumptions with anonymized field findings where permitted
- Compare independent facilitator decisions
- Tighten terminology, questions, handoffs, timing, and interrupted-workflow behavior
- Record where a skill clarified, constrained, changed, or failed to support a decision
- Improve examples without importing confidential material
- Publish an updated evidence-status matrix

The goal is not to delay usefulness until every skill has a case study. It is to make the evidence behind claims progressively stronger and more visible.

## v0.7: Interoperability and Distribution

- Test canonical skills across additional agent platforms
- Add platform adapters without contaminating canonical `SKILL.md` files
- Improve installation, discovery, version, and compatibility guidance
- Define import, export, and cross-library relationship conventions
- Test whether a human facilitator and multiple agent platforms preserve the same consequential boundaries

## v0.8: Adoption and Reuse Evidence

- Capture privacy-respecting evidence of which paths and skills are reused
- Study whether teams change decisions, workflow behavior, or evidence quality
- Improve stewardship, deprecation, migration, and example contribution practices
- Distinguish downloads and completions from demonstrated adoption or impact

## v0.9: Stabilization

- Resolve naming and metadata inconsistencies before stable contracts
- Publish compatibility and deprecation rules
- Harden contribution review, source-refresh, and release automation
- Identify which interfaces must remain stable for `v1.0`
- Remove or redesign methods that repeatedly fail to support useful decisions

## v1.0: Stable Public Contract

Consider `v1.0` when:

- Core metadata, categories, scoring, and facilitation contracts are stable
- Representative human and cross-platform use has informed priority skills
- P0 and P1 feedback can be handled through a reliable maintenance process
- Versioning, migration, attribution, confidentiality, and release practices are durable
- The library has evidence of changed decisions or practices without overstating universal effectiveness

`v1.0` is not a claim that learning is finished. It is a promise that the public contracts are stable enough for others to build on responsibly.
