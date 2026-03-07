# Extruct AI Skills

Official Extruct AI skills for coding agents.

This repository packages Extruct AI workflows as [Agent Skills](https://agentskills.io/) so agents can use Extruct for company discovery, semantic search, lookalike search, Deep Search, AI Tables, enrichment, and people/contact workflows.

It also serves as a Claude Code plugin marketplace via `.claude-plugin/marketplace.json`.
For Codex, skills can also include `agents/openai.yaml` for native display metadata; `extruct-api` includes that file.

## What This Skill Does

`extruct-api` helps agents operate Extruct AI through a bundled CLI wrapper.

It is designed for:
- company discovery with semantic search, lookalike search, and Deep Search
- company and people table workflows
- enrichment, scoring, and contact-finding operations
- inspecting, updating, polling, and reading existing Extruct tasks and tables

Typical prompts:
- "search Extruct for AI procurement startups"
- "find companies similar to Ramp in Extruct"
- "create an Extruct table for target accounts and enrich it"
- "find decision makers at these companies in Extruct"

## Setup

The bundled CLI requires an Extruct API token.

Set:

```bash
export EXTRUCT_API_TOKEN=your_token_here
```

Before first use, the skill typically checks access with:

```bash
/absolute/path/to/extruct-api/scripts/extruct-api auth user
```

If authentication or behavior is unclear, the official Extruct API reference is the source of truth:

- [Extruct API reference](https://www.extruct.ai/docs/api-reference/introduction)

## Install

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

## Available Skills

### `extruct-api`

Run explicit Extruct API tasks through the bundled Extruct CLI. Covers Deep Search, semantic search, lookalike search, company and people tables, column operations, enrichment, and contact finding.

## Repository Structure

```text
.claude-plugin/
  marketplace.json
skills/
  extruct-api/
    SKILL.md
    agents/
    scripts/
    assets/
    references/
```

## Contributing

See [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md) for repository conventions.

## Validation

Run:

```bash
python scripts/validate_repo.py
python -m py_compile skills/extruct-api/scripts/extruct-api
```

A GitHub Action runs the same checks on pushes and pull requests.

## License

[MIT](LICENSE)
