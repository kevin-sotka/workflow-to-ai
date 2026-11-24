# Step 4: Fund (Prompt)

**Purpose:** put honest numbers on the idea so a good idea becomes a funded one, or an honest no, and decide in advance what result counts as success.

## 1. Value

Start from the Step 1 baseline and the Step 2 future-state estimate.

**Time value per month**

```
minutes saved per occurrence = minutes before - minutes after (including new review time)
hours saved per month        = minutes saved x occurrences per month x adoption rate / 60
time value per month         = hours saved per month x loaded hourly rate
```

**Other value per month**
- Errors avoided: (error rate before - error rate after) x occurrences x cost per error
- Revenue effects: faster quotes, fewer lost leads, earlier collections (only with a defensible basis)
- Avoided spend: overtime, temp staff, outsourced work, a hire that is no longer needed

**Loaded hourly rate.** If the person does not know it, a common rule of thumb is annual salary x 1.25 to 1.4, divided by about 2,080 working hours. Label it as assumed. Use the rate of the people whose time is actually saved. An owner's or senior expert's hour is worth more than a junior's.

**Adoption rate.** The share of eligible occurrences where people will really use the helper. It is rarely 100 percent. Conservative cases often use 40 to 60 percent in the first year.

### Capacity is not cash

Hours saved become money only if something changes: overtime stops, a hire is avoided, a contractor is released, or the time is redeployed to work with a value of its own. Otherwise the hours are **capacity**. Capacity is real and worth stating, but never present it as cash savings. In the running document, say which one each line is.

## 2. Cost

**To stand it up (one time)**
- Build time: hours x rate for everyone involved, including the person's own time and any IT, security, or legal review
- Licenses or seats that are new because of this helper
- Integration or connector work
- Training and launch time
- Vendor implementation fees

**To run it (monthly)**
- Subscriptions and usage-based charges (per seat, per message, per credit, per token)
- Upkeep: the owner's time each month, rerunning tests, updating the context pack
- Monitoring and support
- Human review time, unless it is already counted in "minutes after"

Count review time once: either inside "minutes after" (preferred, because it keeps the per-occurrence picture honest) or as a run cost. Not both, and not neither.

## 3. The investment calculator

Fill [../assets/roi-inputs.json](../assets/roi-inputs.json) with three scenarios. Each input can be a plain number or an object with a basis, such as `{"value": 6, "basis": "measured"}`. Then run:

```bash
python scripts/roi_calculator.py roi-inputs.json
```

The script reports, for each scenario:

| Output | Meaning |
|---|---|
| Hours saved per month | After adoption |
| Monthly value | Time value plus other value |
| Setup cost | One time |
| Monthly run cost | Ongoing |
| Net monthly benefit | Value minus run cost |
| Payback period | Months until setup is recovered |
| First-year net | 12 months of net benefit minus setup |
| Three-year net | 36 months of net benefit minus setup |
| Break-even adoption | The adoption rate at which the helper pays for its running cost |
| Input basis | How many inputs are measured, estimated, or assumed |

How to set the scenarios:
- **Conservative:** lower adoption, smaller time savings, higher costs. The case should still hold here.
- **Expected:** the honest best guess.
- **Optimistic:** what happens if it works well and spreads. Never lead the pitch with this one.

Report multi-year figures as multi-year figures. Never relabel a three-year number as a first-year number.

**Sensitivity.** Ask which single input, if wrong, would flip the decision. Usually it is adoption or minutes saved. Name it in the pitch, and plan the test in Step 5 to measure it.

## 4. Success criteria

Set these **before testing**. Thresholds decided after seeing results are not thresholds.

| Kind | Example metric | Example threshold |
|---|---|---|
| **Business** | Minutes per occurrence, turnaround time, cost per transaction, backlog | Median handling time down from 6 to 3 minutes |
| **Quality** | Pass rate on the test set, critical failures, correction rate | 90 percent of test cases pass; zero critical failures |
| **Adoption** | Share of eligible work that goes through the helper, active users | 60 percent of eligible requests within 30 days |
| **Guardrail** | Things that must not get worse | No unreviewed outbound messages; complaints do not rise; no restricted data in unapproved tools |

Include at least one of each. Guardrail metrics are how you prove the helper did not buy speed with risk.

## 5. The pitch

Write it for whoever decides.

**Inside an organization**, for a sponsor or budget owner:
> <Team> spends <time> a month on <task>, and <consequence>. We tested <fix> on <n> real cases and it <result>. In the conservative case it pays back in <months> and saves <capacity or cash> a year, at a cost of <setup> plus <run> a month. We are asking for <decision> to run a <length> pilot, judged on <thresholds>.

**In a small business**, for the owner's own go or no-go:
> This costs me about <time and money> a month today. The fix costs <setup> and <run> a month. If it works as tested, I get back <hours> a month, which I will use for <what>. If it does not hit <threshold> in <weeks>, I stop.

## Gate 4

Does value clear cost in the **conservative** case, or is there a non-financial reason (risk, compliance, wellbeing, customer experience) strong enough to justify it on its own?

- **Pass:** move to Step 5.
- **Not yet:** drop a rung on the ladder (cheaper fix), narrow the scope to the highest-volume slice, widen it to a larger slice of the same problem, or find the input that flips the decision and test that first.

## Output for the running document

```markdown
## 4. Fund: business case

**Value model.** <Formula with the inputs, each labeled measured / estimated / assumed.>

**Three scenarios.** <Table from roi_calculator.py.>

**Cash or capacity.** <Which lines are cash, which are capacity, and what the capacity will be used for.>

**The input that would flip the decision.** <Input, and how Step 5 will measure it.>

**Success criteria.**
| Kind | Metric | Baseline | Threshold | How measured |
|---|---|---|---|---|

**Pitch.** <One paragraph.>

**Gate 4:** pass / reframed

**What, So What, Now What.**
```
