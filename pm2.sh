#!/bin/bash

export PATH="$HOME/.local/bin:$PATH"

# Run Streamlit
chmod +x bash/run_streamlit.sh
pm2 start bash/run_streamlit.sh --name streamlit-app

# Jeda 2 detik
sleep 2

# Run Flask
chmod +x bash/run_flask.sh
pm2 start bash/run_flask.sh --name backend-app

git stash