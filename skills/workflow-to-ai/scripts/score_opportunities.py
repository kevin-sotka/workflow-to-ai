#!/usr/bin/env python3
"""Score and rank workflow pain points, check Gate 1, and sort them into quadrants.

Part of the Workflow to AI skill (The Meatbag Method). Standard library only.

Usage:
    python score_opportunities.py scorecard.csv [--gate 3] [--markdown-only]

CSV columns (each scored 1 to 5):
    idea         short name of the candidate
    discrete     is it a specific, bounded problem?            (5 = very specific)
    valuable     how deeply and widely is the pain felt?        (5 = severe, widespread)
    testable     could a fix be tried on real cases soon?        (5 = many examples on hand)
    frequency    how often does it happen?                      (5 = many times a day)
    data_ready   is the needed information reachable and usable? (5 = one clean system)
    complexity   how hard is the fix likely to be?               (5 = hardest)
    risk         how bad is a mistake?                          (5 = worst)
    notes        optional

Scoring:
    gate     = pass if discrete, valuable, and testable are all at or above the gate (default 3)
    value    = average of valuable and frequency
    ease     = average of (6 - complexity), data_ready, and (6 - risk)
    priority = value x ease (range 1 to 25)
    quadrant = by value (>= 3 is high) and complexity (<= 3 is low):
               quick win, big bet, fill-in, money pit
"""

import argparse
import csv
import sys

FIELDS = ["discrete", "valuable", "testable", "frequency", "data_ready", "complexity", "risk"]


def score(value, field, idea):
    try:
        number = float(str(value).strip())
    except (TypeError, ValueError):
        sys.exit(f"Error: {field} for {idea!r} must be a number from 1 to 5, got {value!r}")
    if not 1 <= number <= 5:
        sys.exit(f"Error: {field} for {idea!r} must be between 1 and 5, got {number:g}")
    return number


def quadrant(value, complexity):
    high_value = value >= 3
    low_complexity = complexity <= 3
    if high_value and low_complexity:
        return "quick win"
    if high_value:
        return "big bet"
    if low_complexity:
        return "fill-in"
    return "money pit"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("scorecard", help="Scorecard CSV")
    parser.add_argument("--gate", type=float, default=3, help="Minimum score for discrete, valuable, testable")
    args = parser.parse_args()

    try:
        with open(args.scorecard, newline="", encoding="utf-8-sig") as handle:
            rows = list(csv.DictReader(handle))
    except FileNotFoundError:
        sys.exit(f"Error: file not found: {args.scorecard}")
    if not rows:
        sys.exit("Error: the scorecard has no rows.")
    missing = [f for f in ["idea"] + FIELDS if f not in rows[0]]
    if missing:
        sys.exit(f"Error: missing columns: {', '.join(missing)}")

    results = []
    for row in rows:
        idea = (row.get("idea") or "").strip()
        if not idea:
            continue
        s = {f: score(row.get(f), f, idea) for f in FIELDS}
        gate_fails = [f for f in ("discrete", "valuable", "testable") if s[f] < args.gate]
        value = (s["valuable"] + s["frequency"]) / 2
        ease = ((6 - s["complexity"]) + s["data_ready"] + (6 - s["risk"])) / 3
        results.append({
            "idea": idea,
            "gate": "pass" if not gate_fails else "reframe: low " + ", ".join(gate_fails),
            "value": value,
            "ease": ease,
            "priority": value * ease,
            "complexity": s["complexity"],
            "risk": s["risk"],
            "quadrant": quadrant(value, s["complexity"]),
            "notes": (row.get("notes") or "").strip(),
        })

    results.sort(key=lambda r: (r["gate"] != "pass", -r["priority"]))

    print("## Candidate ranking")
    print()
    print("| Rank | Idea | Gate 1 | Value | Ease | Priority | Quadrant | Risk |")
    print("|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(results, 1):
        print(f"| {i} | {r['idea']} | {r['gate']} | {r['value']:.1f} | {r['ease']:.1f} | "
              f"{r['priority']:.1f} | {r['quadrant']} | {r['risk']:g} |")
    print()
    print("Priority = value x ease (max 25). Value averages how valuable and how frequent. "
          "Ease averages low complexity, data readiness, and low risk.")
    print()

    passing = [r for r in results if r["gate"] == "pass"]
    if passing:
        top = passing[0]
        print(f"**Suggested starting point:** {top['idea']} ({top['quadrant']}, priority {top['priority']:.1f}).")
        wins = [r for r in passing if r["quadrant"] == "quick win"]
        if wins and wins[0] is not top:
            print(f"Highest-priority quick win: {wins[0]['idea']}. "
                  "A first success often buys the credibility for a bigger bet.")
        high_risk = [r for r in passing[:3] if r["risk"] >= 4]
        for r in high_risk:
            print(f"Note: {r['idea']} scores {r['risk']:g} on risk. "
                  "Check the high-risk tier in references/governance.md before committing.")
    else:
        print("**No candidate passes Gate 1.** Narrow the scope of the strongest idea, "
              "or collect real examples to make it testable.")
    print()

    print("```mermaid")
    print("quadrantChart")
    print("    title Value versus complexity")
    print("    x-axis Low complexity --> High complexity")
    print("    y-axis Low value --> High value")
    print("    quadrant-1 Big bets")
    print("    quadrant-2 Quick wins")
    print("    quadrant-3 Fill-ins")
    print("    quadrant-4 Money pits")
    for r in results:
        x = (r["complexity"] - 1) / 4
        y = (r["value"] - 1) / 4
        name = r["idea"].replace(":", " ").replace('"', "'")[:40]
        print(f"    {name}: [{x:.2f}, {y:.2f}]")
    print("```")


if __name__ == "__main__":
    main()
