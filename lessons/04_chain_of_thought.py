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

PROBLEM = (
    "A phone plan costs $45 per month. Taxes add 9% to the plan price. "
    "There is also a $6 monthly device fee that is NOT taxed. "
    "New customers get $8 off the pre-tax plan price for each of the "
    "first 3 months. How much does a new customer pay in total over "
    "the first 3 months?"
)

bad_messages = [
    {"role": "user", "content": PROBLEM},
]

good_messages = [
    {
        "role": "user",
        "content": (
            f"{PROBLEM}\n\n"
            "Solve this step by step:\n"
            "Step 1: Apply the $8 discount to the monthly plan price.\n"
            "Step 2: Add the 9% tax to the discounted plan price.\n"
            "Step 3: Add the $6 device fee (remember: not taxed).\n"
            "Step 4: Multiply the monthly total by 3.\n"
            "Step 5: State the final answer."
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
        "they try to jump straight to the answer. Watch out for the trap:\n"
        "the device fee is NOT taxed — small models usually miss that.\n\n"
        "The correct answer is $138.99:\n"
        "  ($45 − $8) = $37  →  $37 × 1.09 = $40.33  →  $40.33 + $6 = $46.33\n"
        "  $46.33 × 3 = $138.99\n\n"
        "By providing step-by-step scaffolding, we give the model a\n"
        "structured path to follow. Compare the two outputs and see\n"
        "which one gets closer to the correct answer."
    ),
    max_new_tokens=400,
)