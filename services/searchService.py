from dao.search_dao import SearchDao


class SearchService():
    def __init__(self):
        self.search_dao = SearchDao()

    def get_users_by_search(self, query):
        return self.search_dao.get_user_by_query(query)
