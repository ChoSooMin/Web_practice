class DuplicateException(Exception) :
    def __init__(self, message):
        super().__init__(message + " : 중복된 ID")