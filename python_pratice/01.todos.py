# todo 저장하는 시스템
todos = []
todoNum = 0

# { "todoNum": todoNum, "title": title } 데이터 형식
# 등록, 수정, 삭제, 일정 목록 보기, 전체 삭제 기능

while True :
    print("\n====== TODO ======")
    print("1. TODO 작성하기")
    print("2. TODO 수정")
    print("3. TODO 삭제")
    print("4. TODO 전체 삭제")
    print("5. TODO 목록 보기")
    print("0. 종료")

    menu = input("메뉴를 선택하세요 ")

    if menu == "1" :
        title = input("todo를 입력해주세요 : ")

        todo = { "todoNum": todoNum, "title": title }
        todos.append(todo)
        todoNum += 1

        print("{0}(이)가 등록되었습니다".format(title))
    
    elif menu == "2":
        todoNum = input("수정할 todo 번호 : ")

        while not todoNum.isdecimal() :
            print("todo 번호는 숫자로 입력해주세요")
            todoNum = input("수정할 todo 번호 : ")

        title = input("수정할 todo : ")
        for todo in todos : 
            if todo["todoNum"] == int(todoNum) :
                todo["title"] = title
                print("{0}번째 todo가 변경되었습니다".format(todoNum))
    
    elif menu == "3" :
        todoNum = input("삭제할 todo 번호 : ")
        
        while not todoNum.isdecimal() :
            print("todo 번호는 숫자로 입력해 주세요")
            todoNum = input("삭제할 todo 번호 : ")

        for todo in todos :
            if todo["todoNum"] == int(todoNum) :
                delete = input("todo({0})를 삭제하겠습니까? [y/n]".format(todo["title"]))

                if delete == "y" or delete == "Y" :
                    todos.remove(todo)
                    print("todo({0})를 삭제했습니다".format(todo["title"]))
                else :
                    pass
    
    elif menu == "4" :
        delete = input("todo 전체를 삭제하겠습니까? [y/n]")

        if delete == "y" or delete == "Y" :
            todos.clear()
            print("todo를 모두 삭제했습니다")
        else :
            pass
    
    elif menu == "5" :
        print("===== TODO 목록 =====")
        for todo in todos :
            print("{0}번째 TODO : {1}".format(todo["todoNum"], todo["title"]))
    
    elif menu == "0" :
        print("TODO 프로그램을 종료합니다")
        break

    else :
        print("\n1, 2, 3, 4, 5, 0 번 중 선택하세요")