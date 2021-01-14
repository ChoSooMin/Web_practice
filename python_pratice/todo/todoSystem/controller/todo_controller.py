from service.todo_service import TodoService
from view.view import message_display,list_display

class TodoController :
    def file_read(self) :
        service = TodoService()
        service.file_read()

    def file_write(self) :
        service = TodoService()
        service.file_write()

    def register(self, todo) :
        service = TodoService()
        message = service.register(todo)
        message_display(message)

    def getAllTodos(self) :
        service = TodoService()
        todos = service.getAllTodos()
        list_display(todos)

    def update(self, id, title) :
        if id == "" or title == "" :
            message_display("id와 todo title을 입력해주세요")
        service = TodoService()
        message = service.update(id, title)
        message_display(message)

    def remove(self, id) :
        if id == "" :
            message_display("id를 입력해주세요")
        service = TodoService()
        message = service.remove(id)
        message_display(message)

    def removeAll(self) :
        service = TodoService()
        message = service.removeAll()
        message_display(message)