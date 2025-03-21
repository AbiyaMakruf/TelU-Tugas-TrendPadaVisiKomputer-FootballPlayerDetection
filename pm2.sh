#!/bin/bash
# Setup pm2
chmod +x bash/run_streamlit.sh
pm2 start bash/run_streamlit.sh --name streamlit-app

chmod +x bash/run_flask.sh
pm2 start bash/run_flask.sh --name backend-app

git stash