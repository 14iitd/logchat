from dao.user_dao import UserDao


class UserService():
    def __init__(self):
        self.user_dao = UserDao()

    def get_user_by_token(self, token):
        return self.user_dao.get_user_by_token(token)

    def create_user(self, user_request_data):
        new_user = self.user_dao.create_user(user_request_data)
        return new_user
