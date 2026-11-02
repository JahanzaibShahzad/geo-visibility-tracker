#!/usr/bin/env python3
"""
Generate AI-visibility test prompts for a brand.

Usage:
    python prompts.py --brand "Acme Plumbing" --category "plumber" --city "Austin" [--out prompts.csv]

The script writes a CSV of ready-to-ask prompts. Ask each prompt in
ChatGPT, Perplexity, Gemini, and Copilot, then log the answers in
results_template.csv and run score.py.
"""

import argparse
import csv

PROMPT_TEMPLATES = [
    "Who is the best {category} in {city}?",
    "Recommend a reliable {category} near {city}.",
    "I need a {category} in {city}. Who should I call?",
    "Which {category} in {city} has the best reviews?",
    "Compare the top {category} options in {city}.",
    "What is the most trusted {category} in {city}?",
    "Find me an affordable {category} in {city}.",
    "Which {category} in {city} would you pick for urgent work?",
    "List highly rated {category} businesses in {city}.",
    "Is {brand} a good {category} in {city}?",
    "What do people say about {brand} in {city}?",
    "Should I hire {brand} for {category} work in {city}?",
]


def main():
    parser = argparse.ArgumentParser(description="Generate AI-visibility test prompts for a brand.")
    parser.add_argument("--brand", required=True, help="Brand or business name, e.g. 'Acme Plumbing'")
    parser.add_argument("--category", required=True, help="Business category, e.g. 'plumber'")
    parser.add_argument("--city", required=True, help="City, e.g. 'Austin'")
    parser.add_argument("--out", default="prompts.csv", help="Output CSV path")
    args = parser.parse_args()

    rows = []
    for i, template in enumerate(PROMPT_TEMPLATES, start=1):
        prompt_text = template.format(brand=args.brand, category=args.category, city=args.city)
        kind = "branded" if "{brand}" in template else "unbranded"
        rows.append({"prompt_id": f"P{i:02d}", "kind": kind, "prompt_text": prompt_text})

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["prompt_id", "kind", "prompt_text"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} prompts to {args.out}")
    print("Next: ask each prompt in ChatGPT, Perplexity, Gemini, and Copilot,")
    print("log the answers in results_template.csv, then run: python score.py --results results.csv")


if __name__ == "__main__":
    main()
