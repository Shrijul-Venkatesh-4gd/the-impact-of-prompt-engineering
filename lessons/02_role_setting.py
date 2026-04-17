"""
Lesson 2: Role Setting
======================

Assigning the model a role via the system message primes it to respond
with the right tone, vocabulary, and depth. Without a role, the model
defaults to generic "assistant" behaviour which is often shallow.

This matters even more for small models — they have less capacity to
infer your intent, so an explicit role acts like a strong prior that
steers generation in the right direction.

Key takeaway:
    Use the system message to define WHO the model is and HOW it
    should behave before asking your actual question.
"""

from utils import run_comparison

# ── Prompt pair ──────────────────────────────────────────────────────────

bad_messages = [
    {
        "role": "user",
        "content": "How do I handle errors in my code?",
    },
]

good_messages = [
    {
        "role": "system",
        "content": (
            "You are a senior Python developer who writes clean, production-grade "
            "code. When explaining concepts, you always include a short, runnable "
            "code example. You favour practical advice over theory."
        ),
    },
    {
        "role": "user",
        "content": "How do I handle errors in my code?",
    },
]

# ── Run ──────────────────────────────────────────────────────────────────

run_comparison(
    title="LESSON 2 — ROLE SETTING",
    bad_label="No system role",
    bad_messages=bad_messages,
    good_label="With expert role in system message",
    good_messages=good_messages,
    explanation=(
        "Without a role, the model gives a generic, surface-level answer.\n\n"
        "With a role like 'senior Python developer', the model anchors its\n"
        "vocabulary, examples, and depth to that persona. Notice how the\n"
        "good-prompt response is more practical and code-oriented."
    ),
)