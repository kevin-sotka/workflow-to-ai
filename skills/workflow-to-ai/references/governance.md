# Governance, risk, and security

*Reviewed November 2026. Laws and frameworks change. This is orientation, not legal advice. For anything consequential, the person should involve their legal, privacy, security, or compliance team.*

The goal is proportion: a personal drafting helper should not need a committee, and a helper that screens job applicants should not ship without one.

## Risk tiers

Assign the highest tier that any part of the helper touches.

### Low

**Looks like:** a personal or small-team helper; drafts that a person rewrites before anyone else sees them; public or ordinary internal information; no actions in other systems.

**Required controls:**
- Use a tool the organization has approved for this kind of data
- A person reviews every output before it is used
- No confidential or restricted data in unapproved tools
- Keep the instructions and test cases in a file the team owns

### Medium

**Looks like:** a helper shared across a team; confidential internal data; outputs that reach other people after review; AI that takes actions in systems with a person approving each one (L3).

**Required controls (in addition to low):**
- A named owner and backup
- A test set with thresholds, rerun whenever instructions or the underlying model change
- Access through the organization's existing permissions; the helper sees no more than its users can
- A review checklist for the people checking outputs
- A change log and a way for users to report problems
- Logging of what the helper did, where the platform supports it
- A security review if it reads email, documents from outside the organization, or the web (prompt injection risk)

### High

**Looks like any of these:**
- **Decisions about people:** recruiting and screening, performance, promotion, pay, discipline, termination, task allocation based on personal traits, benefits or leave eligibility
- **Access to essential services or money:** credit, lending, insurance pricing, eligibility for public services
- Legal advice or positions communicated outside the organization; regulatory filings; public policy statements
- Moving money, changing master data (vendor bank details, pay rates), or anything irreversible
- Customer-facing helpers that act without a person reviewing each output (L4)
- Health, safety, or critical infrastructure

**Required controls (in addition to medium):**
- Review by legal, privacy, and compliance before the pilot, and again before scaling
- A named human decision maker of record; the helper informs, a person decides
- A data protection impact assessment or equivalent where personal data is involved
- Testing for unfair outcomes across groups when the helper touches decisions about people
- Clear notice to the people affected, where required
- An audit trail of inputs, outputs, and human decisions
- An incident plan: how problems are detected, who is told, how the helper is paused
- A vendor assessment for any third-party product

## Regulatory landmarks to know about

Point the person to their own counsel for how these apply. Do not interpret them for a specific situation.

- **EU AI Act.** Classifies some uses as high risk, including AI used in employment and worker management, and in access to essential private and public services such as credit. The Digital Omnibus on AI, in force from mid-2026, moved the high-risk obligations for these stand-alone uses to 2 December 2027, and for AI embedded in regulated products to 2 August 2028. Prohibitions and general-purpose model obligations already apply. Relevant if the organization operates in the EU or its outputs are used there.
- **Automated employment decision rules.** Several US cities and states regulate AI used in hiring and employment decisions, with requirements such as bias audits and candidate notice. Any HR helper that ranks, screens, or scores people should go to employment counsel first.
- **Privacy law** (GDPR, state privacy laws, sector rules such as HIPAA and GLBA) applies to personal data whether or not AI is involved. AI does not create an exception.
- **Records and e-discovery.** AI outputs, prompts, and logs may be business records. Ask how long they are kept and who can see them.

## Frameworks worth borrowing from

- **NIST AI Risk Management Framework** (Govern, Map, Measure, Manage), its Generative AI Profile (NIST AI 600-1), and the NIST AI Agent Standards Initiative launched in 2026. Voluntary, widely referenced, and a good shared vocabulary with risk teams. The core framework is under revision.
- **ISO/IEC 42001**, a certifiable AI management system standard. Relevant if the organization is pursuing certification or its customers ask about it.
- **OWASP Top 10 for LLM Applications** and **OWASP Top 10 for Agentic Applications (2026)**. The practical security checklists. The agentic list introduces the principle of least agency: give an agent only the autonomy it needs for a safe, bounded task.

## Security checks for every helper

Ask these in Step 3 and test them in Step 5.

| Risk | Question | Typical control |
|---|---|---|
| **Prompt injection** | Does the helper read content written by outsiders (emails, attachments, web pages, uploaded documents)? Could that content contain instructions? | Treat external content as data; keep the helper's permissions narrow; require approval before actions; include injection cases in the test set |
| **Excessive agency** | Can it do more than its job requires (send, delete, pay, change records)? | Least privilege; draft-only by default; approval for actions |
| **Data leakage** | Could it reveal information to someone who should not see it? | Inherit existing permissions; restrict knowledge sources; test cross-user access |
| **Sensitive data exposure** | Will restricted data flow into a tool not approved for it? | Approved tools only; redact test data; data classification check |
| **Overreliance** | Will people stop checking because it is usually right? | Review checklist; sample audits; track correction rate; keep checkpoints visible |
| **Memory and context poisoning** | Does it remember things across sessions or learn from user input? | Review what it stores; reset paths; owner reviews memory periodically |
| **Supply chain** | Does it use third-party plugins, connectors, skills, or MCP servers? | Use vetted sources; review what each component can access; pin versions |
| **Identity** | Whose permissions does it act with? | Act as the user or as a scoped service identity; never a shared admin account |

## Human oversight that actually works

A checkpoint only protects anyone if the reviewer can do the check in the time they really have.

- Put the **reason and sources** next to every output so the reviewer can verify quickly.
- Give reviewers a **short checklist** built from the failure modes found in Step 5.
- Make **"reject" and "escalate" as quick** as approve.
- **Track the correction rate.** If reviewers never change anything, either the helper is excellent (promote it, with evidence) or the review has become a rubber stamp (fix the review).
- Remember the hard lesson from real pilots: when a helper's failures are hard to see (an invented detail in a polished, confident document), **the review gate is the product.** Design for that.
