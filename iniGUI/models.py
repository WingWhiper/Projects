class Section:
    def __init__(self, name):
        self.name = name
        self.options = []

    def add_option(self, option):
        self.options.append(option)


class Option:
    def __init__(self, name, value, is_bool):
        self.name = name
        self.value = value
        self.is_bool = is_bool
