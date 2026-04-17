"""
Lesson 5: Output Formatting
============================

When you need structured output (JSON, CSV, markdown tables, etc.),
you must explicitly define the format. Small models won't guess it.

This is critical for real-world use cases where LLM output feeds into
downstream code — a JSON response that's sometimes valid and sometimes
prose is useless in a pipeline.

Key takeaway:
    Specify the exact output format, field names, and data types.
    Show a skeleton of the desired structure if possible.
"""

from utils import run_comparison

# ── Prompt pair ──────────────────────────────────────────────────────────

bad_messages = [
    {
        "role": "user",
        "content": (
            "Extract the key details from this job posting:\n\n"
            "We're hiring a Senior Backend Engineer at Acme Corp in Berlin. "
            "The role requires 5+ years of experience with Go or Rust, "
            "familiarity with Kubernetes, and strong system design skills. "
            "Salary range is €85,000–€110,000. Remote-friendly."
        ),
    },
]

good_messages = [
    {
        "role": "system",
        "content": (
            "You are a structured data extraction assistant. "
            "You always respond with valid JSON and nothing else — no "
            "explanation, no markdown, just the JSON object."
        ),
    },
    {
        "role": "user",
        "content": (
            "Extract the key details from this job posting into the "
            "following JSON format:\n\n"
            '{\n'
            '  "title": "<job title>",\n'
            '  "company": "<company name>",\n'
            '  "location": "<city, country>",\n'
            '  "remote": true | false,\n'
            '  "experience_years": <number>,\n'
            '  "skills": ["<skill1>", "<skill2>"],\n'
            '  "salary_min": <number>,\n'
            '  "salary_max": <number>,\n'
            '  "salary_currency": "<currency code>"\n'
            '}\n\n'
            "Job posting:\n"
            "We're hiring a Senior Backend Engineer at Acme Corp in Berlin. "
            "The role requires 5+ years of experience with Go or Rust, "
            "familiarity with Kubernetes, and strong system design skills. "
            "Salary range is €85,000–€110,000. Remote-friendly."
        ),
    },
]

# ── Run ──────────────────────────────────────────────────────────────────

run_comparison(
    title="LESSON 5 — OUTPUT FORMATTING",
    bad_label="No format specified",
    bad_messages=bad_messages,
    good_label="Explicit JSON schema provided",
    good_messages=good_messages,
    explanation=(
        "Without format instructions, the model returns free-form text.\n"
        "That's fine for humans but useless if you need to parse the output\n"
        "programmatically.\n\n"
        "By providing the exact JSON schema, the model fills in the blanks\n"
        "like a form. This combines two techniques: role setting (system\n"
        "message) and output formatting (explicit schema in the user message)."
    ),
)