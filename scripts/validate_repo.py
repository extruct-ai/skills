#!/usr/bin/env python3
"""Lightweight repository validation for Extruct AI skills."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"Missing required file: {path.relative_to(REPO_ROOT)}")


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    content = read_text(skill_md)
    if not content.startswith("---\n"):
        fail(f"{skill_md.relative_to(REPO_ROOT)} must start with YAML frontmatter")

    try:
        _, raw_frontmatter, _ = content.split("---\n", 2)
    except ValueError:
        fail(f"{skill_md.relative_to(REPO_ROOT)} has malformed frontmatter")

    result: dict[str, str] = {}
    for line in raw_frontmatter.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        result[key.strip()] = value.strip().strip("\"'")
    return result


def validate_skills() -> list[Path]:
    if not SKILLS_DIR.is_dir():
        fail("Missing skills/ directory")

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        fail("No skills found under skills/")

    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        frontmatter = parse_frontmatter(skill_md)
        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")

        if name != skill_dir.name:
            fail(
                f"{skill_md.relative_to(REPO_ROOT)} name '{name}' does not match directory "
                f"'{skill_dir.name}'"
            )
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            fail(f"{skill_md.relative_to(REPO_ROOT)} has invalid skill name '{name}'")
        if not description:
            fail(f"{skill_md.relative_to(REPO_ROOT)} must include a non-empty description")

        openai_yaml = skill_dir / "agents" / "openai.yaml"
        if openai_yaml.exists():
            yaml_text = read_text(openai_yaml)
            required_markers = [
                "interface:",
                "display_name:",
                "short_description:",
                "default_prompt:",
            ]
            for marker in required_markers:
                if marker not in yaml_text:
                    fail(
                        f"{openai_yaml.relative_to(REPO_ROOT)} is missing required marker '{marker}'"
                    )

            skill_root = openai_yaml.parent.parent
            for icon_key in ("icon_small", "icon_large"):
                match = re.search(rf"{icon_key}:\s+[\"']?(.+?)[\"']?$", yaml_text, re.MULTILINE)
                if match:
                    raw_icon_path = match.group(1)
                    candidates = [
                        (skill_root / raw_icon_path).resolve(),
                        (openai_yaml.parent / raw_icon_path).resolve(),
                    ]
                    if not any(path.exists() for path in candidates):
                        fail(
                            f"{openai_yaml.relative_to(REPO_ROOT)} references missing asset "
                            f"'{raw_icon_path}'"
                        )

    return skill_dirs


def validate_marketplace(skill_dirs: list[Path]) -> None:
    skill_dir_map = {f"./skills/{path.name}" for path in skill_dirs}
    try:
        payload = json.loads(read_text(MARKETPLACE_PATH))
    except json.JSONDecodeError as exc:
        fail(f"{MARKETPLACE_PATH.relative_to(REPO_ROOT)} is invalid JSON: {exc}")

    plugins = payload.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        fail(".claude-plugin/marketplace.json must contain a non-empty plugins array")

    referenced_paths: set[str] = set()
    for plugin in plugins:
        skills = plugin.get("skills")
        if isinstance(skills, list):
            referenced_paths.update(skills)
        elif isinstance(skills, str) and skills == "./":
            source = plugin.get("source")
            if isinstance(source, str):
                referenced_paths.add(source)
        else:
            fail("Each plugin entry must define skills as an array or './'")

    unknown = sorted(referenced_paths - skill_dir_map)
    if unknown:
        fail(f"Marketplace references unknown skill paths: {', '.join(unknown)}")


def main() -> None:
    skill_dirs = validate_skills()
    validate_marketplace(skill_dirs)
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
