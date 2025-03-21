# 🏆 Tugas Trend Pada Visi Komputer

## 📌 Deskripsi
Proyek ini bertujuan untuk mendeteksi pemain sepak bola dalam gambar menggunakan model **YOLO (You Only Look Once)**. Dengan menggunakan teknik **Deep Learning** dan **Computer Vision**, model ini dapat mengenali objek seperti **pemain**, **wasit**, **penjaga gawang** dan **bola** secara otomatis dalam sebuah pertandingan. 

Proyek ini juga akan mencakup pembuatan antarmuka pengguna berbasis **Streamlit**, deployment ke **AWS EC2/Google Compute Engine**, dan penerapan **Continuous Deployment (CD)** untuk mempermudah pengembangan dan pembaruan sistem.

---

## 🎨 UI
Aplikasi ini memiliki beberapa menu utama:

1️⃣ **Home Page** 🏠 – Penjelasan tentang proyek dan tujuannya.

2️⃣ **Info Model** 📊 – Menampilkan statistik akurasi model, grafik loss, dan hasil training.

3️⃣ **Demo Model** ⚽ – Pengguna dapat:
   - Memilih jenis model YOLO (YOLOv12-n, YOLOv12-s, YOLOv12-m).
   - Menyesuaikan threshold deteksi.
   - Memilih jenis objek yang akan dideteksi (pemain, wasit, penjaga gawang, bola).
   - Mengunggah gambar/video dan melihat hasil deteksi.

---

## 📂 Dataset
Dataset yang digunakan dalam proyek ini bisa diakses di **Roboflow**:
🔗 [Football Players Detection Dataset](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc)

---

## 📂 Slide Presentasi
Slide presentasi dapat diakses melalui tautan berikut **Canva**:
🔗 [Slide Presentasi](https://www.canva.com/design/DAGiMDF5UYg/9ULLnDnABeCkrVTKcxt9SQ/edit?utm_content=DAGiMDF5UYg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

---

## 📂 Tautan Model
https://drive.google.com/drive/folders/1IAjkUzSgOE1D8Nxhyodaj5OgyXRR7U_F?usp=sharing

---

## 📂 Summary Model
BELUM ADA

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
cd backend
python app.py
```

---

# 🎥 Cara Install FFMPEG di Windows dan Server (EC2 / GCP)

FFMPEG adalah tool powerful untuk mengolah video dan audio lewat command line. Berikut ini panduan lengkap untuk menginstalnya di Windows dan juga di server seperti AWS EC2 atau Google Compute Engine (GCE).

---

## 📦 Langkah 1: Install FFMPEG di Windows

### 🔹 Unduh FFMPEG

1. Kunjungi situs resmi: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Klik opsi **Windows**, lalu kamu akan diarahkan ke:
   ➔ [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
3. Scroll ke bagian **Release builds**
4. Klik dan unduh file: `ffmpeg-release-essentials.zip` 📁

### 🔹 Ekstrak dan Pindahkan

1. Ekstrak file ZIP yang sudah diunduh.
2. Ubah nama folder jika perlu, lalu pindahkan ke direktori seperti:
   ```
   C:\ffmpeg
   ```

### 🔹 Tambahkan ke PATH

1. Buka **Start Menu** → cari `Environment Variables` → pilih **"Edit the system environment variables"**
2. Klik tombol **"Environment Variables..."**
3. Pada bagian **System variables**, cari dan pilih `Path`, lalu klik **Edit**
4. Klik **New** ➕, lalu tambahkan path ke folder `bin`:
   ```
   C:\ffmpeg\bin
   ```
5. Klik OK ✅ sampai semua jendela tertutup

### 🔹 Cek Instalasi

1. Buka **Command Prompt** (`cmd`)
2. Ketik:
   ```bash
   ffmpeg -version
   ```
3. Kalau sukses, kamu akan melihat versi dan info build FFMPEG 🔍

---

## 🌐 Langkah 2: Install FFMPEG di Server (AWS EC2 / Google Compute Engine)

### 🚀 Cocok untuk: Ubuntu / Debian based instance

### 🔹 Update & Install

```bash
sudo apt update
sudo apt install -y ffmpeg
```

### 🔹 Verifikasi Instalasi

```bash
ffmpeg -version
```

Jika berhasil, kamu akan melihat informasi versi dan konfigurasi FFMPEG di terminal.

### 🌎 Alternatif: Compile dari Source (Jika butuh versi terbaru)

1. Install dependencies:
```bash
sudo apt update
sudo apt install -y autoconf automake build-essential cmake git libtool pkg-config texinfo wget yasm nasm
```
2. Clone dan build FFMPEG:
```bash
mkdir -p ~/ffmpeg_sources && cd ~/ffmpeg_sources
wget https://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2

tar xjvf ffmpeg-snapshot.tar.bz2
cd ffmpeg
./configure
make -j$(nproc)
sudo make install
```
3. Cek kembali:
```bash
ffmpeg -version
```

---

## 🌟 Siap Digunakan!

Sekarang kamu bisa menggunakan FFMPEG baik di Windows maupun di server untuk mengolah media secara fleksibel lewat command line! 🚀🎧

---

## 🚀 Tutorial Setup CLOUD
---

# 🎥 Cara instalasi library download video youtube
pip install yt-dlp
yt-dlp [URL_VIDEO_ATAU_PLAYLIST]


## 📌 Teknologi yang Digunakan
- **Python 3.9** 🐍
- **YOLOv12** 🏆
- **Streamlit** 🎨
- **Flask** 🔥
- **AWS EC2/Google Compute Engine** ☁️
- **Continuous Deployment (CD)** 🔄

🎯 **Proyek ini bertujuan untuk mempermudah deteksi pemain sepak bola secara otomatis! Selamat mencoba! ⚽🔥**