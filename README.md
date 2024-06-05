## Immigration Consulting Services
Welcome to the Immigration Consulting Services project. 
This web application is designed to assist users with various immigration-related tasks,
including filling out and editing PDF forms, recording and transcribing voice inputs, and providing real-time translations.


## Demo Video

[Watch Demo Video](https://drive.google.com/drive/folders/1A8aLb2WF7TV3xf7Fe11wGln0zlHtZjTv)


# Table of Contents
- Project Structure
- Environment Setup
- Voice Recorder and Translator
- Voice Recorder
- Translator
- Google Cloud Setup
- API Keys

# Project Structure

![image](https://github.com/OlenaTokova/Imigration_Final_project/assets/153076354/447fe5e4-7107-4633-808e-5ad72f16b2e4)


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




