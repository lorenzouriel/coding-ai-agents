from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("./my_finetuned_model")
model = AutoModelForCausalLM.from_pretrained("./my_finetuned_model")

input_text = "Question: What is 2 + 2?\nAnswer:"
inputs = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_new_tokens=20,
    do_sample=True,
    top_p=0.9,
    temperature=0.7
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
