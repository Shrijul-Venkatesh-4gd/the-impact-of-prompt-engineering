"""
main.py — Run all lessons back-to-back.

This loads the model once and then runs each lesson in order.
Useful for a full demo walkthrough.
"""

import importlib.util
import sys
from pathlib import Path

lessons = [
    "01_specificity",
    "02_role_setting",
    "03_few_shot",
    "04_chain_of_thought",
    "05_output_formatting",
]

# Pre-load the model once before running lessons
from utils import load_model, BOLD, RESET, CYAN

load_model()

print(f"\n{BOLD}{CYAN}{'=' * 70}")
print(f"  GOOD PROMPTING TUTORIAL — Running all 5 lessons")
print(f"{'=' * 70}{RESET}\n")

for lesson in lessons:
    print(f"\n{'▓' * 70}\n")
    try:
        filepath = Path(__file__).parent / "lessons" / f"{lesson}.py"
        spec = importlib.util.spec_from_file_location(lesson, filepath)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except Exception as e:
        print(f"Error running {lesson}: {e}", file=sys.stderr)

print(f"\n{BOLD}{CYAN}{'=' * 70}")
print(f"  All lessons complete!")
print(f"{'=' * 70}{RESET}\n")