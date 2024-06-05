import json

# Load the cleaned text
with open('cleaned_text.json', 'r') as f:
    cleaned_text = json.load(f)

# Convert cleaned text to JSONL format
with open('training_data.jsonl', 'w') as f:
    for k, v in cleaned_text.items():
        json.dump({"prompt": f"{k}: ", "completion": v}, f)
        f.write("\n")
