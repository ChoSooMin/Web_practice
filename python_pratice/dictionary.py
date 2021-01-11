# dictionary type : variable_name=  { "name": "value", .... } value: int, float, boolean, str, list
# data access : variable_name{"name"}
# student = { "name": "조수민", "age": 26, "major": "컴퓨터학과" }
# students = []
# students.append({ "name": "조수민", "age": 26, "major": "컴퓨터학과" })
# students.append({ "name": "스노우필드", "age": 26, "major": "인공지능" })
# print("이름: {0}, 나이: {1}, 전공: {2}".format(student["name"], student["age"], student["major"]))

students = [{ "name": "조수민", "age": 26, "major": "컴퓨터학과" }, { "name": "스노우필드", "age": 26, "major": "인공지능" }] # 리스트로 선언
for s in students:
    print("이름: {0}, 나이: {1}, 전공: {2}".format(s["name"], s["age"], s["major"]))

# dictionary 추가, 수정 : "name" : value 쌍으로 추가, 수정 ("name"이라는 키 값이 존재하면 수정, 존재하지 않으면 추가)
students[0]["studentId"] = "cloudMSA01" # studentId 추가
print(students[0])
students[0]["major"] = "인공지능" # key 값이 존재하면 value 값을 수정한다.
print(students[0])

# dictionary 삭제
del students[0]["studentId"] # studentId 삭제 (없는 key 값을 입력할 경우, KeyError가 뜬다)
print(students[0])

# 위의 예제들에서 key를 잘못 입력하면, KeyError가 빈번하게 난다. 이걸 해결하려면?
# get() 메소드 사용 : key check를 해주는 메소드, 없는 경우 None을 return한다
key_value = input("student 속성 입력(name, age, major) ")
while students[0].get(key_value) == None : # get() 사용 -> key_value 값이 없다면 제대로 입력할 때까지 while문
    print("name, age, major 중에서 입력해주세요 ")
    key_value = input("student 속성 입력(name, age, major) ")
print("{0} key의 value 값 : {1} ".format(key_value, students[0][key_value]))