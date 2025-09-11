from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import load_dataset

# Load tokenizer and model
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# GPT-2 needs a padding token
tokenizer.pad_token = tokenizer.eos_token

# Load dataset
dataset = load_dataset("text", data_files={"train": "data/train.txt", "validation": "data/val.txt"})

# Tokenize
def tokenize(batch):
    tokens = tokenizer(
        batch["text"],
        truncation=True,
        padding="max_length",
        max_length=64
    )
    tokens["labels"] = tokens["input_ids"].copy()  # <--- fundamental
    return tokens

tokenized_dataset = dataset.map(tokenize, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="steps",
    eval_steps=10,
    logging_steps=5,
    learning_rate=5e-5,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    weight_decay=0.01,
    save_total_limit=2,
    num_train_epochs=3,
    fp16=True,  # Use mixed precision if your GPU supports it
    logging_dir='./logs'
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"]
)

# Train
trainer.train()

# Save
model.save_pretrained("./my_finetuned_model")
tokenizer.save_pretrained("./my_finetuned_model")