from mongoConnector import mongo_connector
from utils import convert_to_str


class LikeDao():
    def __init__(self):
        self.db = mongo_connector.db

    def like(self, user_id, post_id, user2):
        like_collection = self.db["posts_like"]
        like_data = {"user1": user_id, "post_id": post_id, "post_user": user2}
        new_post = like_collection.insert_one(like_data)
        created_post = like_collection.find_one({"_id": new_post.inserted_id})
        created_post["_id"] = str(created_post["_id"])
        return created_post

    def dislike(self, user_id, post_id):
        like_collection = self.db["posts_like"]
        query = {"user1": user_id, post_id: post_id}
        deleted_post = like_collection.find_one_and_delete(query)
        if deleted_post:
            deleted_post["_id"] = str(deleted_post["_id"])
        return deleted_post
    def haslike(self, user_id, post_id):
        like_collection = self.db["posts_like"]
        query = {"user1": user_id, post_id: post_id}
        post = like_collection.find_one(query)
        if post:
            post["_id"] = str(post["_id"])
        return None

    def get_post_likes(self, post_id):
        like_collection = self.db["posts_like"]
        likes = like_collection.count({"post_id": post_id})
        return likes

    def get_user_like(self, user2):
        like_collection = self.db["posts_like"]
        likes = like_collection.count_documents({"post_user": user2})
        return likes

    def get_likes_by_posts(self,post_ids):
        like_collection = self.db["posts_like"]
        likes = like_collection.aggregate([{"$match": {"post_id": { "$in": post_ids }}},{"$group": {"_id": "$post_id","count": { '$sum': 1 }}},{'$project': {'_id': 0,'post_id': '$_id','count': 1}}])
        return likes

