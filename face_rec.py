import speech_recognition as sr
import cv2
import mediapipe as mp

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to convert speech to text
def speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)  # Using Google Web Speech API
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")


# Main function to call the speech, face, and gesture recognition functions
def main():
    print("Starting speech recognition...")
    speech_to_text()
    

if __name__ == "__main__":
    main()
