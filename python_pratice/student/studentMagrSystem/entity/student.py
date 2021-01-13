class Student :
    # 생성자 : id, name, age, major
    def __init__(self, id, name, age, major):
        self.id = id
        self.name = name
        self.age = age
        self.major = major
    
    # 객체의 id가 같은 경우 True
    def __eq__(self, id) :
        if self.id == id :
            return True
        else :
            return False
    
    # 객체를 대표하는 문자열
    def __str__(self) :
        return "학번: {0}, 나이: {1}, 전공{2}".format(self.id, self.name, self.major)

    