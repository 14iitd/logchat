from mongoConnector import mongo_connector
from utils import convert_to_str
from bson import ObjectId


class UserDao():
    def __init__(self):
        self.db = mongo_connector.db

    def get_user_by_token(self, token):
        user_collection = self.db["users"]
        user = user_collection.find_one({"token": token})
        if user:
            user["id"] = str(user["_id"])
            user["_id"] = None
        return user

    def create_user(self, user_data):
        user_collection = self.db["users"]
        new_user = user_collection.insert_one(user_data)
        user = user_collection.find_one({"_id": new_user.inserted_id})
        user["id"] = str(user["_id"])
        user["_id"] = None
        return user

    def get_user_details(self,user_ids):
        user_collection = self.db["users"]
        user_ids=[ObjectId(x) for x in user_ids]
        #import pdb;pdb.set_trace()
        users = user_collection.find({ "_id": { "$in": user_ids} })
        return users



