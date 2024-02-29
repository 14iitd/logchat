from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException
#B$P*nZ#AU8WU4vs

class MongoDBConnector:
    def __init__(self, mongo_uri: str, db_name: str):
        self.mongo_uri = mongo_uri
        self.db_name = db_name
        self.client = None
        self.db = None
        self.connect()

    def connect(self):
        self.client = MongoClient(self.mongo_uri)
        self.get_database()

    def get_database(self):
        if self.client:
            self.db= self.client[self.db_name]
        else:
            raise HTTPException(status_code=500, detail="MongoDB connection not established")

    def close(self):
        if self.client:
            self.client.close()
#mongo_connector = MongoDBConnector(mongo_uri="mongodb+srv://dev:B$P*nZ#AU8WU4vs@cluster0.hkuutb6.mongodb.net/", db_name="logz")
mongo_connector = MongoDBConnector(mongo_uri="mongodb://localhost:27017", db_name="logz")
# mongo_connector.connect()
# mongo_connector.get_database()["demo"].insert_one({"a": 1})
