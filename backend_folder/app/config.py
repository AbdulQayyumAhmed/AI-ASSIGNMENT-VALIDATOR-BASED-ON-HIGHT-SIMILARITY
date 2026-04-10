from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

MONGO_URL = os.getenv("MONGO_URI", "mongodb+srv://user:uS3er2060@bootcamptracker.roknckd.mongodb.net/")
DB_NAME = os.getenv("DB_NAME", "test")

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

users_col = db["users"]
assignments_col = db["assignments"]
submitted_col = db["student_assignments"]
notifications_col = db["notifications"]