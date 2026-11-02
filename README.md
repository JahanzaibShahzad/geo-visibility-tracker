# GEO Visibility Tracker

A simple toolkit to measure how often your brand shows up in AI search answers
(ChatGPT, Perplexity, Gemini, Copilot, Google AI Overviews).

## Why this exists

Customers now ask AI assistants for recommendations instead of scrolling
Google results. If the AI never mentions your business, you are invisible to
that traffic. This toolkit gives you a repeatable way to test prompts, log
the answers, and score your visibility over time.

## How it works

AI platforms do not offer a free official API for answer testing, so the
testing step is manual and honest:

1. **Generate prompts** for your brand:
   `python prompts.py --brand "Acme Plumbing" --category "plumber" --city "Austin"`
   This writes `prompts.csv` with 12 test prompts (8 unbranded discovery
   prompts, 4 branded prompts that name your business directly).
2. **Ask each prompt** in ChatGPT, Perplexity, Gemini, and Copilot (free tiers
   are enough). Copy `results_template.csv` to `results.csv` and log every
   answer: was your brand mentioned, and at which position.
3. **Score the results**:
   `python score.py --results results.csv --brand "Acme Plumbing"`
   You get a per-platform mention rate and one overall visibility score.
4. **Repeat monthly** with the same prompts and compare scores to track
   whether your GEO work (reviews, citations, schema, PR mentions) is moving
   the needle.

## Files

- `prompts.py` - generates the test prompt set for any brand, category, and city
- `score.py` - scores a filled results CSV per platform and overall
- `results_template.csv` - template for logging answers (with two example rows)
- `requirements.txt` - no external dependencies, Python 3.8+ standard library only

## Scoring

Visibility score = prompts where your brand was mentioned / total prompts asked.
Unbranded prompts (e.g. "best plumber in Austin") measure discovery.
Branded prompts (e.g. "is Acme Plumbing good?") measure reputation accuracy.

## Notes

- Answers vary between runs and accounts; test on the same day for fair comparison.
- A mention with a correct link or phone number is worth more than a bare name mention; use the notes column.
- This measures visibility, not rankings. Pair it with classic local SEO (Google Business Profile, reviews, citations) for the full picture.

## License

MIT
