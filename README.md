# Workflow to AI

**A Meatbag Method skill for turning a workflow pain point into a working, tested AI helper.**

You describe the part of your week that is broken. The skill walks you, step by step, from that frustration to three things you can hold:

1. **A working helper** (an assistant, agent, skill, or automation) built on tools you already own, and tested on your own real cases
2. **An honest business case** with conservative, expected, and optimistic numbers, each labeled as measured, estimated, or assumed
3. **A plan that keeps it alive:** an owner, a scoreboard, a review rhythm, and a written process so nobody is a single point of knowledge

Sometimes the honest answer is that the fix is not AI. The skill treats that as a win.

It is written for operations people: HR, finance, procurement, supply chain, sales, marketing, customer service, legal, government affairs, IT, and anyone else whose work runs on email, documents, spreadsheets, and systems of record. You do not need to be technical.

## Why it works this way

Most AI pilots stall. The pattern behind the ones that pay off is consistent:

- **Redesign the work before adding AI.** McKinsey's research on AI high performers finds they fundamentally redesign workflows rather than insert AI into existing ones, and that this is one of the strongest contributors to real business impact.
- **Integrate into the real workflow, or it stays a demo.** MIT's NANDA study of enterprise generative AI found that most pilots stall with no measurable P&L impact, and pointed to brittle workflows and poor integration as recurring reasons.
- **Prefer the simplest thing that works.** Anthropic's guidance on building agents recommends the simplest solution possible, sometimes no agentic system at all. Gartner expects over 40 percent of agentic AI projects to be canceled by the end of 2027 because of costs, unclear value, or weak risk controls.
- **Test like you mean it.** Evals (tests on real cases, graded consistently) are what separate a helper people trust from one they quietly stop using.

So the skill makes you map before you move, climb a ladder of fixes from the bottom, keep a person accountable for every output, and decide what good looks like before you test.

## The method at a glance

Six gated steps. Inside them sit the four moves of the Meatbag Method: **Pick** one specific thing, **Prompt** it with everything a new hire would need, **Prune** what comes back until it is right, and give it a **Ritual** so it keeps happening.

| Step | Move | What you do | What you leave with |
|---|---|---|---|
| 1. Find | Pick | Map the last real instance of the work, score your pain points, set a baseline, collect real examples | Problem statement, current-state map, baseline |
| 2. Shape | Pick | Eliminate, combine, rearrange, simplify; circle the judgment, underline the copying; climb the ladder of fixes; choose an autonomy level; run a 30-minute taste test | Future-state map, AI fit verdict |
| 3. Source | Prompt | Build, buy, or combine; map the data; assign a risk tier | Sourcing decision, data map, controls |
| 4. Fund | Prompt | Three-scenario business case; success thresholds set before testing | Business case and pitch |
| 5. Build and Test | Prompt, Prune | Build the real helper; test it on 20 to 50 real cases; read every failure; red team; pilot | Helper files, test results, failure log |
| 6. Prove | Ritual | Staged launch, scoreboard, owner, monthly review, written process | Impact plan, build brief |

Every step ends with a gate. A failed gate means reframe, not kill.

## What is inside

```
skills/workflow-to-ai/
├── SKILL.md                 # the method the agent follows
├── references/              # loaded only when a step needs it
│   ├── find.md  shape.md  source.md  fund.md  build.md  test.md  prove.md
│   ├── governance.md        # risk tiers, regulation landmarks, security checks
│   ├── platforms.md         # Microsoft 365, Google, OpenAI, Anthropic, automation tools
│   ├── functions.md         # playbooks for ten operations functions
│   ├── facilitation.md      # running the method with a team or cohort
│   └── worked-example.md    # a complete illustrative run
├── assets/                  # templates: running document, step table, scorecard,
│                            # ROI inputs, helper card, helper instructions,
│                            # eval set, judge prompt, build brief
└── scripts/                 # standard-library Python, no installs
    ├── workflow_map.py      # step table to diagram and time analysis
    ├── score_opportunities.py  # rank pain points, value versus complexity
    ├── roi_calculator.py    # three scenarios, payback, break-even adoption
    └── eval_report.py       # pass rates, thresholds, judge agreement
examples/finance-vendor-inquiries/   # every artifact from the worked example
```

The skill follows the open [Agent Skills](https://agentskills.io) format, so it works in Claude and in the many other agent products that support the standard.

## Install

### Claude (web, desktop, mobile)

1. Download `workflow-to-ai.zip` from this repository's [Releases](../../releases) page.
2. In Claude, open **Settings**, find the **Skills** section, and upload the zip.
3. Start a conversation with something like the prompts below.

### Claude Code

As a plugin:

```
/plugin marketplace add kevin-sotka/workflow-to-ai
/plugin install workflow-to-ai@meatbag-method
```

Or as a personal skill:

```bash
git clone https://github.com/kevin-sotka/workflow-to-ai.git
cp -r workflow-to-ai/skills/workflow-to-ai ~/.claude/skills/
```

### Other agents that support Agent Skills

Copy the `skills/workflow-to-ai` folder into the skills directory your agent reads from (check its documentation for the location). The folder is self-contained.

### No agent at all

The reference files are a readable playbook, and the templates work in any spreadsheet or document tool. The scripts need only Python 3.9 or later.

## Try it

- "Our HR team answers the same benefits questions all day. Can AI help?"
- "I spend every Monday building the same status report from three spreadsheets. Walk me through fixing that."
- "We have twelve AI ideas from our finance team. Help us pick which one to do first."
- "We built a Copilot agent for contract review and nobody uses it. What is wrong?"
- "I'm running an AI workshop for our supply chain team next month. Help me plan it."
- "Write the business case for using AI to draft RFQs."

The skill will ask which mode fits (quick pass, full build, portfolio, check-up, or facilitator), set up a running document, and take it one step at a time.

## A note on data and safety

The skill tells the agent to keep sensitive data inside tools your organization has approved, to keep a named person accountable for every output, and to treat decisions about people (hiring, performance, pay, credit) as high risk that needs legal, HR, or compliance review. It includes orientation on the EU AI Act timeline, the NIST AI Risk Management Framework, ISO/IEC 42001, and the OWASP Top 10 lists for LLM and agentic applications. That orientation is not legal advice. Platform features change monthly, so the skill tells the agent to confirm current vendor documentation before promising a feature.

## About

Written by **Kevin Sotka** as part of **The Meatbag Method**, a plain-language way of teaching AI to people who are not technical, from [Meatbag Made](https://meatbagmade.com/method/).

The method comes from AI enablement programs I designed and delivered for non-technical operations teams across HR, finance, legal and government affairs, supply chain, and marketing. Those programs surfaced more than 100 specific AI use cases and identified more than $12M in three-year net value across 40 participant-built ROI models. This skill is the same method, given away.

Questions, ideas, and stories about what you built with it are welcome as [issues](../../issues).

## Sources

- McKinsey, [The state of AI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) (2025 and 2026 surveys)
- MIT NANDA, The GenAI Divide: State of AI in Business 2025, as reported by [Yahoo Finance](https://finance.yahoo.com/news/mit-report-95-generative-ai-105412686.html) and [The Register](https://www.theregister.com/2025/08/18/generative_ai_zero_return_95_percent)
- Gartner, [Over 40% of agentic AI projects will be canceled by end of 2027](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
- Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), and [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Agent Skills specification](https://agentskills.io/specification) and Anthropic, [Donating Agent Skills to the Agentic AI Foundation](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)
- OWASP GenAI Security Project, [Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [AI Agent Standards Initiative](https://www.nist.gov/caisi/ai-agent-standards-initiative)
- EU Digital Omnibus on AI: [Gibson Dunn summary](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement) and [Hogan Lovells summary](https://www.hoganlovells.com/en/publications/eu-legislators-agree-to-delay-for-highrisk-ai-rules)

## License

[MIT](LICENSE). Use it, adapt it, teach with it. Keep the copyright notice.
