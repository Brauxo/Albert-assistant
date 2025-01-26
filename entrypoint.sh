#!/bin/bash
echo "Starting Ollama server..."
ollama serve &

echo "Waiting for Ollama server to be active..."
while [ "$(ollama list | grep 'NAME')" == "" ]; do
  sleep 1
done

# Le model à pull qui va être utilisé par docker
ollama pull llama3.2

echo "The model is correctly installed ! Waiting for Ollama server to be ready..."
while ! curl -s http://localhost:11434/api/status; do
    sleep 1
done

echo "Ollama is ready. Starting MongoDB..."
while ! nc -z mongo 27017; do
  sleep 1
done

echo "MongoDB is ready. Loading courses..."
python3 load_json.py

echo "Starting Streamlit..."
streamlit run App.py --server.port=8501 --server.address=0.0.0.0