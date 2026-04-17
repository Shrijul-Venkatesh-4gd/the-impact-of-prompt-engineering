# Good Prompting Tutorial

A hands-on tutorial that demonstrates how prompt engineering dramatically improves LLM output — even on a small, locally-run model.

Each lesson runs the **same model** with a **bad prompt** and a **good prompt** side by side so you can see the difference for yourself.

## Why a Small Model?

This tutorial uses [SmolLM2-1.7B-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct) — a 1.7 billion parameter model that fits comfortably on a consumer GPU (or even CPU). We chose a small model deliberately: the gap between bad and good prompts is **more visible** on weaker models. If you can get a 1.7B model to produce structured, accurate output with the right prompt, imagine what these techniques do on a 70B+ model.

## Hardware Requirements

- **GPU**: Any NVIDIA GPU with 4GB+ VRAM (tested on RTX 3050 6GB)
- **CPU-only**: Works too, just slower (~30s per generation instead of ~3s)
- **RAM**: 8GB minimum
- **Disk**: ~4GB for the model download (cached after first run)

## Setup

```bash
git clone https://github.com/<your-username>/good-prompting-tutorial.git
cd good-prompting-tutorial

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

The model downloads automatically on first run (~3.4GB).

## Usage

Run lessons individually:

```bash
python 01_specificity.py
python 02_role_setting.py
python 03_few_shot.py
python 04_chain_of_thought.py
python 05_output_formatting.py
```

Or run all lessons in sequence:

```bash
python run_all.py
```

## Lessons

### 01 — Specificity

**Concept:** Vague prompts produce vague answers. Specific prompts produce useful ones.

- Bad: *"Tell me about Python."*
- Good: *"Explain three reasons why Python is a good first programming language for beginners. Keep each reason to one or two sentences."*

### 02 — Role Setting

**Concept:** A system message that defines the model's persona focuses its tone, vocabulary, and depth.

- Bad: Ask a question with no system context.
- Good: Set the model up as *"a senior Python developer who writes clean, production-grade code."*

### 03 — Few-Shot Examples

**Concept:** Instead of describing the output format, show the model 2–3 examples and let it pattern-match.

- Bad: Ask the model to classify sentiment with no examples.
- Good: Provide three labelled examples, then ask it to classify new inputs.

### 04 — Chain-of-Thought Reasoning

**Concept:** Asking the model to "think step by step" forces it to allocate tokens to intermediate reasoning, reducing errors on multi-step problems.

- Bad: Ask a math word problem directly.
- Good: Break the problem into numbered steps and ask the model to solve each one.

### 05 — Output Formatting

**Concept:** When you need structured output (JSON, CSV, etc.), provide the exact schema. Small models won't guess your format.

- Bad: Ask the model to extract data from text with no format guidance.
- Good: Provide a JSON template with field names and types.

## Experimenting

The best way to learn is to modify the prompts and re-run. Try:

- Making the "good" prompts worse — at what point does quality drop?
- Combining techniques (e.g., role setting + few-shot + output formatting).
- Swapping in a different model by changing `MODEL_ID` in `utils.py`.

## Project Structure

markdown```
├── README.md              ← You are here
├── requirements.txt       ← Python dependencies
├── utils.py               ← Model loading & comparison helpers
├── 01_specificity.py      ← Lesson 1
├── 02_role_setting.py     ← Lesson 2
├── 03_few_shot.py         ← Lesson 3
├── 04_chain_of_thought.py ← Lesson 4
├── 05_output_formatting.py← Lesson 5
└── run_all.py             ← Run every lesson in sequence
```