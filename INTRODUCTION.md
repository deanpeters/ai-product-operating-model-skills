# Finally, the AI Product Operating Model Made Easy(ier)

*AI is easy. Running it well is hard. Here's the missing layer between AI activity and accountable product capability.*

Your pilots, policies, prompt libraries, and maturity charts are not an operating model. You have pilots and agents everywhere and no shared way to decide what deserves to live, scale, or die.

## The AI Portfolio Review With No Kill Switch

Picture the quarterly AI portfolio review.

Fourteen initiatives appear on the screen, neatly arranged in a table with enough green status dots to suggest either institutional excellence or a widespread formatting disorder. Seven have working demos. Three have executive sponsors. Two have vendors eagerly volunteering to help define the problem their software already happens to solve.

One team has built a customer-service copilot. Another is summarizing regulatory documents. Someone in Finance has automated a spreadsheet ritual that has been performed every Thursday since the Taft administration. Marketing has produced an agent that can generate eighty-seven campaign concepts before lunch, thereby solving the long-standing enterprise problem of not having enough mediocre campaign concepts.

Every initiative is described as promising.

Then someone asks a simple question:

> What evidence would cause us to stop one?

The room goes quiet enough to hear the GPU invoices reproducing.

Perhaps the pilot achieved 84 percent accuracy. Is that good? Nobody knows. Perhaps employees saved six hours a week. Nobody measured the time they spent checking the output, rebuilding lost context, or repairing the thing when it wandered into the shrubbery.

Perhaps the system passed Legal review six months ago, before the model changed, the data source changed, the workflow changed, and somebody quietly gave it permission to take actions instead of merely suggesting them.

Nobody wants to kill the pilot. It has a name. It has a steering committee. It has become emotionally significant to a vice president.

So it remains green.

This is how AI theater becomes an operating expense.

The problem is not that the organization lacks models, prompts, prototypes, policies, vendors, or enthusiasm. The problem is that it has no shared machinery for making the decisions surrounding them:

* What deserves investment?
* What must be true before launch or scale?
* What evidence is good enough?
* What may the AI do independently?
* Which decisions require human approval?
* Who owns the consequences?
* What triggers a change, constraint, rollback, pause, or stop?

Those are not model questions.

They are operating-model questions.

**Activity is easy to manufacture. Capability has to survive a consequential decision.**

## Between the Demo and the Capability Is an Operating Model

An AI feature can be prototyped in an afternoon. An organization capable of operating that feature well takes considerably longer.

Somebody still has to connect the idea to a real customer problem and a business outcome worth pursuing. Somebody has to understand the economics beyond the initial vendor quote and the magical spreadsheet cell labeled “productivity gain.”

The product team needs trustworthy context and data. Expected behavior must be defined. Acceptable, unacceptable, and prohibited behavior must be distinguishable before the system begins freelancing inside a customer workflow.

Evaluations must support an actual decision, not simply produce a wall of metrics dense enough to stun an elk. Human authority, review, escalation, fallback, recovery, and incident response must be explicit. Production evidence must change what happens next.

Buying licenses does not do this.

Launching pilots does not do this.

Publishing a responsible-AI policy does not prove people use it when the difficult decision arrives sweating and late on a Friday afternoon.

This distinction led me to build [AI Product Operating Model Skills](https://github.com/deanpeters/ai-product-operating-model-skills), or AIPOM: an open library of practical methods for making AI product work useful, responsible, and repeatable.

AIPOM separates four claims that organizations routinely mash into one cheerful maturity score:

1. We talk about the practice.
2. We documented the practice.
3. People actually use the practice consistently.
4. The practice improves decisions or outcomes.

Those are not four ways of describing the same thing.

A policy proves that a policy exists. A completed workshop proves that people completed a workshop. A generated artifact proves that a model generated an artifact. None of those proves that the organization can repeatedly make a sound decision when customer value, money, uncertainty, authority, and consequences collide.

AIPOM v0.6 contains 41 guided skills across seven connected parts of the work:

1. Strategy and economic outcomes
2. Portfolio and investment choices
3. Product-team workflows
4. Context, knowledge, and data
5. Evaluation and evidence
6. Governance and accountability
7. Capability, adoption, and reuse

These are not seven departments. They are not seven transformation programs requiring seven executive sponsors, seven consultancies, and matching fleece vests.

They are parts of one working system.

The library includes methods for framing opportunities, building economic cases, defining behavior contracts, setting autonomy boundaries, designing evaluations, assigning accountability, reviewing production evidence, responding to incidents, and deciding what to scale, change, constrain, roll back, or retire.

Every skill can be read and facilitated by a human. The same instructions can also guide an AI assistant through the work.

But asking someone to browse 41 skills before making one decision is not humane onboarding.

That is why the most practical part of AIPOM is not the catalog.

It is the Starter Packs.

## Quick Win: Start With a Working Project, Not 41 Browser Tabs

A Starter Pack is a bounded working project built around one recognizable person and one consequential job.

You do not have to understand the entire operating model. You do not need to install a separate graphical platform, import a proprietary canvas, or complete a forty-minute personality assessment that reveals you are an Innovative Teal Strategist with operational mauve tendencies.

You choose the decision currently hurting.

Then you generate or download a focused project containing the relevant methods, dependencies, instructions, workspaces, ledgers, and native entry points for Codex or Claude Code.

There are currently five Starter Packs:

| Starter Pack           | The job                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| **Head of Product**    | Set AI product direction, non-goals, portfolio implications, and first commitments             |
| **CTO**                | Establish a consequence-aware technical readiness bar                                          |
| **Product Operations** | Assess the operating model and create an owned improvement roadmap                             |
| **Product Manager**    | Decide whether one AI initiative should proceed, be constrained, be remediated, pause, or stop |
| **Team Lead**          | Redesign and test one recurring human-AI workflow                                              |

The easiest path is to download a prebuilt Starter Pack from the [v0.6 public preview release](https://github.com/deanpeters/ai-product-operating-model-skills/releases/tag/v0.6).

Extract the package, add whatever context and evidence you already have, then open the folder in your coding agent.

In Codex, start with:

```text
$aipom-start
```

In Claude Code:

```text
/aipom-start
```

The agent reads the project contract, inspects the available material, identifies what is missing, and begins the packaged journey.

For those who would rather generate a pack from the repository:

```bash
git clone https://github.com/deanpeters/ai-product-operating-model-skills.git
cd ai-product-operating-model-skills

./create-starter-pack.sh --list
./create-starter-pack.sh --describe product-manager-initiative
./create-starter-pack.sh
```

Windows users get the equivalent PowerShell wrapper:

```powershell
.\create-starter-pack.ps1
```

You can also call the generator directly:

```bash
python3 scripts/create-starter-pack.py \
  --pack product-manager-initiative \
  --platform both \
  --output ~/aipom/product-manager-initiative \
  --non-interactive
```

The generator supports interactive and non-interactive use, platform selection, descriptions, dry runs, version information, and explicit output directories.

It also refuses to overwrite an existing destination.

Because “the agent probably knew that folder was important” is not a recovery plan.

Once the project exists, place what you already know inside `context/` and the support for what you claim inside `evidence/`.

Do not spend three weeks preparing the perfect evidence package. Missing, stale, conflicting, inaccessible, or suspiciously convenient evidence is part of what the workflow is designed to expose.

Then begin.

That is the first quick win:

> **Turn one fuzzy AI discussion into a bounded working decision.**

## The Starter Packs Are the Door, Not the Gift Shop

The Starter Packs are not merely downloadable swag attached to a more important framework.

They are the access and orchestration layer for the library.

A role alone is too broad. Product Managers appear throughout all 41 skills. Product Operations and Team Leads participate across much of the operating model. A comprehensive “Product Manager Pack” would therefore be the entire library stuffed into a smaller suitcase and labeled convenient.

Instead, each pack combines:

> **Recognizable role + bounded job + explicit completion result**

The Head of Product pack is not “everything a Head of Product could conceivably do with AI.” It helps leadership turn scattered AI ambition into product choices, non-goals, portfolio implications, and owned first commitments.

The CTO pack does not attempt to teach an executive every technical discipline involved in modern AI. It helps establish the evidence, dependencies, context, data, evaluation, control, recovery, and exception rules required for a consequential readiness decision.

The Product Manager pack does not generate a beautiful recommendation memo and declare victory. It helps determine whether one initiative should:

* proceed
* proceed with constraints
* be remediated and reviewed again
* pause
* stop

Stopping is a first-class product decision.

This alone separates the library from much of the AI industrial complex, which can imagine fourteen ways to begin something and treats retirement as an unfortunate character flaw.

The five packs do not contain the same number of skills.

The Head of Product pack currently has two primary skills. The Team Lead pack has six skills after dependencies. The CTO pack contains fourteen. The Product Manager initiative pack contains eighteen.

That unevenness is deliberate.

The packs are shaped by the decision, not padded to look equally impressive in a comparison chart.

A Product Manager evaluating an initiative may need opportunity framing, an outcome-value map, an investment hypothesis, economic reasoning, dependency analysis, evaluation strategy, autonomy boundaries, accountability, incident planning, and an integrated readiness review.

A Head of Product setting direction should not have to wander through all of that initiative-level machinery before making strategic choices.

**Good packaging removes irrelevant complexity without amputating necessary context.**

## Under the Hood: What a Starter Pack Generates

A generated Starter Pack looks roughly like this:

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
├── .agents/
│   └── skills/
│       └── aipom-start/
├── .claude/
│   └── skills/
│       └── aipom-start/
└── library/
    ├── skills/
    ├── assessments/
    ├── commands/
    └── docs/
```

This is not accidental folder decoration.

Each part has a job.

### `AGENTS.md`: The Shared Project Contract

`AGENTS.md` defines how an AI assistant should behave inside the working project.

It establishes the purpose of the pack, how to use supplied context and evidence, how to distinguish evidence from assumptions, where outputs belong, which decisions the AI may recommend, and which decisions remain with accountable humans or qualified specialists.

`CLAUDE.md` does not duplicate this contract. It directs Claude Code to the shared instructions.

That prevents two instruction files from slowly drifting apart until one believes the project is evaluating an initiative and the other believes it is writing a musical about enterprise governance.

### Native Agent Entry Points

Codex discovers the packaged starting skill beneath:

```text
.agents/skills/aipom-start/
```

Claude Code discovers its native entry point beneath:

```text
.claude/skills/aipom-start/
```

Both adapters come from a shared template. They orchestrate the packaged journey without duplicating the canonical skills themselves.

That distinction matters.

Platform-specific entry points are allowed to differ. The operating method should not quietly mutate based on whichever coding agent opened the folder.

### Separate Context, Evidence, and Outputs

The generated project keeps three working areas distinct:

* `context/` holds information needed to understand the decision.
* `evidence/` holds support for claims about value, behavior, readiness, outcomes, controls, or risk.
* `outputs/` holds the artifacts produced through the workflow.

This sounds simple.

It is also the difference between inspectable work and Context Hoarding Disorder, where seventeen documents, four meeting transcripts, an outdated policy, and somebody’s speculative Slack message are dumped into one bucket and promoted to equal citizenship.

### The Context Ledger

`CONTEXT-LEDGER.md` records what was supplied, what appears authoritative, what conflicts, what may be stale, what remains missing, and what should not be trusted for the current decision.

Context is not merely fuel for the model.

It has ownership, provenance, fitness, boundaries, and an expiration date.

### The Decision Log

`DECISION-LOG.md` records decisions, owners, conditions, unresolved questions, and the trigger for returning to the decision.

This matters because generated recommendations have a habit of leaving the room wearing someone else’s authority.

AIPOM keeps the distinction explicit:

> The AI may help structure the decision. It does not become the decision-maker because its prose arrived in complete sentences.

### The Lockfile

`PACK-LOCK.yaml` records which pack, skills, dependencies, source revision, and checksums produced the working project.

It makes the package inspectable and reproducible.

More importantly, it prevents “I think we used the version from sometime in May” from becoming an evidence-management strategy.

## One Source of Truth, Five Working Projects

The repository maintains one canonical copy of each skill.

Starter Packs are generated from machine-readable manifests rather than maintained as five separate forks.

The source structure looks like this:

```text
skills/                          canonical methods
starter-packs/manifests/         canonical pack recipes
starter-packs/schema/            manifest contract
starter-packs/templates/         shared project shell
starter-packs/adapters/          native agent adapters
scripts/create-starter-pack.py   generator
create-starter-pack.sh           macOS and Linux wrapper
create-starter-pack.ps1          Windows PowerShell wrapper
```

Each manifest defines the persona, bounded scenario, operating level, decision, selected skills, dependency behavior, supporting materials, required outputs, supported platforms, and authority boundary.

Required `depends_on` relationships are resolved recursively.

Optional `combine_with` relationships remain recommendations. They do not get dragged automatically into the pack merely because another skill might be nice to have.

This prevents two common forms of Frankensoft.

The first is duplication: five maintained copies of the same method, all slowly decaying at different speeds.

The second is accumulation: every potentially relevant skill shoved into every package until “bounded working project” becomes a spiritually optimistic description of a 600-file directory.

The rule is simple:

> Improve the canonical skill once. Rebuild every affected package.

Generated projects are disposable working copies. The canonical method remains in the library.

That is not glamorous architecture.

It is the kind that survives maintenance.

## Quick Win: Put One Zombie Pilot on Trial

The fastest way to understand the Product Manager Starter Pack is to use it against an initiative your organization is already emotionally attached to.

Choose something low-consequence enough to explore safely but real enough to contain disagreement.

Bring:

* a one-page description of the initiative
* the customer or workflow problem it claims to solve
* the expected business outcome
* whatever economic assumptions exist
* any model or product evaluations
* the proposed degree of AI authority
* known data, platform, or vendor dependencies
* the person currently expected to approve the next step

Then ask the pack to help answer:

> Should this initiative proceed, proceed with constraints, be remediated and reviewed again, pause, or stop?

The workflow will examine the initiative across value, economics, dependencies, workflow, context, data, evaluation, governance, controls, capability, operation, and recovery.

Most importantly, it does not average everything into one reassuring readiness score.

Strong value does not compensate for the absence of rollback.

A good demo does not cancel a critical privacy gap.

An executive sponsor does not magically become an evaluation strategy.

The workflow identifies critical gaps first and states which actions they constrain. It preserves disagreement. It distinguishes evidence from assumptions and required approvals. It routes specialist decisions to the people who actually hold that authority.

A useful first session may produce no grand verdict at all.

It may reveal:

* the outcome has never been defined
* the economic case ignores review and failure costs
* the evaluation set does not represent the intended population
* nobody owns production monitoring
* the AI is being granted authority nobody explicitly approved
* the proposed fallback is “a human will notice”
* the launch decision depends on Legal, Security, or Privacy, none of whom have seen the current design

That is not failure.

That is the work finally becoming visible.

**The quick win is not getting an answer faster. It is exposing what the organization has been pretending it already knows.**

## The 41 Skills Are a Dependency Network, Not a Buffet

Once the reader has entered through a Starter Pack, the larger library begins to make more sense.

The 41 skills are not a checklist of practices every organization must install. They are a dependency network supporting different decisions at different operating levels.

Some skills help teams decide whether an opportunity deserves attention:

* `aipom-opportunity-framing`
* `aipom-outcome-value-map`
* `aipom-use-case-triage`
* `aipom-economic-case-builder`

Some define what the system should do and how the organization will know:

* `aipom-behavior-contract-builder`
* `aipom-evaluation-strategy-advisor`
* `aipom-eval-scorecard-builder`
* `aipom-golden-dataset-builder`

Some address context and data:

* `aipom-context-package-builder`
* `authoritative-source-map`
* `aipom-context-lifecycle-designer`
* `aipom-data-readiness-audit`

Others clarify authority, accountability, and recovery:

* `aipom-autonomy-boundary-designer`
* `aipom-accountability-charter`
* `aipom-risk-control-incident-playbook`
* `aipom-production-evidence-review`

Still others turn local success into organizational capability:

* `aipom-workflow-playbook-builder`
* `workflow-to-skill-converter`
* `aipom-adoption-impact-scorecard`
* `aipom-learning-system-designer`

The point is not to complete them all.

The point is to understand which practices must support the decision in front of you.

An initiative-level decision should not be confused with organization-wide maturity. A workflow redesign should not become an excuse to rewrite the enterprise strategy. A Product Manager should not impersonate Legal because the AI produced a confident paragraph about regulatory readiness.

Frameworks are useful when they improve thinking.

They become bureaucracy when completing the framework replaces the decision it was meant to support.

## The Guardrails Are Part of the Product

The technical packaging includes several deliberately unexciting safeguards:

* The generator refuses to silently overwrite a nonempty destination.
* It does not copy credentials or local secrets.
* It does not modify canonical skill sources.
* It keeps user context, evidence, outputs, and generated dependencies separate.
* It preserves evidence, assumptions, disagreement, and missing information.
* It distinguishes AI recommendations from accountable human decisions.
* It routes legal, privacy, security, safety, financial, governance, technical, operational, and domain decisions toward the appropriate authority.

These are not ornamental governance statements stapled to the back of the product.

They are product behavior.

The release process is similarly fussy.

The repository validates manifests, canonical paths, recursive dependencies, links, metadata, licensing, and package structure. It generates deterministic ZIP archives and SHA-256 checksums. It verifies that the archives can be reproduced, extracted cleanly, and opened with the expected internal links intact.

All five Starter Packs undergo synthetic clean-room cold-start checks. Those tests verify that the agent can recognize the project, find its starting instructions, identify the workspaces, preserve authority boundaries, locate dependencies, and produce the expected kinds of outputs.

Because apparently:

> “Trust me, the ZIP looked fine on my laptop.”

is not a release strategy.

## What the Tests Prove, and What They Absolutely Do Not

This is an honest v0.6 public preview.

The library is structurally validated. The packages build. Their dependencies resolve. Their native agent entry points are discoverable. Their lockfiles, links, folders, and authority boundaries survive synthetic clean-room testing.

That proves the machine starts.

It does not prove the machine improves the organization.

AIPOM has not yet demonstrated that representative organizations will use these practices consistently. It has not established that two different facilitators will produce equally sound outcomes. It has not proved that the library improves customer value, financial performance, safety, trust, or risk.

The worked examples are synthetic.

Representative human use is the next evidence boundary.

That caveat is not launch-copy broccoli. It is the point.

A project about evidence, decision quality, and accountability should not declare itself effective because its own tests passed. That would be a hallucination wrapped in a release note stuffed inside a maturity claim.

Pre-1.0 is the right time to publish the work, expose the assumptions, and invite people to find what does not survive contact with reality.

**Synthetic validation proves the machine starts. Field evidence must prove it goes somewhere useful.**

## Quick Win: Break One Pack Productively

Generic feedback is pleasant and nearly useless.

I do not need forty-seven people to tell me the repository is interesting.

I need people to use one Starter Pack against one real decision and report where the method:

* gives unsafe advice
* invents authority
* ignores missing specialist approval
* demands evidence nobody could reasonably produce
* treats document completion as proof
* hides disagreement
* creates ceremony instead of clarity
* overlooks a critical dependency
* produces a recommendation that cannot be acted upon
* genuinely changes, constrains, pauses, or stops a decision

Start with a low-consequence decision. Protect confidential material. Keep consequential choices with accountable people and qualified specialists.

Then kick the tires.

Question the instructions. Challenge the terminology. Inspect the dependencies. Tell me when the AI assistant becomes too passive, too aggressive, too repetitive, or too certain.

Also tell me when the work succeeds.

Did it expose a disagreement the team had been stepping around? Did it reveal that a pilot had no owner? Did it keep an attractive demo from skipping the evidence bar? Did it help the team create a human-AI workflow that survived beyond one enthusiastic builder?

That is the evidence required to make the library better.

## Start With the Decision Hurting Most

Do not begin by rolling out an AI Product Operating Model.

Please.

The world has suffered enough from nouns turned into transformation programs.

Begin with one consequential decision:

* Where should AI actually fit in our product strategy?
* Is this initiative worth funding, launching, or scaling?
* What must be true before the technology is ready?
* How should humans and AI divide this recurring work?
* What evidence would cause us to continue, change, constrain, roll back, or stop?

Choose the Starter Pack closest to that decision.

Add the context and evidence you already have.

Let the missing pieces remain visible.

Run the workflow with the people who hold the relevant knowledge and authority.

Then make the decision.

You do not need all 41 skills.

You need the smallest working part of the operating model capable of changing what happens next.

AI is easy to start.

**The operating model decides whether it should move, who gets the wheel, and where the brakes are.**
