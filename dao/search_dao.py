from mongoConnector import mongo_connector
from utils import convert_to_str


class SearchDao():
    def __init__(self):
        self.db = mongo_connector.db

    def get_user_by_query(self, q):
        user_collection = self.db["users"]
        print(q)
        import re
        pattern = re.compile(q, re.IGNORECASE)
        # Find documents matching the text search query
        result_text_search = user_collection.find({"username": {"$regex": pattern}})

        # # Find all documents
        # result_all = user_collection.find()

        # Convert cursor objects to lists of dictionaries
        text_search_results = list(result_text_search)
        #all_results = list(result_all)

        # Concatenate both result sets
        combined_results = text_search_results #+ all_results

        # Convert combined results to string representation
        return convert_to_str(combined_results)




