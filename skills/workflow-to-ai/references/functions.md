# Function playbooks

Common starting points by function. These are illustrative patterns to prompt the conversation, not a list to impose. The person's own pain points always come first. Use the matching section during setup to ask sharper questions and to anticipate watch-outs.

Each section lists: **good first candidates** (usually language-heavy, frequent, and checkable), **keep a human on** (circled steps), **watch-outs**, and **metrics** that tend to matter.

## HR and People

- **Good first candidates:** drafting job descriptions from an intake form; answering policy and benefits questions from the handbook (with links to the source); onboarding schedules and welcome packets; summarizing exit interview or engagement survey comments into themes; drafting interview guides from a role profile; converting policy changes into plain-language FAQs.
- **Keep a human on:** any decision about a person (screening, ranking, hiring, performance, pay, discipline, termination, accommodations); sensitive conversations; investigations.
- **Watch-outs:** personnel data is restricted. Helpers that rank, screen, or score people are high risk under the EU AI Act and several US employment rules; involve employment counsel. Check generated content for biased language. Policy answers must cite the current policy and escalate anything ambiguous.
- **Metrics:** time to fill, recruiter hours per requisition, onboarding tasks completed on time, HR inbox volume and response time, policy question deflection with accuracy.

## Finance and Accounting

- **Good first candidates:** responding to vendor payment inquiries; drafting variance commentary from the numbers; summarizing contracts for revenue recognition questions; preparing audit request responses from the document index; expense policy questions; month-end close checklists and status summaries; drafting collection emails by aging bucket.
- **Keep a human on:** approvals, payments, journal entries, changes to vendor master data (especially bank details), judgments about accounting treatment, anything sent to auditors or regulators.
- **Watch-outs:** arithmetic and reconciliations belong in formulas and code, not in a model's head. Every number in an output must trace to a source. Vendor bank detail change requests are a classic fraud vector; never let a helper act on them. Financial data is confidential or restricted.
- **Metrics:** cost per invoice, inquiry response time, days to close, days sales outstanding, error and rework rate, audit request turnaround.

## Procurement and Supply Chain

- **Good first candidates:** drafting RFQs and RFPs from a requirements template; comparing supplier quotes against a standard rubric; summarizing supplier contracts and flagging non-standard terms; expediting emails for late purchase orders; classifying spend; preparing supplier risk summaries from public information; drafting customs or trade compliance documentation for specialist review.
- **Keep a human on:** supplier selection, negotiation, contract approval, trade compliance determinations (classification, origin, sanctions screening decisions), anything that commits spend.
- **Watch-outs:** tariff, classification, and regulatory regimes change quickly; the helper must use current sources and flag uncertainty. Pricing and contract terms are confidential. Supplier emails are external content: test for prompt injection.
- **Metrics:** cycle time from request to purchase order, expediting hours, on-time delivery, analyst hours per analysis, rework rate, savings captured.

## Sales and Revenue Operations

- **Good first candidates:** account research briefs before calls; call note summaries and CRM updates for review; follow-up email drafts; first drafts of proposal sections from a content library; security questionnaire answers from an approved answer bank; qualifying inbound leads against criteria with a human confirming.
- **Keep a human on:** pricing and discounting, contract commitments, relationship-critical communication, forecasts presented to leadership.
- **Watch-outs:** a helper that invents a product capability or a commitment creates real liability. Ground answers in the approved content library. Personal data in CRM records is regulated. Do not let outbound messages send without review.
- **Metrics:** time spent on admin versus selling, CRM data completeness, response time to inbound leads, proposal turnaround, questionnaire turnaround.

## Marketing

- **Good first candidates:** repurposing one approved piece into channel variants; drafting briefs from a campaign intake form; summarizing campaign performance into commentary; customer interview and review synthesis; localization drafts for native review; SEO metadata drafts; checking drafts against the brand voice guide.
- **Keep a human on:** brand and legal claims, final creative approval, anything published, crisis communication.
- **Watch-outs:** claims about products, prices, health, or the environment need substantiation and legal review. Watch for generic, interchangeable copy ("slop"); the brand's voice notes and real examples belong in the context pack. Check rights for any generated images. Disclose AI-generated content where rules or platform policies require it.
- **Metrics:** time from brief to approved draft, production volume per marketer, revision rounds, performance of AI-assisted versus baseline content.

## Customer Service and Operations

- **Good first candidates:** suggested replies from the knowledge base for agent review; ticket summarization and routing; after-call summaries; knowledge article drafts from resolved tickets; quality assurance review against a rubric; escalation briefs.
- **Keep a human on:** refunds and credits above a limit, complaints, vulnerable customers, anything legal or safety related, policy exceptions.
- **Watch-outs:** customer-facing helpers that reply without review are high risk; start at draft-for-review. Inbound customer messages are external content: test for prompt injection. Knowledge base gaps show up as invented answers; fix the knowledge base.
- **Metrics:** handle time, first contact resolution, backlog, quality score, customer satisfaction, escalation rate, agent ramp time.

## Legal

- **Good first candidates:** first-pass contract review against a playbook (flagging deviations for a lawyer); NDA triage; clause comparison against standard positions; summarizing long documents for a lawyer's review; intake triage for legal requests; drafting standard correspondence from templates; organizing document productions.
- **Keep a human on:** legal advice, judgments of risk, negotiation positions, anything sent outside the organization, privilege decisions.
- **Watch-outs:** privileged and confidential material requires approved tools and careful access control. Invented citations and confident misstatements of law are well-documented failure modes; every legal statement must be verified by a lawyer against the source. Check bar and court rules on AI use and disclosure.
- **Metrics:** contract cycle time, lawyer hours per contract type, share of contracts on standard terms, intake response time, outside counsel spend.

## Government Affairs and Public Policy

- **Good first candidates:** compiling executive briefings into a fixed template from approved sources; tracking and summarizing legislation and regulatory activity; drafting meeting prep with stakeholder background; first drafts of comment letters for expert review; maintaining a positions and talking-points library.
- **Keep a human on:** positions, anything said publicly or to officials, political judgment, relationship management.
- **Watch-outs:** failures here are often hard to see in a polished draft, and the cost of one reaching a principal is high. Treat the review gate as the product, and give reviewers a checklist. Sources must be current and cited. Some jurisdictions regulate lobbying communications and disclosures.
- **Metrics:** hours per briefing, briefing turnaround, coverage of tracked issues, rework requested by principals.

## IT and Service Desk

- **Good first candidates:** ticket triage and routing; suggested resolutions from the knowledge base; knowledge article drafts from resolved tickets; change request summaries and risk notes for the change board; access request validation against policy; incident timeline drafts; scripting help for administrators.
- **Keep a human on:** production changes, access grants to sensitive systems, security incident decisions, anything irreversible.
- **Watch-outs:** agents with administrative permissions are high-value targets; apply least privilege and approval steps. Logs and tickets may contain credentials or personal data. Generated scripts must be reviewed and tested before running.
- **Metrics:** mean time to resolve, first contact resolution, ticket backlog, knowledge base coverage, change failure rate.

## Operations, PMO, and Shared Services

- **Good first candidates:** status report drafts from tracker data; meeting notes to action items; SOP drafts from recorded walkthroughs; RAID log summaries; intake form triage; turning tribal knowledge into documented procedures.
- **Keep a human on:** priorities and tradeoffs, resourcing decisions, escalations to leadership.
- **Watch-outs:** status summaries can smooth over real problems; require the helper to surface risks and blockers explicitly. Recorded walkthroughs may contain sensitive information.
- **Metrics:** hours spent on reporting, time from meeting to documented actions, SOP coverage, single points of knowledge removed.
