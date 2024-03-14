class DirectoryException(Exception):
    """Main class for directories exception"""

    def __init__(self, head='Directory Error', message=''):
        super().__init__()
        self.head = head
        self.message = message


class DirectoryAlreadyExistException(DirectoryException):
    """Class for already existed directories"""

    def __init__(self, head='Exist Directory', message='Directory already exist.'):
        super().__init__()
        self.head = head
        self.message = message


class FormatException(Exception):
    """Class for wrong format type"""
    def __init__(self, head='Format', message='Wrong format type'):
        super().__init__()
        self.head = head
        self.message = message
