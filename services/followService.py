from dao.followDao import FollowDao


class FollowService():
    def __init__(self):
        self.follow_dao = FollowDao()

    def follow(self, follow_data):
        return self.follow_dao.follow_user(follow_data)

    def unfollow(self, user, celeb):
        return self.follow_dao.unfollow_user(user1=user, user2=celeb)
    def get_celeb_user_ids(self,user_id):
        return self.follow_dao.get_following_user_ids(user_id)
