"""
Lesson 4: Chain-of-Thought Reasoning
=====================================

Small models often fail at multi-step problems when asked for a direct
answer. They try to jump to the conclusion and get it wrong.

By asking the model to "think step by step", you force it to allocate
tokens to intermediate reasoning. Each generated step provides context
for the next, acting like scratch paper for the model.

Key takeaway:
    For any task that requires logic, math, or multi-step reasoning,
    explicitly ask the model to show its work step by step.
"""

from utils import run_comparison

# ── Prompt pair ──────────────────────────────────────────────────────────

bad_messages = [
    {
        "role": "user",
        "content": (
            "A store sells notebooks for $4 each. If you buy 3 or more, "
            "you get a 15% discount on the total. Tax is 8%. "
            "How much do you pay for 5 notebooks?"
        ),
    },
]

good_messages = [
    {
        "role": "user",
        "content": (
            "A store sells notebooks for $4 each. If you buy 3 or more, "
            "you get a 15% discount on the total. Tax is 8%. "
            "How much do you pay for 5 notebooks?\n\n"
            "Solve this step by step:\n"
            "Step 1: Calculate the price before discount.\n"
            "Step 2: Apply the discount.\n"
            "Step 3: Add tax to the discounted price.\n"
            "Step 4: State the final answer."
        ),
    },
]

# ── Run ──────────────────────────────────────────────────────────────────

run_comparison(
    title="LESSON 4 — CHAIN-OF-THOUGHT REASONING",
    bad_label="Direct question, no reasoning guidance",
    bad_messages=bad_messages,
    good_label="Step-by-step reasoning requested",
    good_messages=good_messages,
    explanation=(
        "Small models frequently make arithmetic and logic errors when\n"
        "they try to jump straight to the answer.\n\n"
        "The correct answer here is $18.36:\n"
        "  5 × $4 = $20  →  $20 × 0.85 = $17  →  $17 × 1.08 = $18.36\n\n"
        "By providing step-by-step scaffolding, we give the model a\n"
        "structured path to follow. Compare the two outputs and see\n"
        "which one gets closer to the correct answer."
    ),
    max_new_tokens=400,
)