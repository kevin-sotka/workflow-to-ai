## Workflow map: Vendor payment inquiries

### Current state

```mermaid
%% Vendor payment inquiries
flowchart TD
    S1["S1: Read the inquiry email<br/><small>AP specialist · Shared inbox · 1 min</small>"]
    S2["S2: Find vendor and invoice number<br/><small>AP specialist · Shared inbox · 1 min</small>"]
    S3["S3: Look up the invoice in the ERP<br/><small>AP specialist · ERP · 1.5 min</small>"]
    S4["S4: Check payment status and holds<br/><small>AP specialist · ERP · 1 min</small>"]
    S5>"S5: Ask the buyer about a hold<br/><small>AP specialist · Teams · 0.5 min</small>"]
    S6["S6: Write the reply<br/><small>AP specialist · Shared inbox · 2 min</small>"]
    S7["S7: Log the inquiry in the tracker<br/><small>AP specialist · Excel · 0.5 min</small>"]
    S8(("S8: Handle disputes and exceptions<br/><small>AP lead · Shared inbox · 1 min</small>"))
    S1 --> S2
    S2 --> S3
    S3 --> S4
    S4 --> S5
    S5 --> S6
    S6 --> S7
    S7 --> S8
    classDef circled fill:#fde68a,stroke:#92400e,stroke-width:2px
    classDef underlined fill:#dbeafe,stroke:#1e3a8a,stroke-dasharray: 4 2
    classDef waiting fill:#f3f4f6,stroke:#6b7280
    class S2 underlined
    class S3 underlined
    class S4 underlined
    class S5 waiting
    class S7 underlined
    class S8 circled
```

Legend: rounded and yellow = circled (judgment, approval, communication, stays human); dashed blue = underlined (copy, lookup, transform, hand over first); grey = waiting.

### Current state: summary

| Measure | Value |
|---|---|
| Steps | 8 |
| Hands-on (touch) minutes per occurrence | 8.5 |
| Waiting minutes per occurrence | 48 |
| Cycle time per occurrence (touch + wait) | 56.5 min |
| Handoffs between people | 1 |
| Steps done by AI or automation | 0 |
| Hands-on hours per month | 59.5 |

**Where the hands-on time goes, by step type**

| Step type | Minutes | Share | Group |
|---|---|---|---|
| copy | 0.5 | 6% | underlined |
| lookup | 2.5 | 29% | underlined |
| transform | 1 | 12% | underlined |
| language | 3 | 35% |  |
| judgment | 1 | 12% | circled |
| wait | 0.5 | 6% |  |

Underlined (copying) time: 4 min (47%). Circled (judgment) time: 1 min (12%).

**Hands-on minutes by role**

| Role | Minutes | Share |
|---|---|---|
| AP specialist | 7.5 | 88% |
| AP lead | 1 | 12% |

**Single points of knowledge:** S8 (Handle disputes and exceptions)

**Error-prone steps:** S2 (Find vendor and invoice number), S4 (Check payment status and holds)

**Most painful steps:** S5 (Ask the buyer about a hold, pain 3), S2 (Find vendor and invoice number, pain 2), S3 (Look up the invoice in the ERP, pain 2)

### Future state

```mermaid
%% Vendor payment inquiries (future)
flowchart TD
    F1["F1: Auto-reply with supplier portal link<br/><small>Automation · Mail flow · 0 min</small>"]
    F2["F2: Extract vendor and invoice number<br/><small>AI helper · Copilot agent · 0 min · L2</small>"]
    F3["F3: Look up status and holds<br/><small>Automation · ERP saved report · 0 min</small>"]
    F4["F4: Draft the reply with sources<br/><small>AI helper · Copilot agent · 0 min · L2</small>"]
    F5(("F5: Review and send<br/><small>AP specialist · Shared inbox · 1.5 min</small>"))
    F6(("F6: Handle disputes and exceptions<br/><small>AP lead · Shared inbox · 1 min</small>"))
    F7["F7: Log the inquiry<br/><small>Automation · Tracker · 0 min</small>"]
    F1 --> F2
    F2 --> F3
    F3 --> F4
    F4 --> F5
    F5 --> F6
    F6 --> F7
    classDef circled fill:#fde68a,stroke:#92400e,stroke-width:2px
    classDef underlined fill:#dbeafe,stroke:#1e3a8a,stroke-dasharray: 4 2
    classDef waiting fill:#f3f4f6,stroke:#6b7280
    class F1 underlined
    class F2 underlined
    class F3 underlined
    class F5 circled
    class F6 circled
    class F7 underlined
```

Legend: rounded and yellow = circled (judgment, approval, communication, stays human); dashed blue = underlined (copy, lookup, transform, hand over first); grey = waiting.

### Future state: summary

| Measure | Value |
|---|---|
| Steps | 7 |
| Hands-on (touch) minutes per occurrence | 2.5 |
| Waiting minutes per occurrence | 0 |
| Cycle time per occurrence (touch + wait) | 2.5 min |
| Handoffs between people | 1 |
| Steps done by AI or automation | 5 |
| Hands-on hours per month | 17.5 |

**Where the hands-on time goes, by step type**

| Step type | Minutes | Share | Group |
|---|---|---|---|
| judgment | 1 | 40% | circled |
| approval | 1.5 | 60% | circled |

Underlined (copying) time: 0 min (0%). Circled (judgment) time: 2.5 min (100%).

**Hands-on minutes by role**

| Role | Minutes | Share |
|---|---|---|
| Automation | 0 | 0% |
| AI helper | 0 | 0% |
| AP specialist | 1.5 | 60% |
| AP lead | 1 | 40% |

**Most painful steps:** F6 (Handle disputes and exceptions, pain 1)

### Before and after

| Measure | Current | Future | Change |
|---|---|---|---|
| Steps | 8 | 7 | -1 |
| Touch minutes per occurrence | 8.5 | 2.5 | -6 |
| Wait minutes per occurrence | 48 | 0 | -48 |
| Handoffs between people | 1 | 1 | +0 |
| Steps done by AI or automation | 0 | 5 | +5 |
| Hands-on hours per month | 59.5 | 17.5 | -42.0 |

These future-state minutes are estimates until Step 5 measures them. Make sure future touch minutes include the time a person spends reviewing AI output.
