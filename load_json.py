import json
import pymongo
from config import MONGO_URL, DB_NAME,COLLECTION_NAME

def load_courses():
    """Charge les cours dans la BDD MongoDB."""
    try:

        client = pymongo.MongoClient(MONGO_URL)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]

        with open("courses.json", "r", encoding="utf-8") as file:
            courses = json.load(file)

        collection.insert_many(courses)

        print(f"✅ Successfully inserted {len(courses)} courses into MongoDB!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    load_courses()