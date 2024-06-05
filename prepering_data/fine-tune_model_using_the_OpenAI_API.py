import openai

openai.api_key = 'YOUR_API_KEY'

def fine_tune_model(training_data_path):
    response = openai.File.create(
        file=open(training_data_path, 'r'),
        purpose='fine-tune'
    )

    fine_tune = openai.FineTune.create(
        training_file=response['id'],
        model='davinci',
        n_epochs=4
    )

    return fine_tune

# Fine-tune the model with the preprocessed data
fine_tuned_model = fine_tune_model('visa_data.json')
