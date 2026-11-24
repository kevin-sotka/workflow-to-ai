"""Smoke tests for the bundled scripts, run against the worked example.

Run from the repository root: python -m unittest discover -s tests
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "skills", "workflow-to-ai", "scripts")
EXAMPLE = os.path.join(ROOT, "examples", "finance-vendor-inquiries")


def run(script, *args, expect_ok=True):
    result = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS, script), *args],
        capture_output=True, text=True,
    )
    if expect_ok and result.returncode != 0:
        raise AssertionError(f"{script} failed: {result.stderr}")
    return result


class WorkflowMap(unittest.TestCase):
    def test_before_and_after(self):
        out = run("workflow_map.py", os.path.join(EXAMPLE, "current.csv"),
                  "--future", os.path.join(EXAMPLE, "future.csv"), "--frequency", "420").stdout
        self.assertIn("flowchart TD", out)
        self.assertIn("| Touch minutes per occurrence | 8.5 | 2.5 | -6 |", out)
        self.assertIn("| Hands-on hours per month | 59.5 | 17.5 | -42.0 |", out)
        self.assertIn("Single points of knowledge", out)

    def test_bad_type_is_rejected(self):
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
            f.write("step_id,step,actor,touch_minutes,type\nS1,Do it,Me,2,magic\n")
        result = run("workflow_map.py", f.name, expect_ok=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("magic", result.stderr)


class ScoreOpportunities(unittest.TestCase):
    def test_ranking_and_gate(self):
        out = run("score_opportunities.py", os.path.join(EXAMPLE, "scorecard.csv")).stdout
        self.assertIn("| 1 | Vendor payment status inquiries | pass |", out)
        self.assertIn("reframe: low discrete, testable", out)
        self.assertIn("quadrantChart", out)


class RoiCalculator(unittest.TestCase):
    def test_example_numbers(self):
        out = run("roi_calculator.py", os.path.join(EXAMPLE, "roi-inputs.json")).stdout
        self.assertIn("| Payback period | 8.8 months | 2.7 months | 2.1 months |", out)
        self.assertIn("Gate 4 check: the conservative case clears its costs.", out)
        self.assertIn("Capacity, not cash", out)

    def test_never_pays_back(self):
        data = {"scenarios": {"conservative": {
            "occurrences_per_month": 10, "minutes_before": 5, "minutes_after": 4,
            "loaded_hourly_rate": 30, "adoption_rate": 0.5,
            "setup_costs": {"build": 1000}, "monthly_run_costs": {"licenses": 500}}}}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(data, f)
        out = run("roi_calculator.py", f.name).stdout
        self.assertIn("never at these inputs", out)
        self.assertIn("does not clear", out)

    def test_adoption_out_of_range(self):
        data = {"scenarios": {"x": {"occurrences_per_month": 1, "minutes_before": 1,
                                    "minutes_after": 0, "loaded_hourly_rate": 1, "adoption_rate": 60}}}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(data, f)
        self.assertNotEqual(run("roi_calculator.py", f.name, expect_ok=False).returncode, 0)


class EvalReport(unittest.TestCase):
    ARGS = ["--critical", "correct,grounded,escalation,safe", "--threshold", "overall=0.9",
            "--threshold", "category:adversarial=1.0"]

    def test_first_version_fails(self):
        out = run("eval_report.py", os.path.join(EXAMPLE, "eval-results-v0.1.csv"), *self.ARGS).stdout
        self.assertIn("| Overall pass rate (runs) | 77% |", out)
        self.assertIn("**Gate 5 verdict:** not yet", out)
        self.assertIn("0.86", out)

    def test_fixed_version_passes(self):
        out = run("eval_report.py", os.path.join(EXAMPLE, "eval-results-v0.3.csv"), *self.ARGS).stdout
        self.assertIn("**Gate 5 verdict:** thresholds met.", out)
        self.assertIn("T23", out)

    def test_reliability_across_runs(self):
        rows = "case_id,category,run,dim:correct\nA,typical,1,pass\nA,typical,2,fail\nB,typical,1,pass\nB,typical,2,pass\n"
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
            f.write(rows)
        out = run("eval_report.py", f.name, "--critical", "correct").stdout
        self.assertIn("| Overall pass rate (runs) | 75% |", out)
        self.assertIn("| Reliable cases (every run passed) | 50% |", out)


class SkillPackage(unittest.TestCase):
    def test_validates(self):
        result = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "validate_skill.py"),
                                 os.path.join(ROOT, "skills", "workflow-to-ai")],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_voice(self):
        result = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "lint_voice.py"), ROOT],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)


if __name__ == "__main__":
    unittest.main()
