from controller.todo_controller import TodoController
from view.view import menu_dispay, menu_select, message_display, input_display, update_display,delete_display

controller = TodoController()

controller.file_read()

while True :
    menu_dispay()

    menu = menu_select()

    if menu == "1" :
        todo = input_display()
        controller.register(todo)

    elif menu == "2" :
        id, title = update_display()
        controller.update(id, title)

    elif menu == "3" :
        id = delete_display()
        controller.remove(id)

    elif menu == "4" :
        controller.removeAll()

    elif menu == "5" :
        controller.getAllTodos()

    elif menu == "0" :
        message_display("TODO 프로그램을 종료합니다.")
        controller.file_write()
        break

    else :
        print()
        message_display("\n1, 2, 3, 4, 5, 0번 중 선택하세요")