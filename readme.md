# **Projet DEVOPS-CHATBOT**

## **Auteurs**

**ESIEE PARIS projet DEVOPS de E4 fillière DSIA**

-   **Owen BRAUX** 
-   **Elliot CAMBIER** 

**Année 2025**

## **REQUIREMENTS**

Attention pour faire tourner ce projet dans des conditions optimale il est nécessaire d'avoir : 

- Un processeur multicoeur ou une carte graphique avec 4 Gb de VRAM. 
- Au moins 8 Gb de RAM (12 si CPU)

(si c'est insuffisant il faut utiliser [llama3.2:1b](https://ollama.com/library/llama3.2))

## **Description**

Une application web permettant d'accéder à un assistant (CHATBOT) utilisant un modèle LLM (Large Language Model) de votre choix, avec le modèle **llama3.2** utilisé par défaut. Cette application offre des fonctionnalités d'interaction en langage naturel via texte ou microphone, ainsi que la possibilité de sauvegarder et télécharger l'historique des conversations.

---

## **Sommaire**
1. [Prérequis](#1---prérequis)
2. [Installation](#2---installation)
3. [Exécution](#3---exécution)
4. [Déploiement avec Docker](#4---déploiement-avec-docker)
5. [Déploiement avec Kubernetes](#5---déploiement-avec-kubernetes)
6. [Fonctionnalités](#6---fonctionnalités)
---

## **Guide de l'utilisateur**

### **1 - Prérequis**

#### **I -Pour un Setup sur VM/AWS**

1. **Setup up Docker :**
 **[Docker Desktop](https://www.docker.com/products/docker-desktop/)**

2. **Setup up minikube (avec Kubernetes) :** 
 **[Kubernetes](https://kubernetes.io/releases/download/)**
 **[Minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download)**

3. **AWS (en cours de développement)**
 - Des configurations supplémentaires pour AWS seront fournies ultérieurement.


#### **II -Pour une installation locale**

1. **[ollama](https://ollama.com/)**
 - Installez Ollama pour accéder aux modèles LLM.
 - Documentation Python pour Ollama : [ollama-python](https://github.com/ollama/ollama-python).

2. **[Git](https://git-scm.com/)**
 - Nécessaire pour cloner le projet depuis le dépôt GitHub.

3. **[MongoDB](https://www.mongodb.com/docs/manual/installation/)**
 - Pour créer nos bases de données qui vont être accéder par le chatbot

4. **[FFmpeg](https://ffmpeg.org/download.html) [NON NECESSAIRE (SAUF SI L'AUDIO EST SOUHAITE)]**
 - Permet de lire et de traiter les fichiers audio.
 - Vous pouvez utiliser ce dépôt pour obtenir une version précompilée : [FFmpeg Builds](https://github.com/BtbN/FFmpeg-Builds/releases).
 - Ajoutez **ffmpeg.exe** à votre `PATH` pour un accès global.

---

### **2 - Installation**

Clonez le projet et installez les dépendances :

```sh
git clone https://github.com/Brauxo/PROJET-CHATBOT
cd PROJET-CHATBOT

pip install -r requirements.txt
```

* * * * *

### **3 - Exécution**

#### **Pour lancer l'application en local (sur son pc):**

1.  Assurez-vous que les modèles LLM nécessaires sont téléchargés via Ollama et que Ollama soit lancé :
```
`ollama start
```
Nous conseillons llama3.2 ou llama3.2:1b . 
En alternative : Le modèle DeepSeek-R1:1.5B, récemment lancé, est particulièrement intéressant car il nécessite très peu de puissance et offre des performances correctes. 
```
ollama run llama3.2 
```

2. Setup de la base de données.

Pour créer une base de données avec celle fournie (le json)
```
python load_json.py
```

De plus dans le fichier config.py il faut remplacer MONGO_URL par l'adresse locale de mongoDB : 
```
MONGO_URL = "mongodb://localhost:27017/"
```

3.  Exécutez l'application Streamlit (obligatoire !) :

```
streamlit run App.py
```

4.  Accédez à l'interface via votre navigateur à l'adresse : http://localhost:8501


### **4 - Déploiement avec Docker**

Pour exécuter le projet sur Docker, il suffit de rentrer la commande suivante
!!! IMPORTANT : L'initialisation du docker prend du temps (environ 10 minutes sur mon pc)
```
docker compose up -d
```

L'app est désormais accessible sur ce lien.

http://localhost:8501

* * * * *

### **5 - Déploiement avec Kubernetes**

Pour le déploiement avec Kubernetes, nous utilisons minikube.


### **6 - Fonctionnalités**

L'application offre les fonctionnalités suivantes :

1.  **Interaction via texte ou voix [DESACTIVE SUR DOCKER]**:
    -   Entrez vos messages via le clavier ou utilisez le microphone pour une interaction vocale.

2.  **Gestion de l'historique des conversations** :
    -   L'historique complet de la conversation est affiché ou réduit à la dernière réponse du bot.
    -   Téléchargez l'historique en format texte pour une sauvegarde locale.

3.  **Conversion texte-parole [DESACTIVE PAR DEFAULT]** :
    -   Les réponses du chatbot peuvent être lues à haute voix via un moteur de synthèse vocale.

4.  **Effacement des données** :
    -   Réinitialisez facilement l'historique des conversations à tout moment.

* * * * *


