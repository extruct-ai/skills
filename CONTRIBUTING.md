# Contributing

## Adding or Updating a Skill

1. Create or update a skill under `skills/<skill-name>/`.
2. Ensure `SKILL.md` includes valid frontmatter.
3. Keep the skill name aligned with the directory name.
4. Put large reference material in `references/` instead of expanding `SKILL.md`.
5. If the skill should be installable through Claude Code, update `.claude-plugin/marketplace.json`.

## Validation

Before opening a PR:

- confirm the skill path exists
- confirm `name:` in `SKILL.md` matches the folder name
- confirm JSON files parse cleanly
- run `python scripts/validate_repo.py`
- run `python -m py_compile skills/extruct-api/scripts/extruct-api`
- confirm no credentials or private data are committed

## Pull Requests

Open a pull request with:
- a short summary of the change
- any new skill names added to the marketplace manifest
- any behavior or compatibility notes users should know
