"""
Lesson 1: Specificity
=====================

The single most impactful prompting improvement is being specific.

Vague prompts force the model to guess what you want — and small models
guess poorly. A specific prompt narrows the problem space so even a 1.7B
parameter model can give a focused, useful answer.

Key takeaway:
    Tell the model WHAT you want, WHO it's for, HOW LONG it should be,
    and WHAT FORMAT to use.
"""

from utils import run_comparison

# ── Prompt pair ──────────────────────────────────────────────────────────

bad_messages = [
    {"role": "user", "content": "Tell me about Python."},
]

good_messages = [
    {
        "role": "user",
        "content": (
            "Explain three reasons why Python is a good first programming "
            "language for beginners. Keep each reason to one or two sentences."
        ),
    },
]

# ── Run ──────────────────────────────────────────────────────────────────

run_comparison(
    title="LESSON 1 — SPECIFICITY",
    bad_label="Vague prompt",
    bad_messages=bad_messages,
    good_label="Specific prompt",
    good_messages=good_messages,
    explanation=(
        "A vague prompt like 'Tell me about Python' could lead anywhere:\n"
        "the snake, the language, Monty Python, history, syntax, etc.\n"
        "The model wastes tokens figuring out scope.\n\n"
        "A specific prompt pins down the topic, audience, length, and structure\n"
        "so the model can focus entirely on generating useful content."
    ),
)