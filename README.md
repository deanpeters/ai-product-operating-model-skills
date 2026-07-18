# AI Product Operating Model Skills

AI is easy to start. It is much harder to run well.

Most organizations do not need another pile of prompts, demos, pilots, or “AI strategy” slides. They need practical ways to decide what is worth doing, help teams do the work, tell whether it is working, keep people accountable, and stop the things that are not earning their keep.

That is what this repository is for.

AI Product Operating Model Skills (AIPOM) is a collection of guided methods for people trying to make AI product work useful, responsible, and repeatable. You can use it with a human facilitator or an AI assistant. You do not need to be a programmer, an AI evangelist, or a framework collector.

[Download the v0.6 public preview](https://github.com/deanpeters/ai-product-operating-model-skills/releases/tag/v0.6), [find your role](docs/TARGET-PERSONAS.md), or [start with the problem in front of you](docs/STARTING-PATHS.md).

> **Honest v0.6 label:** This is a `v0.6 public preview`. The library is structurally validated and synthetically forward-tested, including clean-room cold-start checks for all five Starter Packs, but it has not yet proved its effectiveness through representative organizational use. The examples are synthetic. Kick the tires, question the recommendations, and keep consequential decisions with accountable people and qualified specialists. See [Evidence Status](docs/EVIDENCE-STATUS.md).

## Find Yourself Here

You may come to this library with a title, a problem, or simply the sinking feeling that your organization has a lot of AI activity and no shared way to run it.

| If this sounds like you… | What is in it for you | Start here |
|---|---|---|
| **You set direction or fund the work.** | Make clearer choices about where AI belongs, what deserves investment, what must be true before scaling, and what should stop. | [Executive Field Guide](docs/EXECUTIVE-FIELD-GUIDE.md) |
| **You are the Head of Product, CPO, or SVP of Product.** | Turn AI ambition into product choices, non-goals, portfolio implications, and commitments that teams can actually use. | [Head of Product flow](docs/personas/HEAD-OF-PRODUCT.md) |
| **You are the CTO or equivalent senior technology leader.** | Set consequence-aware expectations for dependencies, context, data, evaluation, reliability, recovery, and technical readiness. | [CTO flow](docs/personas/CTO.md) |
| **You work in Product Operations.** | Turn scattered initiatives and one-off team habits into owned, repeatable practices without creating process theater. | [Product Operations flow](docs/personas/PRODUCT-OPERATIONS.md) |
| **You are a Product Manager.** | Take an AI opportunity from problem evidence through value, behavior, evaluation, authority, launch decisions, and production learning. | [Product Manager flow](docs/personas/PRODUCT-MANAGER.md) |
| **You lead a product, engineering, design, research, data, or operations team.** | Translate broad direction into work the team can perform, review, stop, recover, and improve. | [Team Lead flow](docs/personas/TEAM-LEAD.md) |
| **You design, research, build, evaluate, or operate AI products.** | See where your work fits, what evidence others need from you, and how decisions travel across the product lifecycle. | [Skills by target persona](catalog/skills-by-persona.md) |
| **You work in legal, privacy, security, safety, risk, finance, or AI governance.** | Bring specialist judgment into the work early, with clear authority, evidence, escalation, and decision boundaries. | [Governance and Accountability package](docs/adoption-packages/GOVERNANCE-AND-ACCOUNTABILITY.md) |
| **You facilitate, consult, coach, or teach.** | Run practical engagements that preserve context and produce a decision, owner, and next move instead of a decorative workshop output. | [Starting Paths](docs/STARTING-PATHS.md) |
| **You want to build or improve the library.** | Use a clear contribution contract, examples, validation, and release process. | [Contribution Guide](CONTRIBUTING.md) |

The [Target Personas](docs/TARGET-PERSONAS.md) guide explains how these roles work together without pretending that one role owns every decision.

## There Is Room for Your Working Style Too

- **Strategists** can connect AI choices to customer and business outcomes.
- **Operators** can turn decisions into routines that survive contact with real work.
- **Builders** can see the context, behavior, evaluation, control, and recovery expectations around what they build.
- **Skeptics** can demand evidence, expose wishful thinking, and help stop expensive theater.
- **Facilitators** can guide a group without stealing its decisions.
- **Teachers and coaches** can use the methods to explain not only what to do, but why it works and where it fails.
- **People cleaning up after somebody else’s pilot** can establish ownership, evidence, boundaries, and a responsible next move.

You do not have to buy into a grand transformation. Start with one decision that matters.

## What Can You Use It to Do?

- Decide whether an AI idea deserves discovery, funding, launch, scale, constraint, or retirement
- Connect AI behavior to customer value, business value, cost, and risk
- Define what an AI product should and should not do
- Decide what AI may do alone, what needs approval, and what it must never do
- Prepare trusted context and data for recurring work
- Build evaluations that support real product decisions instead of producing a wall of metrics
- Redesign a team workflow without automating the wrong thing
- Assign ownership, review, escalation, fallback, and incident responsibilities
- Review production evidence and change, constrain, roll back, or retire the system
- Turn a practice that works into something another team can safely reuse
- Review the portfolio and move money and people away from zombie pilots

The point is not to complete a canvas. The point is to make a better decision and improve how the work happens next time.

## Start with What Is Hurting

You do not need to study all 41 skills before doing useful work.

### “We have AI ambition, but no usable product direction.”

Use [Set AI Product Direction](docs/journeys/SET-AI-PRODUCT-DIRECTION.md) when leadership needs to choose where AI belongs, what the organization will avoid, how current investments fit, and what moves first.

You will leave with explicit product choices and non-goals, portfolio implications, owned first commitments, evidence gaps, and a dated reason to revisit the direction.

### “Every team has a different definition of technically ready.”

Use [Establish the AI Technical Readiness Bar](docs/journeys/ESTABLISH-AI-TECHNICAL-READINESS-BAR.md) when launch, scale, dependency, data, evaluation, recovery, or autonomy decisions lack shared technical evidence expectations.

You will leave with consequence-aware readiness classes, required evidence, non-negotiable gaps, owners and reviewers, exception rules, and review triggers.

### “Our AI work is all over the place.”

Use [Assess an Organization](docs/journeys/ASSESS-AN-ORGANIZATION.md) when initiatives, policies, team practices, and ownership do not line up across the organization.

You will leave with a clear view of the most important gaps, what needs attention first, who owns it, and what should happen over the next 30, 90, 180, and 365 days.

### “Should we fund, launch, scale, constrain, or stop this thing?”

Use [Evaluate an AI Initiative](docs/journeys/EVALUATE-AN-AI-INITIATIVE.md) when a specific idea, pilot, investment, launch, sensitive-data use, or increase in AI authority needs a decision.

You will leave with a clear recommendation, the evidence behind it, unresolved specialist decisions, any conditions or limits, named owners, and a reason to return for review.

### “AI is changing how my team works.”

Use [Redesign a Product-Team Workflow](docs/journeys/REDESIGN-A-PRODUCT-TEAM-WORKFLOW.md) when recurring work is slow, inconsistent, overloaded, or being changed through AI assistance.

You will leave with a picture of how the work really happens, clear human and AI responsibilities, a small test, measures that include hidden burden and failure, and a decision to adopt, revise, contain, or stop.

Not sure? Use the [starting-path comparison](docs/STARTING-PATHS.md). Each path also has a smaller 60–90 minute version when you need to scope the problem before committing to the full journey.

If you already use Codex or Claude Code, [Starter Packs](starter-packs/README.md) can generate a focused working project for one of these five jobs, including the relevant methods, context and evidence folders, working ledgers, and plain-language start instructions. Compare the deliberately different primary and dependency sets in [Skills by Starter Pack](catalog/skills-by-starter-pack.md).

Run `./create-starter-pack.sh` on macOS or Linux, or `.\create-starter-pack.ps1` in Windows PowerShell, to open the guided pack builder. Generated projects provide `$aipom-start` in Codex and `/aipom-start` in Claude Code.

All five generated pack shapes pass an automated [synthetic cold-start gate](docs/validation/starter-pack-cold-start-report.md). That verifies packaging and start readiness, not representative human usability or improved decisions.

## What Is in the Box?

- **41 guided skills.** Each explains when to use it, who should participate, what to bring, how to run it, what it produces, what commonly goes wrong, and what should happen next.
- **Templates and examples.** Every skill includes a reusable template, a synthetic worked example, and a synthetic weak example that shows failure modes.
- **Five end-to-end journeys.** Set product direction, establish the technical readiness bar, assess the organization, evaluate an initiative, or redesign a team workflow.
- **Six executive adoption packages.** Start with alignment, investment, readiness, workflow, governance, or a quarterly portfolio decision.
- **Role-led guides.** Heads of Product, CTOs, Product Operations, Product Managers, and Team Leads each have a plain-English route through the library.
- **Starter Packs.** Generate a bounded working project for product direction, technical readiness, an organization baseline, an initiative decision, or workflow redesign without navigating the full catalog first.
- **A 35-question organization assessment.** Use evidence and disagreement to find the most important conditions—not to manufacture one flattering score.
- **Human and AI facilitation guidance.** The methods work as readable facilitation guides and as instructions an AI assistant can follow.
- **Automated checks.** The repository checks skill structure, links, packages, and release integrity so contributors can change it without quietly breaking it.

Browse the [complete skill catalog](catalog/INDEX.md), including the generated [skills by target persona](catalog/skills-by-persona.md) view.

## How the Pieces Fit Together

AIPOM looks at seven connected parts of the work:

1. **Strategy and outcomes** — Where could AI create value, and what should improve?
2. **Portfolio and investment** — Which ideas should receive time and money, and which should stop?
3. **Product-team workflows** — How should people and AI work together in recurring decisions?
4. **Context, knowledge, and data** — What information can the system and team trust and use?
5. **Evaluation and evidence** — What does acceptable behavior look like, and how will we know?
6. **Governance and accountability** — Who decides, what is allowed, and what happens when things go wrong?
7. **Capability, adoption, and reuse** — How do people learn, improve, and reuse practices that actually work?

These are connected parts of one working system, not seven departments or seven transformation programs.

The methods can also focus on four different levels:

| Level | Plain-English question |
|---|---|
| Organization | Does the company have a workable way to run AI product work? |
| Portfolio | Are we putting money and people behind the right things? |
| Product team | Can the team perform the work clearly, safely, and repeatedly? |
| Initiative | Is this particular AI bet worth doing and ready for its next step? |

## Evidence Matters

AIPOM keeps four claims separate:

1. We talk about the practice.
2. We wrote the practice down.
3. People actually use the practice consistently.
4. The practice improves decisions or outcomes.

Those are not the same thing.

A policy, workshop, license, training course, generated document, or maturity score does not prove that the organization can do the work. When evidence is absent, AIPOM does not award a maturity score above `2 — Emerging`.

Read the [Evidence Standard](docs/EVIDENCE-STANDARD.md), [scoring model](assessments/scoring-model.md), and [Public Preview Contract](docs/PUBLIC-PREVIEW.md) for the detailed rules and current limitations.

## Explore Further

### Understand and use AIPOM

- [Introduction](INTRODUCTION.md) — the story behind AIPOM and an invitation to kick the tires
- [Documentation Guide](docs/README.md) — find current guidance, canonical standards, release records, and validation materials
- [Current-State Handoff](docs/HANDOFF.md) — restart information for a coworker or coding agent
- [Executive Field Guide](docs/EXECUTIVE-FIELD-GUIDE.md) — the leadership case and a practical first 90 days
- [Executive Adoption Packages](docs/adoption-packages/README.md) — six recognizable executive decisions
- [Target Personas](docs/TARGET-PERSONAS.md) — who the library serves and how the roles work together
- [Starting Paths](docs/STARTING-PATHS.md) — choose a route based on the problem in front of you
- [Operating Model](docs/OPERATING-MODEL.md) — the fuller explanation of the system
- [Skill Catalog](catalog/INDEX.md) — browse all 41 skills

### Inspect the evidence and release

- [Evidence Status](docs/EVIDENCE-STATUS.md) — what has and has not been demonstrated
- [Public Preview Contract](docs/PUBLIC-PREVIEW.md) — responsible-use and feedback boundaries
- [Validation Hub](docs/validation/README.md) — synthetic tests and prepared field-validation materials
- [Post-Release Roadmap](docs/POST-RELEASE-ROADMAP.md) — the route toward stronger evidence and a stable `v1.0`

### Contribute or integrate

- [Contribution Guide](CONTRIBUTING.md) — the contributor entry point
- [Repository Working Agreement](AGENTS.md) — principles, boundaries, and workflow
- [Skill Specification](docs/SKILL-SPEC.md) — the detailed skill requirements
- [Adaptive Facilitation](docs/ADAPTIVE-FACILITATION.md) — how guided methods respond to supplied context

## For Maintainers

Install the one development dependency:

```bash
python3 -m pip install -r requirements-dev.txt
```

Run the complete verification suite:

```bash
./scripts/test-library.sh
```

Regenerate catalogs after changing skill information:

```bash
python3 scripts/generate-catalog.py
```

Build release files after validation succeeds:

```bash
./scripts/build-release.sh
```

Generated catalog and distribution files must not be edited directly.

## What This Is Not

AIPOM is not a prompt library, vendor comparison, AI tool tutorial, machine-learning engineering handbook, legal opinion, or collection of maturity charts with nothing useful behind them.

The library uses credible existing methods where they already solve the underlying problem. Examples must be public, appropriately licensed, anonymized, or clearly labeled as synthetic. Productside client-confidential material does not belong here.

## License

This work is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/). See [LICENSE](LICENSE) for the legal code.
