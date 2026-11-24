#!/usr/bin/env python3
"""Validate a skill folder against the Agent Skills specification (agentskills.io/specification).

Usage: python tools/validate_skill.py skills/workflow-to-ai

Checks: SKILL.md exists with YAML frontmatter; name rules; description length; optional
field limits; name matches the folder; SKILL.md under 500 lines; relative links resolve.
Standard library only (a minimal frontmatter reader, not a full YAML parser).
"""

import os
import re
import sys

ALLOWED = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}


def frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    block, body = text[4:end], text[end + 5:]
    fields, current = {}, None
    for line in block.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):
            if current:
                fields[current] = (fields[current] + "\n" + line.strip()).strip()
            continue
        key, _, value = line.partition(":")
        current = key.strip()
        fields[current] = value.strip().strip('"').strip("'")
    return fields, body


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    folder = sys.argv[1].rstrip("/")
    errors = []
    path = os.path.join(folder, "SKILL.md")
    if not os.path.isfile(path):
        sys.exit(f"FAIL: {path} not found")
    text = open(path, encoding="utf-8").read()
    fields, body = frontmatter(text)
    if fields is None:
        sys.exit("FAIL: SKILL.md must start with YAML frontmatter between --- lines")

    name = fields.get("name", "")
    if not name:
        errors.append("name is required")
    elif len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        errors.append("name must be 1-64 lowercase letters, digits, and single hyphens, "
                      "not starting or ending with a hyphen")
    if name and name != os.path.basename(os.path.abspath(folder)):
        errors.append(f"name {name!r} must match the folder name {os.path.basename(os.path.abspath(folder))!r}")

    desc = fields.get("description", "")
    if not desc:
        errors.append("description is required")
    elif len(desc) > 1024:
        errors.append(f"description is {len(desc)} characters; the limit is 1024")

    comp = fields.get("compatibility")
    if comp is not None and not 1 <= len(comp) <= 500:
        errors.append("compatibility must be 1-500 characters")

    unknown = set(fields) - ALLOWED
    if unknown:
        errors.append(f"unknown top-level fields: {', '.join(sorted(unknown))}")

    lines = text.count("\n") + 1
    if lines > 500:
        errors.append(f"SKILL.md is {lines} lines; keep it under 500")

    for md_root, _, files in os.walk(folder):
        for f in files:
            if not f.endswith(".md"):
                continue
            md = os.path.join(md_root, f)
            for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", open(md, encoding="utf-8").read()):
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                resolved = os.path.normpath(os.path.join(os.path.dirname(md), target))
                if not os.path.exists(resolved):
                    errors.append(f"broken link in {os.path.relpath(md, folder)}: {target}")

    print(f"Skill: {name}")
    print(f"Description: {len(desc)} characters")
    print(f"SKILL.md: {lines} lines, about {len(body.split())} words")
    if errors:
        for e in errors:
            print(f"FAIL: {e}")
        sys.exit(1)
    print("PASS")


if __name__ == "__main__":
    main()
