from PIL import Image
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import io
import base64
import os
import subprocess

# Backend API URL
# Load environment variables from .env file
load_dotenv()

# Get API URL from environment variable
API_URL = os.getenv("API_URL")

# Converter
def convert_to_h264(input_path, output_path):
    command = [
        "ffmpeg",
        "-i", input_path,
        "-vcodec", "libx264",
        "-acodec", "aac",
        output_path
    ]
    subprocess.run(command, check=True)

# Cleanup
def cleanup_files(files_or_dirs):
    for path in files_or_dirs:
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                os.rmdir(path)

# Sidebar navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Info Model", "Demo Model"])

if menu == "Home":
    st.image("images/thumbnail/thumbnail_dashboard.webp", use_container_width=True)
    st.title("Football Player Detection Project")
    st.write("""
    ## Tentang Proyek Ini
    Proyek ini menggunakan teknologi **YOLO (You Only Look Once)** untuk mendeteksi pemain sepak bola dalam gambar.
    Dengan memanfaatkan deep learning dan computer vision, model dapat mengenali objek seperti **pemain**, **wasit**, **Penjaga Gawang** dan **bola**
    dalam berbagai skenario pertandingan.
    
    ### Fitur Utama:
    - **Deteksi pemain sepak bola dalam gambar** menggunakan model YOLOv12-n, YOLOv12-s, dan YOLOv12-m.
    - **Pengguna dapat memilih model YOLO yang ingin digunakan.**
    - **Menyesuaikan ambang batas deteksi (threshold confidence).**
    - **Memilih kelas objek yang ingin dideteksi**, seperti pemain, wasit, atau bola.
    - **Hasil deteksi ditampilkan langsung di dalam aplikasi.**
    
    ### Cara Menggunakan:
    1. **Pilih menu "Demo Model"** dari sidebar.
    2. **Unggah gambar** yang ingin dideteksi.
    3. **Atur parameter deteksi** seperti model, threshold, dan kelas objek.
    4. **Klik tombol "Deteksi Objek"**, dan lihat hasilnya!
    
    
    **Selamat mencoba Football Player Detection! ⚽️🔥**
    """)

elif menu == "Info Model":
    st.title("Info Model")
    st.write("Berikut adalah ringkasan dari hasil training model YOLO untuk Football Player Detection.")
    summary_data = {
        "Training Loss": "images/info_model/training_loss.jpg",
        "Validation Accuracy": "images/info_model/validation_accuracy.jpg"
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

    # Pilihan mode input
    data_input_mode = st.radio("Pilih Metode Input", ("Upload Gambar", "Gunakan Video yang Disediakan"))

    if data_input_mode == "Upload Gambar":
        uploaded_file = st.file_uploader("Upload Gambar untuk Prediksi", type=["jpg", "png", "jpeg"])
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Gambar yang Diupload", use_container_width=True)
            
            if st.button("Deteksi Objek"):
                img_bytes = io.BytesIO()
                image.save(img_bytes, format="JPEG")
                img_bytes = img_bytes.getvalue()
                
                selected_classes = [CLASS_MAPPING[class_name] for class_name in selected_classes]
                
                files = {"image": ("image.jpg", img_bytes, "image/jpeg")}
                data = {"model_variant": model_variant, "threshold": threshold, "selected_classes": selected_classes}
                
                response = requests.post(API_URL, files=files, data=data)
                
                if response.status_code == 200:
                    result_data = response.json()
                    result_image_bytes = base64.b64decode(result_data["result_image"])
                    result_image = Image.open(io.BytesIO(result_image_bytes))
                    st.image(result_image, caption="Hasil Deteksi", use_container_width=True)
                    detections = result_data["detections"]

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
                    st.error("Terjadi kesalahan dalam proses deteksi. Coba lagi.")

    elif data_input_mode == "Gunakan Video yang Disediakan":
        video_options = {"Video 1": "videos/test_videos_1.mp4", "Video 2": "videos/test_videos_2.mp4"}
        selected_video = st.selectbox("Pilih Video", list(video_options.keys()))
        video_path = video_options[selected_video]
        st.video(video_path)
        
        if st.button("Deteksi Objek dalam Video"):
            cleanup_files(["output/output_video.mp4", "output/converted.mp4"])
            with open(video_path, "rb") as f:
                video_bytes = f.read()
            
            selected_classes = [CLASS_MAPPING[class_name] for class_name in selected_classes]
            
            files = {"video": (video_path, video_bytes, "video/mp4")}
            data = {"model_variant": model_variant, "threshold": threshold, "selected_classes": selected_classes}
            
            with st.spinner("Memproses video, mohon tunggu..."):
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    result_data = response.json()
                    result_video_bytes = base64.b64decode(result_data["result_video"])
                    result_video_path = "output/output_video.mp4"

                    with open(result_video_path, "wb") as f:
                        f.write(result_video_bytes)

                    convert_to_h264(result_video_path, "output/converted.mp4")
                    st.success("Deteksi selesai! Berikut hasilnya:")
                    st.video("output/converted.mp4")
                else:
                    st.error("Terjadi kesalahan dalam proses deteksi video. Coba lagi.")