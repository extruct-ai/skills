# Extruct API Skill

Give coding agents a structured way to search, enrich, and operate Extruct workflows.

This skill helps agents use Extruct for company discovery, Deep Search, lookalike search, AI Tables, enrichment, and contact-finding without relying on ad hoc prompts.

## Overview

Use it when you want an agent to:
- discover companies with semantic search, lookalike search, or Deep Search
- build and update company or people tables
- enrich rows, add columns, score records, and inspect task progress
- find people at companies and retrieve contact data

Typical prompts:
- "Help me integrate the Extruct API into this codebase."
- "Research the competitive landscape around vercel.com using Extruct."
- "Give me an overview of my Extruct AI workspace."
- "Search Extruct for AI procurement startups."
- "Find companies similar to Ramp in Extruct."
- "Create an Extruct table for target accounts and enrich it."
- "Find decision makers at these companies in Extruct."

## Prerequisites

The bundled CLI requires an Extruct API token.

Get one from the [Extruct dashboard](https://app.extruct.ai/api-tokens).

Set:

```bash
export EXTRUCT_API_TOKEN=your_token_here
```

## Install

### Vercel Skills CLI

```bash
npx skills add extruct-ai/skills
```

### Claude Code

```bash
/plugin marketplace add extruct-ai/skills
/plugin install extruct-skills
```

### Codex and other Agent Skills compatible tools

Copy or symlink the skill into `.agents/skills/`:

```bash
cp -r skills/extruct-api .agents/skills/
```

Codex will discover the skill from `.agents/skills/` and can use the bundled `agents/openai.yaml` metadata for display and prompting.

You can also install from GitHub with Codex's `$skill-installer` once the repository is public.

## How It Works

Once installed, the skill gives the agent a structured path for common Extruct workflows instead of relying on ad hoc prompts. It helps the agent choose the right Extruct path, construct valid requests, inspect existing tasks and tables before mutating them, and carry async work through to completion.

The skill uses the same `EXTRUCT_API_TOKEN` as the API examples in the Extruct docs and treats the public Extruct API contract as the source of truth.

## What You Can Do

- Run Semantic Search, Lookalike Search, and Deep Search
- Help agents build against the Extruct API with the right workflow and payload shape
- Create, inspect, update, run, and read Extruct tables
- Add enrichment, scoring, and contact-finding workflows to existing tables
- Poll long-running tasks and return results in a consistent shape

## Available Skill

### `extruct-api`

## Contributing

See [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md) for repository conventions.

## Validation

Run:

```bash
python scripts/validate_repo.py
python -m py_compile skills/extruct-api/scripts/extruct-api
```

A GitHub Action runs the same checks on pushes and pull requests.

## Resources

- [Extruct API skill docs](https://www.extruct.ai/docs/build-with-ai-agents/extruct-api-skill)
- [Extruct API reference](https://www.extruct.ai/docs/api-reference/introduction)
- [Agent Skills](https://agentskills.io/)

## License

[MIT](LICENSE)
