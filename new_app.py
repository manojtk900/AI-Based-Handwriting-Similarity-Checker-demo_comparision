from flask import Flask, render_template, request
import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def preprocess(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Failed to load image:", image_path)
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Remove noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Adaptive threshold
    thresh = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11,
        2
    )

    # Edge detection
    edges = cv2.Canny(thresh, 50, 150)

    # Resize
    resized = cv2.resize(edges, (128, 128))

    # Normalize
    normalized = resized / 255.0

    return normalized.flatten().reshape(1, -1)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    color = "white"

    if request.method == "POST":
        file1 = request.files.get("file1")
        file2 = request.files.get("file2")

        if not file1 or not file2:
            result = "Please upload both images."
            color = "yellow"
            return render_template("index.html", result=result, color=color)

        path1 = os.path.join(UPLOAD_FOLDER, file1.filename)
        path2 = os.path.join(UPLOAD_FOLDER, file2.filename)

        file1.save(path1)
        file2.save(path2)

        vec1 = preprocess(path1)
        vec2 = preprocess(path2)

        if vec1 is None or vec2 is None:
            result = "Error loading image. Upload valid JPG/PNG files."
            color = "red"
            return render_template("index.html", result=result, color=color)

        # Hybrid similarity
        cos_sim = cosine_similarity(vec1, vec2)[0][0]
        euclid_dist = np.linalg.norm(vec1 - vec2)
        similarity = cos_sim - (euclid_dist * 0.01)

        if similarity > 0.75:
            result = f"Same Writer ✅ (Score: {similarity:.2f})"
            color = "lime"
        else:
            result = f"Different Writer ❌ (Score: {similarity:.2f})"
            color = "red"

    return render_template("index.html", result=result, color=color)


if __name__ == "__main__":
    app.run(debug=True)
