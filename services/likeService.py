from dao.like_dao import LikeDao
from dao.post_dao import PostDao


class LikeService():
    def __init__(self):
        self.like_dao = LikeDao()
        self.post_dao = PostDao()

    def get_likes_by_post_ids(self,post_ids):
        likes = self.like_dao.get_likes_by_posts(post_ids)

        like_map={}
        for item in likes:
            like_map[item["post_id"]]=item.get("count")
        #import pdb;
        #pdb.set_trace()
        return like_map

    def like_post(self, user_id, post_id):
        post_details = self.post_dao.get_post_by_id(post_id)
        return self.like_dao.like(user_id, post_id, post_details.get("user_id"))
    def dislike_post(self, user_id, post_id):
        post_details = self.post_dao.get_post_by_id(post_id)
        return self.like_dao.dislike(user_id, post_id, post_details.get("user_id"))
    def haslike_post(self, user_id, post_id):
        return self.like_dao.haslike(user_id, post_id)

    def unlike_post(self, user_id, post_id):
        return self.like_dao.unlike(user_id,post_id)
