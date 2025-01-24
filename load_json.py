import json
import pymongo

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "chatbot_db"
COLLECTION_NAME = "courses"

def load_courses():
    """Load courses from a JSON file into MongoDB."""
    try:
        # Connect to MongoDB
        client = pymongo.MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]

        # Load JSON data
        with open("courses.json", "r", encoding="utf-8") as file:
            courses = json.load(file)

        # Insert into MongoDB
        collection.insert_many(courses)

        print(f"✅ Successfully inserted {len(courses)} courses into MongoDB!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    load_courses()