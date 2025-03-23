from flask import Flask, request, jsonify
from ultralytics import YOLO
import os
import base64

import uuid

app = Flask(__name__)

# Load YOLO models
models = {
    "YOLOv12-n": YOLO("best_model/nano-720.pt"),
    "YOLOv12-s": YOLO("best_model/small-720.pt"),
    "YOLOv12-m": YOLO("best_model/medium-720.pt")
}

INPUT_DIR = "predicts/input"
RESULT_DIR = "predicts/results"
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Football Player Detection API is running!"})

@app.route("/predict", methods=["POST"])
def detect():
    if "image" in request.files:
        return process_image(request)
    elif "video" in request.files:
        return process_video(request)
    else:
        return jsonify({"error": "No image or video provided"}), 400

def process_image(request):
    image_file = request.files["image"]
    model_variant, threshold, selected_classes = get_request_parameters(request)
    
    if model_variant not in models:
        return jsonify({"error": "Invalid model variant"}), 400
    
    filename = str(uuid.uuid4()) + ".jpg"
    input_path = os.path.join(INPUT_DIR, filename)
    result_path = os.path.join(RESULT_DIR, filename)
    
    image_file.save(input_path)
    try:
        results = models[model_variant](input_path, conf=threshold, classes=selected_classes)
        detections = extract_detections(results)
        results[0].save(result_path)
        
        with open(result_path, "rb") as img_file:
            result_image_base64 = base64.b64encode(img_file.read()).decode("utf-8")
        
        cleanup_files([input_path, result_path])
        return jsonify({
            "message": "Detection complete",
            "result_image": result_image_base64,
            "detections": detections
        })
    except Exception as e:
        cleanup_files([input_path])
        return jsonify({"error": str(e)}), 500

def process_video(request):
    cleanup_files(["runs/detect/predict"])
    video_file = request.files["video"]
    model_variant, threshold, selected_classes = get_request_parameters(request)
    
    if model_variant not in models:
        return jsonify({"error": "Invalid model variant"}), 400
    
    format_name = str(uuid.uuid4())
    filename_input =  format_name+ ".mp4"
    filename_result = format_name + ".avi"
    input_path = os.path.join(INPUT_DIR, filename_input)
    result_path = os.path.join("runs/detect/predict", filename_result)
    
    video_file.save(input_path)

    result = models[model_variant](input_path, conf=threshold, classes=selected_classes, save=True) 

    with open(result_path, "rb") as vid_file:
        result_video_base64 = base64.b64encode(vid_file.read()).decode("utf-8")
    
    cleanup_files([input_path, result_path, "runs/detect/predict"])

    return jsonify({
        "message": "Video processing complete",
        "result_video": result_video_base64,
    })

def get_request_parameters(request):
    model_variant = request.form.get("model_variant", "YOLOv12-n")
    threshold = float(request.form.get("threshold", 0.5))
    selected_classes = request.form.getlist("selected_classes")
    selected_classes = [int(c) for c in selected_classes if c.isdigit()]
    return model_variant, threshold, selected_classes

def extract_detections(results):
    detections = []
    for result in results:
        for box in result.boxes:
            detections.append({
                "class_id": int(box.cls.item()),
                "confidence": float(box.conf.item()),
                "bbox": [float(i) for i in box.xywhn[0].tolist()]
            })
    return detections

def cleanup_files(files_or_dirs):
    for path in files_or_dirs:
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                os.rmdir(path)

if __name__ == "__main__":
    app.run(debug=True)
