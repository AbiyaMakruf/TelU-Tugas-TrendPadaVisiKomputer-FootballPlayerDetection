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

## 📊🎤 Slide Presentasi
Slide presentasi dapat diakses melalui tautan berikut di **Canva**:
🔗 [Slide Presentasi](https://www.canva.com/design/DAGiMDF5UYg/Sp6sjfia9T3MzExoZYf6eA/view?utm_content=DAGiMDF5UYg&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h0cdd43996d)

---

## 🔗🤖 Tautan Model
Model-model yang digunakan dapat diakses melalui tautan berikut di **Google Drive**:
🔗 [Model YOLO](https://drive.google.com/drive/folders/1IAjkUzSgOE1D8Nxhyodaj5OgyXRR7U_F?usp=sharing)

---

## 🧠📄 Summary Model
### YOLOv12 - Attention Centric Model
YOLOv12 adalah iterasi terbaru dalam Ultralytics YOLO yang memperkenalkan arsitektur yang berpusat pada ***Attention Mechanism*** untuk meningkatkan akurasi deteksi sambil mempertahankan kecepatan inferensi. Peningkatan ini memungkinkan YOLOv12 mencapai keseimbangan optimal antara akurasi dan efisiensi, menjadikannya pilihan untuk analitik pertandingan bola secara *real-time*.

### Pelatihan Model
3 Ukuran model dilatih dan dievaluasi dengan 3 ukuran input berbeda seperti tabel dibawah dengan *VRAM Usage* sebagai berikut

| |480x480|640x640|720x720|
|-|-------|-------|-------|
|nano|1.61G|3.54G|5.16G|
|small|2.90G|5.35G|8.03G|
|medium |5.24G|10.21G|13.10G| 

Peningkatan ukuran model (GFLOPs) meningkat seiring dengan meningkatnya ukuran input dan ukuran arsitektur. Maka pada penelitian ini akan menjawab mana yang lebih berpengaruh antara ukuran input dan ukuran model pada performa model, terutama performa pada deteksi bola dengan menimbang ukuran model.

***Hyperparameter Pelatihan Model***
|Parameter|Nilai|
|---------|-----|
|Epoch|50|
|Batch|12|
|Worker|8|
|Optimizer|AdamW|
|Learning Rate|0.00125|
|Momentum|0.900|

### Hasil Pelatihan Model

#### YOLOv12-nano
![image](readme/info_model/Res%20YOLOv12-nano.png)
- **Pada proses pelatihan**, berdasarkan nilai mAP50 pada data validasi yang dicek setiap epochnya. Pada model YOLOv12-nano, peningkatan yang signifikan terjadi dari ukuran input 480x480 ke 640x640, namun peningkatan tidak terlalu signifikan pada model dengan ukuran input 640x640 ke 720x720.
- **Sedangkan pada data uji**, dapat dilihat bahwa kelas *ball* tidak dapat dideteksi sama sekali pada model dengan ukuran input 480x480. Model dengan ukuran input 640x640 dan 720x720 berhasil mendeteksi *ball*, tetapi masih sangat buruk. Jika melihat pada kelas lain, peningkatan performa deteksi yang signifikan terjadi pada model dengan ukuran input 480x480 ke model dengan ukuran 640x640. Bedasarkan hal tersebut, meningkatkan ukuran input dapat meningkatkan performa deteksi model tetapi dengan *diminishing return*.

#### YOLOv12-small
![image](readme/info_model/Res%20YOLOv12-small.png)
- **Pada proses pelatihan**, model YOLOv12-small, peningkatan performa antara model dengan ukuran input 480x480 dengan model 640x640 tidak terlalu se-signifikan seperti yang terjadi pada YOLOv12-nano. Akurasi mAP50 pada ketiga model juga memiliki peningkatan yang signifikan.
- **Sedangkan pada data uji**, model YOLOv12-small dengan ukuran input 480x480 berhasil mendeteksi bola dengan mAP50-95 kurang dari 0.1. Pada data uji, perbedaan performa antara ukuran input 480x480 dengan 640x640 masih terlihat cukup signifikan. Ketiga YOLOv12-small memiliki peningkatan akurasi pada seluruh kelas dibandingkan YOLOv12-nano. Hal tersebut membuktikan bahwa ukuran model sangat berpengaruh terhadap akurasi deteksi model.

#### YOLOv12-medium
![image](readme/info_model/Res%20YOLOv12-medium.png)
- **Pada proses pelatihan**, perbedaan antara ukuran input tidak begitu signifikan pada YOLOv12-medium dibandingkan YOLOv12-small ataupun YOLOv12-nano. Ketiga model memiliki hasil yang tidak terlalu jauh satu sama lain menandakan model yang lebih besar sudah memiliki ekstraksi fitur yang lebih baik.
- **Sedangkan pada data uji**, perbedaan antara model YOLOv12-medium dengan ukuran input 640x640 dengan 720x720 sangat sedikit. Perbedaan antara ukuran input 480x480 dengan 640x640 juga tidak teralalu signifikan dibandingkan YOLOv12-small ataupun YOLOv12-nano. Pada titik ini, peningkatan ukuran input lebih dari 640x640 tidak diperlukan.

### Perbandingan Hasil Antara Ukuran Model

#### Hasil pelatihan
![image](readme/info_model/Res%20Overall%20Training.png)
- Dari ketiga ukuran model, peningkatan signifikan terjadi antara YOLOv12-nano ke YOLOv12-small. Peningkatan tidak terlalu signifikan antara YOLOv12-small dan YOLOv12-medium. Berdasarkan hal tersebut **YOLOv12-small** memiliki balance terbaik antara kecepatan dan akurasi.

#### Hasil pada data uji
![image](readme/info_model/Res%20Overall%20Testing.png)
- Perbandingan antara input size juga terlihat bahwa model YOLOv12-small dengan input size 640x640 memiliki performa yang seimbang, dimana perbedaan performa ukuran model 480x480 dengan 640x640 memiliki peningkatan yang signifikan, sedangkan peningkatan antara model dengan ukuran input 640x640 dengan 720x720, peningkatan tidak terlalu signifikan.

### Kesimpulan
Berdasarkan hal tersebut maka **YOLOv12-small dengan ukuran input 640x640 merupakan model terbaik yang memiliki *balance* antara performa dan kecepatan deteksi**

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

Akses aplikasi melalui `http://<external_ip>:8501`.

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
