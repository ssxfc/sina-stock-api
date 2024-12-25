class UnSupportedException(Exception):
    def __init__(self, message):
        self.message = message


class CannotParsedException(Exception):
    def __init__(self, message):
        self.message = message