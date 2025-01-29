# `ollama run deepseek-r1:1.5b` pour télécharger le bon modèle
MODEL_NAME = "llama3.2"  # possibilité de changer avec n'importe quel modèle

# Ajoute des paths pour l'historique (pas utilisé dans le projet DEVOPS)
#HISTORY_FILE = "chat_history.json"

#Pour implementer du tts (pas utilisé dans le projet DEVOPS)
#FFMPEG_EXECUTABLE = "ffmpeg.exe"

# Le System prompt à  utiliser
SYSTEM_PROMPT = """Tu es Albert, un chatbot de l'ecole ESIEE Paris qui aide  les élèves dans leurs cours. 
Tu as été créé par Owen BRAUX et Elliot CAMBIER.
Tu dois communiquer en français et tu dois être poli et respectueux envers les utilisateurs.
Tu dois répondre de manière claire et détaillée aux questions des utilisateurs.
Tu peux aussi chercher des informations dans la base de données de cours en utilisant la commande `/search <Nom du cours>`.
"""

LANGUAGE = 'fr-FR' #pour la détection audio



# Paramètre de la BDD
#MONGO_URL = "mongodb://mongo:27017/"  # Pour docker
MONGO_URL = "mongodb://localhost:27017/" # En local
DB_NAME = "chatbot_db"
COLLECTION_NAME = "courses"