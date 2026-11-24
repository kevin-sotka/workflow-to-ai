# Step 1: Find (Pick)

**Purpose:** turn a vague frustration into one concrete, scoped problem worth solving, with a picture of how the work happens today and what it costs.

The output of this step is the foundation for everything else. A good map and a real baseline make the business case honest and the test set real. A fuzzy map produces a helper that solves a problem nobody quite has.

## 1. Capture the current workflow

### Use the last real instance

People describe the idealized version of their work when asked "how does this process work?" Ask instead:

> "Walk me through the last time you did this, start to finish. What kicked it off?"

Then keep them in that specific instance:

- "What did you open first?"
- "Where did that number come from?"
- "Who did you have to wait on, and for how long?"
- "What would have happened if you skipped that step?"
- "Was that a normal one, or an unusual one? What does a bad one look like?"
- "Who else knows how to do this? What happens when you are out?"

If they have screenshots, a checklist, an SOP, sample emails, or a spreadsheet, ask for them. Real artifacts beat recollection.

### Fill the step table

Use [../assets/workflow-map.csv](../assets/workflow-map.csv). One row per step. Minutes are averages per occurrence: if a step happens in one case out of five and takes 20 minutes, enter 4.

| Column | What goes in it |
|---|---|
| `step_id` | S1, S2, and so on |
| `step` | Verb first, in their words: "Look up invoice in ERP" |
| `actor` | Role, not name: "AP specialist" |
| `tool` | System or medium: "Outlook", "SAP", "Excel", "phone" |
| `input` | What the step needs |
| `output` | What the step produces |
| `touch_minutes` | Hands-on time per occurrence |
| `wait_minutes` | Elapsed time waiting before the step can finish |
| `type` | One of the step types below |
| `pain` | 0 (fine) to 3 (the worst part) |
| `error_prone` | `y` if mistakes happen here |
| `single_point` | `y` if only one person knows how to do it |
| `notes` | Anything odd, any workaround |

### Step types

Classifying each step is the most useful thing you will do in this step, because the type predicts what kind of fix fits.

| Type | Looks like | Usual fix |
|---|---|---|
| `copy` | Moving information from one place to another, retyping, copy-paste | Integration, template, rules-based automation |
| `lookup` | Finding a record, checking a status, searching a folder | Search, a report, a connector, retrieval |
| `transform` | Reformatting, extracting fields, reconciling | Rules if structured; AI if the input is messy |
| `language` | Drafting, summarizing, translating, rewriting for an audience | Generative AI with review |
| `classify` | Sorting, tagging, routing, triaging | Rules if clear-cut; AI if judgment-like |
| `judgment` | Deciding with context, weighing tradeoffs, exceptions | Stays human; AI may prepare the information |
| `approval` | Sign-off, authorization | Stays human; make it faster and better informed |
| `communication` | Relationship work: calls, negotiation, sensitive news | Stays human; AI may help prepare |
| `wait` | Nothing happens until someone else acts | Process change, not AI |

In conversation, this is "circle the judgment, underline the copying." Mark `judgment`, `approval`, and `communication` steps as circled. Mark `copy`, `lookup`, and simple `transform` steps as underlined.

### Run the map script

```bash
python scripts/workflow_map.py current.csv --frequency 400 --title "Vendor payment inquiries"
```

`--frequency` is occurrences per month. The script prints a Mermaid diagram, total touch and wait time, monthly hours, the share of time in each step type, handoff count, and single points of knowledge. Paste its output into the running document.

## 2. Funnel the ideas

When the person has more than one frustration, list them all first without judging. Then score each candidate 1 to 5 in [../assets/opportunity-scorecard.csv](../assets/opportunity-scorecard.csv):

| Criterion | Question | 1 | 5 |
|---|---|---|---|
| `discrete` | Is it a specific, bounded problem? | "Everything about onboarding" | "Drafting the day-one schedule for each new hire" |
| `valuable` | How deeply and widely is the pain felt? | Mild annoyance for one person | Daily pain for a team, or real money or risk |
| `testable` | Could we try a fix on real cases soon? | No examples, no access | Dozens of real examples on hand |
| `frequency` | How often does it happen? | A few times a year | Many times a day |
| `data_ready` | Is the information needed reachable and usable? | Scattered, on paper, restricted | One system, clean, accessible |
| `complexity` | How hard is the fix likely to be? (5 is hardest) | Configuration of a tool they own | New integration, high-risk data, many teams |
| `risk` | How bad is a mistake? (5 is worst) | Internal draft nobody relies on | Decisions about people, money movement, regulators |

```bash
python scripts/score_opportunities.py scorecard.csv
```

The script checks the gate (discrete, valuable, and testable each at 3 or above), ranks candidates, and sorts them into four quadrants: **quick wins** (high value, low complexity), **big bets** (high value, high complexity), **fill-ins** (low value, low complexity), and **money pits** (low value, high complexity). Start with a quick win unless there is a strong reason not to. A first success buys the credibility for a big bet.

## 3. Ask why until it is actionable

Use repeated "why" questions to get past the symptom. Stop when the answer is something the person can act on.

> "We spend hours answering vendor emails." Why? "They keep asking where their payment is." Why? "They can't see payment status." Why? "The supplier portal shows it, but nobody told them it exists."

That chain moved the best fix from AI to a process change. Good. It often happens.

## 4. Set the baseline

Estimate today's cost across five dimensions. Rough numbers are fine as long as each is labeled **measured**, **estimated**, or **assumed**.

| Dimension | What to capture | How to get it fast |
|---|---|---|
| Money | Direct cost, rework, penalties, lost revenue | Finance reports, invoices, the person's estimate |
| Time, and whose time | Hours per month, by role; an owner's or senior expert's hour is not a junior's hour | Touch time from the map multiplied by frequency; time three real instances |
| Wellbeing | After-hours work, stress, turnover risk, dread | Ask directly: "What does this do to your week?" |
| Error rate | How often it goes wrong and what a mistake costs | Count rework, corrections, complaints over the last month |
| External risk | Customers, compliance, safety, reputation | Ask: "What is the worst thing that has happened because of this?" |

Quick measurement methods, in order of preference:
1. **Count from a system:** tickets, emails, records, transactions per month
2. **Time it:** have the person time the next three instances
3. **Sample:** pull the last ten instances and estimate each
4. **Ask:** the person's best estimate, labeled as assumed

## 5. Collect the examples now

Before leaving this step, ask the person to gather 10 to 30 real past instances of the work: the inputs, and ideally what a good output looked like. Redact names and sensitive fields if needed. Include the weird ones. These become the test set in Step 5, and collecting them now is the cheapest moment to do it.

If they cannot produce any real examples, that is a signal about testability. Note it.

## Gate 1

Is the problem **discrete, valuable, and testable**?

- **Pass:** move to Step 2.
- **Not discrete:** narrow to one slice of the process (one document type, one request type, one region).
- **Not valuable:** choose another candidate from the funnel.
- **Not testable:** find a version with examples, or plan how to collect them for two weeks before continuing.

## Output for the running document

```markdown
## 1. Find: problem and baseline

**Problem statement.** <One paragraph: who, what, how often, why it matters, in their words.>

**Current workflow.** <Mermaid diagram and stats from workflow_map.py.>

**Circled (judgment) steps:** <list>. **Underlined (copying) steps:** <list>.

**Candidates considered.** <Ranked table from score_opportunities.py, if more than one.>

**Root cause.** <The "why" chain in two or three sentences.>

**Baseline.**
| Dimension | Today | Basis |
|---|---|---|
| Money | | measured / estimated / assumed |
| Time (whose) | | |
| Wellbeing | | |
| Error rate | | |
| External risk | | |

**Examples collected:** <count, location, redaction notes>

**Gate 1:** pass / reframed (see Reframes)

**What, So What, Now What.**
```
