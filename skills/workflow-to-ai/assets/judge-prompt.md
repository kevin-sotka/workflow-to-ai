# Judge prompt template

*Use one judge prompt per dimension. Judging several dimensions at once makes the grades harder to trust and harder to debug. Calibrate every judge against at least 20 expert grades before relying on it (see references/test.md).*

---

You are grading one output from an AI helper on a single dimension: **<dimension name>**.

## What the helper was asked to do

<One-paragraph description of the helper's job.>

## The dimension

**<Dimension name>** passes when: <precise definition>.

It fails when: <precise definition, with the most common failure modes listed>.

Examples from expert grading:
- PASS: <short example and the expert's reason>
- FAIL: <short example and the expert's reason>

## The case

Input:
<input>

Reference answer or expected outcome:
<expected>

Sources available to the helper:
<sources>

Helper output:
<output>

## How to answer

Think through the evidence first, then give a verdict. Compare the output against the sources and the expected outcome. Do not reward length, confidence, or polish. If the evidence is not sufficient to decide, answer UNKNOWN rather than guessing.

Respond in exactly this format:

```
Reasoning: <two to four sentences citing the specific evidence>
Verdict: PASS | FAIL | UNKNOWN
```
