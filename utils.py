import speech_recognition as sr
from ollama import chat
from config import MODEL_NAME, SYSTEM_PROMPT, LANGUAGE, MONGO_URL, DB_NAME,COLLECTION_NAME
import os
import pymongo 
from bson import ObjectId


class Utils:
    @staticmethod
    def get_db_connection():
        """Connecter à la base de données MongoDB."""
        try:
            client = pymongo.MongoClient(MONGO_URL)
            return client[DB_NAME]  
        except Exception as e:
            print(f"❌ Erreur de connexion à MongoDB : {e}")
            return None

    @staticmethod
    def add_course(title, category, content):
        """Ajoute un nouveau cours dans la base de données."""
        db = Utils.get_db_connection()
        if db is not None: 
            db[COLLECTION_NAME].insert_one({
                "title": title,
                "category": category,
                "content": content
            })

    @staticmethod
    def get_all_courses():
        """Récupère tous les cours depuis la base de données."""
        db = Utils.get_db_connection()
        if db is not None:  
            return list(db[COLLECTION_NAME].find({}))
        return []

    @staticmethod
    def delete_course(course_id):
        """Supprime un cours par son ID."""
        db = Utils.get_db_connection()
        if db is not None:  
            db[COLLECTION_NAME].delete_one({"_id": ObjectId(course_id)})

    @staticmethod
    def search_courses(query):
        """Cherche le cours et génère une réponse par IA."""
        db = Utils.get_db_connection()
        
        if db is None:
            return "Erreur de connexion à la base de données."

        try:
            results = db[COLLECTION_NAME].find({
                "$or": [
                    {"title": {"$regex": query, "$options": "i"}},
                    {"category": {"$regex": query, "$options": "i"}},
                    {"content": {"$regex": query, "$options": "i"}}
                ]
            })

            results_list = list(results)
            if not results_list:
                return "Désolé, aucun cours ne correspond à votre recherche."

            courses_text = "\n\n".join(
                [f"**{doc['title']}** ({doc['category']})\n{doc['content']}" for doc in results_list]
            )

            ai_prompt = (
                "Voici des informations sur les cours trouvés dans la base de données :\n\n"
                f"{courses_text}\n\n"
                "À partir de ces informations, répondez à la question de l'utilisateur de manière claire et détaillée."
            )

            response = chat(model=MODEL_NAME, messages=[{"role": "user", "content": ai_prompt}])

            return response.message.content

        except Exception as e:
            return f"Erreur lors de la recherche : {e}"


    @staticmethod
    def process_input(messages):
        """Envoie la réponse de l'user à l'IA puis génère une réponse."""
        try:
            system_prompt_message = {"role": "system", "content": SYSTEM_PROMPT} # Permet de ne pas manipuler le bot.
            messages_with_prompt = [system_prompt_message] + messages
            response = chat(model=MODEL_NAME, messages=messages_with_prompt)
            return response.message.content
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def get_audio():
        """Capture l'audio du microphone et le convertit en texte."""
        if os.path.exists('/.dockerenv'):
            print("Utilisation de Docker, le micro est désactivé.")
            return None
        else:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                try:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, phrase_time_limit=10)
                    text = recognizer.recognize_google(audio, language=LANGUAGE)
                    return text
                except sr.UnknownValueError:
                    return None
                except sr.RequestError as e:
                    print(f"Erreur avec le service de reconnaissance vocale : {e}")
                    return None