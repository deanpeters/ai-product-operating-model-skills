# Starter Pack Synthetic Cold-Start Report

This report records the automated clean-room cold-start gate for the five AIPOM Starter Packs on 2026-07-18.

## Result

**Pass for all five Starter Packs.** Each deterministic release ZIP was extracted into an empty temporary directory and evaluated without relying on the source repository's working tree.

This is synthetic packaging and instruction evidence. It is not representative human field validation and does not establish decision quality, adoption, impact, or compliance.

## Acceptance Contract

Each extracted pack had to demonstrate:

1. A single safe archive root and successful integrity check.
2. A readable persona, trigger, consequential decision, completion result, and authority boundary.
3. Plain-language instructions for adding existing context and evidence.
4. Visible `context/`, `evidence/`, and `outputs/` workspaces plus context and decision ledgers.
5. `$aipom-start` discovery for Codex and `/aipom-start` discovery for Claude Code.
6. A shared start skill that reads supplied material before asking questions and supports guided, context-dump, and best-guess modes.
7. The packaged persona guide, journey, command, primary methods, and recursive dependencies.
8. A lockfile whose pack identity, platform, skill closure, and generated-file hashes match the extracted project.
9. Required outputs and human authority limits visible in both the public README and agent working contract.
10. Internal Markdown links that remain valid after clean extraction.

## Persona Results

| Persona and pack | Primary | Dependencies | Total | Expected first consequential motion | Result |
|---|---:|---:|---:|---|---|
| Head of Product — `head-of-product-direction` | 2 | 0 | 2 | Bound the product-direction decision, decision owner, horizon, and consequence before drafting a strategy thesis | Pass |
| CTO — `cto-technical-readiness` | 5 | 9 | 14 | Define the consequence classes that require different technical evidence and recovery expectations | Pass |
| Product Operations — `product-operations-assessment` | 9 | 1 | 10 | Bound the organizational assessment and establish what evidence and perspectives already exist | Pass |
| Product Manager — `product-manager-initiative` | 4 | 14 | 18 | Frame the opportunity and current condition before evaluating the proposed AI initiative | Pass |
| Team Lead — `team-lead-workflow` | 5 | 1 | 6 | Choose one recurring decision or productive motion and establish its observed baseline before redesigning it | Pass |

## What the Automation Actually Did

The release workflow generated all five packs for both supported native layouts, built deterministic ZIPs, extracted each ZIP into a new temporary directory, seeded clearly labeled synthetic context and missing-evidence notes, inspected the start contract, verified locked file hashes and dependency closure, and checked the required user-facing and agent-facing instructions.

The generated machine-readable result is written to `dist/STARTER-PACK-COLD-START.yaml`. It is disposable release output; this report is the canonical evidence summary.

## Evidence Boundary

The automated gate did not:

- Ask a representative Head of Product, CTO, Product Operations practitioner, Product Manager, or Team Lead to use the pack.
- Evaluate an actual Codex or Claude response.
- Measure whether a person understood the package without assistance.
- Test whether the methods improved a real decision or organizational practice.
- Execute the PowerShell wrapper on Windows.

The result supports publishing the packs as part of a synthetic-data public preview. It does not support calling them field-proven or generally usable without further evidence.

## Next Evidence Motion

Run one observed cold start with each target persona. Give participants only the repository README or a downloaded pack, then observe whether they can select the right package, begin without assistance, supply appropriate material, explain the first decision, identify retained specialist authority, and describe what completion should produce.
