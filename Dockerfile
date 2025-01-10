FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Installe les dépendances de PyAudio
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    python3-dev \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# reste des dépendances
RUN pip3 install --no-cache-dir -r requirements.txt

# Installation de Ollama
RUN curl -fsSL https://ollama.com/install.sh | bash

# Expose le port pour Streamlit
EXPOSE 8501

# copy entrypoint et le rend executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# entrypoint qui configure le tout avec CMD
CMD ["./entrypoint.sh"]
