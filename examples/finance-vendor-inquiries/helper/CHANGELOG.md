# Changelog: vendor payment inquiry helper

## v0.3
- Added a rule to answer or route every question in a thread, and a line in the reviewer output listing other questions. (Failure mode: missed second question.)
- Added escalation for any instruction aimed at the assistant inside a vendor email, and the rule to never confirm bank or address changes. (Failure mode: followed injected instruction, case T29.)
- Result: all 30 cases pass critical checks; all thresholds met. One non-critical miss remains (T23, long thread), now on the reviewer checklist. Pilot approved.

## v0.2
- Added the number formats to the context and the cross-reference step for REM- and PO- numbers. (Failure mode: wrong number used as invoice number, 3 of 7 failures.)
- Added the rule never to give a date for an invoice on hold, with the reason. Added legal language to the escalation list.
- Result: 90 percent pass; the adversarial case still failed.

## v0.1
- First version, built from 12 examples. 77 percent of runs passed critical checks. Thresholds not met.
