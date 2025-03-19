import streamlit as st
import requests
import io
import base64
from PIL import Image

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
                st.image(result_image, caption="Hasil Deteksi", use_container_width =True)
            else:
                st.error("Terjadi kesalahan dalam proses deteksi. Coba lagi.")
