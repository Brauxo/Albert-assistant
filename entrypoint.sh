#!/bin/bash

echo "Waiting for Ollama..."
while ! nc -z ollama 11434; do
    sleep 1
done

echo "Ollama is ready. Starting MongoDB..."
while ! nc -z mongo 27017; do
  sleep 1
done

echo "MongoDB is ready. Loading courses..."
python3 src/load_json.py

echo "Starting Streamlit..."
streamlit run src/App.py --server.port=8501 --server.address=0.0.0.0