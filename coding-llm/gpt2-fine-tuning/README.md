# Fine-tuning GPT-2 
This project demonstrates how to fine-tune a GPT-2 model (or similar causal language models) on a custom text dataset using the Hugging Face Transformers and Datasets libraries.

This project was related to the free LLM course provided by [Hugging Face!](https://huggingface.co/learn/llm-course/en/chapter0/1?fw=pt)

### Features
- Loads and configure GPT-2
- Prepares dataset from raw `.txt`
- Tokenizes and batches data
- Configure training via `TrainingArguments`
- Saves and reload fine-tuned models locally

### Getting Started
**1. Install Dependencies**
```bash
uv add torch transformers datasets accelerate peft
```

**2. Prepare your dataset**
Add your text data in two files:
- `train.txt`: training data
- `val.txt`: validation data

Each line should contain one training example (more for some cases hahaha).

**3. Run**
- To run: `uv run .\train_gpt2.py`
- To test: `uv run .\test.py`

To understand more about the code, [click here!](/docs/explanation.md)