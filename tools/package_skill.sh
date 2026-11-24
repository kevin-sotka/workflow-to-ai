#!/usr/bin/env bash
# Build dist/workflow-to-ai.zip for uploading to Claude or attaching to a GitHub release.
# The zip contains one top-level folder, workflow-to-ai/, with SKILL.md inside it.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/validate_skill.py skills/workflow-to-ai
mkdir -p dist
rm -f dist/workflow-to-ai.zip
(cd skills && zip -rq ../dist/workflow-to-ai.zip workflow-to-ai -x '*/__pycache__/*' '*.pyc' '*/.DS_Store')
echo "Built dist/workflow-to-ai.zip"
unzip -l dist/workflow-to-ai.zip | tail -1
