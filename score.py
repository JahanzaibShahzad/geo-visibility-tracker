#!/usr/bin/env python3
"""
Score AI-visibility results.

Usage:
    python score.py --results results.csv [--brand "Acme Plumbing"]

Reads a results CSV with columns:
    date, platform, prompt_id, prompt_text, brand_mentioned, mention_position, notes

brand_mentioned: yes / no
mention_position: 1, 2, 3 ... (position of the brand in the answer's list, blank if not mentioned)

Prints a per-platform visibility report and an overall score.
"""

import argparse
import csv
from collections import defaultdict


def main():
    parser = argparse.ArgumentParser(description="Score AI-visibility results.")
    parser.add_argument("--results", required=True, help="Results CSV path")
    parser.add_argument("--brand", default="", help="Brand name (shown in the report header)")
    args = parser.parse_args()

    per_platform = defaultdict(lambda: {"asked": 0, "mentioned": 0, "positions": []})
    total_asked = 0
    total_mentioned = 0

    with open(args.results, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            platform = row.get("platform", "").strip() or "unknown"
            mentioned = row.get("brand_mentioned", "").strip().lower() == "yes"
            per_platform[platform]["asked"] += 1
            total_asked += 1
            if mentioned:
                per_platform[platform]["mentioned"] += 1
                total_mentioned += 1
                pos = row.get("mention_position", "").strip()
                if pos.isdigit():
                    per_platform[platform]["positions"].append(int(pos))

    header = f"AI Visibility Report for {args.brand}" if args.brand else "AI Visibility Report"
    print("=" * len(header))
    print(header)
    print("=" * len(header))

    if total_asked == 0:
        print("No results found in the CSV.")
        return

    for platform in sorted(per_platform):
        stats = per_platform[platform]
        rate = (stats["mentioned"] / stats["asked"] * 100) if stats["asked"] else 0
        avg_pos = ""
        if stats["positions"]:
            avg = sum(stats["positions"]) / len(stats["positions"])
            avg_pos = f", avg position {avg:.1f}"
        print(f"- {platform}: mentioned in {stats['mentioned']}/{stats['asked']} prompts ({rate:.0f}%){avg_pos}")

    overall = (total_mentioned / total_asked * 100) if total_asked else 0
    print("-" * 40)
    print(f"Overall visibility score: {overall:.0f}% ({total_mentioned}/{total_asked} prompts)")
    print()
    print("Tip: re-run the same prompts monthly and compare scores to track progress.")


if __name__ == "__main__":
    main()
