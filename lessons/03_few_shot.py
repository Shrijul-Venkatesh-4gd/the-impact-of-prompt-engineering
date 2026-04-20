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

TARGET_REVIEW = "Arrived two weeks late, but the product itself is genuinely great."

bad_messages = [
    {
        "role": "user",
        "content": (
            "What is the sentiment of this product review?\n\n"
            f"\"{TARGET_REVIEW}\""
        ),
    },
]

good_messages = [
    {
        "role": "user",
        "content": (
            "Classify the sentiment of product reviews as exactly one word: "
            "positive, negative, or neutral. Here are some examples:\n\n"
            "Review: \"Absolutely love this camera, best purchase ever!\"\n"
            "Sentiment: positive\n\n"
            "Review: \"Stopped working after two days, very disappointed.\"\n"
            "Sentiment: negative\n\n"
            "Review: \"Does what it says, nothing more.\"\n"
            "Sentiment: neutral\n\n"
            "Review: \"Took forever to ship but it's actually really good.\"\n"
            "Sentiment: positive\n\n"
            "Now classify this review using the exact same format:\n\n"
            f"Review: \"{TARGET_REVIEW}\"\n"
            "Sentiment:"
        ),
    },
]

# ── Run ──────────────────────────────────────────────────────────────────

run_comparison(
    title="LESSON 3 — FEW-SHOT EXAMPLES",
    bad_label="Zero-shot (no examples, vague format)",
    bad_messages=bad_messages,
    good_label="Few-shot (4 labelled examples)",
    good_messages=good_messages,
    explanation=(
        "The review below is mixed: late shipping (negative) but great\n"
        "product (positive). A small model with no examples will often\n"
        "ramble, hedge, or return a full paragraph of analysis instead\n"
        "of a single label.\n\n"
        "With 4 examples — including one 'late-but-good' case that matches\n"
        "our tricky review's pattern — the model locks onto the exact\n"
        "format ('Sentiment: <label>') and picks the dominant sentiment."
    ),
)