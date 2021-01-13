# 부모 class (Super Class) : attribute와 operation 자식class(Sub Class)에서 사용 허용 (상속)
class Person : 
    def __init__(self, id, name) :  # Person() : 생성자 호출 시 내부적으로 호출 
        self.id = id                # 객체 생성시 초기화 구현
        self.name = name            # { "id": id, "name": name }

    def info(self) : # self는 꼭 넣어줘야 한다. #객체 operation :member method
        print("학번: {0}, 이름: {1}".format(self.id, self.name), end = " ") # 공백 문자

    def __str__(self) :
        return "학번: {0}, 이름: {1}".format(self.id, self.name)

# Person의 Sub Class
class Student(Person) :
    def __init__(self, id, name, major) :
        super().__init__(id, name)  # Super Class의 생성자 호출
        self.major = major

    # def student_info(self) : # self 필요
    #     super().info()                # Super Class의 메소드 호출
    #     print("전공: {0}".format(self.major))

    def __str__(self) :
        return super().__str__() + ", 전공: {0}".format(self.major)

    def info(self) : 
        super().info()
        print("전공: {0}".format(self.major))

class Teacher(Person) :
    def __init__(self, id, name, subject) :
        super().__init__(id, name)
        self.subject = subject

    # def teacher_info(self) :
    #     super().info()
    #     print("과목: {0}".format(self.subject))

    def __str__(self) :
        return super().__str__() + ", 과목: {0}".format(self.subject)

    def info(self) : 
        super().info()
        print("과목: {0}".format(self.subject))

class Employee(Person) :
    def __init__(self, id, name, department) :
        super().__init__(id, name)
        self.department = department
    
    # def employee_info(self) :
    #     super().info()
    #     print("부서 : {0}".format(self.department))

    def __str__(self) :
        return super().__str__() + ", 부서: {0}".format(self.department)

    def info(self) :
        super().info()
        print("부서 : {0}".format(self.department))

# 사용자 코드
# 객체 생성 : Class이름([argumentlist])
student = Student("CMSA07", "조수민", "컴퓨터공학과")
students = Student("CMSA07", "조수민", "컴퓨터공학과")
teacher = Teacher("T001", "숨", "클라우드")
employee = Employee("E001", "숨숨", "백엔드 개발")

# isinstance() 함수
# print("isinstance student Student : ", isinstance(student, Student))
# print("isinstance student Teacher : ", isinstance(student, Teacher))
# print("isinstance student Person : ", isinstance(student, Person))

# 객체 사용 : object이름.변수, object이름.기능([argumentlist])
# student.student_info()
# teacher.teacher_info()
# employee.employee_info()

# print(student)
# print(teacher)
# print(employee)

# 다형성 : 한 가지 타입으로 여러 형태 사용 ex) Person 타입의 Student, Teacher, Employee
#       Super에서 제공되는 method를 Sub에서 재정의할 수 있다. - 사용자가 Super의 method를
#       호출하더라도 재정의된 Sub의 method가 다양하게 응답될 수 있다.
student.info()
teacher.info()
employee.info()