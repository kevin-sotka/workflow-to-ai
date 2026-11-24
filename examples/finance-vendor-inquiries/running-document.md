# Vendor payment inquiries: Workflow to AI

*Illustrative example. The company, people, and numbers are fictional, built to show what a finished running document looks like. The raw files and script outputs are in this folder.*

**Owner:** AP team lead, a 300-person distribution company
**Setting:** Inside an organization
**Function:** Finance (accounts payable)
**Decision maker:** Controller
**Mode:** Full build
**Status:** Step 6 of 6, Prove. Gates: 1 pass, 2 pass, 3 pass, 4 pass, 5 pass (v0.3), 6 pass
**Last updated:** example

## Summary

**What:** Vendors email the AP inbox about 420 times a month asking when they will be paid. Each one takes about 8.5 hands-on minutes, nearly half of it looking things up and copying them. The supplier portal already shows payment status, but vendors were never told about it.

**So what:** About 60 hours a month of a three-person team's time goes to answering a question a report already answers. Mistakes (quoting the wrong invoice, giving dates for held invoices) create more emails and occasional duplicate-payment risk.

**Now what:** Pilot is complete and met its thresholds. Roll out to the full AP team on the 1st, with the monthly review on the first Monday.

## 1. Find: problem and baseline

**Problem statement.** The AP team answers about 420 vendor "where is my payment" emails a month from a shared inbox. Each needs the specialist to find the right invoice (vendors often quote remittance or PO numbers), check three ERP screens, sometimes chase a buyer about a hold, and write a reply. Only the AP lead knows the dispute rules.

**Current workflow.** See `outputs-workflow-map.md`. 8 steps, 8.5 touch minutes and 48 average waiting minutes per inquiry, 59.5 hands-on hours a month. Underlined (copying) time is 47 percent of the total; circled (judgment) time is 12 percent.

**Circled steps:** S8 handle disputes. **Underlined steps:** S2 find numbers, S3 look up invoice, S4 check status, S7 log.

**Candidates considered.** Five AP pain points scored (`outputs-scorecard.md`). Vendor payment inquiries ranked first (quick win, priority 18.0). Vendor bank detail changes scored high on value but 5 on risk; kept human by design. "Improve vendor onboarding" failed Gate 1 as stated (too broad).

**Root cause.** Vendors ask because they cannot see status. They cannot see status because nobody told them the portal shows it. When they do ask, the answer takes long because the hold reason lives in a separate screen and sometimes only in a buyer's head.

**Baseline.**
| Dimension | Today | Basis |
|---|---|---|
| Money | About 60 hours a month at a $40 loaded rate | measured hours, assumed rate |
| Time (whose) | AP specialists 88 percent, AP lead 12 percent | measured (timed 12 instances) |
| Wellbeing | Inbox backlog on Mondays; specialists stay late at month end | person's account |
| Error rate | About 1 in 25 replies quotes the wrong invoice or a date for a held invoice | estimated from last month's follow-ups |
| External risk | Vendor relations; duplicate payments when vendors resend invoices | estimated |

**Examples collected:** 42 real emails from the last two months, vendor names redacted.

**Gate 1:** pass

## 2. Shape: solution shape

**Redesign.** Eliminate: S7 manual logging (the mail flow can log). Rearrange: add the hold reason to the status report so S5 (chasing the buyer) disappears for most holds. Simplify: an auto-acknowledgment with the supplier portal link.

**Ladder rungs.** Rung 2 (portal link, a feature already owned), rung 3 (hold reason in one report), rung 4 (logging and lookup as automation), rung 5 (AI extracts numbers and drafts replies, specialist reviews).

**Future-state workflow.** See `outputs-workflow-map.md`. Touch time drops from 8.5 to 2.5 minutes (estimated), waiting from 48 to 0.

| Step | Actor | Autonomy | Checkpoint |
|---|---|---|---|
| F2 Extract numbers | AI helper | L2 | Format rule check |
| F4 Draft reply | AI helper | L2 | Specialist reviews every draft |
| F5 Review and send | AP specialist | n/a | Reviewer checklist |
| F6 Disputes | AP lead | n/a | Human decision |

**Pattern.** Chain with checks: extract, validate against number formats, deterministic lookup, draft, human review. No agent needed: the path is the same every time.

**Taste test.** Five emails in Copilot Chat with a rough prompt: three good drafts, one used a remittance number as the invoice number, one gave a date for a held invoice. Fixing took 1 to 5 minutes. Plausible, and the context pack needs the number formats.

**AI fit verdict.** Partial fit. The portal link and report change do a large share of the work. AI earns its place on reading messy emails and drafting replies, where checking (about a minute) is much faster than producing (about five).

**Gate 2:** pass

## 3. Source: sourcing decision

**Chosen approach.** Combine: Microsoft 365 Copilot agent (already licensed and approved for internal financial data) plus a Power Automate flow and an ERP saved report.

**Options considered.** A dedicated AP automation product was quoted at a much higher annual cost and a three-month implementation; kept on file for the invoice exception use case. A custom build was ruled out: no engineering capacity, and no need.

**Data map.**
| Item | Source | Owner | Access path | Quality | Sensitivity | Freshness |
|---|---|---|---|---|---|---|
| Invoice status and dates | ERP | AP lead | Saved report via flow | Good | Confidential | Daily refresh |
| Hold reason | ERP | Purchasing | Added to report | New field | Confidential | Daily |
| Vendor email | Shared inbox | AP | Flow trigger | Messy | Confidential; external content | Real time |

**Risk tier.** Medium: shared helper, confidential data, external content (prompt injection risk), outputs reach vendors after review. Controls: owner and backup, test set and thresholds, existing permissions, reviewer checklist, change log, injection cases in the test set.

**What would change this decision.** If IT cannot publish the saved report within two weeks, fall back to a daily export the flow reads.

**Gate 3:** pass

## 4. Fund: business case

**Three scenarios.** See `outputs-roi.md`. Conservative: payback 8.8 months, first-year net $1,900, three-year net $16,300. Expected: payback 2.7 months, first-year net $13,140. Fewer emails from the portal link are counted as other value.

**Cash or capacity.** Capacity. About 17 to 28 hours a month come back to the team. The controller has agreed they go to the month-end close, which currently runs late.

**The input that would flip the decision.** Minutes after (including review). Step 5 measures it.

**Success criteria.**
| Kind | Metric | Baseline | Threshold | How measured |
|---|---|---|---|---|
| Business | Median hands-on minutes per inquiry | 8.5 | 3.5 or less | Timed sample, 20 per week |
| Quality | Test set runs passing critical checks | n/a | 90 percent, 100 percent on escalate and adversarial | eval_report.py |
| Adoption | Share of inquiries drafted by the helper | 0 | 60 percent in 30 days | Flow run count |
| Guardrail | Replies sent without review; bank or address changes acknowledged | 0 | 0 | Audit of sent items |

**Pitch.** The AP team spends about 60 hours a month answering "where is my payment" emails. We tested a reviewed-draft helper plus two process changes on 30 real emails, and it met every quality threshold. In the conservative case it pays back in under nine months and gives the team back 17 hours a month for close, at a setup cost of $5,300 and $360 a month. We are asking for a four-week pilot with two specialists.

**Gate 4:** pass

## 5. Build and Test

### Build
**Helper:** vendor payment inquiry helper, v0.3, Microsoft 365 Copilot agent plus Power Automate. Files in `helper/`.
**Context pack:** number formats, hold reason glossary, reply rules, five example replies. Left out: the full vendor master file (not needed; the report carries what is needed).
**Tools and permissions:** read-only report access; drafts only, no send permission.

### Test
**Test set:** 30 cases (15 typical, 6 hard, 4 edge, 3 escalate, 2 adversarial). Sample in `helper/tests/`.
**Results.** v0.1: 77 percent passing, thresholds not met (`outputs-eval-v0.1.md`). v0.3: 100 percent of runs pass critical checks, all thresholds met (`outputs-eval-v0.3.md`).
**Judge calibration.** On v0.1 outputs, judge and expert agreed on 95 percent of "correct" grades (kappa 0.86).

**Failure modes and fixes.**
| Mode | Count (v0.1) | Cause | Fix | Result |
|---|---|---|---|---|
| Wrong number used as invoice number | 3 | Number formats not in context | Added formats and cross-reference step | Fixed in v0.2 |
| Date given for a held invoice | 1 | No rule for holds | Rule plus reason | Fixed in v0.2 |
| Replied to a legal threat | 1 | Escalation list incomplete | Added legal language | Fixed in v0.2 |
| Followed an injected instruction | 1 | No untrusted-content rule | Rule, escalation, never confirm bank changes | Fixed in v0.3 |
| Missed second question in a thread | 1 | Long threads | Rule plus reviewer line | Improved; on checklist |

**Red team.** Hidden instructions in emails, bank change requests, a request for another vendor's status, missing invoice numbers. All handled in v0.3.

**Pilot.** Hypothesis: if two specialists use the helper for four weeks, median hands-on minutes per inquiry fall from 8.5 to 3.5 or less, with zero unreviewed sends. Result: median 3.0 minutes, 71 percent adoption, zero guardrail breaches, three new edge cases added to the test set.

**Gate 5:** pass

## 6. Prove: impact plan

**Launch plan.** Full AP team on the 1st. Fifteen-minute training: one live case, the reviewer checklist, how to escalate. Champion: the pilot specialist.

**Scoreboard.** Median minutes per inquiry, test set pass rate, correction rate, adoption, guardrail breaches, inquiry volume (to track the portal effect).

**Owner and backup.** AP team lead; senior AP specialist. **Monthly review:** first Monday. **Retirement criteria:** inquiry volume falls below 100 a month, or the ERP vendor adds an equivalent feature.

**New process.** SOP updated, including the dispute rules that only the AP lead knew.

**30 / 60 / 90 days.** 30: adoption and quality. 60: decide whether to extend to the "Scheduled" case at L3 (send after one-click approval). 90: report capacity used for close.

**Gate 6:** pass

**Three-sentence summary.** Vendors were emailing us 420 times a month for payment status that our portal already shows. We told them about the portal, put the hold reason in one report, and added a helper that drafts replies a specialist approves in about a minute. Hands-on time per inquiry fell from 8.5 to 3 minutes in the pilot, with no quality incidents, and the hours now go to month-end close.

**Next action.** AP team lead reruns the test set and brings the scoreboard to the controller on the first Monday of next month.

## Assumptions to confirm

1. Loaded hourly rate of $40 (assumed from typical AP salaries; finance to confirm).
2. Portal link reduces inquiry volume by 15 to 30 percent (estimated; track for 60 days).

## Reframes

| Date | Gate | What did not pass | How we reframed |
|---|---|---|---|
| Week 1 | Gate 1 | "Improve vendor onboarding" was too broad | Parked; revisit as a narrower slice later |
| Week 3 | Gate 5 | v0.1 missed thresholds | Fixed top failure modes in v0.2 and v0.3 |
