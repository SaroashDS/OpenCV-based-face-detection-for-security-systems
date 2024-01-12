# Face Detection System for Security Systems

<p align="center">
  <img src="https://github.com/SaroashDS/OpenCV-based-face-detection-for-security-systems/assets/144798692/d8c6768c-e65a-41b4-8f82-5a06a011ffcc" alt="Project Banner" width="400">
</p>

## Overview
Welcome to the Face Detection System for Security Systems project! This project is designed to implement a robust face detection and recognition system to enhance security measures. Leveraging computer vision techniques and machine learning, the system can detect and recognize faces in real-time.

## Problem Statement
In many security systems, the need for accurate and real-time identification of individuals is crucial. Traditional methods may fall short, leading to the development of this Face Detection System to address these concerns and provide a more effective solution.

## Solution
The project consists of three main components:

1. **Face Data Collection:**
   To build a reliable face recognition model, a module for face data collection has been implemented. This module captures facial images through the computer's webcam and stores them in a dataset directory. Users can specify the number of samples to collect. The datset can collect n nuber of images, you will have to specify in the script

![](https://github.com/SaroashDS/OpenCV-based-face-detection-for-security-systems/assets/144798692/da857817-1764-4d79-842f-ca53c3694bd5)

3. **Model Training:**
   The collected facial images are used to train the LBPH Face Recognizer model. This model learns the unique features of each individual's face and establishes a baseline for future recognition.
<p align="center">
  <img src="https://github.com/SaroashDS/OpenCV-based-face-detection-for-security-systems/assets/144798692/a6446794-2ec0-4de1-9bf5-4bf96d2b8528" alt="Image" width="400">
</p>

5. **Real-time Face Detection:**
   The core of the system lies in the real-time face detection and recognition module. This module continuously captures video frames from the webcam, detects faces, and recognizes individuals based on the trained model.
<p align="center">
  <img src="https://github.com/SaroashDS/OpenCV-based-face-detection-for-security-systems/assets/144798692/a2785ad2-2312-4eac-bd92-ceea4b2e20e4" alt="Image" width="400">
</p>

## Dependencies
- OpenCV: `pip install opencv-python`
- NumPy: `pip install numpy`

## How to Use
1. **Clone the repository:**
2. Install dependencies
3. Run the desired module:

   - Face Data Collection: python face_data_collection.py
   - Model Training: python train_model.py
   - Real-time Face Detection: python real_time_face_detection.py

## Results
The model performed very well and only detected the person (me) on which it was trained while it rejected others. The model confidence level was set on 85% for a better result.

**Unknown Person**

<p align="center">
  <img src="https://github.com/SaroashDS/OpenCV-based-face-detection-for-security-systems/assets/144798692/1ff0dd16-6b2b-4c26-9136-cb8fc0a5be1b" alt="Unknown Person" title="Unknown Person" width="400">
</p>


**Approved Person**

<p align="center">
  <img src="https://github.com/SaroashDS/OpenCV-based-face-detection-for-security-systems/assets/144798692/a2785ad2-2312-4eac-bd92-ceea4b2e20e4" alt="Image" title="Approved Person" width="400">
</p>

## Conclusion
The Face Detection System for Security Systems offers an effective and accessible solution for enhancing security measures through facial recognition technology. Your feedback is definitely appreicated. This will help me improve the project
