#!/bin/bash
# Jalankan pertama kali untuk setup environment
# Install pip
sudo apt update -y
sudo apt upgrade -y
sudo apt install python3-pip -y
pip3 install --upgrade pip


# Install pip -r requirements
pip3 install -r requirements.txt

# Menambahkan path 
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
source ~/.bashrc


# Download .pt if not found
gdown 1RvFi1cMAZp5RTjjbjPn3cK_Ebb6Mf0r- -O backend/best_model/medium-720.pt
gdown 1OMFlFuNvI9axowTJPpuCheruSVD8-Cq6 -O backend/best_model/nano-720.pt
gdown 1Scw_vGEoh4KUzygCoj1hcI0LxPIORw5I -O backend/best_model/small-720.pt

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt install npm -y

# Install pm2
sudo npm install pm2 -g

# Install libgl1
sudo apt install -y libgl1

# Install ffmpeg
sudo apt update
sudo apt install ffmpeg -y