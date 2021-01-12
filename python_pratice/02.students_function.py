# 수강생 관리 시스템
students = [] # global variable

# 수강생 등록 : list students에 id 중복체크하고 존재하지 않는 경우 정보 저장하고 message 리턴
def register(student) :
    index = is_exist(student["id"])
    if (index < 0) :
        students.append(student)
        return "{0}(이)가 등록되었습니다".format(student["name"])
    else :
        return "이미 등록된 수강생입니다"


# 수강생 목록 : list students 목록 리턴
def getAllStudents() :
    print("====== 수강생 목록 보기 ======")

    for student in students :
        print("수강생번호: {0}, 이름: {1}, 나이: {2}, 전공: {3}".format(student["id"], student["name"], student["age"], student["major"]))
    return

# 수강생 수정 : id 검색해서 전공정보 수정하고 message 리턴
def update(id, major) :
    index = is_exist(id)
    
    if index > -1 : 
        students[index]["major"] = major
        return "{0}의 전공 정보가 수정되었습니다".format(student["id"])
    else :
        return "{0}의 정보가 존재하지 않습니다".format(student["id"])

# 수강생 삭제 : id 검색해서 수강생 정보 삭제 message 리턴
def remove(id) :
    index = is_exist(id)

    if index > -1 : 
        students.pop(int(index))
        return "{0}의 정보를 삭제했습니다".format(id)
    else :
        return "{0}의 정보가 존재하지 않습니다".format(id)

# 수강생 존재여부 : id 검색해서 list students의 index 값 리턴
def is_exist(id) :
    for index, student in enumerate(students) :
        if student["id"] == id :
            return index
        
    return -1

# menu display
def menu_display() :
    print("\n====== Cloud MSA 반 수강생 관리 시스템 ======")
    print("1. 수강생 정보 등록")
    print("2. 수강생 목록 보기")
    print("3. 수강생 정보 수정")
    print("4. 수강생 정보 삭제")
    print("0. 종료")

# message display
def message_display(message) :
    print(message)


while True:
    menu_display()

    menu = input("메뉴를 선택하세요 ")

    if menu == "1" :
        id = input("학번: ")
        name = input("이름: ")
        age = input("나이: ")
        while not age.isdecimal():
            print("나이는 숫자로 입력해주세요")
            age = input("나이: ")
        major = input("전공: ")

        student = { "id": id, "name": name, "age": age, "major": major }

        message_display(register(student)) # 함수 사용

    elif menu == "2" :
        getAllStudents()

    elif menu == "3" :
        id = input("수정할 수강생 번호: ")

        while not id.isdecimal() :
            print("수강생 번호는 숫자로 입력해 주세요")
            id = input("수정할 수강생 번호: ")

        major = input("수정할 전공: ")
        message_display(update(id, major))

    elif menu == "4" :
        id = input("삭제할 수강생 번호: ")

        while not id.isdecimal() :
            print("수강생 번호는 숫자로 입력해 주세요")
            id = input("삭제할 수강생 번호: ")

        message_display(remove(id))

    elif menu == "0" :
        print("수강생 관리 프로그램을 종료합니다")
        break
    else:
        print("\n1, 2, 3, 4, 0 번 중 선택하세요")