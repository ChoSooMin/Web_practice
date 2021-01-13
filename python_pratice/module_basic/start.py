# import test_module as test # test_module을 test라는 이름으로 사용하겠다 => ModuleNotFoundError 발생
# import test_package.test_module as test
# import test_package.test_module2 as test2
from test_package import *

radius = test_module.number_input()
print(test_module.get_circle_area(radius))
print(test_module.get_circumference(radius))

x, y = test_module2.number_input()
print(test_module2.get_circumference(x, y))
print(test_module2.get_rectangle_area(x, y))

print("# 메인의 __name__ 출력 #")
print(__name__) # 출력하면 __main__이라고 뜬다. -> 파이썬은 시작하는 파일을 entry point인 main으로 인식한다.
print()