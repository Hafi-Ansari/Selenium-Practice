from pymongo import MongoClient
from dotenv import load_dotenv
from boilerplate import get_boilerplate_code
from description import get_problem_description
import os

load_dotenv()
connection_string = os.getenv("MONGODB_CONNECTION_STRING")


# Create a MongoDB client
client = MongoClient(connection_string)

# Access a database
db = client["leetcode-questions"]

# Access a collection
collection = db["demo"]