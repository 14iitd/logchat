from dao.user_dao import UserDao
from dao.followDao import FollowDao
from dao.like_dao import LikeDao


class ProfileService():
    def __init__(self):
        self.user_dao = UserDao()
        self.follow_dao=FollowDao()
        self.like_dao=LikeDao()

    def check_username(self, username):
        return self.user_dao.username_exists(username)

    def get_profile_details(self, user_id):
        profile = self.user_dao.get_profile_details(user_id)
        del profile["token"]
        profile["followers"] = self.follow_dao.get_followers(user_id)
        profile["following"] = self.follow_dao.get_followings(user_id)
        profile["likes"] = self.like_dao.get_user_like(user_id)
        return profile

    def update_user_details(self, user_id, updated_data):
        self.user_dao.update_profile_data(user_id, updated_data)
        return True
    def is_following(self,current_user,user_id):
        return self.follow_dao.is_following(user= current_user,celeb=user_id)
