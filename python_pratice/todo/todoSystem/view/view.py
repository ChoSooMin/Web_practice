from entity.todo import Todo

# menu display
def menu_display() :
    print("\n====== TODO ======")
    print("1. TODO 작성하기")
    print("2. TODO 수정")
    print("3. TODO 삭제")
    print("4. TODO 전체 삭제")
    print("5. TODO 목록 보기")
    print("0. 종료")

# menu select display
def menu_select() :
    menu = input("메뉴를 선택하세요 ")
    return menu

# message display
def message_display(message) :
    print(message)

# list display
def list_display(todos) :
    print("===== TODO 목록 =====")
    for todo in todos :
        print(todo)

# Todo input display
def input_display() :
    id = input("id : ")
    title = input("title : ")

    return Todo(id, title)

# update input display
def update_display() :
    id = input("수정할 id : ")
    title = input("수정할 todo : ")
    return (id, title)

# delete input display
def delete_display() :
    id = input("삭제할 id : ")
    return id