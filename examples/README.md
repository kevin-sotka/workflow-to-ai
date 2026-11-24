# Examples

Illustrative runs of the method. Companies, people, and numbers are fictional.

## finance-vendor-inquiries

An accounts payable team drowning in "where is my payment" emails. Every artifact from a full build:

| File | Step | What it is |
|---|---|---|
| `running-document.md` | All | The finished running document |
| `current.csv`, `future.csv` | 1, 2 | Step tables for the current and future workflow |
| `outputs-workflow-map.md` | 1, 2 | Output of `workflow_map.py` |
| `scorecard.csv`, `outputs-scorecard.md` | 1 | Five pain points scored and ranked |
| `roi-inputs.json`, `outputs-roi.md` | 4 | Three-scenario business case |
| `helper/` | 5 | The helper's instructions, reviewer checklist, changelog, and sample test cases |
| `eval-results-v0.1.csv`, `outputs-eval-v0.1.md` | 5 | First test run: thresholds not met |
| `eval-results-v0.3.csv`, `outputs-eval-v0.3.md` | 5 | After fixing the top failure modes: thresholds met |

Regenerate the outputs from the repository root:

```bash
S=skills/workflow-to-ai/scripts
E=examples/finance-vendor-inquiries
python $S/workflow_map.py $E/current.csv --future $E/future.csv --frequency 420 --title "Vendor payment inquiries"
python $S/score_opportunities.py $E/scorecard.csv
python $S/roi_calculator.py $E/roi-inputs.json
python $S/eval_report.py $E/eval-results-v0.3.csv --critical correct,grounded,escalation,safe --threshold overall=0.9
```
