# 🏆 Tugas Trend Pada Visi Komputer

## 📌 Deskripsi
Proyek ini bertujuan untuk mendeteksi pemain sepak bola dalam gambar menggunakan model **YOLO (You Only Look Once)**. Dengan memanfaatkan teknik **Deep Learning** dan **Computer Vision**, model ini dapat mengenali objek seperti **pemain**, **wasit**, **penjaga gawang**, dan **bola** secara otomatis dalam sebuah pertandingan. ⚽🤖

Proyek ini juga mencakup pembuatan antarmuka pengguna berbasis **Streamlit**, deployment ke **AWS EC2/Google Compute Engine**, serta penerapan **Continuous Deployment (CD)** untuk mempermudah pengembangan dan pembaruan sistem. 🚀

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
Dataset yang digunakan dalam proyek ini dapat diakses di **Roboflow**:
🔗 [Football Players Detection Dataset](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc)

---

## 📂 Slide Presentasi
Slide presentasi dapat diakses melalui tautan berikut di **Canva**:
🔗 [Slide Presentasi](https://www.canva.com/design/DAGiMDF5UYg/9ULLnDnABeCkrVTKcxt9SQ/edit?utm_content=DAGiMDF5UYg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

---

## 📂 Tautan Model
Model-model yang digunakan dapat diakses melalui tautan berikut di **Google Drive**:
🔗 [Model YOLO](https://drive.google.com/drive/folders/1IAjkUzSgOE1D8Nxhyodaj5OgyXRR7U_F?usp=sharing)

---

## 📂 Summary Model
⏳ **BELUM ADA**

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
cd frontend
streamlit run app.py
```

### 🔹 **5. Jalankan Backend Flask**
```bash
cd backend
python app.py
```

---

## 🎥 Cara Install FFMPEG di Windows

FFMPEG adalah tool powerful untuk mengolah video dan audio lewat command line. Berikut ini panduan lengkap untuk menginstalnya di Windows dan juga di server seperti AWS EC2 atau Google Compute Engine (GCE). 🎞️

### 📦 Langkah 1: Install FFMPEG di Windows

#### 🔹 Unduh FFMPEG
1. Kunjungi situs resmi: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Klik opsi **Windows**, lalu kamu akan diarahkan ke:
   ➔ [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
3. Scroll ke bagian **Release builds**.
4. Klik dan unduh file: `ffmpeg-release-essentials.zip` 📁.

#### 🔹 Ekstrak dan Pindahkan
1. Ekstrak file ZIP yang sudah diunduh.
2. Ubah nama folder jika perlu, lalu pindahkan ke direktori seperti:
   ```
   C:\ffmpeg
   ```

#### 🔹 Tambahkan ke PATH
1. Buka **Start Menu** → cari `Environment Variables` → pilih **"Edit the system environment variables"**.
2. Klik tombol **"Environment Variables..."**.
3. Pada bagian **System variables**, cari dan pilih `Path`, lalu klik **Edit**.
4. Klik **New** ➕, lalu tambahkan path ke folder `bin`:
   ```
   C:\ffmpeg\bin
   ```
5. Klik OK ✅ sampai semua jendela tertutup.

#### 🔹 Cek Instalasi
1. Buka **Command Prompt** (`cmd`).
2. Ketik:
   ```bash
   ffmpeg -version
   ```
3. Kalau sukses, kamu akan melihat versi dan info build FFMPEG 🔍.

---

## 🚀 Tutorial Setup CLOUD

### 🔹 Membuat Virtual Machine di Google Compute Engine
1. Buat virtual machine dengan nama `football-detection`, region `Jakarta`, dan zone `any`.
2. Pada bagian **Machine Configuration**, pilih:
   - **Series**: E2
   - **Machine Type**: e2-standard-2
3. Pilih OS **Ubuntu** dan storage 50GB.
4. Matikan backup data di **Data Protection**.
5. Aktifkan **HTTP** dan **HTTPS Traffic** di bagian **Networking**.
6. Tambahkan SSH key public yang sudah dibuat:
   ```bash
   ssh-keygen -t ed25519 -C "aabbiiyyaa@gmail.com"
   ```
7. Klik **Create VM** dan tunggu hingga VM berjalan.

### 🔹 Membuat Firewall Rule
1. Buka menu **Firewall** dan buat rule baru:
   - **Name**: allow-streamlit-flask (atau nama bebas).
   - **Network**: default (atau jaringan yang digunakan VM).
   - **Priority**: 1000 (default).
   - **Direction of traffic**: Ingress.
   - **Action on match**: Allow.
   - **Targets**: All instances in the network.
   - **Source IP ranges**: 0.0.0.0/0.
   - **Protocols and ports**: Centang **Specified protocols and ports** → tcp:80,8501.
2. Klik **Create**.

### 🔹 Deploy Aplikasi
1. Login ke VM menggunakan SSH:
   ```bash
   ssh -i <nama_key> aabbiiyyaa@<external_ip>
   ```
2. Clone repository:
   ```bash
   git clone https://github.com/AbiyaMakruf/TelU-Tugas-TrendPadaVisiKomputer-FootballPlayerDetection.git
   cd TelU-Tugas-TrendPadaVisiKomputer-FootballPlayerDetection
   chmod +x init.sh
   chmod +x pm2.sh
   ./init.sh
   ./pm2.sh
   ```
3. Untuk restart server:
   ```bash
   pm2 restart 0 1
   ```

Akses aplikasi melalui `http://<external_ip>`.

---

## 🎥 Cara Setup Workflow
Buat 4 variabel secret di GitHub:
- **SSH_HOST**: Public external IP VM GCP.
- **SSH_USERNAME**: Sesuaikan dengan email di public key.
- **SSH_KEY**: Private key yang sudah di-add ke VM.
- **SSH_PORT**: 22.

---

## 🎥 Cara Instalasi Library Download Video YouTube
Install library:
```bash
pip install yt-dlp
```
Download video atau playlist:
```bash
yt-dlp [URL_VIDEO_ATAU_PLAYLIST]
```

---

## 📌 Teknologi yang Digunakan
- **Python 3.9** 🐍
- **YOLOv12** 🏆
- **Streamlit** 🎨
- **Flask** 🔥
- **AWS EC2/Google Compute Engine** ☁️
- **Continuous Deployment (CD)** 🔄
- **FFMPEG Converter** 🎞️
- **yt-dlp** 📹

---

## 👥 Authors
- **Muhammad Abiya Makruf**  
  🔗 [LinkedIn](https://www.linkedin.com/in/abiyamakruf/) | [GitHub](https://github.com/AbiyaMakruf)

- **Muhammad Rafly Arjasubrata**  
  🔗 [LinkedIn](https://www.linkedin.com/in/raflyarj/) | [GitHub](https://github.com/MuhRaflyArj)

🎯 **Proyek ini bertujuan untuk mempermudah deteksi pemain sepak bola secara otomatis! Selamat mencoba! ⚽🔥**