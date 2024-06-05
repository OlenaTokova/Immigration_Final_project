import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Function to extract key points from hand landmarks
def extract_keypoints(results):
    keypoints = []
    for hand_landmarks in results.multi_hand_landmarks:
        for landmark in hand_landmarks.landmark:
            keypoints.append(landmark.x)
            keypoints.append(landmark.y)
            keypoints.append(landmark.z)
    return keypoints

# Load pre-trained model (Replace 'path_to_model' with your model path)
model = tf.keras.models.load_model('path_to_model')

# Function to recognize gestures using the trained model
def recognize_gestures():
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            keypoints = extract_keypoints(results)
            keypoints = np.array(keypoints).reshape(1, -1)
            prediction = model.predict(keypoints)
            predicted_label = np.argmax(prediction, axis=1)
            
            cv2.putText(frame, str(predicted_label), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('Sign Language Recognition', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Main function to call gesture recognition
def main():
    print("Starting sign language recognition...")
    recognize_gestures()

if __name__ == "__main__":
    main()
