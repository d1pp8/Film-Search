from databases.mongodb.client import mongo_client
from config.config import config
from datetime import datetime

def log_search(search_type: str, param: dict, result_count: int):
    collection = mongo_client.get_collection(config.MONGO_COLLECTION)

    document = {
        "timestamp": datetime.now(),
        "search_type": search_type,
        "param": param,
        "result_count": result_count
    }

    collection.insert_one(document)

