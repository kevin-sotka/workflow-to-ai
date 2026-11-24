#!/usr/bin/env python3
"""Check Markdown files against the Meatbag Method voice rules.

Usage: python tools/lint_voice.py [folder]

Flags: em dashes (anywhere in .md, .py, .json, .csv), exclamation points in prose,
and the words "just", "simply", "easy", and "obviously" in prose.
Code blocks and inline code are skipped for the word and punctuation checks.
"""

import os
import re
import sys

BANNED = re.compile(r"\b(just|simply|easy|easily|obviously)\b", re.IGNORECASE)
EXCLAIM = re.compile(r"!(?![\[=(])")
SKIP_DIRS = {".git", "__pycache__", "dist", "node_modules"}


def prose_lines(text):
    in_code = False
    for number, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        yield number, re.sub(r"`[^`]*`", "", line)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    problems = []
    for folder, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            path = os.path.join(folder, f)
            if not f.endswith((".md", ".py", ".json", ".csv", ".yml")):
                continue
            text = open(path, encoding="utf-8").read()
            for number, line in enumerate(text.splitlines(), 1):
                if chr(0x2014) in line:
                    problems.append(f"{path}:{number}: em dash")
            if f.endswith(".md"):
                for number, line in prose_lines(text):
                    if BANNED.search(line):
                        problems.append(f"{path}:{number}: avoid {BANNED.search(line).group(0)!r}")
                    if EXCLAIM.search(line):
                        problems.append(f"{path}:{number}: exclamation point")
    for p in problems:
        print(p)
    print(f"{len(problems)} voice issue(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
