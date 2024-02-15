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

    def get_recents_of_user(self, user_id):
        chat_user_id = self.app + "#" + user_id
        return self.chat_dao.get_chat_rooms(chat_user_id)
    def get_chat_room(self,userid1, userid2):
        chat_user_id1 = self.app + "#" + userid1
        chat_user_id2 = self.app + "#" + userid2
        room_key=self.app+"#"+chat_user_id1+"#"+chat_user_id2
        room=self.chat_dao.get_chatroom_id(room_key)
        if room:
            return room
        else:
            return None
    def create_chat_room(self, userid1, userid2):
        chat_user_id1 = self.app + "#" + userid1
        chat_user_id2 = self.app + "#" + userid2
        room_key=self.app+"#"+chat_user_id1+"#"+chat_user_id2
        room_data={
            "key":room_key,
            "type":"DM",
            "name":None,
            "created_at":None,
            "updated_at":None,
            "users":[chat_user_id1,chat_user_id2],
            "app":self.app
        }
        return self.chat_dao.create_chat_room(room_data)

    def get_chat_room_details(self, chat_room_key, user_id):
        chat_user_id1 = self.app + "#" + user_id
        chats = self.chat_dao.get_chats(chat_room_key)


    def send_chat(self, chat_room_id, user_id):

        return self.post_dao.get_post()
