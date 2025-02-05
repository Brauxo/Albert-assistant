#!/bin/bash

# Start Ollama in the background.

ollama serve &
pid=$!
sleep 5

echo "🔴 Retrieve model..."
ollama pull llama3.2




echo "🟢 Done!"

# Wait for Ollama process to finish.
wait $pid