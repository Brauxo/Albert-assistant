FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    python3-dev \
    build-essential \
    curl \
    netcat-openbsd \  
    && rm -rf /var/lib/apt/lists/*


RUN pip3 install --no-cache-dir -r requirements.txt


RUN curl -fsSL https://ollama.com/install.sh | bash


EXPOSE 8501


COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh


CMD ["./entrypoint.sh"]