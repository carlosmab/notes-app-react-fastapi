import os
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.getenv('MONGODB_URI')

cluster = MongoClient(MONGODB_URI)
db = cluster["notesapp"]

