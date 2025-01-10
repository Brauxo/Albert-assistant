import streamlit as st
from utils import Utils
#import pyttsx3 pour l'audio
import threading

class Interface:
    def __init__(self):
        st.set_page_config(page_title="Chatbot Brauxo V1", page_icon="🤖")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        if "show_full_history" not in st.session_state:
            st.session_state.show_full_history = True

    #audio pas utilisé
    '''
    def speak_text(self, text):
        """
        Permet de retransmette un texte sous tts
        """
        def run_speech():
            local_engine = pyttsx3.init()
            local_engine.setProperty("rate", 150)
            local_engine.setProperty("volume", 1.0)
            local_engine.say(text)
            local_engine.runAndWait()
            local_engine.stop()

        speech_thread = threading.Thread(target=run_speech)
        speech_thread.start()
     '''
    
    def handle_user_input(self, user_input):
        """
        Gère l'entrée utilisateur et ajoute la réponse au chat
        """
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        bot_response = Utils.process_input(st.session_state.chat_history)
        st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
        #self.speak_text(bot_response) #audio pas utilisé

    def display_ui(self):
        """
        Gère l'affichage de l'interface utilisateur
        """
        st.title("ChatNOW V1")

        # Entrée utilisateur
        input_option = st.radio("Choisissez la méthode d'entrée :", ("Clavier", "Microphone"))

        if input_option == "Clavier":
            user_input = st.text_input("Tapez quelque chose :", placeholder="👋 Commencez une conversation...")
            if st.button("Envoyer") and user_input:
                self.handle_user_input(user_input)

        elif input_option == "Microphone":
            if st.button("🎙️ Parler"):
                st.info("Écoute... Parlez dans le microphone.")
                user_input = Utils.get_audio()
                st.success("Audio capturé. Traitement en cours...")
                if user_input:
                    self.handle_user_input(user_input)
                else : 
                    st.error("Désolé, je n'ai pas compris ce que vous avez dit. Veuillez réessayer.")

        # Montre l'historique
        if st.button("Changer l'affichage de la discussion"):
            st.session_state.show_full_history = not st.session_state.show_full_history

        self.display_chat_history()

        # Vide la mémoire
        if st.button("Vider la mémoire"):
            st.session_state.chat_history = []
            st.success("Historique des conversations effacé !")

        # Télécharge l'historique de la discussion
        if st.session_state.chat_history:
            chat_text = "\n".join(
                [f"{'Vous' if msg['role'] == 'user' else 'Bot'}: {msg['content']}" for msg in st.session_state.chat_history]
            )
            st.download_button(
                label="Télécharger l'historique des conversations",
                data=chat_text,
                file_name="historique_conversations.txt",
                mime="text/plain",
            )

    def display_chat_history(self):
        """
        Affiche l'historique de la conversation
        """
        if st.session_state.show_full_history:
            if st.session_state.chat_history:
                st.write("### Historique des conversations :")
                for message in st.session_state.chat_history:
                    role = "Vous" if message["role"] == "user" else "Bot"
                    st.write(f"**{role} :** {message['content']}")
        else:
            if st.session_state.chat_history and st.session_state.chat_history[-1]["role"] == "assistant":
                last_response = st.session_state.chat_history[-1]["content"]
                st.text_area("Dernière réponse du bot", value=last_response, height=100, disabled=True)
