from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create or connect to your database
db = client["fashion_db"]

# Create or connect to your collection
user_collection = db["users"]
