class Task:
    def __init__(self, orginal_language, created_at, tarns_language, task_id=None):
        self.orginal_language = orginal_language
        self.created_at = created_at
        self.task_id = task_id
        self.tarns_language = tarns_language

    def get_attrs_as_dict(self):
        return {
            "id": self.task_id,
            "orginal_language": self.orginal_language,
            "created_at": self.created_at,
            "tarns_language": self.tarns_language
        }
