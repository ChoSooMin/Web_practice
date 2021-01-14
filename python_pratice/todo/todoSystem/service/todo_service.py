from dao.file_dao import file_read, file_write # 파일에서 데이터를 읽어오고, 저장하기 위해
from exception.idnotfound_exception import IDNotFoundException

class TodoService :

    todos = []

    # todo 존재여부
    def is_exist(self, id) :
        for index, student in enumerate(TodoService.todos) :
            if todo.id == id :
                return index

        return -1

    # todo 등록
    def register(self, todo) :
        index = self.is_exist(todo.id)

        if index < 0 :
            TodoService.todos.append(todo)
            return "{0}(이)가 등록되었습니다".format(todo.id)

    # todo 목록
    def getAllTodos(self) :
        return TodoService.todos

    # todo 수정
    def update(self, id, title) :
        index = self.is_exist(id)

        if index > -1 :
            TodoService.todos[index].title = title
            return "{0}(이)가 수정되었습니다".format(id)

        else :
            try :
                raise IDNotFoundException(id)
            except IDNotFoundException as updateError :
                return str(updateError)

    # todo 삭제
    def remove(self, id) :
        index = self.is_exist(id)

        if index > -1 :
            TodoService.todos.pop(index)
            return "{0}를 삭제했습니다".format(index)

        else :
            try :
                raise IDNotFoundException(id)
            except IDNotFoundException as removeError :
                return str(removeError)

    # todo 전체 삭제
    def removeAll(self) :
        todos.clear()
        return "todo를 모두 삭제했습니다"

    def file_read(self) : # 프로그램 시작시 파일에서 데이터를 읽어온다
        TodoService.todos = file_read()

    def file_write(self) : # 프로그램 끝날 때 파일에 데이터를 저장한다
        file_write(TodoService.todos)