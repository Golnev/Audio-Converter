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


class EmptyDirectoryException(DirectoryException):
    """Class for empty directory"""

    def __init__(self, head='Empty Directory', message='Directory is empty.'):
        super().__init__()
        self.head = head
        self.message = message


class FormatException(Exception):
    """Class for wrong format type"""
    def __init__(self, head='Format', message=''):
        super().__init__()
        self.head = head
        self.message = message


class WrongFormatException(FormatException):
    def __init__(self, head='Wrong format', message='Wrong format type.'):
        super().__init__()
        self.head = head
        self.message = message


class EqualFormatTypesException(FormatException):
    def __init__(self, head='Equal format', message='Equal format types.'):
        super().__init__()
        self.head = head
        self.message = message
