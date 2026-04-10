from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URL)

db = client[os.getenv("DB_NAME", "test")]

users_col = db["users"]
assignments_col = db["assignments"]
submitted_col = db["student_assignments"]
notifications_col = db["notifications"]