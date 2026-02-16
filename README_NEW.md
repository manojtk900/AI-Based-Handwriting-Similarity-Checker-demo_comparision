##
 
 Handwriting Writer Verification System (v2)
 
An AI-based handwriting verification system that determines whether two handwritten English samples belong to the same person using advanced image preprocessing and similarity analysis.

This upgraded version improves robustness using edge detection and adaptive thresholding techniques.
📌 Project Overview

This system allows users to upload two handwritten English images.
The application processes both images using computer vision techniques and compares their structural writing patterns using hybrid similarity metrics.
The system predicts whether both samples are written by the same person.
🚀 What's New in Version 2
Version 2 introduces significant improvements over the basic pixel comparison model:
Adaptive thresholding for lighting correction
Noise removal using Gaussian blur
Edge detection for capturing writing structure
Hybrid similarity (Cosine + Euclidean)
Improved decision threshold
Enhanced UI with colored results
🛠️ Technologies Used
Python
Flask
OpenCV
NumPy
Scikit-learn
🧠 How the System Works
Step 1: Image Upload
User uploads two handwritten English samples.
Step 2: Preprocessing
Each image undergoes:
Grayscale conversion
Gaussian blur (noise removal)
Adaptive thresholding
Canny edge detection
Resizing to 128×128
Normalization
Step 3: Feature Extraction
The processed image is flattened into a feature vector.
Step 4: Similarity Calculation
Hybrid similarity is computed using:
Cosine similarity
Euclidean distance adjustment
Step 5: Decision
If similarity score > 0.75
→ Same Writer ✅
Else
→ Different Writer ❌

#$📂 Project Structure
Copy code

handwriting_demo/
│
├── app.py
├── static/
│     └── uploads/
├── templates/
│     └── index.html
└── README.md
▶️ How to Run the Project
1️⃣ Clone Repository
Copy code

git clone <your_repo_link>
cd handwriting_demo
2️⃣ Create Virtual Environment
Copy code

python -m venv venv
3️⃣ Activate Environment (Windows)
Copy code

.\venv\Scripts\activate
4️⃣ Install Dependencies
Copy code

pip install flask opencv-python numpy scikit-learn
5️⃣ Run Application
Copy code

python app.py
6️⃣ Open Browser
Copy code

http://127.0.0.1:5000
##
⚠️ Limitations
No deep learning model yet
Sensitive to extreme rotation
Works best when same sentence is written
Prototype-level biometric verification
🔮 Future Improvements
CNN-based feature extraction
Siamese Neural Network implementation
Training on IAM Handwriting Dataset
Writer embedding generation
Accuracy benchmarking
Cloud deployment
REST API version
Mobile integration
🎯 Project Category
Computer Vision
Biometric Authentication
Writer Verification
Pattern Recognition
👨‍💻 Author
Manoj T K
Computer Science Engineering
AI & Machine Learning Enthusiast

--Thank you 🙏 ---------------_--------
