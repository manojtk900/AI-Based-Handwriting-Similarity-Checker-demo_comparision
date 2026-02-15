from flask import Flask, render_template, request
import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def preprocess(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if image loaded correctly
    if img is None:
        print("Failed to load image:", image_path)
        return None

    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    return img.flatten().reshape(1, -1)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file1 = request.files.get("file1")
        file2 = request.files.get("file2")

        if not file1 or not file2:
            result = "Please upload both images."
            return render_template("index.html", result=result)

        path1 = os.path.join(UPLOAD_FOLDER, file1.filename)
        path2 = os.path.join(UPLOAD_FOLDER, file2.filename)

        file1.save(path1)
        file2.save(path2)

        vec1 = preprocess(path1)
        vec2 = preprocess(path2)

        if vec1 is None or vec2 is None:
            result = "Error loading image. Please upload valid JPG/PNG images."
            return render_template("index.html", result=result)

        similarity = cosine_similarity(vec1, vec2)[0][0]

        if similarity > 0.90:
            result = f"Same Writer ✅ (Similarity: {similarity:.2f})"
        else:
            result = f"Different Writer ❌ (Similarity: {similarity:.2f})"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
