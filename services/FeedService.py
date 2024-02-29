from dao.post_dao import PostDao
from dao.user_dao import UserDao
from timeUtils import format_time_ago
from services.likeService import LikeService
from services.followService import FollowService
#from services.reLogService import ReLogService


class FeedService():
    def __init__(self):
        self.post_dao = PostDao()
        self.user_dao = UserDao()
        self.likeService= LikeService()
        self.followService=FollowService()
        #self.relogService =

    def get_feed_for_user(self, user_id):
        following = self.followService.get_celeb_user_ids(user_id)
        following.append(user_id)
        posts = self.post_dao.get_post(following)+self.post_dao.get_recommended_post()
        user_ids=[]
        post_ids=[]
        for item in posts:
            # item["posted_at"]=format_time_ago(item.get("created_at"))
            if item.get("relog_post_id"):
                post_ids.append(str(item.get("relog_post_id")))
            else:
                # user_ids.append(item.get("user_id"))
                post_ids.append(str(item.get("_id")))
        posts = self.post_dao.get_post_details(post_ids)
        for item in posts:
            item["posted_at"]=format_time_ago(item.get("created_at"))
            user_ids.append(item.get("user_id"))
        users = self.user_dao.get_user_details(user_ids)
        users_map = {}
        for item in users:
            temp_user_id=str(item["_id"])
            users_map[temp_user_id] = {"id":temp_user_id,
                                       "name":item["username"],
                                       "profile_image":item.get("image_url")}
        #print(users_map)

        likes_map=self.likeService.get_likes_by_post_ids(post_ids)
        for item in posts:
            #import pdb;pdb.set_trace()
            item["user"] = users_map.get(item["user_id"])
            item["likes"]=likes_map.get(item["_id"])
            item["relog"] = 2
            item["share"] = 31
        #import pdb;
        #pdb.set_trace()
        return posts
