# Platforms: where helpers get built

*Checked November 2026. These products change monthly, sometimes weekly. Use this page to orient, then confirm the current vendor documentation before giving setup steps or promising a feature. What the organization has licensed and approved matters more than what any platform can do in principle.*

## Choose by the job, then by what they own

| The job | Usually the right kind of tool |
|---|---|
| A personal helper that drafts, summarizes, or rewrites with saved instructions | Saved instructions or a personal assistant: a Gem, a custom GPT or Project, a Claude Project or skill, a Copilot agent for one person |
| A team helper that answers questions from the team's documents | A shared assistant grounded in a document library: Microsoft 365 Agent Builder or a SharePoint agent, a shared Gem or Gemini Enterprise agent, a shared ChatGPT Project or workspace agent, a shared Claude Project |
| A multi-step process across systems, with triggers and approvals | An agent or workflow builder: Copilot Studio, Gemini Enterprise Agent Designer, ChatGPT workspace agents, or an automation platform with an AI step |
| Moving data between systems on a schedule, by fixed rules | Rules-based automation: Power Automate, Zapier, Make, n8n, an RPA platform, or built-in workflow features of the core system. No model needed. |
| High volume, customer-facing, or deeply integrated | An engineered build by IT with model APIs and agent SDKs, with full testing and monitoring |

Start with the tool the organization already pays for and has approved for the data involved.

## Microsoft 365

- **Microsoft 365 Copilot Chat** for individual drafting and summarizing.
- **Agent Builder** inside Microsoft 365 Copilot: no-code agents (also called declarative agents) grounded in SharePoint, files, and Microsoft Graph content. They follow existing Microsoft 365 permissions and data policies. A good first home for a team knowledge helper. Agents built here can be copied into Copilot Studio if they outgrow it.
- **SharePoint agents** for helpers scoped to a site or document library.
- **Copilot Studio**: the fuller low-code platform for multi-step agents with topics, tools, actions, triggers, and publishing to Teams and other channels. Licensed through Power Platform.
- **Power Automate** for deterministic flows, and for chaining an AI step into a rules-based process.
- **Microsoft 365 Agents Toolkit** for developers building agents in code.
- **Microsoft Agent 365** for governance, identity, and observability once an organization has many agents.

## Google Workspace and Google Cloud

- **Gemini in Workspace** (Gmail, Docs, Sheets, Drive) for in-place drafting and summarizing.
- **Gems** for reusable personal instructions.
- **Gemini Enterprise app** with **Agent Designer**: no-code agents built with natural language or a visual editor, including schedule- or trigger-based agents with human-in-the-loop approval checkpoints, connected to Workspace, Microsoft 365, and other business systems.
- **Workspace Studio** for building no-code agents inside Google Workspace.
- **Gemini Enterprise Agent Platform** (the evolution of Vertex AI) and the Agent Development Kit for engineering teams.

## OpenAI

- **ChatGPT Projects** and **custom GPTs** for saved instructions and files.
- **Workspace agents** in ChatGPT Business, Enterprise, and Edu: shared agents that follow team processes, connect to tools, ask for approval, run in the cloud, and can work in ChatGPT and Slack. OpenAI describes them as the evolution of GPTs.
- **Agents SDK** for developers.
- Note: OpenAI announced it is winding down the visual Agent Builder and the hosted Evals product, with both unavailable on the platform from 30 November 2026. Do not start new work there. Workspace agents (no-code) and the Agents SDK (code) are the recommended routes.

## Anthropic

- **Claude Projects** for shared instructions and a knowledge base.
- **Skills** in the Agent Skills format (this skill is one), usable across Claude's apps and in Claude Code, and portable to other platforms that support the standard.
- **Connectors** to business tools through the Model Context Protocol, plus Claude inside Microsoft 365, Google Workspace, and Slack where the organization has enabled them.
- **Claude Code** and the **Agent SDK** for developers building agents in code.

## Cross-platform standards worth knowing

- **Agent Skills** (agentskills.io): an open format for packaging instructions, references, and scripts as a folder with a `SKILL.md`. Originally developed by Anthropic and now adopted by dozens of agent products, including ChatGPT, GitHub Copilot, VS Code, and Cursor. Packaging a helper as a skill keeps it portable.
- **Model Context Protocol (MCP)**: an open standard for connecting AI assistants to tools and data, now hosted by the Agentic AI Foundation at the Linux Foundation alongside AGENTS.md. Many connectors across platforms use it.
- **Plain files.** Whatever the platform, keep the instructions, context pack, and test set in files the team owns. That is the most portable format of all.

## Automation platforms

Power Automate, Zapier, Make, n8n, and RPA platforms (UiPath, Automation Anywhere, and others) are often the right home for the deterministic parts of a workflow, with an AI step for the language-heavy part. A common, reliable shape: trigger, then extract with AI, then validate with rules, then a human approves, then the automation writes to the system of record.

## Questions to ask before choosing

1. Is the tool approved for the data this helper will touch?
2. Does it inherit the users' existing permissions, or does it need its own access?
3. Can it reach the data source, through an approved connector?
4. Can a person approve actions before they happen?
5. Does it log what the helper did?
6. Who can edit the helper, and is there version history?
7. What does it cost at the expected volume (seats, messages, credits, usage)?
8. Can the instructions and test set be exported if we switch?
