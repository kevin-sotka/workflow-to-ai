# Step 6: Prove (Ritual)

**Purpose:** make the impact provable, make the new way of working stick, and keep the helper healthy after launch. Give it a home and a schedule, so it still works in a busy week.

Most AI pilots that stall do so here, after a successful demo. The work in this step is unglamorous and decisive.

## 1. Launch plan

- **Stage it.** Start with the pilot group, then one team, then wider. Each stage has a go or no-go check against the scoreboard.
- **Train in fifteen minutes.** Show the helper on a real case, show how to check its output with the reviewer checklist, show how to reject or escalate, and show how to report a problem. The most important habit to teach: **read it like it is wrong.**
- **Name a champion** in each team: a respected peer who uses it visibly and collects feedback. Leading by example beats announcements.
- **Say what is in it for them.** Be specific about what each role gets back (time, fewer evening catch-ups, fewer errors to fix) and what stays theirs.
- **Say what is not changing.** People worry about what the helper means for their job. Name which decisions and relationships remain human, in plain words.

## 2. The scoreboard

| Metric | Kind | Baseline | Target | Source | Frequency | Owner |
|---|---|---|---|---|---|---|
| Median minutes per case | Business | 6.0 (measured) | 3.0 | Ticket timestamps | Weekly | Team lead |
| Test set pass rate | Quality | 0.93 (v0.4) | at least 0.90 | eval_report.py | Monthly and on change | Helper owner |
| Correction rate | Quality | n/a | under 20 percent | Reviewer log | Weekly | Helper owner |
| Share of eligible cases using helper | Adoption | 0 | 60 percent | Usage report | Weekly | Champion |
| Unreviewed outbound messages | Guardrail | 0 | 0 | Audit log | Monthly | Helper owner |

Compare against the Step 1 baseline, not against memory.

## 3. Signals to watch

| Signal | What it might mean |
|---|---|
| Correction rate rising | Inputs have changed, the model changed, or the context pack is stale |
| Correction rate near zero for weeks | Either it is excellent (consider promoting autonomy, with evidence) or reviewers have stopped checking (audit a sample) |
| Escalations rising | New kinds of cases, or a policy change the helper does not know about |
| Usage falling | It is not saving time, it is hard to reach, or trust was lost after a visible mistake. Ask users. |
| Complaints or incidents | Pause if needed, add the case to the test set, fix, rerun |
| Cost per case rising | Usage-based pricing changes, longer inputs, more retries |

## 4. Ownership and upkeep

- **Owner and backup,** by name. The owner keeps the instructions, context pack, test set, and changelog current.
- **Monthly review (30 minutes):** the scoreboard, the failure log, user feedback, any policy changes that affect the context pack.
- **Rerun the test set** whenever the instructions, context, tools, or underlying model change. Vendors update models without notice. A monthly rerun catches silent drift.
- **Change log** for every change, with the test result after.
- **Retirement criteria:** decide now what would cause the helper to be switched off (sustained low use, the process changes, a better tool arrives). Retiring a helper on purpose is good housekeeping.

## 5. Write the new process down

Update or create the SOP so someone else could do the work tomorrow, with or without the helper:
- The new steps, who does each one, and where the helper fits
- How to check the helper's output, with the reviewer checklist
- What to do when the helper is unavailable
- Where the files live and who owns them

The method started by finding single points of knowledge. This step removes them.

## 6. 30, 60, 90 days

| Checkpoint | Question | Possible decisions |
|---|---|---|
| 30 days | Is it being used, and is it working on real cases? | Continue, fix, or pause |
| 60 days | Is the scoreboard moving toward target? | Expand to more users, adjust, or narrow |
| 90 days | Did it deliver the business case? | Scale, promote one autonomy level (with evidence), hand to IT for a production build, or retire |

## 7. Portfolio view (for teams with several helpers)

Keep a catalog of use cases with status and a value-versus-complexity read, using the quadrants from `scripts/score_opportunities.py`: quick wins, big bets, fill-ins, money pits. Review it quarterly with the sponsor. Each finished helper makes the next one cheaper: the method, the templates, and the test habits carry over.

## 8. Diagnosing a helper that is not paying off (check-up mode)

Ask for usage numbers, ten recent real outputs, and ten minutes with two users. Then match the symptom:

| Symptom | Usual causes | Go back to |
|---|---|---|
| **Nobody uses it** | Hard to reach (a separate app, extra logins); not in the flow of work; nobody was shown how; it solved a problem the team does not feel | Step 1 (is the pain real?), Step 6 launch plan (training, champion, placement) |
| **People use it, but no time is saved** | Checking the output takes as long as doing the work; outputs need heavy rewriting; the slow part of the workflow was never the part the helper touches | Step 2 (fit test, redesign the workflow around it), Step 5 (count fixing minutes) |
| **People stopped trusting it** | One visible mistake; confident wrong answers; no sources shown, so checking is slow | Step 5 (failure modes, sources in the output), the reviewer checklist |
| **Quality drifted** | The underlying model changed; policies or source data changed; new kinds of inputs | Step 5 (rerun the test set, add new cases), refresh the context pack |
| **It works, but nobody can prove it** | No baseline was taken; nothing is measured | Step 1 baseline (measure the old way on a sample), Step 6 scoreboard |
| **Costs crept up** | Usage-based pricing, long inputs, retries, an agent doing many steps | Step 4 (rerun the numbers), Step 2 (a simpler pattern) |

Most check-ups find the problem in the workflow or the launch, not in the model. Fix the cheapest cause first.

## 9. Build brief (for a production build)

If the helper will be rebuilt by IT or engineering, or scaled beyond what a no-code tool supports, write [../assets/build-brief.md](../assets/build-brief.md). It should be clear enough for a developer or a coding agent to build from without a meeting. Include the test set; it becomes their acceptance test.

## Gate 6

Can the impact be measured against the baseline, and can the person explain the problem, the fix, and the numbers to someone else in plain words?

If not, fill the gap before calling it done. Teaching it is the proof of understanding.

## Closing the engagement

Give the person:
1. A **three-sentence summary** they could say out loud to the decision maker: the problem, what changed, and the result with its numbers.
2. The **finished running document** and the **helper folder**.
3. **One concrete next action** with a date or trigger attached (for example, "Rerun the test set on the first Monday of next month, and bring the scoreboard to the team meeting on the 15th").

## Output for the running document

```markdown
## 6. Prove: impact plan

**Launch plan.** <Stages, training, champions, dates.>
**Scoreboard.** <Table.>
**Owner and backup.** <Names.> **Monthly review:** <day>. **Retirement criteria:** <list>.
**New process.** <Link to SOP.>
**30 / 60 / 90 day checkpoints.** <Dates and decision rules.>
**Build brief.** <Link, if applicable.>
**Gate 6:** pass / reframed
**Three-sentence summary.**
**Next action.** <Action, owner, date.>
```
