# 🏆 Tugas Trend Pada Visi Komputer

## 📌 Deskripsi
Proyek ini bertujuan untuk mendeteksi pemain sepak bola dalam gambar menggunakan model **YOLO (You Only Look Once)**. Dengan menggunakan teknik **Deep Learning** dan **Computer Vision**, model ini dapat mengenali objek seperti **pemain**, **wasit**, dan **bola** secara otomatis dalam sebuah pertandingan. 

Proyek ini juga akan mencakup pembuatan antarmuka pengguna berbasis **Streamlit**, deployment ke **AWS EC2**, dan penerapan **Continuous Deployment (CD)** untuk mempermudah pengembangan dan pembaruan sistem.

---

## ✅ To-Do List
1️⃣ **Training Model** 🏋️‍♂️
2️⃣ **Membuat Web UI menggunakan Streamlit** 🖥️
3️⃣ **Deploy ke EC2** ☁️
4️⃣ **Menerapkan Continuous Deployment (CD)** 🚀

---

## 🎨 UI
Aplikasi ini memiliki beberapa menu utama:
1️⃣ **Home Page** 🏠 – Penjelasan tentang proyek dan tujuannya.
2️⃣ **Info Model** 📊 – Menampilkan statistik akurasi model, grafik loss, dan hasil training.
3️⃣ **Demo Model** ⚽ – Pengguna dapat:
   - Memilih jenis model YOLO (YOLOv5, YOLOv7, YOLOv8).
   - Menyesuaikan threshold deteksi.
   - Memilih jenis objek yang akan dideteksi (pemain, wasit, bola).
   - Mengunggah gambar dan melihat hasil deteksi.

---

## 📂 Dataset
Dataset yang digunakan dalam proyek ini bisa diakses di **Roboflow**:
🔗 [Football Players Detection Dataset](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc)

---

## 🚀 Tutorial Setup & Deployment
### 🔹 **1. Install Anaconda**
Jika belum memiliki **Anaconda**, silakan install terlebih dahulu dari [situs resmi Anaconda](https://www.anaconda.com/).

### 🔹 **2. Buat dan Aktifkan Environment Anaconda**
```bash
conda create --name football_detection python=3.9 -y
conda activate football_detection
```

### 🔹 **3. Install Dependencies**
Pastikan dependencies terinstal dengan menjalankan perintah berikut:
```bash
pip install -r requirements.txt
```

### 🔹 **4. Jalankan Aplikasi Streamlit (Frontend)**
```bash
streamlit run app.py
```

### 🔹 **5. Jalankan Backend Flask**
```bash
python app.py
```

---

## 📌 Teknologi yang Digunakan
- **Python 3.9** 🐍
- **YOLOv5, YOLOv7, YOLOv8** 🏆
- **Streamlit** 🎨
- **Flask** 🔥
- **AWS EC2** ☁️
- **Continuous Deployment (CD)** 🔄

🎯 **Proyek ini bertujuan untuk mempermudah deteksi pemain sepak bola secara otomatis! Selamat mencoba! ⚽🔥**