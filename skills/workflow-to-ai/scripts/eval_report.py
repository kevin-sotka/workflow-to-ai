#!/usr/bin/env python3
"""Summarize eval results for an AI helper: pass rates, thresholds, reliability, judge agreement.

Part of the Workflow to AI skill (The Meatbag Method). Standard library only.

Usage:
    python eval_report.py results.csv [--critical correct,grounded]
                          [--threshold overall=0.9] [--threshold dim:correct=0.95]
                          [--threshold category:escalate=1.0] [--threshold fix_minutes=2]

Results CSV: one row per case per run.
    case_id        required
    category       typical, hard, edge, escalate, adversarial (any label works)
    run            run number (optional, default 1)
    dim:<name>     pass, fail, or unknown, as graded by code checks or a model judge
    human:<name>   optional expert grade for the same dimension, used to check the judge
    fix_minutes    optional minutes the expert needed to make the output usable
    note           optional description of what went wrong

Rules:
    A run passes when no critical dimension fails and, if --all-dimensions is set,
    no dimension at all fails. "unknown" counts as not passed and is reported separately.
    Where a human grade exists, it overrides the judge grade for pass rates.
    A case is "reliable" when every run of it passes (pass^k).
"""

import argparse
import csv
import sys
from collections import OrderedDict, defaultdict

PASS = {"pass", "p", "1", "true", "yes", "y"}
FAIL = {"fail", "f", "0", "false", "no", "n"}
UNKNOWN = {"unknown", "u", "?", "n/a", "na", ""}


def grade(value):
    v = str(value or "").strip().lower()
    if v in PASS:
        return "pass"
    if v in FAIL:
        return "fail"
    if v in UNKNOWN:
        return "unknown"
    sys.exit(f"Error: grade {value!r} is not pass, fail, or unknown.")


def rate(items):
    items = list(items)
    return (sum(1 for x in items if x) / len(items)) if items else None


def fmt(value):
    return "n/a" if value is None else f"{value:.0%}"


def kappa(pairs):
    """Cohen's kappa for binary pass/fail pairs (judge, human)."""
    pairs = [(a, b) for a, b in pairs if a in ("pass", "fail") and b in ("pass", "fail")]
    n = len(pairs)
    if n == 0:
        return None, None, 0
    agree = sum(1 for a, b in pairs if a == b) / n
    p_judge = sum(1 for a, _ in pairs if a == "pass") / n
    p_human = sum(1 for _, b in pairs if b == "pass") / n
    expected = p_judge * p_human + (1 - p_judge) * (1 - p_human)
    k = None if expected == 1 else (agree - expected) / (1 - expected)
    return agree, k, n


def parse_thresholds(raw):
    out = OrderedDict()
    for item in raw or []:
        if "=" not in item:
            sys.exit(f"Error: threshold {item!r} must look like name=value")
        key, value = item.split("=", 1)
        try:
            out[key.strip()] = float(value)
        except ValueError:
            sys.exit(f"Error: threshold value in {item!r} is not a number")
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("results", help="Eval results CSV")
    parser.add_argument("--critical", default="", help="Comma-separated critical dimensions")
    parser.add_argument("--all-dimensions", action="store_true",
                        help="Require every dimension to pass, not only critical ones")
    parser.add_argument("--threshold", action="append",
                        help="overall=, dim:<name>=, category:<name>=, reliable=, or fix_minutes= (max average)")
    args = parser.parse_args()

    try:
        with open(args.results, newline="", encoding="utf-8-sig") as handle:
            rows = list(csv.DictReader(handle))
    except FileNotFoundError:
        sys.exit(f"Error: file not found: {args.results}")
    if not rows:
        sys.exit("Error: the results file has no rows.")
    columns = list(rows[0].keys())
    if "case_id" not in columns:
        sys.exit("Error: the results file needs a case_id column.")
    dims = [c.split(":", 1)[1] for c in columns if c.startswith("dim:")]
    if not dims:
        sys.exit("Error: no dim:<name> columns found. Add one column per graded dimension.")
    critical = [d.strip() for d in args.critical.split(",") if d.strip()]
    for d in critical:
        if d not in dims:
            sys.exit(f"Error: critical dimension {d!r} has no dim:{d} column.")
    if not critical and not args.all_dimensions:
        args.all_dimensions = True

    runs = []
    agreement = defaultdict(list)
    for row in rows:
        cid = (row.get("case_id") or "").strip()
        if not cid:
            continue
        final = {}
        for d in dims:
            judge = grade(row.get(f"dim:{d}"))
            human_raw = row.get(f"human:{d}")
            human = grade(human_raw) if human_raw not in (None, "") else None
            if human is not None:
                agreement[d].append((judge, human))
            final[d] = human if human is not None else judge
        must = dims if args.all_dimensions else critical
        passed = all(final[d] == "pass" for d in must)
        fix = row.get("fix_minutes")
        try:
            fix = float(fix) if fix not in (None, "") else None
        except ValueError:
            sys.exit(f"Error: fix_minutes for {cid} is not a number: {fix!r}")
        runs.append({
            "case": cid,
            "category": (row.get("category") or "uncategorized").strip() or "uncategorized",
            "run": (row.get("run") or "1").strip(),
            "grades": final,
            "passed": passed,
            "fix": fix,
            "note": (row.get("note") or "").strip(),
        })

    cases = OrderedDict()
    for r in runs:
        cases.setdefault(r["case"], []).append(r)

    overall = rate(r["passed"] for r in runs)
    reliable = rate(all(r["passed"] for r in rs) for rs in cases.values())
    print("## Eval report")
    print()
    rule = "every dimension" if args.all_dimensions else "critical dimensions (" + ", ".join(critical) + ")"
    print(f"{len(cases)} cases, {len(runs)} runs. A run passes when {rule} pass.")
    print()
    print("| Measure | Result |")
    print("|---|---|")
    print(f"| Overall pass rate (runs) | {fmt(overall)} |")
    print(f"| Reliable cases (every run passed) | {fmt(reliable)} |")
    fixes = [r["fix"] for r in runs if r["fix"] is not None]
    avg_fix = sum(fixes) / len(fixes) if fixes else None
    if avg_fix is not None:
        print(f"| Average fixing minutes per output | {avg_fix:.1f} |")
    print()

    print("**By dimension**")
    print()
    print("| Dimension | Pass | Fail | Unknown | Pass rate | Critical |")
    print("|---|---|---|---|---|---|")
    dim_rates = {}
    for d in dims:
        g = [r["grades"][d] for r in runs]
        p, f, u = g.count("pass"), g.count("fail"), g.count("unknown")
        dim_rates[d] = p / len(g) if g else None
        print(f"| {d} | {p} | {f} | {u} | {fmt(dim_rates[d])} | {'yes' if d in critical else ''} |")
    print()

    print("**By category**")
    print()
    print("| Category | Runs | Pass rate |")
    print("|---|---|---|")
    cat_rates = OrderedDict()
    by_cat = defaultdict(list)
    for r in runs:
        by_cat[r["category"]].append(r["passed"])
    for c, vals in by_cat.items():
        cat_rates[c] = rate(vals)
        print(f"| {c} | {len(vals)} | {fmt(cat_rates[c])} |")
    print()

    if agreement:
        print("**Judge versus expert agreement**")
        print()
        print("| Dimension | Pairs | Agreement | Cohen's kappa | Read |")
        print("|---|---|---|---|---|")
        for d, pairs in agreement.items():
            agree, k, n = kappa(pairs)
            if n == 0:
                continue
            if k is None:
                read = "all one label; add varied cases"
            elif k >= 0.8:
                read = "strong; judge usable"
            elif k >= 0.6:
                read = "moderate; spot-check"
            else:
                read = "weak; rewrite judge prompt"
            ktxt = "n/a" if k is None else f"{k:.2f}"
            print(f"| {d} | {n} | {agree:.0%} | {ktxt} | {read} |")
        print()

    thresholds = parse_thresholds(args.threshold)
    verdicts = []
    if thresholds:
        print("**Thresholds**")
        print()
        print("| Threshold | Target | Actual | Met |")
        print("|---|---|---|---|")
        for key, target in thresholds.items():
            if key == "overall":
                actual, met = overall, overall is not None and overall >= target
            elif key == "reliable":
                actual, met = reliable, reliable is not None and reliable >= target
            elif key.startswith("dim:"):
                actual = dim_rates.get(key[4:])
                met = actual is not None and actual >= target
            elif key.startswith("category:"):
                actual = cat_rates.get(key[9:])
                met = actual is not None and actual >= target
            elif key == "fix_minutes":
                met = avg_fix is not None and avg_fix <= target
                print(f"| average fix minutes | at most {target:g} | "
                      f"{'n/a' if avg_fix is None else f'{avg_fix:.1f}'} | {'yes' if met else 'no'} |")
                verdicts.append(met)
                continue
            else:
                sys.exit(f"Error: unknown threshold {key!r}")
            print(f"| {key} | {target:.0%} | {fmt(actual)} | {'yes' if met else 'no'} |")
            verdicts.append(met)
        print()

    critical_fails = [r for r in runs if any(r["grades"][d] == "fail" for d in critical)]
    if verdicts:
        ok = all(verdicts) and not critical_fails
        print(f"**Gate 5 verdict:** {'thresholds met' if ok else 'not yet'}"
              + ("" if not critical_fails else f" ({len(critical_fails)} runs with a critical failure)") + ".")
        print()

    flagged = [r for r in runs if not r["passed"] or any(g != "pass" for g in r["grades"].values())]
    if flagged:
        print("**Outputs to read** (group these into failure modes and fix the biggest one first; "
              "non-critical misses are listed too)")
        print()
        print("| Case | Category | Run | Run passed | Not passed | Note |")
        print("|---|---|---|---|---|---|")
        for r in flagged:
            bad = [f"{d} ({r['grades'][d]})" for d in dims if r["grades"][d] != "pass"]
            print(f"| {r['case']} | {r['category']} | {r['run']} | {'yes' if r['passed'] else 'no'} | "
                  f"{', '.join(bad)} | {r['note']} |")
    else:
        print("Every dimension passed on every run. Before celebrating, check that the set includes hard, "
              "edge, escalate, and adversarial cases.")

if __name__ == "__main__":
    main()
