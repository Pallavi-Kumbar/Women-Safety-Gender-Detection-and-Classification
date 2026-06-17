# AI-Based Women Safety Analysis using Real-Time Gender Detection

## Overview

AI-Based Women Safety Analysis is a computer vision project that performs real-time face detection and gender classification using TensorFlow and OpenCV. The system analyzes live webcam feeds, identifies male and female individuals, calculates a crowd-based risk score, and generates alerts when a potentially unsafe situation is detected.

This project demonstrates the application of Machine Learning, Computer Vision, and Real-Time Video Processing for safety monitoring and risk assessment.

---

## Features

* Real-time webcam-based monitoring
* Face detection using OpenCV
* Gender classification using a CNN model built with TensorFlow
* Male and female population counting
* Dynamic risk assessment based on crowd composition
* Automated alert generation for high-risk situations
* Automatic capture and storage of high-risk frames

---

## Project Architecture

```text
Webcam Feed
      │
      ▼
Face Detection (OpenCV)
      │
      ▼
Face Extraction
      │
      ▼
Gender Classification (TensorFlow CNN)
      │
      ▼
Male/Female Counting
      │
      ▼
Risk Assessment Engine
      │
      ▼
Alert Generation & Frame Capture
```

---

## Dataset

The model is trained using the UTKFace Dataset.

Dataset Attributes:

* Age
* Gender
* Race

Gender Labels:

* 0 → Male
* 1 → Female

---

## Technologies Used

* Python
* TensorFlow
* OpenCV
* Scikit-learn
* NumPy

---

## Project Structure

```text
WomenSafetyProject/
│
├── dataset/
│   ├── male/
│   └── female/
│
├── models/
│   └── gender_model.h5
│
├── alerts/
│
├── train.py
├── detect.py
├── safety_analyzer.py
└── prepare_dataset.py
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd WomenSafetyProject
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install tensorflow
pip install opencv-python
pip install numpy
pip install pandas
pip install scikit-learn
pip install matplotlib
```

---

## Training the Model

Prepare the dataset:

```bash
python prepare_dataset.py
```

Train the gender classification model:

```bash
python train.py
```

The trained model will be saved inside:

```text
models/gender_model.h5
```

---

## Running the Project

Start real-time detection:

```bash
python detect.py
```

Press **Q** to exit the application.

---

## Sample Output

```text
Male Count      : 6
Female Count    : 2
Danger Score    : 75
Risk Level      : HIGH RISK
Alert Generated : YES
```

---

## Future Enhancements

* YOLO-based face/person detection
* MobileNet/EfficientNet transfer learning
* Email and SMS alerts
* Dashboard for analytics and visualization
* Location-aware safety monitoring
* Cloud deployment for real-time surveillance

---

## Learning Outcomes

* Computer Vision using OpenCV
* Convolutional Neural Networks (CNNs)
* TensorFlow Model Training
* Real-Time Video Processing
* Machine Learning Model Evaluation
* Risk Assessment and Alert Systems

---
