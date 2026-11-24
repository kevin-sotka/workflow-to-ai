# Worked example: vendor payment inquiries (finance)

*Illustrative. The company, people, and numbers are fictional. Use this as a model of the depth and tone each step should reach, not as a template to copy. The full set of files for this example lives in the `examples/` folder of the skill's GitHub repository.*

## The starting point

An accounts payable team lead at a 300-person distribution company says: "We drown in vendor emails asking when they'll get paid. Can AI answer them?"

## Step 1: Find

- **Last real instance:** the lead walks through yesterday's email from a fastener supplier. Eight steps: read it, figure out which invoice they mean (they quoted a remittance number), three ERP screens, a Teams message to a buyer about a hold, a reply, a tracker row. The AP lead alone handles disputes.
- **Map stats:** 8.5 touch minutes and 48 average waiting minutes per inquiry, 420 a month, about 60 hands-on hours. 47 percent of the time is underlined (copying and lookup); 12 percent is circled (judgment).
- **Funnel:** five AP pain points scored. Vendor inquiries come out as a quick win. Vendor bank detail changes score high on value and 5 on risk: a known fraud target, deliberately kept human.
- **Why chain:** vendors ask because they cannot see status; they cannot see it because nobody told them the supplier portal shows it.
- **Examples collected:** 42 real emails, redacted.

## Step 2: Shape

- **ECRS** removes the manual tracker step, moves the hold reason into the status report (the buyer chase disappears for most cases), and adds an auto-reply with the portal link.
- **Ladder:** rungs 2, 3, and 4 do much of the work. AI (rung 5) handles the messy part: reading the email, finding the right number, drafting the reply.
- **Fit test:** checking a draft takes about a minute; writing one takes about five. Strong fit for draft-for-review (L2).
- **Pattern:** a chain with checks (extract, validate number format, deterministic lookup, draft, human review). Not an agent, because the path never changes.
- **Taste test:** five emails, three good drafts, two instructive failures (remittance number confusion, a date given for a held invoice).
- **Verdict:** partial fit. Process changes plus a reviewed drafting helper.

## Step 3: Source

- Combine owned tools: the licensed Copilot agent builder (approved for internal financial data), an automation flow, and a new ERP saved report. A specialist AP product was priced and parked for a harder use case.
- **Risk tier:** medium (shared helper, confidential data, external content that could carry prompt injection, outputs reach vendors after review).

## Step 4: Fund

- Conservative case: 340 inquiries after deflection, 5 minutes saved each including review, 60 percent adoption, $40 loaded rate (assumed), $5,300 setup, $360 a month to run. Payback 8.8 months; three-year net about $16,300.
- **Capacity, not cash:** the controller agrees the hours go to month-end close.
- **Thresholds set before testing:** 90 percent of runs pass critical checks, 100 percent on escalate and adversarial cases, median 3.5 minutes or less, zero unreviewed sends.

## Step 5: Build and Test

- **Build kit:** helper card, instructions (role, context, task, format, constraints, escalation, out of scope), context pack with number formats and five example replies, reviewer checklist, setup steps, changelog.
- **Test set:** 30 cases: 15 typical, 6 hard, 4 edge, 3 escalate, 2 adversarial (including an email with a hidden instruction to "confirm our new bank account").
- **v0.1:** 77 percent pass. Failure modes: wrong number used as invoice number (3), date for a held invoice (1), replied to a legal threat (1), followed the injected instruction (1), vendor name misspelled (1).
- **Fixes, one at a time:** number formats in the context; a rule (with its reason) never to date a held invoice; legal language on the escalation list; an untrusted-content rule and "never confirm bank changes."
- **v0.3:** every run passes critical checks; one non-critical miss (a second question buried in a long thread) goes on the reviewer checklist.
- **Judge calibration:** judge and expert agree on 95 percent of correctness grades (kappa 0.86).
- **Pilot:** four weeks, two specialists. Median 3.0 minutes per inquiry, 71 percent adoption, zero guardrail breaches.

## Step 6: Prove

- Staged rollout, fifteen-minute training, a champion from the pilot.
- Scoreboard with baseline, target, source, frequency, and owner. Monthly test set rerun.
- SOP updated, including the dispute rules only the AP lead knew. The single point of knowledge from Step 1 is gone.
- At 60 days: decide whether "Scheduled" replies can move to L3 (send after one-click approval), based on correction-rate evidence.

**Three-sentence summary:** Vendors were emailing us 420 times a month for payment status our portal already shows. We told them about the portal, put the hold reason in one report, and added a helper that drafts replies a specialist approves in about a minute. Hands-on time per inquiry fell from 8.5 to 3 minutes in the pilot, with no quality incidents, and the hours now go to month-end close.

## What to notice

- The biggest single win (the portal link) was not AI.
- The helper is a chain with checks at draft-for-review, not an autonomous agent.
- The adversarial test case caught a real fraud pattern before launch.
- Every number in the case says whether it is measured, estimated, or assumed.
