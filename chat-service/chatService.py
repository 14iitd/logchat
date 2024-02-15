from dao.followDao import FollowDao


class FollowService():
    def __init__(self):
        self.follow_dao = FollowDao()

    def get_feed_for_user(self, user_id):
        return self.post_dao.get_post()
