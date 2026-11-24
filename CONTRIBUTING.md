# Contributing

Thank you for wanting to make this better.

- **Stories are the most useful contribution.** If you used the skill on a real workflow, open an issue and tell us what worked, what confused you, and where the helper failed. Leave out anything confidential.
- **Corrections to platform details** (`references/platforms.md`) are welcome as pull requests, with a link to the vendor's current documentation.
- **New function playbooks** or improvements to existing ones are welcome. Keep them illustrative and generic, and never include real client or employer details.
- **Style:** plain, complete sentences for a smart reader who is not technical. No em dashes. No exclamation points. Skip the small words that make a worried reader feel behind (the list is in `tools/lint_voice.py`).

Before opening a pull request, run:

```bash
python -m unittest discover -s tests
python tools/validate_skill.py skills/workflow-to-ai
python tools/lint_voice.py .
```
