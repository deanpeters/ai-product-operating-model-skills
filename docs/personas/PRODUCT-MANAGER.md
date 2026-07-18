# AIPOM for Product Managers

## What Is in It for You

AIPOM gives Product Managers a decision path for taking an AI opportunity from problem evidence through value, behavior, context, evaluation, authority, launch or investment decisions, and production learning.

It helps you:

- Challenge solution-first and vendor-first ideas
- Connect AI behavior to customer and economic outcomes
- Make assumptions and missing evidence visible
- Coordinate product, technical, operational, and governance work
- Define what the system should do, how it will be evaluated, and where people retain authority
- Reach explicit fund, test, launch, constrain, pause, or stop decisions
- Learn from production evidence instead of treating launch as completion

The Product Manager leads product decisions and evidence integration. The role does not replace engineering, design, research, data, operations, finance, or accountable specialist judgment.

## Your Plain-English Flow

### 1. Frame the problem before the AI solution

Use [AI Opportunity Framing](../../skills/aipom-opportunity-framing/SKILL.md) to define the affected people, current condition, alternatives, consequence, evidence, and next uncertainty.

**Your job:** prevent a demo, mandate, or vendor feature from becoming the problem statement.

### 2. Explain how value should happen

Use the [AI Outcome and Value Map](../../skills/aipom-outcome-value-map/SKILL.md) to connect system behavior to user behavior, product outcomes, economics, and risk. Use the [AI Bet Charter](../../skills/aipom-bet-charter/SKILL.md) to name the owner, scope, constraints, next test, and stop conditions.

**Your job:** expose the causal assumptions and choose the smallest useful learning motion.

### 3. Prepare the product to behave responsibly

Use the [authoritative source map](../../skills/authoritative-source-map/SKILL.md), [data readiness audit](../../skills/aipom-data-readiness-audit/SKILL.md), and [context package builder](../../skills/aipom-context-package-builder/SKILL.md) to establish what the system may rely on. Use the [behavior contract](../../skills/aipom-behavior-contract-builder/SKILL.md) and [evaluation strategy advisor](../../skills/aipom-evaluation-strategy-advisor/SKILL.md) to define acceptable behavior and decision-relevant evidence.

**Your job:** integrate the work and make tradeoffs explicit. Specialists still own their technical and governance decisions.

### 4. Define human responsibility and authority

Use the [human-AIPOM work contract](../../skills/human-aipom-work-contract/SKILL.md), [accountability charter](../../skills/aipom-accountability-charter/SKILL.md), and [autonomy boundary designer](../../skills/aipom-autonomy-boundary-designer/SKILL.md) to state what AI may do, what people review or decide, and what triggers escalation or fallback.

**Your job:** eliminate vague “human in the loop” claims and keep accountability human.

### 5. Make the material decision

Use the [economic case builder](../../skills/aipom-economic-case-builder/SKILL.md), [platform dependency audit](../../skills/aipom-platform-dependency-audit/SKILL.md), and [initiative readiness review](../../skills/aipom-initiative-readiness-review/SKILL.md) in proportion to the commitment and consequence.

**Your job:** arrive at a scoped proceed, constrain, remediate, pause, or stop recommendation with conditions, owners, expiry, and a re-review trigger.

### 6. Learn from operation

Use the [production evidence review](../../skills/aipom-production-evidence-review/SKILL.md) and [risk-control incident playbook](../../skills/aipom-risk-control-incident-playbook/SKILL.md) to monitor behavior, outcomes, burden, controls, incidents, and affected-user evidence.

**Your job:** change, constrain, roll back, or retire the product when evidence requires it.

## Start Here

- If the opportunity is early: [AI Investment Decision](../adoption-packages/AI-INVESTMENT-DECISION.md)
- If launch or scale is pending: [Evaluate an AI Initiative](../journeys/EVALUATE-AN-AI-INITIATIVE.md)
- If the product changes recurring team work: [Human-AI Workflow Pilot](../adoption-packages/HUMAN-AI-WORKFLOW-PILOT.md)

To generate the bounded Product Manager working project from the repository root:

```bash
./create-starter-pack.sh --pack product-manager-initiative
```

The generated project starts with `$aipom-start` in Codex or `/aipom-start` in Claude Code.

## You Are Done When

The accountable decision has been made at a defined scope, the evidence and assumptions are visible, specialist decisions are recorded, conditions have owners and expiry, and the next learning or review motion is explicit.
