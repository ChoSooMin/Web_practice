class Person : 
    def __init__(self, id, name) :
        self.id = id
        self.name = name

    def info(self) : # self는 꼭 넣어줘야 한다.
        print("학번: {0}, 이름: {1}".format(self.id, self.name), end = " ") # 공백 문자

class Student(Person) :
    def __init__(self, id, name, major) :
        super().__init__(id, name)
        self.major = major

    def student_info(self) : # self 필요
        super.info()
        print("전공: {0}".format(self.major))