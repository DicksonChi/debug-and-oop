import uuid


class Option:
    def __init__(self, name, content):
        self.option_id = uuid.uuid4()
        self.name = name
        self.content = content
        self.is_answer = False

    def get_name(self):
        return self.name

    def get_content(self):
        return self.content

    def choose_option(self):
        self.is_answer = True

    def un_choose_option(self):
        self.is_answer = False
