# Step 2: Shape (Pick)

**Purpose:** design how the work should happen, starting with the simplest fix, and decide precisely where generative AI belongs and how much it is allowed to do.

The most common failure in AI projects is inserting a model into a workflow that should have been redesigned. Large surveys of AI adopters keep finding the same thing: the organizations getting real value are the ones that redesign the work, not the ones that add AI to the old process. This step is where that happens.

## 1. Redesign the work first (ECRS)

Go through the step table one row at a time and ask four questions, in this order:

| Question | Prompt to the person |
|---|---|
| **Eliminate** | "What would happen if this step stopped tomorrow? Who would notice?" |
| **Combine** | "Could this be done at the same time as another step, or by the same person?" |
| **Rearrange** | "Would doing this earlier prevent a problem later?" (for example, validating inputs at intake instead of fixing them at the end) |
| **Simplify** | "Could a template, a standard form, a checklist, or a default make this step shorter?" |

Wait steps deserve special attention. Waiting is rarely an AI problem. It is usually a handoff, an approval queue, or a missing input, and the fix is a process change.

## 2. Circle the judgment, underline the copying

Using the step types from Step 1:

- **Underlined** steps (`copy`, `lookup`, simple `transform`) are candidates to hand over to a machine.
- **Circled** steps (`judgment`, `approval`, `communication`) stay with a person. AI may prepare the information, but the person decides.
- Steps in between (`language`, `classify`, messy `transform`) are where generative AI usually earns its place.

## 3. Walk the ladder of fixes

Start at the bottom. Stop at the first rung that solves the problem well enough.

| Rung | Fix | Example |
|---|---|---|
| 1 | **Change or remove the step** | Stop producing a weekly report nobody reads |
| 2 | **Use a feature of a tool they already own** | Turn on the supplier portal's payment status page; use an existing approval workflow |
| 3 | **Put the information in one place** | A shared tracker, a standard intake form, a single source of truth |
| 4 | **Rules-based automation** | A flow that copies fields between systems, a scheduled report, an RPA bot for a stable screen |
| 5 | **AI assists a person** | AI drafts, summarizes, extracts, or classifies; a person reviews and sends |
| 6 | **AI acts, with approval** | AI updates a record or sends a message after a person approves |
| 7 | **AI acts and reports** | AI handles routine cases on its own; a person audits a sample and handles exceptions |

Most good solutions combine rungs: a process change plus a form (rungs 1 and 3) plus an AI draft for the messy part (rung 5). That combination is normal and usually best.

## 4. The generative AI fit test

**Good signals.** Generative AI tends to fit when most of these are true:
- The work is language-heavy: reading, writing, summarizing, explaining, rewriting
- Inputs are unstructured or vary a lot (emails, PDFs, notes, transcripts, free text)
- There is a recognizable pattern, but rules cannot capture every variation
- A good draft has value even if a person polishes it
- Real examples of good output exist
- **Checking the output is much faster than producing it**

**Poor signals.** Look for another rung when:
- The task needs exact arithmetic or deterministic rules (use a spreadsheet, a formula, or code; AI can write that code)
- Nobody can check the output, and a mistake is costly
- The helper cannot reach the data it needs
- It is a decision about a person with no human oversight planned
- The task happens rarely, so the build cost never pays back
- The real problem is a policy, an incentive, a missing decision, or a person

The bold question is the one that matters most. If a person has to redo the work to verify it, AI assistance saves little time and adds risk. If verifying takes a minute and producing takes twenty, it is a strong candidate.

## 5. Choose an autonomy level for each AI step

| Level | Name | Who does what | Use when |
|---|---|---|---|
| L0 | Human only | No AI | Judgment, relationships, high-stakes decisions |
| L1 | Suggest | AI offers ideas or information; the person writes | Early trust, high variability |
| L2 | Draft for review | AI drafts; the person edits and sends | **The default starting point** |
| L3 | Act with approval | AI prepares the action; the person approves each one | Repetitive actions with a clear approval moment |
| L4 | Act and report | AI acts on routine cases; the person audits samples and handles exceptions | Only after test and pilot data show it is reliable |

Rules:
- **Start at L2** unless the evidence says otherwise.
- **Promote one level at a time,** and only with evidence: test results, pilot data, and a sample audit.
- **Least agency.** Give each AI step the minimum autonomy and the minimum permissions it needs. A helper that drafts does not need permission to send.
- Anything that reaches a customer, a regulator, or another person outside the team; moves money; or cannot be undone gets at least L3.

## 6. Choose the simplest pattern

Most operations helpers need nothing fancier than the first two patterns.

| Pattern | What it is | Good for |
|---|---|---|
| **Single helper** | One set of instructions plus a context pack and examples | Drafting, summarizing, answering questions from a knowledge base |
| **Chain with checks** | Step A's output feeds step B, with a check in between | Extract fields, validate them, then draft a reply |
| **Router** | Classify the input first, then send it to the right specialized handling | Mixed request types in one inbox |
| **Parallel review** | Several independent checks run at once and results are combined | Contract or policy review against several criteria |
| **Draft and critique** | One pass drafts, another critiques against a rubric, then revise | Writing where quality criteria are clear |
| **Agent with tools** | The model decides which tools to use and in what order | Open-ended, multi-step work that cannot be scripted in advance |

A **workflow** follows predefined steps. An **agent** decides its own steps. Workflows are more predictable, cheaper, and easier to test. Choose an agent only when the path genuinely cannot be written down in advance, and expect to spend more on testing and controls. Many projects branded as agents would be better as a chain with checks.

## 7. Run a taste test

Before investing in the business case, spend thirty minutes checking that the core AI step is plausible:

1. Pick three to five real examples from Step 1, including one hard one.
2. In a tool they already have and are allowed to use, give the AI a rough version of the instructions and the context a new hire would need.
3. Read the outputs like they are wrong. Count the minutes of fixing each one would need.
4. Note what it got right, what it got wrong, and what it needed that it did not have.

This is not the test. It is a feasibility check. If it is hopeless on simple cases, reshape before going further. If it is close, you have learned what the context pack needs.

## 8. Draw the future state

Copy the step table to a future-state version. For each step, record the new actor (`person`, `AI`, `automation`, or a role), the autonomy level for AI steps, the checkpoint, and the new expected touch minutes (including review time). Run:

```bash
python scripts/workflow_map.py current.csv --future future.csv --frequency 400
```

The script shows minutes saved per occurrence and per month. Use those numbers in Step 4, labeled as estimated until Step 5 measures them.

## 9. State the AI fit verdict

One of:
- **Good fit:** AI handles <steps> at <level>, because <reason>.
- **Partial fit:** a process change does most of the work; AI helps with <step>.
- **Not needed:** <the non-AI fix> solves it. Say this plainly and treat it as a success.

## Gate 2

Is there a simpler fix than AI that solves this well enough? If yes, take it. You can still come back for the AI piece once the simpler fix is in place and the remaining problem is clearer.

## Output for the running document

```markdown
## 2. Shape: solution shape

**Redesign (ECRS).** <Steps removed, combined, rearranged, simplified, and why.>

**Ladder rung(s) chosen.** <Rungs and one-line rationale for each.>

**Future-state workflow.** <Mermaid diagram, before and after comparison from workflow_map.py.>

| Step | Actor | Autonomy | Checkpoint |
|---|---|---|---|

**Pattern.** <Single helper / chain / router / ...> because <reason>.

**Taste test.** <Examples tried, what worked, what failed, minutes of fixing.>

**AI fit verdict.** <Good fit / Partial fit / Not needed>, because <reason>.

**Gate 2:** pass / reframed

**What, So What, Now What.**
```
