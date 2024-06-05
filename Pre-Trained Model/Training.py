import os
import cv2
import numpy as np
import pandas as pd
import mediapipe as mp
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands

# Function to extract key points from hand landmarks
def extract_keypoints(image):
    hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1)
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    keypoints = []
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                keypoints.append(landmark.x)
                keypoints.append(landmark.y)
                keypoints.append(landmark.z)
    return keypoints

# Load the dataset
data_dir = 'C:/Users/Elena/Downloads/asl_alphabet_test'
images = []
labels = []
for label in os.listdir(data_dir):
    label_dir = os.path.join(data_dir, label)
    if os.path.isdir(label_dir):
        for image_file in os.listdir(label_dir):
            image_path = os.path.join(label_dir, image_file)
            image = cv2.imread(image_path)
            keypoints = extract_keypoints(image)
            if keypoints:
                images.append(keypoints)
                labels.append(label)

# Convert to numpy arrays
X = np.array(images)
y = np.array(labels)

# Encode labels
le = LabelEncoder()
y = le.fit_transform(y)

# Normalize the data
X = np.array(X)
y = np.array(y)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Check data shape and label distribution
print(f'X_train shape: {X_train.shape}, X_test shape: {X_test.shape}')
print(f'y_train distribution: {np.bincount(y_train)}, y_test distribution: {np.bincount(y_test)}')

# Define the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(len(le.classes_), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Save the model
model.save('sign_language_model.h5')
np.save('classes.npy', le.classes_)
