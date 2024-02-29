from dao.post_dao import PostDao


class PostService():
    def __init__(self):
        self.post_dao = PostDao()

    def get_user_post(self, user_id):
        return self.post_dao.get_posts_of_user(user_id)

    def create_post(self, post_data):
        post_data = self.post_dao.create_post(post_data)
        return post_data

    def update_post(self, user_id,post_id, data):
        post = self.post_dao.get_post_by_id(post_id)
        if post.get("user_id")==user_id:
             self.post_dao.update_post(post_id,data)
        else:
            raise Exception("userId not matching ")
        return data

    def delete_post(self, user_id, post_id):
        post = self.post_dao.get_post_by_id(post_id)
        if post.get("user_id")==user_id:
            self.post_dao.delete_post(post_id)
        else:
            raise Exception("userId not matching ")
