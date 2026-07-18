# AIPOM for CTOs

This persona includes Chief Technology Officers and equivalent senior technology leaders such as a Chief Digital and Technology Officer, Chief Architect with enterprise authority, or SVP of Engineering or Technology acting as the accountable technical executive.

## What Is in It for You

AIPOM helps you define the technical evidence and operating conditions required to support AI products at their proposed scale, data use, dependency, reliability, and authority.

It helps you:

- Distinguish a successful demonstration from a supportable technical capability
- Expose model, vendor, data, infrastructure, integration, talent, and exit dependencies
- Set purpose-specific context and data readiness expectations
- Require evaluation evidence that supports product and operating decisions
- Define monitoring, fallback, rollback, incident, and recovery expectations
- Clarify technical ownership and the decisions that remain with other authorities
- Constrain scale or autonomy when evidence and recovery capability are insufficient

The CTO owns accountable technical decisions within the organization's governance model. The role does not independently decide product value, approve every investment, authorize regulated data use, accept legal or enterprise risk, or certify compliance.

## Your Plain-English Flow

### 1. Define the consequence the technical bar must support

Name the intended users, environment, scale, data, autonomy, critical dependencies, and consequences of failure or degradation.

**Your job:** prevent one generic “production ready” label from hiding materially different technical obligations.

### 2. Expose dependencies and exit constraints

Use the [platform dependency audit](../../skills/aipom-platform-dependency-audit/SKILL.md) to map model, vendor, data, infrastructure, contract, talent, portability, switching, and concentration exposure.

**Your job:** decide what may be accepted, mitigated, diversified, constrained, renegotiated, or exited.

### 3. Set context and data evidence expectations

Use the [context readiness advisor](../../skills/aipom-context-readiness-advisor/SKILL.md) and [data readiness audit](../../skills/aipom-data-readiness-audit/SKILL.md) in proportion to the proposed behavior and consequence.

**Your job:** require named sources, ownership, provenance, permissions, refresh, quality, and lifecycle evidence without impersonating data, privacy, or legal authorities.

### 4. Define evaluation and operating evidence

Use the [evaluation strategy advisor](../../skills/aipom-evaluation-strategy-advisor/SKILL.md) to connect product, model, workflow, human, and production evaluation to real decisions.

**Your job:** establish what evidence is required before launch, scale, material change, or increased autonomy.

### 5. Require usable failure and recovery systems

Use the [risk-control incident playbook](../../skills/aipom-risk-control-incident-playbook/SKILL.md) to connect preventive controls, detection, containment, fallback, rollback, communication, investigation, and learning.

**Your job:** ensure detection maps to an authorized action and that recovery is demonstrated rather than asserted.

## Start Here

- To establish an organization-level technical decision standard: [Establish the AI Technical Readiness Bar](../journeys/ESTABLISH-AI-TECHNICAL-READINESS-BAR.md)
- To review one material launch or scale decision: [Initiative Readiness](../adoption-packages/INITIATIVE-READINESS.md)
- To examine vendor and platform concentration: [AI Investment Decision](../adoption-packages/AI-INVESTMENT-DECISION.md)
- To establish decision rights and recovery: [Governance and Accountability](../adoption-packages/GOVERNANCE-AND-ACCOUNTABILITY.md)

To generate the bounded CTO working project from the repository root:

```bash
./create-starter-pack.sh --pack cto-technical-readiness
```

The generated project starts with `$aipom-start` in Codex or `/aipom-start` in Claude Code.

## You Are Done When

The proposed consequence has an explicit technical evidence bar, critical dependencies and gaps constrain the appropriate actions, technical owners and specialist decisions are named, recovery expectations are testable, exceptions expire, and the next review trigger is explicit.
