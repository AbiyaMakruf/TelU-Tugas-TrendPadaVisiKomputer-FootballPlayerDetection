from flask import Flask, request, jsonify
from ultralytics import YOLO
import os
import numpy as np
import base64

import uuid

app = Flask(__name__)

# Load YOLO models
models = {
    "YOLOv12-n": YOLO("best_model/yolov12-s.pt"),
    "YOLOv12-s": YOLO("best_model/yolov12-s.pt"),
    "YOLOv12-m": YOLO("best_model/yolov12-s.pt")
}

# Create directory for saving images
INPUT_DIR = "images/input"
RESULT_DIR = "images/results"
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Football Player Detection API is running!"})

@app.route("/detect", methods=["POST"])
def detect():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    image_file = request.files["image"]
    model_variant = request.form.get("model_variant", "YOLOv8")
    threshold = float(request.form.get("threshold", 0.5))
    selected_classes = request.form.getlist("selected_classes")

    print("Model variant:", model_variant)
    print("Selected classes:", selected_classes)
    print(threshold)
    
    if model_variant not in models:
        return jsonify({"error": "Invalid model variant"}), 400
    
    # Generate unique filename
    filename = str(uuid.uuid4()) + ".jpg"
    input_path = os.path.join(INPUT_DIR, filename)
    result_path = os.path.join(RESULT_DIR, filename)
    
    # Save the input image
    image_file.save(input_path)
    
    # Run YOLO detection
    results = models[model_variant](input_path, conf=threshold, classes=[int(c) for c in selected_classes])
    results[0].save(result_path)

    # Buka hasil gambar dan ubah menjadi base64
    with open(result_path, "rb") as image_file:
        result_image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

    # Hapus file input dan output
    os.remove(input_path)
    os.remove(result_path)

    return jsonify({
        "message": "Detection complete",
        "result_image": result_image_base64
    })

if __name__ == "__main__":
    app.run(debug=True)
