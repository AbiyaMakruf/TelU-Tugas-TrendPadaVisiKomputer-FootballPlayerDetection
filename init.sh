#!/bin/bash

set -e  # Stop jika terjadi error

#  🔧 Updating dan install pip...
sudo apt update -y
sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv

# 📦 Install dependencies dari requirements.txt...
pip3 install --user -r requirements.txt

# 🛠️ Menambahkan ~/.local/bin ke PATH (jika belum ada)...
if ! grep -q "$HOME/.local/bin" ~/.bashrc; then
  echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
fi
source ~/.bashrc

# ⬇️  Download model .pt ke backend/best_model/...
mkdir -p backend/best_model
gdown 1RvFi1cMAZp5RTjjbjPn3cK_Ebb6Mf0r- -O backend/best_model/medium-720.pt
gdown 1OMFlFuNvI9axowTJPpuCheruSVD8-Cq6 -O backend/best_model/nano-720.pt
gdown 1Scw_vGEoh4KUzygCoj1hcI0LxPIORw5I -O backend/best_model/small-720.pt

# 🟩 Menginstal Node.js & npm...
curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt install -y nodejs npm

# 🚀 Menginstal PM2...
sudo npm install -g pm2

# 🖼️ Menginstal libgl1 untuk OpenCV...
sudo apt install -y libgl1

# 🎥 Menginstal ffmpeg...
sudo apt install -y ffmpeg

# Setup pm2
chmod +x bash/run_streamlit.sh
pm2 start bash/run_streamlit.sh --name streamlit-app

chmod +x bash/run_flask.sh
pm2 start bash/run_flask.sh --name backend-app

echo "✅ Setup selesai! VM siap digunakan 💥"
