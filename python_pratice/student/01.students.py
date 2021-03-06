# 수강생 관리 시스템
students = []
id = 0

while True:
    print("\n====== Cloud MSA 반 수강생 관리 시스템 ======")
    print("1. 수강생 정보 등록")
    print("2. 수강생 목록 보기")
    print("3. 수강생 정보 수정")
    print("4. 수강생 정보 삭제")
    print("0. 종료")

    menu = input("메뉴를 선택하세요 ")

    if menu == "1" :
        name = input("이름: ")
        age = input("나이: ")
        while not age.isdecimal():
            print("나이는 숫자로 입력해주세요")
            age = input("나이: ")
        major = input("전공: ")

        student = { "id": id, "name": name, "age": age, "major": major }
        students.append(student)
        id += 1
        print("{0}(이)가 등록되었습니다".format(name))
    elif menu == "2" :
        print("====== 수강생 목록 보기 ======")
        for student in students:
            print("수강생번호: {0}, 이름: {1}, 나이: {2}, 전공: {3}".format(student["id"], student["name"], student["age"], student["major"]))
    elif menu == "3" :
        id = input("수정할 수강생 번호: ")

        while not id.isdecimal() :
            print("수강생 번호는 숫자로 입력해 주세요")
            id = input("수정할 수강생 번호: ")
        
        major = input("수정할 전공: ")
        for student in students : 
            if student["id"] == int(id) :
                student["major"] = major
                print("{0}의 전공 정보가 수정되었습니다".format(student["name"]))
    elif menu == "4" :
        id = input("삭제할 수강생 번호: ")

        while not id.isdecimal() :
            print("수강생 번호는 숫자로 입력해 주세요")
            id = input("삭제할 수강생 번호: ")

        for student in students : 
            if student["id"] == int(id) : 
                delete = input("{0}의 정보를 삭제하시겠습니까? [y/n] ".format(student["name"]))

                if delete == "y" or delete == "Y" :
                    students.remove(student)
                    print("{0}의 정보를 삭제헀습니다".format(student["name"]))
                else : 
                    pass
    elif menu == "0" :
        print("수강생 관리 프로그램을 종료합니다")
        break
    else:
        print("\n1, 2, 3, 4, 0 번 중 선택하세요")