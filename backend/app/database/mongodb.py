from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from app.config import  MONGODB_URL, DATABASE_NAME

client = None
db = None

def connect_to_mongodb():
    global client, db
    try:
        client = MongoClient(MONGODB_URL, serverSelectionTimeoutMS=5000)
        client.admin.command('ping')  # Check if the server is available
        db = client[DATABASE_NAME]
        print("Connected to MongoDB")
    except ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")
        raise

def close_mongodb_connection():
    global client
    if client:
        client.close()
        print("MongoDB connection closed")

def get_database():
    if db is None:
        raise RuntimeError("Database connection is not established. Call connect_to_mongodb() first.")
    return db