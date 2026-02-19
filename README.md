✍️ Handwriting Writer Verification System

A simple AI-based system that verifies whether two handwritten English samples belong to the same person using image similarity techniques.

📌 Project Overview

This project demonstrates a basic handwriting verification system where users can upload two handwritten images. The system compares them using cosine similarity and determines whether they were written by the same person.

This is a prototype version built using Flask and OpenCV.

🚀 Features

Upload two handwritten images

Automatic grayscale conversion

Image resizing and normalization

Cosine similarity comparison

Similarity confidence score

Simple and clean UI

Built with Flask backend

🛠️ Technologies Used

Python

Flask

OpenCV

NumPy

Scikit-learn

🧠 How It Works

User uploads two handwritten English images.

Images are converted to grayscale.

Images are resized to 128x128.

Pixel values are normalized.

Cosine similarity is calculated between image vectors.

If similarity is above threshold (0.90), system predicts same writer.


📂 Project Structure
handwriting_demo/
│
├── app.py
├── static/
│     └── uploads/
├── templates/
│     └── index.html
└── README.md

▶️ How to Run the Project

Clone the repository:

git clone <your_repo_link>
cd handwriting_demo


Create virtual environment:

python -m venv venv


Activate virtual environment:

Windows:

.\venv\Scripts\activate


Install dependencies:

pip install flask opencv-python numpy scikit-learn


Run the application:

python app.py


Open browser:

http://127.0.0.1:5000

⚠️ Limitations

Pixel-based comparison only

Sensitive to lighting and rotation

No deep learning model used

Prototype level implementation

🔮 Future Improvements

CNN-based feature extraction

Siamese Neural Network

Writer embedding model

Noise removal and background correction

Accuracy evaluation metrics

Dataset training (IAM Dataset)

Deployment to cloud

🎯 Future Scope

This project can be extended into a full AI-powered biometric writer verification system using deep learning techniques such as Siamese Networks and Contrastive Loss.

Author

Manoj T K
Computer Science Engineering
Machine Learning & AI Enthusiast
