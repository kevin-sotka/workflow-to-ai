#!/usr/bin/env python3
"""Turn a workflow step table (CSV) into a Mermaid diagram and summary statistics.

Part of the Workflow to AI skill (The Meatbag Method). Standard library only.

Usage:
    python workflow_map.py current.csv [--future future.csv] [--frequency 400] [--title "Name"]

Required CSV columns: step_id, step, actor, touch_minutes, type
Minutes are averages per occurrence. If a step happens in one case out of five and takes
240 minutes of waiting, enter 48. Actors named "AI ...", "Automation", "System", "Bot",
"Script", or "Flow" count as machine steps and are skipped when counting handoffs.

Optional columns: tool, input, output, wait_minutes, pain, error_prone, single_point,
                  autonomy, checkpoint, notes

Step types: copy, lookup, transform, language, classify, judgment, approval,
            communication, wait
"""

import argparse
import csv
import sys
from collections import OrderedDict

STEP_TYPES = [
    "copy", "lookup", "transform", "language", "classify",
    "judgment", "approval", "communication", "wait",
]
CIRCLED = {"judgment", "approval", "communication"}
UNDERLINED = {"copy", "lookup", "transform"}
REQUIRED = ["step_id", "step", "actor", "touch_minutes", "type"]


def num(value, field, row_id):
    if value is None or str(value).strip() == "":
        return 0.0
    try:
        return float(str(value).strip())
    except ValueError:
        sys.exit(f"Error: {field} for step {row_id} is not a number: {value!r}")


def yes(value):
    return str(value or "").strip().lower() in {"y", "yes", "true", "1"}


def load(path):
    try:
        with open(path, newline="", encoding="utf-8-sig") as handle:
            rows = list(csv.DictReader(handle))
    except FileNotFoundError:
        sys.exit(f"Error: file not found: {path}")
    if not rows:
        sys.exit(f"Error: {path} has no rows.")
    missing = [c for c in REQUIRED if c not in rows[0]]
    if missing:
        sys.exit(f"Error: {path} is missing required columns: {', '.join(missing)}")
    steps = []
    for row in rows:
        sid = (row.get("step_id") or "").strip()
        if not sid:
            continue
        step_type = (row.get("type") or "").strip().lower()
        if step_type not in STEP_TYPES:
            sys.exit(
                f"Error: step {sid} has type {step_type!r}. Use one of: {', '.join(STEP_TYPES)}"
            )
        steps.append({
            "id": sid,
            "step": (row.get("step") or "").strip(),
            "actor": (row.get("actor") or "").strip() or "unassigned",
            "tool": (row.get("tool") or "").strip(),
            "touch": num(row.get("touch_minutes"), "touch_minutes", sid),
            "wait": num(row.get("wait_minutes"), "wait_minutes", sid),
            "type": step_type,
            "pain": num(row.get("pain"), "pain", sid),
            "error_prone": yes(row.get("error_prone")),
            "single_point": yes(row.get("single_point")),
            "autonomy": (row.get("autonomy") or "").strip(),
            "checkpoint": (row.get("checkpoint") or "").strip(),
        })
    return steps


def safe_label(text):
    return text.replace('"', "'").replace("[", "(").replace("]", ")")


def mermaid(steps, title):
    lines = ["```mermaid", "flowchart TD"]
    if title:
        lines.insert(1, f"%% {safe_label(title)}")
    for s in steps:
        label = f"{s['id']}: {s['step']}<br/><small>{s['actor']}"
        if s["tool"]:
            label += f" · {s['tool']}"
        label += f" · {s['touch']:g} min"
        if s["autonomy"]:
            label += f" · {s['autonomy']}"
        label += "</small>"
        label = safe_label(label)
        node = s["id"].replace(" ", "_")
        if s["type"] in CIRCLED:
            lines.append(f'    {node}(("{label}"))')
        elif s["type"] == "wait":
            lines.append(f'    {node}>"{label}"]')
        else:
            lines.append(f'    {node}["{label}"]')
    for a, b in zip(steps, steps[1:]):
        lines.append(f"    {a['id'].replace(' ', '_')} --> {b['id'].replace(' ', '_')}")
    lines.append("    classDef circled fill:#fde68a,stroke:#92400e,stroke-width:2px")
    lines.append("    classDef underlined fill:#dbeafe,stroke:#1e3a8a,stroke-dasharray: 4 2")
    lines.append("    classDef waiting fill:#f3f4f6,stroke:#6b7280")
    for s in steps:
        node = s["id"].replace(" ", "_")
        if s["type"] in CIRCLED:
            lines.append(f"    class {node} circled")
        elif s["type"] in UNDERLINED:
            lines.append(f"    class {node} underlined")
        elif s["type"] == "wait":
            lines.append(f"    class {node} waiting")
    lines.append("```")
    lines.append("")
    lines.append("Legend: rounded and yellow = circled (judgment, approval, communication, stays human); "
                 "dashed blue = underlined (copy, lookup, transform, hand over first); grey = waiting.")
    return "\n".join(lines)


MACHINE_WORDS = ("automation", "system", "bot", "script", "flow")


def is_machine(actor):
    a = actor.strip().lower()
    return a == "ai" or a.startswith("ai ") or a.startswith("ai-") or any(w in a for w in MACHINE_WORDS)


def stats(steps, frequency):
    touch = sum(s["touch"] for s in steps)
    wait = sum(s["wait"] for s in steps)
    people = [s for s in steps if not is_machine(s["actor"])]
    handoffs = sum(1 for a, b in zip(people, people[1:]) if a["actor"] != b["actor"])
    machine_steps = len(steps) - len(people)
    by_type = OrderedDict((t, 0.0) for t in STEP_TYPES)
    for s in steps:
        by_type[s["type"]] += s["touch"]
    by_actor = OrderedDict()
    for s in steps:
        by_actor[s["actor"]] = by_actor.get(s["actor"], 0.0) + s["touch"]
    return {
        "steps": len(steps),
        "touch": touch,
        "wait": wait,
        "cycle": touch + wait,
        "handoffs": handoffs,
        "machine_steps": machine_steps,
        "by_type": by_type,
        "by_actor": by_actor,
        "monthly_hours": touch * frequency / 60 if frequency else None,
        "single_points": [s for s in steps if s["single_point"]],
        "error_prone": [s for s in steps if s["error_prone"]],
        "top_pain": sorted([s for s in steps if s["pain"] > 0], key=lambda s: -s["pain"])[:3],
    }


def pct(part, whole):
    return f"{(100 * part / whole):.0f}%" if whole else "n/a"


def report(steps, st, label):
    out = [f"### {label}: summary", ""]
    out.append("| Measure | Value |")
    out.append("|---|---|")
    out.append(f"| Steps | {st['steps']} |")
    out.append(f"| Hands-on (touch) minutes per occurrence | {st['touch']:g} |")
    out.append(f"| Waiting minutes per occurrence | {st['wait']:g} |")
    out.append(f"| Cycle time per occurrence (touch + wait) | {st['cycle']:g} min |")
    out.append(f"| Handoffs between people | {st['handoffs']} |")
    out.append(f"| Steps done by AI or automation | {st['machine_steps']} |")
    if st["monthly_hours"] is not None:
        out.append(f"| Hands-on hours per month | {st['monthly_hours']:.1f} |")
    out.append("")
    out.append("**Where the hands-on time goes, by step type**")
    out.append("")
    out.append("| Step type | Minutes | Share | Group |")
    out.append("|---|---|---|---|")
    for t, m in st["by_type"].items():
        if m:
            group = "circled" if t in CIRCLED else "underlined" if t in UNDERLINED else ""
            out.append(f"| {t} | {m:g} | {pct(m, st['touch'])} | {group} |")
    underlined = sum(m for t, m in st["by_type"].items() if t in UNDERLINED)
    circled = sum(m for t, m in st["by_type"].items() if t in CIRCLED)
    out.append("")
    out.append(f"Underlined (copying) time: {underlined:g} min ({pct(underlined, st['touch'])}). "
               f"Circled (judgment) time: {circled:g} min ({pct(circled, st['touch'])}).")
    out.append("")
    out.append("**Hands-on minutes by role**")
    out.append("")
    out.append("| Role | Minutes | Share |")
    out.append("|---|---|---|")
    for actor, m in st["by_actor"].items():
        out.append(f"| {actor} | {m:g} | {pct(m, st['touch'])} |")
    out.append("")
    if st["single_points"]:
        out.append("**Single points of knowledge:** " + ", ".join(
            f"{s['id']} ({s['step']})" for s in st["single_points"]))
        out.append("")
    if st["error_prone"]:
        out.append("**Error-prone steps:** " + ", ".join(
            f"{s['id']} ({s['step']})" for s in st["error_prone"]))
        out.append("")
    if st["top_pain"]:
        out.append("**Most painful steps:** " + ", ".join(
            f"{s['id']} ({s['step']}, pain {s['pain']:g})" for s in st["top_pain"]))
        out.append("")
    return "\n".join(out)


def compare(cur, fut, frequency):
    saved = cur["touch"] - fut["touch"]
    out = ["### Before and after", ""]
    out.append("| Measure | Current | Future | Change |")
    out.append("|---|---|---|---|")
    out.append(f"| Steps | {cur['steps']} | {fut['steps']} | {fut['steps'] - cur['steps']:+d} |")
    out.append(f"| Touch minutes per occurrence | {cur['touch']:g} | {fut['touch']:g} | {-saved:+g} |")
    out.append(f"| Wait minutes per occurrence | {cur['wait']:g} | {fut['wait']:g} | {fut['wait'] - cur['wait']:+g} |")
    out.append(f"| Handoffs between people | {cur['handoffs']} | {fut['handoffs']} | {fut['handoffs'] - cur['handoffs']:+d} |")
    out.append(f"| Steps done by AI or automation | {cur['machine_steps']} | {fut['machine_steps']} | "
               f"{fut['machine_steps'] - cur['machine_steps']:+d} |")
    if frequency:
        out.append(f"| Hands-on hours per month | {cur['monthly_hours']:.1f} | {fut['monthly_hours']:.1f} | "
                   f"{fut['monthly_hours'] - cur['monthly_hours']:+.1f} |")
    out.append("")
    out.append("These future-state minutes are estimates until Step 5 measures them. "
               "Make sure future touch minutes include the time a person spends reviewing AI output.")
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("current", help="Current-state step table CSV")
    parser.add_argument("--future", help="Future-state step table CSV (optional)")
    parser.add_argument("--frequency", type=float, default=0,
                        help="Occurrences per month, to compute monthly hours")
    parser.add_argument("--title", default="", help="Workflow name for the report heading")
    args = parser.parse_args()

    current = load(args.current)
    cur_stats = stats(current, args.frequency)
    heading = f"## Workflow map: {args.title}" if args.title else "## Workflow map"
    print(heading)
    print()
    print("### Current state")
    print()
    print(mermaid(current, args.title))
    print()
    print(report(current, cur_stats, "Current state"))
    if args.future:
        future = load(args.future)
        fut_stats = stats(future, args.frequency)
        print("### Future state")
        print()
        print(mermaid(future, args.title + " (future)" if args.title else "future"))
        print()
        print(report(future, fut_stats, "Future state"))
        print(compare(cur_stats, fut_stats, args.frequency))


if __name__ == "__main__":
    main()
