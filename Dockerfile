#PAS FINI !!!!
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exposition du port pour la communication avec le bot
EXPOSE 8080


ENV MODEL_NAME="llama3.2"


CMD ["python", "streamlit run App.py "]