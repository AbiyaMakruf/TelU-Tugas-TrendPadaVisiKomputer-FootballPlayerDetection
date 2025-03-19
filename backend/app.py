from flask import Flask, request, jsonify
from ultralytics import YOLO
import os
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

@app.route("/predict", methods=["POST"])
def detect():
    # Periksa apakah ada file gambar
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    image_file = request.files["image"]
    model_variant = request.form.get("model_variant", "YOLOv12-n")  # Default ke YOLOv12-n
    threshold = float(request.form.get("threshold", 0.5))
    
    # Ambil dan validasi kelas yang dipilih
    selected_classes = request.form.getlist("selected_classes")  # Mendapatkan list dari form-data
    try:
        selected_classes = [int(c) for c in selected_classes if c.isdigit()]  # Hanya angka yang valid
    except ValueError:
        return jsonify({"error": "Invalid class IDs"}), 400

    # Validasi apakah model tersedia
    if model_variant not in models:
        return jsonify({"error": "Invalid model variant"}), 400

    # Simpan gambar sementara dengan nama unik
    filename = str(uuid.uuid4()) + ".jpg"
    input_path = os.path.abspath(os.path.join(INPUT_DIR, filename))
    result_path = os.path.abspath(os.path.join(RESULT_DIR, filename))

    image_file.save(input_path)

    try:
        # Jalankan deteksi dengan YOLO
        results = models[model_variant](input_path, conf=threshold, classes=selected_classes)

        # Ambil bounding box, confidence, dan class ID dari hasil deteksi
        detections = []
        for result in results:
            for box in result.boxes:
                detections.append({
                    "class_id": int(box.cls.item()),  # ID kelas
                    "confidence": float(box.conf.item()),  # Confidence score
                    "bbox": [float(i) for i in box.xywhn[0].tolist()]  # [x_center, y_center, width, height] normalisasi
                })

        # Simpan hasil gambar
        results[0].save(result_path)

        # Buka hasil gambar dan ubah menjadi base64
        with open(result_path, "rb") as image_file:
            result_image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

        # Hapus file input dan output untuk menghemat penyimpanan
        os.remove(input_path)
        os.remove(result_path)

        return jsonify({
            "message": "Detection complete",
            "result_image": result_image_base64,
            "detections": detections  # Mengembalikan data deteksi untuk statistik
        })

    except Exception as e:
        # Jika terjadi kesalahan, hapus file input untuk menghindari penyimpanan yang tidak perlu
        if os.path.exists(input_path):
            os.remove(input_path)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
