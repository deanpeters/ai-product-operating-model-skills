# AI Is Easy to Start. Running It Is the Hard Part.

*Introducing AI Product Operating Model Skills: a practical, open library for turning scattered AI activity into accountable product practice.*

Most organizations do not have an AI idea problem.

They have demos. Pilots. Executive mandates. Teams experimenting with new tools. Vendors promising transformation. A growing collection of policies, prompt libraries, prototypes, and slide decks with arrows pointing toward the future.

What they often do not have is a shared way to decide which opportunities deserve investment, what evidence is good enough to proceed, how people and AI should divide the work, who owns the consequences, or when an initiative should be constrained or stopped.

That is an operating-model problem.

It is also why I created [AI Product Operating Model Skills](https://github.com/deanpeters/ai-product-operating-model-skills), or AIPOM: an open library of practical methods for people trying to make AI product work useful, responsible, and repeatable.

## The Gap Between an AI Demo and an AI Capability

An AI feature can be prototyped in an afternoon. An organization capable of operating that feature well takes more work.

Somebody still has to connect the idea to a real customer and business outcome. Somebody has to understand the economics. Teams need trustworthy context and data. Expected behavior must be defined and evaluated. Human authority, review, escalation, fallback, and recovery need to be explicit. Production evidence has to change decisions. Useful practices need to survive beyond the person who invented them.

Buying licenses does not do this. Launching pilots does not do this. Completing a canvas does not do this. Even publishing a responsible-AI policy does not prove that people use it when a difficult product decision arrives.

AIPOM is designed around that distinction. It separates four very different claims:

1. We discuss a practice.
2. We documented a practice.
3. People use the practice consistently.
4. The practice demonstrably improves decisions or outcomes.

The library does not award maturity for aspiration. It asks for evidence, names assumptions when evidence is missing, and keeps consequential decisions with accountable people.

## What Is in the Library

AIPOM v0.6 contains 41 guided skills across seven connected parts of an AI product operating model:

1. Strategy and economic outcomes
2. Portfolio and investment choices
3. Product-team workflows
4. Context, knowledge, and data
5. Evaluation and evidence
6. Governance and accountability
7. Capability, adoption, and reuse

These are not seven departments and they are not seven transformation programs. They are parts of one working system.

The skills help people do concrete work: frame an AI opportunity, build an economic case, establish investment gates, define acceptable behavior, prepare authoritative context, set autonomy boundaries, design evaluation scorecards, assign accountability, review production evidence, respond to incidents, and decide what to scale, change, constrain, or retire.

Every skill is intended to work in two ways. A human facilitator can read it and run the method. An AI assistant can use the same instructions to guide the work adaptively. Either way, the person using it should leave with more than a completed template. They should understand the evidence, reasoning, tradeoffs, failure modes, decision authority, and next organizational move.

## Start with Your Job, Not the Catalog

A 41-skill library may be comprehensive, but “please browse our comprehensive catalog” is not a humane onboarding experience.

So v0.6 introduces five role-led journeys and five downloadable **Starter Packs**:

- **Head of Product, CPO, or SVP of Product:** set AI product direction and turn broad ambition into choices, non-goals, portfolio implications, and owned commitments.
- **CTO or equivalent technology leader:** establish a consequence-aware technical readiness bar across dependencies, data, evaluation, reliability, recovery, and autonomy.
- **Product Operations:** create an evidence-based operating-model baseline and convert scattered practices into an owned improvement roadmap.
- **Product Manager:** evaluate an AI initiative from problem evidence through value, behavior, authority, readiness, and production learning.
- **Team Lead:** redesign a recurring product-team workflow with explicit human and AI responsibilities, review points, measures, and stop conditions.

Each Starter Pack is a focused working project rather than a photocopy of the entire library. It contains the primary methods for that job, only the dependencies those methods require, plain-language instructions, spaces for context and evidence, decision and assumption ledgers, and native starting points for Codex and Claude Code.

The packs are generated from canonical manifests, so we can improve a skill once and rebuild every affected package without maintaining five drifting copies. People on macOS or Linux can use the Bash wrapper; Windows users get a PowerShell wrapper; and anyone who prefers explicit arguments can use the Python command directly.

## What AIPOM Refuses to Pretend

There is plenty of pressure in AI work to make activity look like progress.

AIPOM deliberately resists that pressure. A radar chart is not an intervention. A workshop output is not organizational maturity. A high average score cannot compensate for a missing safety or accountability control. An AI recommendation does not absorb human responsibility. More tokens, licenses, logins, pilots, and generated documents do not automatically create customer value or organizational capability.

The project also does not begin with a vendor. It begins with a decision, workflow, outcome, body of evidence, or organizational condition. The canonical skills are platform-neutral. Packaging can adapt them for different AI environments without turning the methods themselves into advertisements for one provider.

And this is not a substitute for legal, privacy, security, safety, financial, regulatory, technical, or domain expertise. A useful operating model brings those people into the work with clear authority. It does not use an AI facilitator to route around them.

## An Honest v0.6 Label

This is a public preview, not a victory lap.

The complete library passes automated structural, metadata, source-traceability, and link validation. Release archives build reproducibly. Representative skills have been exercised with synthetic scenarios. All five Starter Packs pass automated clean-room cold-start checks, including dependency closure, lockfile integrity, internal links, workspaces, authority boundaries, and native agent discovery.

That proves the repository is coherent and the packages can stand up cleanly. It does **not** prove that representative organizations will use the methods consistently, that two human facilitators will reach equally sound decisions, or that AIPOM improves customer, business, safety, or risk outcomes.

Those are the next evidence questions. All current worked examples are clearly labeled synthetic, and the repository includes a field-validation kit so real-world findings can strengthen the methods without smuggling confidential material into a public project.

Pre-1.0 is the right place to be candid about this. The point of publishing now is to let people inspect it, try it, challenge it, and help expose what does not survive contact with real work.

## Kick the Tires

If your organization has a lot of AI activity but no shared way to run it, start with one consequential decision:

- Where should AI actually fit in our product strategy?
- Is this initiative worth funding, launching, or scaling?
- What must be true before the technology is ready?
- How should humans and AI share this recurring work?
- What evidence would cause us to continue, change, constrain, or stop?

Then choose the role or journey closest to that decision. Use the full library with a human facilitator or an AI assistant, or download one of the five Starter Packs and work inside a bounded project.

I am especially interested in feedback that finds an unsafe recommendation, missing authority, evidence gap, confusing term, impractical step, or moment where the method produces ceremony instead of a better decision. I also want to hear when a skill genuinely changes a decision, exposes a hidden disagreement, stops weak work, or helps a team establish a practice it can repeat.

The repository is available at [github.com/deanpeters/ai-product-operating-model-skills](https://github.com/deanpeters/ai-product-operating-model-skills). Version 0.6 and its Starter Packs are available from the [latest release](https://github.com/deanpeters/ai-product-operating-model-skills/releases/tag/v0.6).

AIPOM is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](LICENSE). Use it, adapt it, teach with it, question it, and share improvements under the same terms.

AI is easy to start. Let’s get better at running it.
