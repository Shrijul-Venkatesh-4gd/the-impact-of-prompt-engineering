"""
utils.py — Shared model loading and inference helpers.

Loads SmolLM2-1.7B-Instruct once and provides a simple `generate` function
that all lesson scripts use. This keeps each lesson focused on the prompting
technique rather than boilerplate.
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "HuggingFaceTB/SmolLM2-360M-Instruct"

_model = None
_tokenizer = None


def load_model():
    """Load the model and tokenizer onto the GPU (or CPU fallback)."""
    global _model, _tokenizer

    if _model is not None:
        return _model, _tokenizer

    print(f"Loading {MODEL_ID} ...")
    device = "cuda" if torch.cuda.is_available() else "cpu"

    _tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    _model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        dtype=torch.float16 if device == "cuda" else torch.float32,
        device_map=device,
    )

    print(f"Model loaded on {device}.\n")
    return _model, _tokenizer


def generate(messages: list[dict], max_new_tokens: int = 300) -> str:
    """
    Generate a response from a list of chat messages.

    Args:
        messages: A list of dicts with 'role' and 'content' keys,
                  e.g. [{"role": "user", "content": "Hello"}]
        max_new_tokens: Maximum number of tokens to generate.

    Returns:
        The model's response as a string.
    """
    model, tokenizer = load_model()

    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
        )

    # Decode only the newly generated tokens
    new_tokens = output_ids[0][inputs["input_ids"].shape[1] :]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()


# ── Pretty printing helpers ──────────────────────────────────────────────

CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"
DIM = "\033[2m"


def print_header(title: str):
    width = 70
    print(f"\n{BOLD}{'═' * width}")
    print(f"  {title}")
    print(f"{'═' * width}{RESET}\n")


def print_prompt(label: str, messages: list[dict], color: str = CYAN):
    print(f"{color}{BOLD}┌─ {label}{RESET}")
    for msg in messages:
        role = msg["role"].upper()
        print(f"{color}│ [{role}]{RESET} {msg['content']}")
    print(f"{color}{BOLD}└─{RESET}")


def print_response(label: str, text: str, color: str = CYAN):
    print(f"\n{color}{BOLD}► {label}{RESET}")
    print(f"{DIM}{'─' * 50}{RESET}")
    print(text)
    print(f"{DIM}{'─' * 50}{RESET}\n")


def run_comparison(
    title: str,
    bad_label: str,
    bad_messages: list[dict],
    good_label: str,
    good_messages: list[dict],
    explanation: str,
    max_new_tokens: int = 300,
):
    """Run a side-by-side comparison of a bad and good prompt."""
    print_header(title)
    print(f"{DIM}{explanation}{RESET}\n")

    # ── Bad prompt ──
    print_prompt(f"❌ {bad_label}", bad_messages, RED)
    bad_response = generate(bad_messages, max_new_tokens=max_new_tokens)
    print_response("Response (bad prompt)", bad_response, RED)

    # ── Good prompt ──
    print_prompt(f"✅ {good_label}", good_messages, GREEN)
    good_response = generate(good_messages, max_new_tokens=max_new_tokens)
    print_response("Response (good prompt)", good_response, GREEN)