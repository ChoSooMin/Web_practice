class Todo:
    def __init__(self, id, title) :
        self.id = id
        self.title = title

    def __eq__(self, id) :
        if self.id == id :
            return True
        else :
            return False

    def __str__(self) :
        return "{0}번째 TODO : {1}".format(self.id, self.title)