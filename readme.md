# **Projet DEVOPS-CHATBOT**

## **Auteurs**

**ESIEE PARIS projet DEVOPS de E4 fillière DSIA**

-   **Owen BRAUX** 
-   **Elliot CAMBIER** 

**Année 2025**

## **Description**

Une application web permettant d'accéder à un assistant (CHATBOT) utilisant un modèle LLM (Large Language Model) de votre choix, avec le modèle **llama3.2** utilisé par défaut. Cette application offre des fonctionnalités d'interaction en langage naturel via texte ou microphone, ainsi que la possibilité de sauvegarder et télécharger l'historique des conversations.

---

## **Sommaire**
1. [Prérequis d'installation](#1---prérequis-dinstallation)
2. [Installation](#2---installation)
3. [Run](#3---run)
4. [Fonctionnalités](#4---fonctionnalités)
5. [To-DO](#5---to-do)

---

## **Guide de l'utilisateur**

### **1 - Prérequis d'installation**

#### **Setup AWS**

 **[Docker Desktop](https://www.docker.com/products/docker-desktop/) (en cours de développement)**
 - Docker sera utilisé pour conteneuriser et déployer l'application à l'avenir. Faites une installation classique pour votre système d'exploitation.

 **AWS (en cours de développement)**
 - Des configurations supplémentaires pour AWS seront fournies ultérieurement.

#### **Instalation locale**

Avant de commencer, il faut installer ces 

1. **[ollama](https://ollama.com/)**
 - Installez Ollama pour accéder aux modèles LLM.
 - Documentation Python pour Ollama : [ollama-python](https://github.com/ollama/ollama-python).

2. **[Git](https://git-scm.com/)**
 - Nécessaire pour cloner le projet depuis le dépôt GitHub.

3. **[FFmpeg](https://ffmpeg.org/download.html) [NON NECESSAIRE (SAUF SI L'AUDIO EST SOUHAITé**
 - Permet de lire et de traiter les fichiers audio.
 - Vous pouvez utiliser ce dépôt pour obtenir une version précompilée : [FFmpeg Builds](https://github.com/BtbN/FFmpeg-Builds/releases).
 - Ajoutez **ffmpeg.exe** à votre `PATH` pour un accès global.

---

### **2 - Installation**

1. Clonez le projet :
```
git clone https://github.com/Brauxo/PROJET-CHATBOT
```

1.  Installez les dépendances Python nécessaires :
```
pip install -r requirements.txt
```

* * * * *

### **3 - Run**

Pour lancer l'application en local (sur son pc):

1.  Assurez-vous que les modèles LLM nécessaires sont téléchargés via Ollama et que Ollama soit lancé :
```
`ollama start
```

```
`ollama run llama3.2`
```

2.  Exécutez l'application Streamlit (obligatoire !) :

```
streamlit run App.py`
```

3.  Accédez à l'interface via votre navigateur à l'adresse : http://localhost:8501

* * * * *

### **4 - Fonctionnalités**

L'application offre les fonctionnalités suivantes :

1.  **Interaction via texte ou voix** :
    -   Entrez vos messages via le clavier ou utilisez le microphone pour une interaction vocale.

2.  **Gestion de l'historique des conversations** :
    -   L'historique complet de la conversation est affiché ou réduit à la dernière réponse du bot.
    -   Téléchargez l'historique en format texte pour une sauvegarde locale.

3.  **Conversion texte-parole [DESACTIVE PAR DEFAULT]** :
    -   Les réponses du chatbot peuvent être lues à haute voix via un moteur de synthèse vocale.

4.  **Effacement des données** :
    -   Réinitialisez facilement l'historique des conversations à tout moment.

* * * * *

### **5 - To-DO**

-   **Intégration AWS** 
-   **Docker** 
-   **Interface utilisateur avancée** 

* * * * *

