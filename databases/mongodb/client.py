from pymongo import MongoClient
from config.config import config

class MongoDBClient:
    def __init__(self):
        self.client = MongoClient(config.MONGO_URI)
        self.db = self.client[config.MONGO_DB]

    def get_collection(self, name):
        return self.db[name]


mongo_client = MongoDBClient()