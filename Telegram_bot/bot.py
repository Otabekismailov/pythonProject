
class Student:
    def __init__(self, full_name, chat_id):
        self.full_name = full_name
        self.chat_id = chat_id

    def get_student(self):
        return {
            "chat_id": self.chat_id,
            "full_name": self.full_name
        }
