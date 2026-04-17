"""
Case Study: Build Your Own Prompt
=================================

You've seen the five techniques in isolation. Now let's combine them.

SCENARIO:
    You're building a tool that reads customer support emails and
    extracts structured data so tickets can be auto-routed to the
    right team. Your input is a raw customer email. Your output
    needs to be a JSON object that a downstream system can parse.

This script runs FOUR versions of the prompt — from terrible to
production-grade — so you can see how stacking techniques transforms
the output.

After running this, try writing your OWN prompt in the playground
section at the bottom of this file.
"""

from utils import load_model, generate, print_header, print_prompt, print_response, DIM, RESET, BOLD, RED, YELLOW, CYAN, GREEN

# ── The raw customer email (same for all versions) ──────────────────────

CUSTOMER_EMAIL = """\
Subject: BROKEN SCREEN after 2 days!!!

Hi,

I bought the ProMax 15 phone from your website on March 3rd (order
#ORD-99821). It arrived on March 5th and the screen cracked on its
own the next morning — I didn't drop it or anything. There's a huge
crack going from the top left corner to the bottom right.

I want a full refund, not a replacement. I already bought another
phone because I need one for work. My phone number is 555-0178 and
my email is dana.cole@email.com.

This is really frustrating. I've been a customer for 3 years and
I've never had a problem before.

— Dana Cole
"""

load_model()

# ═══════════════════════════════════════════════════════════════════════
# VERSION 1: No techniques — the worst possible prompt
# ═══════════════════════════════════════════════════════════════════════

print_header("VERSION 1 — No techniques (baseline)")
print(f"{DIM}What happens when you just dump the email into the model.{RESET}\n")

v1_messages = [
    {"role": "user", "content": f"Handle this email:\n\n{CUSTOMER_EMAIL}"},
]

print_prompt("Prompt", v1_messages, RED)
print_response("Response", generate(v1_messages, max_new_tokens=400), RED)


# ═══════════════════════════════════════════════════════════════════════
# VERSION 2: Specificity only
# ═══════════════════════════════════════════════════════════════════════

print_header("VERSION 2 — Adding specificity")
print(f"{DIM}We tell the model exactly what to extract.{RESET}\n")

v2_messages = [
    {
        "role": "user",
        "content": (
            "Read the following customer support email and extract these "
            "details: customer name, order number, product name, issue "
            "description, and what the customer wants (refund, replacement, "
            "or other).\n\n"
            f"{CUSTOMER_EMAIL}"
        ),
    },
]

print_prompt("Prompt", v2_messages, YELLOW)
print_response("Response", generate(v2_messages, max_new_tokens=400), YELLOW)


# ═══════════════════════════════════════════════════════════════════════
# VERSION 3: Specificity + Role + Output format
# ═══════════════════════════════════════════════════════════════════════

print_header("VERSION 3 — Adding role setting + output format")
print(f"{DIM}We add a system role and request JSON output with a schema.{RESET}\n")

v3_messages = [
    {
        "role": "system",
        "content": (
            "You are a customer support ticket parser. You read raw customer "
            "emails and extract structured data. You always respond with valid "
            "JSON and nothing else — no explanation, no markdown fences."
        ),
    },
    {
        "role": "user",
        "content": (
            "Extract ticket data from this email into the following JSON format:\n\n"
            '{\n'
            '  "customer_name": "<full name>",\n'
            '  "email": "<email address>",\n'
            '  "phone": "<phone number>",\n'
            '  "order_id": "<order number>",\n'
            '  "product": "<product name>",\n'
            '  "issue_category": "damaged | defective | missing | wrong_item | other",\n'
            '  "issue_summary": "<one sentence summary>",\n'
            '  "resolution_requested": "refund | replacement | repair | other",\n'
            '  "sentiment": "angry | frustrated | neutral | satisfied",\n'
            '  "priority": "high | medium | low"\n'
            '}\n\n'
            f"Email:\n{CUSTOMER_EMAIL}"
        ),
    },
]

print_prompt("Prompt", v3_messages, CYAN)
print_response("Response", generate(v3_messages, max_new_tokens=400), CYAN)


# ═══════════════════════════════════════════════════════════════════════
# VERSION 4: All techniques — the production prompt
# ═══════════════════════════════════════════════════════════════════════

print_header("VERSION 4 — All techniques combined (production-grade)")
print(f"{DIM}We add few-shot examples and chain-of-thought reasoning.{RESET}\n")

v4_messages = [
    {
        "role": "system",
        "content": (
            "You are a customer support ticket parser. You read raw customer "
            "emails and extract structured data for an automated routing system.\n\n"
            "Rules:\n"
            "- Respond ONLY with valid JSON, no explanation or markdown.\n"
            "- If a field is not mentioned in the email, use null.\n"
            "- For priority: 'high' if the customer is angry or the issue "
            "affects their work/safety; 'medium' for frustrated customers; "
            "'low' for neutral inquiries.\n"
            "- For issue_category: choose the single best fit from the enum."
        ),
    },
    # Few-shot example 1
    {
        "role": "user",
        "content": (
            "Extract ticket data from this email:\n\n"
            "Subject: Wrong color\n"
            "Hi, I ordered the blue SmartWatch V2 (order #ORD-44210) but "
            "received a red one. Can you send the correct color? Thanks, "
            "Mike Rivera, mike.r@mail.com"
        ),
    },
    {
        "role": "assistant",
        "content": (
            '{\n'
            '  "customer_name": "Mike Rivera",\n'
            '  "email": "mike.r@mail.com",\n'
            '  "phone": null,\n'
            '  "order_id": "ORD-44210",\n'
            '  "product": "SmartWatch V2",\n'
            '  "issue_category": "wrong_item",\n'
            '  "issue_summary": "Received red SmartWatch V2 instead of the blue one ordered.",\n'
            '  "resolution_requested": "replacement",\n'
            '  "sentiment": "neutral",\n'
            '  "priority": "low"\n'
            '}'
        ),
    },
    # Few-shot example 2
    {
        "role": "user",
        "content": (
            "Extract ticket data from this email:\n\n"
            "Subject: Never arrived!!\n"
            "My order #ORD-78553 for the ErgoChair Plus was supposed to "
            "arrive last Monday. It's been 10 days and nothing. I work from "
            "home and my back is killing me. I need this resolved NOW. "
            "Please refund me. — Priya Sharma, priya.s@company.co, 555-9032"
        ),
    },
    {
        "role": "assistant",
        "content": (
            '{\n'
            '  "customer_name": "Priya Sharma",\n'
            '  "email": "priya.s@company.co",\n'
            '  "phone": "555-9032",\n'
            '  "order_id": "ORD-78553",\n'
            '  "product": "ErgoChair Plus",\n'
            '  "issue_category": "missing",\n'
            '  "issue_summary": "Order has not arrived after 10 days, affecting ability to work from home.",\n'
            '  "resolution_requested": "refund",\n'
            '  "sentiment": "angry",\n'
            '  "priority": "high"\n'
            '}'
        ),
    },
    # Actual email to parse
    {
        "role": "user",
        "content": (
            f"Extract ticket data from this email:\n\n{CUSTOMER_EMAIL}"
        ),
    },
]

print_prompt("Prompt", v4_messages, GREEN)
print_response("Response", generate(v4_messages, max_new_tokens=400), GREEN)


# ═══════════════════════════════════════════════════════════════════════
# PLAYGROUND: Try your own prompt!
# ═══════════════════════════════════════════════════════════════════════

print_header("YOUR TURN — Playground")
print(
    f"Edit the 'my_messages' list below and re-run this script to test\n"
    f"your own prompt against the same customer email.\n\n"
    f"The email is stored in the CUSTOMER_EMAIL variable — reference it\n"
    f"in your prompt with {{CUSTOMER_EMAIL}} inside an f-string.\n"
)

# ──────────────────────────────────────────────────────────────────────
# UNCOMMENT THE BLOCK BELOW AND WRITE YOUR OWN PROMPT
# ──────────────────────────────────────────────────────────────────────

# my_messages = [
#     {
#         "role": "system",
#         "content": "Your system message here...",
#     },
#     {
#         "role": "user",
#         "content": f"Your prompt here...\n\n{CUSTOMER_EMAIL}",
#     },
# ]
#
# print_prompt("Your prompt", my_messages, CYAN)
# print_response("Your response", generate(my_messages, max_new_tokens=400), CYAN)