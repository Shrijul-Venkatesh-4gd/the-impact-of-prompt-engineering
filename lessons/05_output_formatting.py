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

JOB_POSTING = (
    "Hey folks! Super excited to finally open this req. We're Nimbus "
    "Logistics — our HQ is in Amsterdam but the whole engineering team "
    "is fully remote across the EU. The role is officially \"Lead "
    "Platform Engineer\" (our CEO keeps calling it \"Staff Infra Lead\" "
    "in meetings — please ignore, the official title is the first one). "
    "You'll need at least 7 years building distributed systems, ideally "
    "in Scala though strong Java folks are welcome too. You MUST have "
    "shipped something on AWS or GCP at real scale — Azure experience "
    "is nice to have but not required. Comp is €130k–€165k base plus "
    "equity. We're hoping to close this by end of April."
)

bad_messages = [
    {
        "role": "user",
        "content": f"Extract the key details from this job posting:\n\n{JOB_POSTING}",
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
            '  "title": "<official job title>",\n'
            '  "company": "<company name>",\n'
            '  "location": "<city, country>",\n'
            '  "remote": true | false,\n'
            '  "experience_years": <number>,\n'
            '  "required_skills": ["<skill1>", "<skill2>"],\n'
            '  "nice_to_have_skills": ["<skill1>"],\n'
            '  "salary_min": <number>,\n'
            '  "salary_max": <number>,\n'
            '  "salary_currency": "<currency code>"\n'
            '}\n\n'
            f"Job posting:\n{JOB_POSTING}"
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