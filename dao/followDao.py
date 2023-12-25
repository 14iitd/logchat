from mongoConnector import mongo_connector
from utils import convert_to_str


class FollowDao():
    def __init__(self):
        self.db = mongo_connector.db

    def follow_user(self, user1 ,user2):
        """
        :param user1: user1 follows user2
        :param user2: user2 is followed by user1
        :return:
        """
        follow_collection = self.db["follow"]
        new_follow = follow_collection.insert_one({"user1": user1, "user2": user2})
        user = follow_collection.find_one({"_id": new_follow.inserted_id})
        return convert_to_str(user)

    def follow_hashtag(self, following_user_id, hashtag):
        tag_follow_collection = self.db["hashtag_follow"]
        new_follow = tag_follow_collection.insert_one({"follower": following_user_id, "tag": hashtag})
        user = tag_follow_collection.find_one({"_id": new_follow.inserted_id})
        return convert_to_str(user)

    def unfollow_user(self, user1, user2):
        follow_collection = self.db["follow"]
        update_data = {"$set": {"status": "deleted"}}
        query = {"user1": user1, "user2": user2}
        result = follow_collection.update_one(query, update_data)
        return result.matched_count()

    def get_followers(self, user2):
        follow_collection = self.db["follow"]
        count = follow_collection.count({ "user2": user2 })
        return count

    def get_followings(self, user1):
        follow_collection = self.db["follow"]
        count = follow_collection.count({"user1": user1})
        return count

    def get_followed_hashtags(self, user_id):
        return None