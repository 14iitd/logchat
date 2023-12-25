from dao.post_dao import PostDao

class ReLogService():
    def __init__(self):
        self.post_dao = PostDao()

    def get_user_post(self, user_id):
        return self.post_dao.get_posts_of_user(user_id)

    def create_relog(self, post_data, user2):
        post_data["relog_user_id"]=user2
        post_data = self.post_dao.create_post(post_data)
        return post_data
    # def get_post_by_id(self,post_id):
