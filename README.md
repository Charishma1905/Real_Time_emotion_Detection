# Real_Time_emotion_Detection
 Real-Time Emotion Detection using Deep Learning
 Overview

This project implements a real-time emotion detection system using a webcam. It captures live video, detects faces, and predicts human emotions using pre-trained deep learning models from the DeepFace library.

The system identifies the dominant emotion in each frame and displays it on the screen.

 Features
Real-time webcam-based emotion detection
Uses pre-trained deep learning models (no custom training)
Displays dominant emotion on live video
Handles frames without faces safely
Simple and lightweight implementation
 Tech Stack
Programming Language
Python 3.10.11
Libraries Used
opencv-python (cv2) – video capture and display
deepface – emotion detection
dlib – face detection backend
face_recognition – facial processing support
numpy – numerical operations
pandas – data handling (optional, not used directly in core logic)
os – system operations (built-in)
cmake – required for dlib installation
Additional File
dlib-19.22.99-cp310-cp310-win_amd64.whl (manual installation for Windows)
Project Structure
emotion-detection/
│
├── main.py                # Main program
├── requirements.txt      # Dependencies (optional)
├── README.md             # Documentation
└── dlib wheel file       # For manual install (Windows)
 Installation
Step 1: Install Python

Make sure you have:

Python 3.10.11 installed
Step 2: Install Required Libraries
pip install numpy pandas deepface opencv-python face_recognition
Step 3: Install dlib (Important)

For Windows:

pip install dlib-19.22.99-cp310-cp310-win_amd64.whl

If this fails, your setup is weak (compiler issue). Fix CMake + Visual Studio Build Tools.

 How to Run
python main.py
Webcam opens automatically
Emotion is displayed on screen
Press q to exit
 Workflow
Capture video from webcam
Read frame-by-frame
Pass frame to DeepFace
Detect emotion using pre-trained model
Extract dominant emotion
Display emotion on screen
Repeat continuously
 Code Explanation (Core Logic)
cap = cv2.VideoCapture(0)
Opens webcam
result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
Analyzes emotion from frame
enforce_detection=False prevents crashes if no face is detected
emotion = result[0]['dominant_emotion']
Extracts the main emotion
cv2.putText()
Displays emotion on video
 Performance
Input FPS: ~25–30 FPS
Processing time: ~50–200 ms per frame
Output FPS: ~5–15 FPS

 This is not truly real-time at high performance — it’s limited by DeepFace processing.

Emotions Detected
Happy
Sad
Angry
Fear
Surprise
Neutral
Disgust
