# Establish the AI Technical Readiness Bar

Use this entry path to define the technical evidence and operating conditions required before AI products may launch, scale, change materially, or receive greater authority.

## Entry Modes

- **Guided:** begin with the highest-consequence technical decision the standard must support.
- **Context dump:** inspect architecture, dependency, data, evaluation, monitoring, incident, and recovery material before asking gaps.
- **Best guess:** label assumptions, propose a provisional minimum bar, and constrain scale or authority until evidence exists.

## Sequence

1. Define the scope, decision classes, consequences, accountable technical authority, and specialist decisions the readiness bar must support.
2. Use [`aipom-platform-dependency-audit`](../skills/aipom-platform-dependency-audit/SKILL.md) to define dependency, portability, concentration, and exit evidence.
3. Use [`aipom-context-readiness-advisor`](../skills/aipom-context-readiness-advisor/SKILL.md) and [`aipom-data-readiness-audit`](../skills/aipom-data-readiness-audit/SKILL.md) proportionate to behavior and consequence.
4. Use [`aipom-evaluation-strategy-advisor`](../skills/aipom-evaluation-strategy-advisor/SKILL.md) to define decision-relevant evaluation coverage and thresholds.
5. Use [`aipom-risk-control-incident-playbook`](../skills/aipom-risk-control-incident-playbook/SKILL.md) to define monitoring, control, containment, fallback, rollback, incident, and recovery expectations.
6. Assemble the readiness bar by decision class, including required evidence, owner, reviewer, exception authority, expiry, and re-review trigger.

## Context Handoff

Preserve scope, consequence tiers, architecture and dependencies, context and data conditions, behavior and evaluation requirements, production signals, recovery evidence, owners, exceptions, disagreements, and unresolved specialist decisions.

## Stop and Escalation Rules

- Do not treat a prototype, vendor claim, architecture diagram, or completed checklist as readiness evidence.
- Do not let strong model performance compensate for a critical dependency, data, security, recovery, or authority gap.
- Do not let the CTO absorb product, finance, legal, privacy, security, safety, risk, or governance authority.
- Constrain launch, scale, data use, or autonomy when the applicable technical bar is unmet.

## Completion

Finish with consequence-aware readiness classes, required technical evidence, non-negotiable gaps, owners and reviewers, exception and expiry rules, permitted interim motions, and a dated review trigger.
