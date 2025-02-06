import json
import pymongo
import os
from src.config import DB_NAME,COLLECTION_NAME

# check si c'est un env docker
if os.path.exists('/.dockerenv'): # Pour Docker 
    MONGO_URL = "mongodb://mongo:27017/"
else: # En Local 
    MONGO_URL = "mongodb://localhost:27017/"

def load_courses():
    """Charge les cours dans la BDD MongoDB."""
    try:

        client = pymongo.MongoClient(MONGO_URL)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]

        with open("data/courses.json", "r", encoding="utf-8") as file:
            courses = json.load(file)

        collection.insert_many(courses)

        print(f"✅ Successfully inserted {len(courses)} courses into MongoDB!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    load_courses()