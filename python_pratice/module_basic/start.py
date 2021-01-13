# import test_module as test # test_module을 test라는 이름으로 사용하겠다 => ModuleNotFoundError 발생
import test_package.test_module as test

radius = test.number_input()
print(test.get_circle_area(radius))
print(test.get_circumference(radius))

print("# 메인의 __name__ 출력 #")
print(__name__)
print()