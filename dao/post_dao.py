from mongoConnector import mongo_connector
from utils import convert_to_str


class PostDao():
    def __init__(self):
        self.db = mongo_connector.db

    def get_posts_of_user(self, user_id):
        post_collection = self.db["posts"]
        user_posts = list(post_collection.find({"user_id": user_id}))
        return convert_to_str(user_posts)

    def create_post(self, post):
        post_collection = self.db["posts"]
        new_post = post_collection.insert_one(post)
        created_post = post_collection.find_one({"_id": new_post.inserted_id})
        created_post["_id"] = str(created_post["_id"])
        return created_post

    def get_post(self):
        post_collection = self.db["posts"]
        user_posts = list(post_collection.find().sort("created_at", -1))
        return convert_to_str(user_posts)

    def get_post_by_id(self, post_id):
        from bson import ObjectId
        post_collection = self.db["posts"]
        user_posts = list(post_collection.find({"_id": ObjectId(post_id)}))[0]
        return user_posts
