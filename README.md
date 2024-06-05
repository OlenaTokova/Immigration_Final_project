## Immigration Consulting Services
Welcome to the Immigration Consulting Services project. 
This web application is designed to assist users with various immigration-related tasks,
including filling out and editing PDF forms, recording and transcribing voice inputs, and providing real-time translations.

# Table of Contents
- Project Structure
- Environment Setup
- Voice Recorder and Translator
- Voice Recorder
- Translator
- Google Cloud Setup
- API Keys

# Project Structure

Immigration_Consulting_Services/
├── templates/
│   ├── home.html
│   ├── visa.html
│   ├── immigrant_visas.html
│   ├── non_immigrant_visas.html
│   ├── client.html
│   ├── applications.html
│   ├── edit_pdf.html
│   ├── voice_to_text.html
│   └── online_helper.html
├── static/
│   ├── style.css
│   └── log.png
├── client_applications/
│   ├── [PDF files will be saved here]
├── pdf_Application/
│   ├── [Edited PDF files will be saved here]
├── Addition_information/
│   ├── [Additional PDF files]
├── app.py
├── translator.py
├── forms.py
├── models.py
├── config.py
└── requirements.txt

# Environment Setup

Clone the repository

![image](https://github.com/OlenaTokova/Imigration_Final_project/assets/153076354/b3529559-44cf-44ae-a716-17870303ff90)

Set up a virtual environment

![image](https://github.com/OlenaTokova/Imigration_Final_project/assets/153076354/97041960-b23c-4ee8-a918-c628227c00a1)

Install the required dependencies
![image](https://github.com/OlenaTokova/Imigration_Final_project/assets/153076354/888f597b-97e3-472e-b6a4-99350c45a3e9)

# Set up environment variables:
Create a .env file in the project root and add the following environment variables:
![image](https://github.com/OlenaTokova/Imigration_Final_project/assets/153076354/26f37ecc-f034-4598-a482-44d4fa9bfd9a) 

# Voice Recorder and Translator
Voice Recorder
The voice recorder feature allows users to record their voice, transcribe it into text in real-time, and display the transcription on the webpage.

# Translator
The translator feature converts the transcribed text into the desired language in real-time.

# Google Cloud Setup
Create a project in Google Cloud Console:

- Go to Google Cloud Console.
- Create a new project.
- Enable necessary APIs:

# Enable the Google Cloud Speech-to-Text API.
- Enable the Google Cloud Translation API.
- Create a service account:
- Go to the IAM & Admin section.
- Create a new service account.
- Download the JSON key file and save it in your project directory.
- Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of this file.

API Keys
Ensure you have the following keys set up in your .env file:

![image](https://github.com/OlenaTokova/Imigration_Final_project/assets/153076354/c32f15d8-5b79-4e0e-ab59-f0ace9c0a8af)




