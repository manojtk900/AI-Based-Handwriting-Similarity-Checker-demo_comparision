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
