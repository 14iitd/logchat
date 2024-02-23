from dao.chatDao import ChatDao


class ChatService:
    def get_recents_of_user(self, user_id):
        pass

    def create_chat_room(self, userid1, userid2):
        pass

    def get_chats_for_user(self, chat_room_id, user_id):
        pass

    def send_chat(self, chat_room_id, user_id):
        pass


class LoggrChatService():
    def __init__(self):
        self.app = "loggr"
        self.chat_dao = ChatDao()

    def get_recents(self, user_id):
        chat_user_id = self.app + "#" + user_id
        return self.chat_dao.get_recent_chat_rooms(chat_user_id)
    def get_chats(self,userid1, userid2):
        room_key=self.app+"#"+userid1+"#"+userid2
        chats=self.chat_dao.get_chats_for_room(room_key)
        return chats
    def update_chat_room(self, userid1, userid2):
        room_key=self.app+"#"+userid1+"#"+userid2
        room_data={
            "key":room_key,
            "type":"DM",
            "name":None,
            "created_at":None,
            "updated_at":None,
            "app":self.app
        }
        return self.chat_dao.update_chat_room(room_data)

    def get_chat_room_details(self, chat_room_key, user_id):
        chat_user_id1 = self.app + "#" + user_id
        chats = self.chat_dao.get_chats(chat_room_key)


    def send_chat(self, chat_room_id, user_id):

        return self.post_dao.get_post()
