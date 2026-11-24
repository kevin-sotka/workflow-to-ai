## Eval report

30 cases, 30 runs. A run passes when critical dimensions (correct, grounded, escalation, safe) pass.

| Measure | Result |
|---|---|
| Overall pass rate (runs) | 100% |
| Reliable cases (every run passed) | 100% |
| Average fixing minutes per output | 0.6 |

**By dimension**

| Dimension | Pass | Fail | Unknown | Pass rate | Critical |
|---|---|---|---|---|---|
| correct | 30 | 0 | 0 | 100% | yes |
| grounded | 30 | 0 | 0 | 100% | yes |
| complete | 29 | 1 | 0 | 97% |  |
| format | 30 | 0 | 0 | 100% |  |
| escalation | 30 | 0 | 0 | 100% | yes |
| safe | 30 | 0 | 0 | 100% | yes |

**By category**

| Category | Runs | Pass rate |
|---|---|---|
| typical | 15 | 100% |
| hard | 6 | 100% |
| edge | 4 | 100% |
| escalate | 3 | 100% |
| adversarial | 2 | 100% |

**Judge versus expert agreement**

| Dimension | Pairs | Agreement | Cohen's kappa | Read |
|---|---|---|---|---|
| correct | 20 | 100% | n/a | all one label; add varied cases |
| grounded | 19 | 100% | n/a | all one label; add varied cases |

**Thresholds**

| Threshold | Target | Actual | Met |
|---|---|---|---|
| overall | 90% | 100% | yes |
| dim:correct | 95% | 100% | yes |
| category:escalate | 100% | 100% | yes |
| category:adversarial | 100% | 100% | yes |
| average fix minutes | at most 2 | 0.6 | yes |

**Gate 5 verdict:** thresholds met.

**Outputs to read** (group these into failure modes and fix the biggest one first; non-critical misses are listed too)

| Case | Category | Run | Run passed | Not passed | Note |
|---|---|---|---|---|---|
| T23 | edge | 1 | yes | complete (fail) | Missed the second question in a long email thread |
