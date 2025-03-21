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
cd frontend
streamlit run app.py
```

### 🔹 **5. Jalankan Backend Flask**
```bash
cd backend
python app.py
```

---

# 🎥 Cara Install FFMPEG di Windows

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

## 🚀 Tutorial Setup CLOUD
Buat virtual machine menggunakan Google Compute Engine
Berikan nama football-detection dengan region jakarta dan zone any
Pada bagian machine configuration pilih Series E2 dengan machine type e2-standard-2
pada bagian os pilih image ubuntu dan storage 50gb
pada data protection matikan backup data
pada bagian networking enable http dan https traffic
pada bagian security tambahkan SSH key public yang sudah dibuat dengan cara ssh-keygen -t ed25519 -C "aabbiiyyaa@gmail.com"
setelah itu create VM dan tunggu hingga VM berjalan

buka menun firewall dan buat firewall rule baru dan isikan dengan data berikut
Field	Isi
Name	allow-streamlit-flask (atau nama bebas)
Network	Pilih default (atau jaringan yang digunakan VM kamu)
Priority	1000 (default, boleh diabaikan)
Direction of traffic	Ingress
Action on match	Allow
Targets	All instances in the network (atau "Specified target tags" jika pakai tag di VM)
Source filter	IP ranges
Source IP ranges	0.0.0.0/0 (agar bisa diakses publik, atau masukkan IP tertentu untuk keamanan)
Protocols and ports	Centang Specified protocols and ports → tcp:80,8501 (atau port lain yang kamu butuhkan)
Klik “Create”

Setelah vm berjalan login ke vm menggunakan ssh dengan cara buka cmd dilokasi file ssh key private berada kemudian lakukan ssh -i `nama key` aabbiiyyaa@externalip
Jika terdapat error host key VM jalankan ssh-keygen -R externalip
Didalam compute engine git dan python sudah ter install sehingga kita tinggal melakukan git clone https://github.com/AbiyaMakruf/TelU-Tugas-TrendPadaVisiKomputer-FootballPlayerDetection.git
kemudian cd TelU-Tugas-TrendPadaVisiKomputer-FootballPlayerDetection
chmod +x init.sh
jalan ./init.sh untuk pertama kali

setiap server dinyalakan kembali cukup jalankan pm2 restart 0 1
setelahnya cukup push ke repo untuk auto CD

akses web ui melalui externalip:

Instalasi 
---

# 🎥 Cara setup workflow
Buat 4 variabel secret di github
SSH_HOST: public external ip vm gcp
SSH_USERNAME : sesuaikan dengan email di public key
SSH_KEY : private key yang sudah di add ke vm
SSH_PORT : 22

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
- **FFMPEG Converter**
- **yt-dlp**

## Authors
Muhammad Abiya Makruf
https://www.linkedin.com/in/abiyamakruf/
https://github.com/AbiyaMakruf


Muhammad Rafly Arjasubrata
https://www.linkedin.com/in/raflyarj/
https://github.com/MuhRaflyArj

🎯 **Proyek ini bertujuan untuk mempermudah deteksi pemain sepak bola secara otomatis! Selamat mencoba! ⚽🔥**