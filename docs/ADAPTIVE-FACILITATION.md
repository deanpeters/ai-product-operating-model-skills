# Adaptive Facilitation Standard

This document is the source of truth for interactive advisors and workflow skills.

## Core Principle

The facilitator should spend questions only where answers can change the diagnosis, recommendation, artifact, or next action.

Anything supplied with the request already counts as context. Do not ask the user to repeat it.

## Entry Modes

Every interactive advisor and workflow supports three modes.

### Guided Mode

- Ask one question at a time.
- Explain unfamiliar concepts before requesting judgment.
- Adapt each next question to the information already gathered.
- Use small batches only when questions are tightly connected and easy to answer together.

### Context-Dump Mode

- Accept notes, documents, assessment results, links, existing artifacts, or outputs from earlier skills.
- Extract facts, evidence, assumptions, decisions, ownership, and gaps.
- Confirm only material ambiguities.
- Ask only for missing information that could change the result.

### Best-Guess Mode

- Continue with reasonable assumptions.
- Label assumptions visibly.
- Reduce confidence where evidence is weak.
- Do not score an unverified practice above `2 — Emerging`.
- Identify what evidence would confirm or change the recommendation.

## Context Ledger

Workflows should maintain a compact ledger containing:

| Field | Purpose |
|---|---|
| Supplied context | What the user or repository already provided |
| Evidence | Inspectable support for a claim |
| Assumptions | Necessary beliefs not yet supported by evidence |
| Decisions | Choices reached and why |
| Ownership | Who decides, contributes, reviews, and remains accountable |
| Unresolved questions | Gaps that could alter the result |
| Outputs | Artifacts or recommendations already produced |
| Next actions | Named motion, owner, and expected evidence |

Pass this ledger between component skills. Do not make users re-enter earlier work.

## Questions

Good questions are plain-language, answerable, and consequential.

Do:

- Recognize uncertainty as a valid answer.
- Ask for examples of actual use when maturity matters.
- Ask whose perspective is represented and whose is missing.
- Surface disagreements rather than forcing consensus.
- Stop asking when enough is known to act responsibly.

Do not:

- Read every empty template field aloud.
- Ask questions already answered in supplied material.
- Require artificial precision.
- treat executive confidence as evidence of consistent practice.

## Decision Points

At meaningful choices:

1. Present numbered options.
2. Explain when each option fits.
3. Recommend a default when evidence supports one.
4. Accept selections such as `1`, `1 and 3`, or custom text.
5. Synthesize combined selections instead of restarting.

Numbered options are for decisions, not for turning the entire conversation into a questionnaire.

## Conflicting Evidence

When sources or participants disagree:

- Preserve the differing claims and their sources.
- Distinguish a disagreement about facts from one about values, risk tolerance, or strategy.
- Explain why the disagreement matters.
- Avoid manufacturing a single score merely to simplify reporting.
- Recommend the smallest next action that could resolve the consequential uncertainty.

## Human Accountability

For automation, agents, governance, evaluation, or consequential recommendations, state:

- What AI may do independently
- What requires human review
- Who decides
- Who is accountable
- What triggers escalation
- What the system must never do
- How failures are detected, corrected, and learned from

## Pause and Resume

Before pausing, record:

- Current stage
- Evidence reviewed
- Decisions made
- Assumptions still in use
- Open questions
- Next requested input or action

On resume, restate only the minimum necessary context and continue from the recorded stage.

## Completion Criteria

An interactive advisor or workflow is complete when it has produced:

- The promised artifact, diagnosis, or recommendation
- Evidence used
- Assumptions made
- Decisions reached
- Unresolved questions
- Named decision authority and accountability where relevant
- A specific next action
- Related skills that logically follow

Do not end with only a generic invitation to continue exploring.

