from mongoConnector import mongo_connector
from utils import convert_to_str
from bson import ObjectId


class UserDao():
    def __init__(self):
        self.db = mongo_connector.db

    def get_user_by_token(self, token, email):

        user_collection = self.db["users"]
        user = user_collection.find_one({
            "$or": [
                {"token": token},
                {"email": email}
            ]
        })
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

    def get_user_details(self, user_ids):
        try:
            user_collection = self.db["users"]
            user_ids = [ObjectId(x) for x in user_ids if ObjectId.is_valid(x)]
            # import pdb;pdb.set_trace()
            users = user_collection.find({"_id": {"$in": user_ids}})
            return users
        except:
            return {}

    def username_exists(self, username):
        user_collection = self.db["users"]
        user = user_collection.find_one({"username": username})
        if not user:
            return False
        return True

    def get_profile_details(self, user_id):
        user_collection = self.db["users"]
        user = user_collection.find_one({"_id": ObjectId(user_id)})
        if user:
            user["id"] = str(user["_id"])
            user["_id"] = None
        return user

    def update_profile_data(self, user_id, data):
        user_collection = self.db["users"]
        user_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"bio": data.get("bio"), "full_name": data["name"], "image_url": data["profile_image"],
                      "username": data["username"]}}
        )
        return True
