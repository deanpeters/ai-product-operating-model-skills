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
- Role-led execution flows for Product Operations, Product Managers, and Team Leads
- A README that leads with the operating problem and bounded starting decisions

This work is intended to make the preview easier to understand, try, and critique. It does not change the `v0.5` evidence label or claim field validation.

### Immediate next work

1. Cold-test the README and persona flows with Product Operations, Product Managers, and Team Leads.
2. Run the three prepared human-validation pilots and independent-facilitator calibration.
3. Correct tactical gaps, terminology friction, unsafe recommendations, and material differences in facilitation.
4. Decide whether the next tagged snapshot is `v0.6` or whether the repository will explicitly add patch-version support. Do not overwrite `v0.5`.

See the [current-state handoff](HANDOFF.md) for restart instructions, source-of-truth boundaries, commands, and known limitations.

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
