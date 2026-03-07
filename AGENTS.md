# AGENTS.md

Guidance for agents and contributors working in this repository.

## Repository Purpose

This repository contains official Extruct AI skills following the Agent Skills format.

It also serves as a Claude Code plugin marketplace via `.claude-plugin/marketplace.json`.

## Repository Structure

```text
.claude-plugin/
  marketplace.json
skills/
  extruct-api/
    SKILL.md
    agents/
    scripts/
    references/
```

## Skill Requirements

Each skill must live under `skills/<skill-name>/`.

Required:
- `SKILL.md`

Optional:
- `scripts/`
- `references/`
- `assets/`
- `agents/`

## Source Of Truth

When skill instructions and the public API surface might diverge, prefer the official Extruct API reference as the source of truth:

- https://www.extruct.ai/docs/api-reference/introduction

Use local skill guidance first for standard workflows and bundled CLI usage. Consult the official docs when:
- endpoint behavior is unclear
- the user asks for a capability not covered by the bundled CLI
- a request may depend on recently changed API behavior

## SKILL.md Rules

Frontmatter must include:

```yaml
---
name: extruct-api
description: Clear description of what the skill does and when to use it.
---
```

Rules:
- `name` must exactly match the directory name
- use lowercase letters, numbers, and hyphens only
- `description` should explain both capability and activation cues
- keep `SKILL.md` concise and move supporting detail into `references/`

## Marketplace Rules

When adding or renaming a skill:
- update `.claude-plugin/marketplace.json`
- ensure all listed skill paths exist
- keep plugin descriptions human-readable for marketplace browsing

## Codex Metadata

Codex-specific metadata can live under `skills/<skill-name>/agents/openai.yaml`.

Use it for:
- display name
- short description
- icon references
- brand color
- default prompt

Keep Codex metadata additive and avoid duplicating core instructions from `SKILL.md`.

## Scripts

Scripts should be self-contained and callable from the skill instructions.

Prefer stable interfaces and machine-readable output where practical.

## Contributor Checklist

- folder name matches `name:` in `SKILL.md`
- skill description is clear and specific
- supporting files are loaded on demand rather than embedded inline
- marketplace manifest is updated
- no secrets or tokens are committed
- `python scripts/validate_repo.py` passes
