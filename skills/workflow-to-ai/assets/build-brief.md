# Build brief: <helper name>

*For a developer, an IT team, or a coding agent building a production version. It should be possible to build from this brief without a meeting. Keep it tool-agnostic unless a platform has been chosen.*

## 1. Goal

<One paragraph: the problem, who has it, and what the helper changes. Link to the running document.>

## 2. Users and volume

- Users: <roles, count>
- Volume: <occurrences per day or month, peaks>
- Where they work: <the systems and channels they already use>

## 3. Current and future process

<Before and after maps from workflow_map.py. Mark every human checkpoint.>

## 4. Inputs and outputs

| | Description | Format | Source or destination | Example |
|---|---|---|---|---|
| Input | | | | |
| Output | | | | |

## 5. Behavior

- Instructions: see `helper/<name>/instructions.md` (tested version v<x>)
- Context pack: see `helper/<name>/context/`
- Pattern: <pattern and steps>
- Deterministic steps that must not be done by the model: <lookups, arithmetic, validation rules>
- Escalation rules: <list>
- Out of scope: <list>

## 6. Data and integrations

| Data | System | Access needed (read or write) | Sensitivity | Owner |
|---|---|---|---|---|

## 7. Security and governance

- Risk tier: <low / medium / high> and required controls
- Identity: <acts as the user, or as a scoped service identity>
- Permissions: least privilege; list each permission and why
- Prompt injection handling: <external content treated as data; actions require approval>
- Logging and retention: <what is logged, for how long, who can see it>
- Approvals required before launch: <security, privacy, legal, compliance>

## 8. Human checkpoints

| Checkpoint | Who | What they see | What they can do | How it is recorded |
|---|---|---|---|---|

## 9. Acceptance criteria

- The test set in `helper/<name>/tests/` passes at or above: <thresholds from Step 4>
- No critical failures
- Red team cases handled: <list>
- Performance: <response time, cost per case limits>

## 10. Known edge cases and failure modes

<From the Step 5 failure log, with how each was addressed.>

## 11. Monitoring after launch

<The scoreboard from Step 6, plus technical monitoring: errors, latency, cost, usage.>

## 12. Open questions

1. <Question, owner, due date>
