from dao.post_dao import PostDao


class PostService():
    def __init__(self):
        self.post_dao = PostDao()

    def get_user_post(self, user_id):
        return self.post_dao.get_posts_of_user(user_id)

    def create_post(self, post_data):
        post_data = self.post_dao.create_post(post_data)
        return post_data
    # def get_post_by_id(self,post_id):
