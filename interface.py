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

    def display_ui(self):
        """Affiche l'interface utilisateur """
        st.title("ESIEE Paris assistant 🤖")

        tab1, tab2, tab3 = st.tabs(["🏠 accueil","🤖 Chatbot", "📚 Gestion des Cours"])

        with tab1:
            self.display_accueil()

        with tab2:
            self.display_chat_interface()

        with tab3:
            self.display_course_management()

    def display_accueil(self):
        """Affiche l'interface de l'accueil."""
        st.header("Bienvenue sur l'accueil de l'assistant ESIEE Paris !")
        st.write("""
            Cet assistant vous permet d'interagir avec un chatbot pour obtenir de l'aide et gérer vos cours.
            Utilisez les onglets ci-dessus pour naviguer entre les différentes fonctionnalités.
            /search <query> pour rechercher des cours.
        """)


    def display_chat_interface(self):
        """Affiche l'interface du chatbot."""
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
                else:
                    st.error("Désolé, je n'ai pas compris ce que vous avez dit. Veuillez réessayer.")

        self.display_chat_history()

    def display_course_management(self):
        """Affiche la gestion des cours : ajout et suppression."""
        st.header("📌 Ajouter un nouveau cours")

        # Formulaire d'ajout de cours
        title = st.text_input("Titre du cours")
        category = st.text_input("Catégorie")
        content = st.text_area("Contenu du cours")

        if st.button("Ajouter le cours"):
            if title and category and content:
                Utils.add_course(title, category, content)
                st.success(f"✅ Le cours **{title}** a été ajouté avec succès !")
            else:
                st.error("❌ Veuillez remplir tous les champs avant d'ajouter un cours.")

        st.divider()

        st.header("📚 Liste des cours disponibles")

        courses = Utils.get_all_courses()
        if not courses:
            st.info("Aucun cours trouvé dans la base de données.")
        else:
            for course in courses:
                # Evite les erreurs
                category = course.get('category', 'Inconnue')  
                with st.expander(f"📖 {course['title']} ({category})"):
                    st.write(course['content'])
                    if st.button(f"❌ Supprimer {course['title']}", key=course["_id"]):
                        Utils.delete_course(course["_id"])
                        st.warning(f"Le cours **{course['title']}** a été supprimé.")
                        st.rerun()  # Recharge la page après suppression


    def display_chat_history(self):
        """Affiche l'historique de la conversation"""
        if st.session_state.show_full_history:
            if st.session_state.chat_history:
                st.write("### Conversation actuel : ")

                for message in reversed(st.session_state.chat_history):  
                    col1, col2 = st.columns([0.5, 4])  
                    
                    if message["role"] == "user":
                        col1.image("img/user.png", width=60)  
                    else:
                        col1.image("img/bot.png", width=60)   
                    
                    col2.write(f"{message['content']}")
        else:
            if st.session_state.chat_history and st.session_state.chat_history[-1]["role"] == "assistant":
                last_response = st.session_state.chat_history[-1]["content"]
                st.text_area("Dernière réponse : ", value=last_response, height=100, disabled=True)

    def handle_user_input(self, user_input):
        """
        Gère l'entrée utilisateur et ajoute la réponse au chat.
        """
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # On utilise la commande "/search <query>" pour chercher dans nos cours
        if user_input.startswith("/search"):
            query = user_input.replace("/search", "").strip()
            if query:
                bot_response = Utils.search_courses(query)
            else:
                bot_response = "Veuillez spécifier un terme de recherche après `/search`."
        else:
            bot_response = Utils.process_input(st.session_state.chat_history)  # réponse du bot

        st.session_state.chat_history.append({"role": "assistant", "content": bot_response})



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