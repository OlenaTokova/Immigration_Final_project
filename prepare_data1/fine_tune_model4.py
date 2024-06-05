import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to upload the training file
def upload_file(file_path):
    response = openai.File.create(
        file=open(file_path, "rb"),
        purpose='fine-tune'
    )
    return response

# Function to fine-tune the model
def fine_tune_model(training_file_id):
    response = openai.FineTune.create(
        training_file=training_file_id,
        model="davinci",  # You can choose another model if needed
        n_epochs=4
    )
    return response

# Upload the training data file
training_file_response = upload_file('training_data.jsonl')
training_file_id = training_file_response['id']

# Fine-tune the model with the uploaded file
fine_tuned_model = fine_tune_model(training_file_id)
print(fine_tuned_model)
