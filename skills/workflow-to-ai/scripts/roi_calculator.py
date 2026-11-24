#!/usr/bin/env python3
"""Three-scenario business case for an AI helper: value, cost, payback, and break-even adoption.

Part of the Workflow to AI skill (The Meatbag Method). Standard library only.

Usage:
    python roi_calculator.py roi-inputs.json [--currency "$"] [--months 36]

Input JSON (see assets/roi-inputs.json): a "scenarios" object with keys such as
"conservative", "expected", "optimistic". Each scenario has:

    occurrences_per_month       number of times the work happens each month
    minutes_before              hands-on minutes per occurrence today
    minutes_after               hands-on minutes per occurrence with the helper,
                                INCLUDING the time a person spends reviewing its output
    loaded_hourly_rate          fully loaded cost of an hour of the people doing the work
    adoption_rate               share of eligible occurrences that will use the helper (0 to 1)
    other_value_per_month       optional: errors avoided, avoided spend, revenue effects
    setup_costs                 object of one-time costs, e.g. {"build_hours_cost": 3000}
    monthly_run_costs           object of monthly costs, e.g. {"licenses": 300}
    value_type                  optional: "cash" or "capacity" (default "capacity")

Any number may instead be an object {"value": 6, "basis": "measured"} where basis is
measured, estimated, or assumed. The report counts each basis so the reader knows how
much of the case is evidence and how much is guesswork.
"""

import argparse
import json
import math
import sys

BASES = ("measured", "estimated", "assumed")
NUMERIC = ["occurrences_per_month", "minutes_before", "minutes_after",
           "loaded_hourly_rate", "adoption_rate"]


class Inputs:
    def __init__(self):
        self.basis_counts = {b: 0 for b in BASES}
        self.basis_counts["unlabeled"] = 0

    def read(self, raw, field, scenario, required=True):
        if raw is None:
            if required:
                sys.exit(f"Error: scenario {scenario!r} is missing {field}.")
            return 0.0
        basis = "unlabeled"
        if isinstance(raw, dict):
            basis = str(raw.get("basis", "unlabeled")).lower()
            raw = raw.get("value")
            if basis not in self.basis_counts:
                sys.exit(f"Error: {field} in {scenario!r} has basis {basis!r}; "
                         f"use one of {', '.join(BASES)}.")
        try:
            number = float(raw)
        except (TypeError, ValueError):
            sys.exit(f"Error: {field} in scenario {scenario!r} is not a number: {raw!r}")
        self.basis_counts[basis] += 1
        return number

    def read_group(self, group, field, scenario):
        if group is None:
            return 0.0, {}
        if not isinstance(group, dict):
            return self.read(group, field, scenario), {}
        items = {}
        for key, raw in group.items():
            items[key] = self.read(raw, f"{field}.{key}", scenario)
        return sum(items.values()), items


def money(amount, currency):
    sign = "-" if amount < 0 else ""
    return f"{sign}{currency}{abs(amount):,.0f}"


def compute(name, spec, currency, horizon):
    reader = Inputs()
    v = {f: reader.read(spec.get(f), f, name) for f in NUMERIC}
    if not 0 <= v["adoption_rate"] <= 1:
        sys.exit(f"Error: adoption_rate in {name!r} must be between 0 and 1 (for example 0.6).")
    other = reader.read(spec.get("other_value_per_month"), "other_value_per_month", name, required=False)
    setup, setup_items = reader.read_group(spec.get("setup_costs"), "setup_costs", name)
    run, run_items = reader.read_group(spec.get("monthly_run_costs"), "monthly_run_costs", name)

    minutes_saved = v["minutes_before"] - v["minutes_after"]
    hours_saved = minutes_saved * v["occurrences_per_month"] * v["adoption_rate"] / 60
    time_value = hours_saved * v["loaded_hourly_rate"]
    monthly_value = time_value + other
    net_monthly = monthly_value - run
    payback = setup / net_monthly if net_monthly > 0 else math.inf
    first_year = 12 * net_monthly - setup
    horizon_net = horizon * net_monthly - setup

    # Adoption at which time value plus other value covers the running cost.
    full_time_value = minutes_saved * v["occurrences_per_month"] * v["loaded_hourly_rate"] / 60
    if full_time_value > 0:
        breakeven = max(0.0, (run - other) / full_time_value)
    else:
        breakeven = math.inf

    return {
        "name": name,
        "minutes_saved": minutes_saved,
        "hours_saved": hours_saved,
        "monthly_value": monthly_value,
        "setup": setup,
        "run": run,
        "net_monthly": net_monthly,
        "payback": payback,
        "first_year": first_year,
        "horizon_net": horizon_net,
        "breakeven": breakeven,
        "adoption": v["adoption_rate"],
        "value_type": str(spec.get("value_type", "capacity")).lower(),
        "basis": reader.basis_counts,
        "setup_items": setup_items,
        "run_items": run_items,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("inputs", help="ROI inputs JSON file")
    parser.add_argument("--currency", default=None, help="Currency symbol (default from file or $)")
    parser.add_argument("--months", type=int, default=36, help="Horizon for the multi-year net (default 36)")
    args = parser.parse_args()

    try:
        with open(args.inputs, encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError:
        sys.exit(f"Error: file not found: {args.inputs}")
    except json.JSONDecodeError as err:
        sys.exit(f"Error: {args.inputs} is not valid JSON: {err}")

    scenarios = data.get("scenarios")
    if not isinstance(scenarios, dict) or not scenarios:
        sys.exit("Error: the file needs a non-empty \"scenarios\" object.")
    currency = args.currency or data.get("currency", "$")
    results = [compute(name, spec, currency, args.months) for name, spec in scenarios.items()]

    title = data.get("title", "Business case")
    print(f"## {title}")
    print()
    header = "| Measure | " + " | ".join(r["name"].capitalize() for r in results) + " |"
    print(header)
    print("|---|" + "---|" * len(results))

    def row(label, fn):
        print(f"| {label} | " + " | ".join(fn(r) for r in results) + " |")

    years = args.months / 12
    horizon_label = f"{years:g}-year net" if args.months % 12 == 0 else f"{args.months}-month net"
    row("Minutes saved per occurrence", lambda r: f"{r['minutes_saved']:g}")
    row("Adoption rate", lambda r: f"{r['adoption']:.0%}")
    row("Hours saved per month", lambda r: f"{r['hours_saved']:,.1f}")
    row("Monthly value", lambda r: money(r["monthly_value"], currency))
    row("Setup cost (one time)", lambda r: money(r["setup"], currency))
    row("Monthly run cost", lambda r: money(r["run"], currency))
    row("Net monthly benefit", lambda r: money(r["net_monthly"], currency))
    row("Payback period", lambda r: "never at these inputs" if math.isinf(r["payback"])
        else f"{r['payback']:.1f} months")
    row("First-year net", lambda r: money(r["first_year"], currency))
    row(horizon_label.capitalize(), lambda r: money(r["horizon_net"], currency))
    def breakeven_text(r):
        if math.isinf(r["breakeven"]) or r["breakeven"] > 1:
            return "not reachable"
        if r["breakeven"] == 0:
            return "0% (other value covers running cost)"
        return f"{r['breakeven']:.0%}"
    row("Break-even adoption", breakeven_text)
    row("Value is", lambda r: r["value_type"])
    print()

    print("**Input basis** (how much of each scenario is evidence):")
    print()
    for r in results:
        b = r["basis"]
        total = sum(b.values())
        parts = [f"{b[k]} {k}" for k in ("measured", "estimated", "assumed", "unlabeled") if b[k]]
        print(f"- {r['name'].capitalize()}: {', '.join(parts)} (of {total} inputs)")
    print()

    notes = []
    for r in results:
        if r["minutes_saved"] <= 0:
            notes.append(f"In the {r['name']} scenario the helper saves no time per occurrence. "
                         "Check that minutes_after is lower than minutes_before, including review time.")
        if r["net_monthly"] <= 0:
            notes.append(f"In the {r['name']} scenario the running cost is higher than the value. "
                         "Look for a cheaper rung, a narrower scope, or a non-financial reason.")
    capacity = [r["name"] for r in results if r["value_type"] != "cash"]
    if capacity:
        notes.append("Capacity, not cash, in: " + ", ".join(capacity) + ". Hours come back to the team. "
                     "Say what that time will be used for, and do not present it as budget savings.")
    conservative = next((r for r in results if r["name"].lower() == "conservative"), None)
    if conservative:
        verdict = "clears" if conservative["net_monthly"] > 0 and conservative["first_year"] > 0 else \
            "covers its running cost but not its setup in year one" if conservative["net_monthly"] > 0 else \
            "does not clear"
        notes.append(f"Gate 4 check: the conservative case {verdict} its costs.")
    seen = set()
    if notes:
        print("**Notes**")
        print()
        for n in notes:
            if n not in seen:
                print(f"- {n}")
                seen.add(n)


if __name__ == "__main__":
    main()
