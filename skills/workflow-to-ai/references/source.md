# Step 3: Source (Prompt)

**Purpose:** decide what to build, what to buy, and what to combine; confirm the helper can reach the data it needs; and set the level of control the risk calls for.

Read [governance.md](governance.md) for risk tiers and controls, and [platforms.md](platforms.md) for what each major platform offers today.

## 1. Start with what they already own

Before anything new, list:

- **Approved AI tools:** which assistants and agent builders the organization has licensed and approved, and for which data (for example, "Copilot is approved for internal data; ChatGPT is not approved for customer data")
- **Core systems:** ERP, HRIS, CRM, ticketing, document management, e-signature, the shared drive
- **Automation tools:** Power Automate, Zapier, Make, n8n, an RPA platform, built-in workflow features of their core systems
- **People:** who in IT, data, security, legal, or procurement needs to be involved, and how long their reviews usually take

Research on enterprise generative AI pilots has found that buying from specialized vendors and working with partners reaches production more often than building in-house from scratch. A licensed assistant configured well beats a custom build that never ships.

## 2. Compare build, buy, and combine

| Option | What it means | Typical fit |
|---|---|---|
| **Configure** | Saved instructions, a shared assistant, or a no-code agent in a tool they already own | Most first helpers. Fastest, cheapest, inherits existing permissions. |
| **Buy** | A vendor product built for this task (an AP automation tool, a contract review product, a recruiting platform feature) | Common, well-defined problems where vendors have invested heavily |
| **Combine** | Owned tools plus light automation plus an AI step, or a vendor product plus custom instructions | Messy real-world workflows that cross systems |
| **Build** | Custom code against model APIs, with engineering support | High volume, unusual requirements, or a core differentiator |

Compare the options that are realistic on:

| Criterion | Question |
|---|---|
| Cost to stand up | Licenses, build hours, setup, training |
| Cost to run | Subscriptions, usage, upkeep hours, review time |
| Time to first working version | Days, weeks, or months? |
| Who maintains it | A named person, IT, a vendor? What happens when they leave? |
| Data access | Can it reach the data it needs with existing permissions? |
| Governance fit | Is it approved for this data and risk tier? |
| Lock-in | How hard is it to switch later? Are the instructions and test set portable? |

Portability tip: keep the helper's instructions, context pack, and test set in plain files the team owns. They move between platforms. Packaging a repeatable procedure as an Agent Skill folder (the open format this skill uses) makes it usable in any platform that supports the standard.

## 3. Map the data

For every piece of information the helper needs:

| Field | Question |
|---|---|
| Item | What information? (invoice status, policy text, employee start date) |
| Source | Which system or document holds the trusted version? |
| Owner | Who is responsible for it? |
| Access path | How will the helper reach it? (connector, export, upload, retrieval index, the person pastes it) |
| Format and quality | Structured or not? Current? Known errors? |
| Sensitivity | Public, internal, confidential, or restricted (see below) |
| Freshness | How current must it be? Real time, daily, quarterly? |

**Sensitivity classes** (use the organization's own scheme if it has one):

- **Public:** published information
- **Internal:** ordinary business information, not for outsiders
- **Confidential:** contracts, pricing, financials, strategy, customer lists
- **Restricted:** personal data, health data, payroll and personnel records, payment card or bank data, privileged legal material, export-controlled or regulated data

Restricted data narrows tool choices sharply. Say so plainly, and route the question to whoever owns data protection.

If the information the helper needs is scattered or unreliable, that is often the real project. Fixing the source of truth (rung 3 on the ladder) may deliver more value than the AI step.

## 4. Assign the risk tier

Use [governance.md](governance.md) to assign low, medium, or high, and copy the required controls into the running document. The tier drives how much testing, review, and sign-off Steps 5 and 6 need.

## 5. Pick a direction

Write:
- The chosen option and platform
- The options considered and why they lost
- **What would change the decision** (for example, "if IT cannot connect the ERP report within two weeks, we fall back to a daily export")

## Gate 3

Can the chosen approach reach the data it needs, inside the rules the organization already has?

- **Pass:** move to Step 4.
- **Data unreachable:** change the access path, narrow the scope to data that is reachable, or make fixing the data source the project.
- **Not approved for this data:** choose an approved tool, remove the sensitive data from scope, or bring in the people who own the rules before continuing.

## Output for the running document

```markdown
## 3. Source: sourcing decision

**Chosen approach.** <Configure / buy / combine / build> on <platform>, because <reason>.

**Options considered.**
| Option | Stand-up cost | Run cost | Time to v1 | Maintainer | Data access | Governance fit | Lock-in |
|---|---|---|---|---|---|---|---|

**Data map.**
| Item | Source | Owner | Access path | Quality | Sensitivity | Freshness |
|---|---|---|---|---|---|---|

**Risk tier.** <Low / medium / high>, because <reason>. Required controls: <list>.

**What would change this decision.** <Trigger and fallback.>

**Gate 3:** pass / reframed

**What, So What, Now What.**
```
