"""
Lesson 3: Few-Shot Examples
===========================

Instead of describing the output format you want, SHOW the model what
it looks like by providing a few examples. This is called "few-shot"
prompting and it's one of the most reliable ways to control a model's
output — especially a small one.

Small models struggle to follow complex format descriptions but are
surprisingly good at pattern-matching from examples.

Key takeaway:
    When you need a specific output structure, give 2-3 examples of
    input → output pairs. The model will mimic the pattern.
"""

from utils import run_comparison

# ── Prompt pair ──────────────────────────────────────────────────────────

bad_messages = [
    {
        "role": "user",
        "content": (
            "Classify the sentiment of these reviews as positive, negative, "
            "or neutral:\n"
            "1. The battery life is incredible, lasts all day.\n"
            "2. Broke after one week, total waste of money.\n"
            "3. It's an okay phone, nothing special."
        ),
    },
]

good_messages = [
    {
        "role": "user",
        "content": (
            "Classify the sentiment of product reviews. Here are some examples:\n\n"
            "Review: \"Absolutely love this camera, best purchase ever!\"\n"
            "Sentiment: positive\n\n"
            "Review: \"Stopped working after two days, very disappointed.\"\n"
            "Sentiment: negative\n\n"
            "Review: \"Does what it says, nothing more.\"\n"
            "Sentiment: neutral\n\n"
            "Now classify these reviews:\n\n"
            "Review: \"The battery life is incredible, lasts all day.\"\n"
            "Sentiment:\n\n"
            "Review: \"Broke after one week, total waste of money.\"\n"
            "Sentiment:\n\n"
            "Review: \"It's an okay phone, nothing special.\"\n"
            "Sentiment:"
        ),
    },
]

# ── Run ──────────────────────────────────────────────────────────────────

run_comparison(
    title="LESSON 3 — FEW-SHOT EXAMPLES",
    bad_label="Zero-shot (no examples)",
    bad_messages=bad_messages,
    good_label="Few-shot (3 examples provided)",
    good_messages=good_messages,
    explanation=(
        "Without examples, the model might return inconsistent formats:\n"
        "full sentences, extra commentary, different label names, etc.\n\n"
        "With a few examples, the model locks onto the exact pattern —\n"
        "'Sentiment: positive/negative/neutral' — and reproduces it\n"
        "consistently. This is especially powerful for classification tasks."
    ),
)