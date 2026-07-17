# Weak Example: “Keep a Human in the Loop”

**Synthetic weak example.** This is intentionally inadequate.

## Proposed Boundary

> The support bot can handle normal customer requests. A human will stay in the loop for risky situations, and administrators can turn it off if anything goes wrong.

## Why It Fails

- “Handle” bundles classification, drafting, sending, refunds, and account changes into one vague action.
- “Normal” and “risky” have no operational definitions.
- The reviewer, evidence, response time, and decision authority are unnamed.
- No prohibited actions or permission limits are stated.
- No monitoring, escalation triggers, safe fallback, or rollback evidence is provided.
- The example assumes an off switch works without testing it.
- It treats the existence of a statement as proof of operational control.

## Minimum Repair

Split the workflow into atomic actions, classify each boundary, name the decision and accountability owners, define escalation and stop conditions, and run a bounded test showing that reviewers and controls work under representative conditions.

