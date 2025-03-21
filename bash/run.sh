#!/bin/bash
chmod +x run_streamlit.sh
pm2 start ./run_streamlit.sh --name streamlit-app

chmod +x run_flask.sh
pm2 start ./run_flask.sh --name backend-app

