import json
import re

# Load the extracted text
with open('extracted_text.json', 'r') as f:
    extracted_text = json.load(f)

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'\n+', ' ', text)  # Remove new lines
    return text

cleaned_text = {k: clean_text(v) for k, v in extracted_text.items()}

# Save the cleaned text
with open('cleaned_text.json', 'w') as f:
    json.dump(cleaned_text, f, indent=4)
