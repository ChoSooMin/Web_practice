from controller_view.student_controller import StudentController
from view_template.template_view import menu_display, message_display, menu_select, input_display, update_display, delete_display

controller = StudentController()

controller.file_read()
while True:
    menu_display()

    menu = menu_select() # 메뉴를 선택해주세요

    if menu == "1" :
        student = input_display()
        controller.register(student)

    elif menu == "2" :
        controller.getAllStudents()

    elif menu == "3" :
        id, major = update_display()
        controller.update(id, major)

    elif menu == "4" :
        id = delete_display()
        controller.remove(id)

    elif menu == "0" :
        message_display("수강생 관리 프로그램을 종료합니다")
        controller.file_write()
        break
    else:
        print("")
        message_display("1, 2, 3, 4, 0 번 중 선택하세요")