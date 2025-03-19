import streamlit as st
import requests
import io
import base64
from PIL import Image
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Backend API URL
API_URL = "http://127.0.0.1:5000/detect"

# Sidebar navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Info Model", "Demo Model"])

if menu == "Home":
    st.title("Football Player Detection Project")
    st.write("""
    Project ini bertujuan untuk mendeteksi pemain sepak bola dalam gambar menggunakan model YOLO. 
    Pengguna dapat mencoba model secara online dan memilih berbagai varian YOLO yang tersedia.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Football_player.svg/800px-Football_player.svg.png", use_container_width =True)

elif menu == "Info Model":
    st.title("Info Model")
    st.write("Berikut adalah ringkasan dari hasil training model YOLO untuk Football Player Detection.")
    summary_data = {
        "Training Loss": "training_loss.png",
        "Validation Accuracy": "validation_accuracy.png"
    }
    for key, img_path in summary_data.items():
        st.subheader(key)
        st.image(img_path, use_container_width =True)

elif menu == "Demo Model":
    CLASS_MAPPING = {
        "Ball": 0,
        "Goalkeeper": 1,
        "Player": 2,
        "Referee": 3
    }

    st.title("Demo Model Football Player Detection")
    
    st.sidebar.subheader("Pengaturan Model")
    model_variant = st.sidebar.selectbox("Pilih Varian Model YOLO", ["YOLOv12-n", "YOLOv12-s", "YOLOv12-m"])
    threshold = st.sidebar.slider("Threshold Confidence", 0.0, 1.0, 0.5)
    selected_classes = st.sidebar.multiselect("Pilih Kelas yang Dideteksi", ["Ball", "Goalkeeper", "Player", "Referee"], default=["Player"])
    
    uploaded_file = st.file_uploader("Upload Gambar untuk Prediksi", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar yang Diupload", use_container_width =True)
        
        if st.button("Deteksi Objek"):
            # Convert image to bytes
            img_bytes = io.BytesIO()
            image.save(img_bytes, format="JPEG")
            img_bytes = img_bytes.getvalue()

            # Mapping selected classes to class indices
            selected_classes = [CLASS_MAPPING[class_name] for class_name in selected_classes]
            
            # Prepare request payload
            files = {"image": ("image.jpg", img_bytes, "image/jpeg")}
            data = {"model_variant": model_variant, "threshold": threshold, "selected_classes": selected_classes}
            
            # Send request to backend
            response = requests.post(API_URL, files=files, data=data)
            
            if response.status_code == 200:
                result_data = response.json()
                
                # Decode base64 result image
                result_image_bytes = base64.b64decode(result_data["result_image"])
                result_image = Image.open(io.BytesIO(result_image_bytes))
                
                # Display result image
                st.image(result_image, caption="Hasil Deteksi", use_column_width=True)

                # Extract detection results
                detections = result_data["detections"]  # List of dicts with keys: class_id, confidence, bbox (x, y, w, h)

                if detections:
                    # Convert detections to DataFrame
                    df = pd.DataFrame(detections)

                    # Convert class_id to class names
                    df["class_name"] = df["class_id"].map({v: k for k, v in CLASS_MAPPING.items()})

                    # Display statistics
                    st.subheader("📊 Statistik Deteksi Objek")

                    # 1. Jumlah objek per kelas
                    class_counts = df["class_name"].value_counts().reset_index()
                    class_counts.columns = ["Kelas", "Jumlah"]
                    st.write("**Jumlah Objek per Kelas:**")
                    st.dataframe(class_counts)

                    # Plot jumlah objek per kelas
                    fig, ax = plt.subplots()
                    ax.bar(class_counts["Kelas"], class_counts["Jumlah"])
                    ax.set_xlabel("Kelas")
                    ax.set_ylabel("Jumlah")
                    ax.set_title("Jumlah Objek per Kelas")
                    st.pyplot(fig)

                    # 2. Confidence score rata-rata per kelas
                    avg_confidence = df.groupby("class_name")["confidence"].mean().reset_index()
                    avg_confidence.columns = ["Kelas", "Confidence Rata-rata"]
                    st.write("**Confidence Score Rata-rata per Kelas:**")
                    st.dataframe(avg_confidence)

                    # 3. Rata-rata ukuran bounding box per kelas
                    df["bbox_area"] = df["bbox"].apply(lambda x: x[2] * x[3])  # width * height
                    avg_bbox_size = df.groupby("class_name")["bbox_area"].mean().reset_index()
                    avg_bbox_size.columns = ["Kelas", "Rata-rata Ukuran Bounding Box"]
                    st.write("**Rata-rata Ukuran Bounding Box per Kelas:**")
                    st.dataframe(avg_bbox_size)
                
                else:
                    st.warning("Tidak ada objek yang terdeteksi dalam gambar ini.")
            else:
                st.error("Terjadi kesalahan dalam proses deteksi. Coba lagi.")
