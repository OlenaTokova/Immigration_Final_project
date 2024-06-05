import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to generate advice
def generate_advice(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # Replace with your fine-tuned model ID if applicable
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Test the fine-tuned model with a sample prompt
prompt = "What documents are needed for an F-1 Student Visa?"
advice = generate_advice(prompt)
print(advice)
