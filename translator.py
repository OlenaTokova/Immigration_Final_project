import os
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account
import openai

# Set up Google Translate API credentials
credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
if credentials_path is None:
    raise ValueError("The GOOGLE_APPLICATION_CREDENTIALS environment variable is not set.")
credentials = service_account.Credentials.from_service_account_file(credentials_path)
translate_client = translate.Client(credentials=credentials)

def translate_text(text, target_language):
    translation = translate_client.translate(text, target_language=target_language)
    return translation['translatedText']

def transcribe_audio(audio_base64):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Audio.transcribe(
        model="whisper-1",
        file=openai.File.create(file=audio_base64, purpose='transcription'),
        language="auto"
    )
    return response['text']
