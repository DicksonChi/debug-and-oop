import uuid


class Question:
    def __init__(self, name, content):
        self.question_id = uuid.uuid4()
        self.name = name
        self.content = content
        self.options = list()

    def get_name(self):
        return self.name

    def get_content(self):
        return self.content

    def add_option(self, option):
        self.options.append(option)

    def get_options(self):
        return self.options

    def choose_right_answer(self, option_id):
        for option in self.options:
            if option.option_id == option_id:
                option.choose_option()
            else:
                option.un_choose_option()

    def get_right_answer(self):
        right_option = None
        for option in self.options:
            if option.is_answer:
                right_option = option
                break
        return right_option
