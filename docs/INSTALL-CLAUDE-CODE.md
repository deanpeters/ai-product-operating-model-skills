# Install AIPOM in Claude Code

Claude Code users can install the complete AIPOM library as one plugin. This is the quickest route when you want AIPOM methods available across existing projects without generating a separate working project first.

## Quick Setup

In Claude Code, add this repository as a marketplace and install AIPOM:

```text
/plugin marketplace add deanpeters/ai-product-operating-model-skills
/plugin install aipom@aipom-skills
/reload-plugins
```

Then describe the decision or organizational condition you need to work on. Claude can select a relevant skill automatically, or you can invoke a namespaced skill directly:

```text
/aipom:aipom-initiative-readiness-review
```

The plugin also exposes five workflow commands, including:

```text
/aipom:aipom-evaluate-initiative
/aipom:aipom-assess-organization
/aipom:aipom-redesign-workflow
```

Use `/help` if your installed Claude Code version displays a different grouping for skills and legacy workflow commands.

## Plugin or Starter Pack?

Use the plugin when:

- You already have a project and want AIPOM methods available inside it.
- You know the skill or workflow you want to use.
- You want Claude to discover relevant AIPOM skills from your request.

Use a [Starter Pack](../starter-packs/README.md) when:

- You want a bounded, job-led starting point rather than the complete catalog.
- You need context, evidence, decision, and output folders prepared for the work.
- You want a durable working ledger and `PACK-LOCK.yaml` source record.
- You expect the work to continue across sessions or move between people and agents.

The plugin and Starter Packs load the same canonical skills. The plugin is a distribution path; it does not replace the working-project structure or evidence discipline of a Starter Pack.

## Update or Remove

Refresh the marketplace and update the plugin through Claude Code's plugin interface:

```text
/plugin marketplace update aipom-skills
/plugin update aipom@aipom-skills
```

To remove it:

```text
/plugin uninstall aipom@aipom-skills
```

## Maintainer Verification

From the repository root, run:

```bash
python3 scripts/validate-claude-plugin.py
claude plugin validate .
./scripts/test-library.sh
```

The repository root is the plugin source so `skills/` and `commands/` remain canonical. Do not create separately maintained copies for Claude Code.
