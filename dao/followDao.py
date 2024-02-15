from mongoConnector import mongo_connector
from utils import convert_to_str


class FollowDao():
    def __init__(self):
        self.db = mongo_connector.db

    def follow_user(self, follow_data):
        """

        :return:
        """
        follow_collection = self.db["follow"]
        new_follow = follow_collection.insert_one({"user": follow_data["user_id"], "celeb": follow_data["celeb"]})
        user = follow_collection.find_one({"_id": new_follow.inserted_id})
        return convert_to_str(user)

    # def follow_hashtag(self, following_user_id, hashtag):
    #     tag_follow_collection = self.db["hashtag_follow"]
    #     new_follow = tag_follow_collection.insert_one({"follower": following_user_id, "tag": hashtag})
    #     user = tag_follow_collection.find_one({"_id": new_follow.inserted_id})
    #     return convert_to_str(user)

    def unfollow_user(self, user1, user2):
        follow_collection = self.db["follow"]
        query = {"user": user1, "celeb": user2}
        result = follow_collection.delete_one(query)
        return result.matched_count()

    def get_followers(self, celeb):
        follow_collection = self.db["follow"]
        count = follow_collection.count({"celeb": celeb})
        return count

    def get_followings(self, user):
        follow_collection = self.db["follow"]
        count = follow_collection.count({"user": user})
        return count

    def get_following_user_ids(self, user):
        follow_collection = self.db["follow"]
        celeb = follow_collection.find({"user": user})
        res = []
        for ce in celeb:
            res.append(ce["celeb"])
        return res
    def is_following(self,user,celeb):
        follow_collection = self.db["follow"]
        celeb = follow_collection.find({"user": user,"celeb":user})
        if celeb:
            return True
        return False

