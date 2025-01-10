import speech_recognition as sr
from ollama import chat
from config import MODEL_NAME, SYSTEM_PROMPT, LANGUAGE


class Utils:
    @staticmethod
    def process_input(messages):
        """
        Envoie l'historique des messages au modèle et récupère la réponse.
        """
        try:
            system_prompt_message = {"role": "system", "content": SYSTEM_PROMPT}
            messages_with_prompt = [system_prompt_message] + messages
            response = chat(model=MODEL_NAME, messages=messages_with_prompt)
            return response.message.content
        except Exception as e:
            return f"Error: {e}"


    @staticmethod
    def get_audio():
        """
        Capture l'audio depuis le microphone et le convertit en texte.
        """
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, phrase_time_limit=10)  # limite de 10 secondes par phrase
                text = recognizer.recognize_google(audio, language=LANGUAGE)
                return text
            except sr.UnknownValueError:
                return None
            except sr.RequestError as e:
                print(f"Impossible de demander des résultats au service de reconnaissance vocale ; {e}")
                return None
