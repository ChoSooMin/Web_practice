values = [100, 200, 300]

# 함수 정의
def print_3_times(*value, data='test') :
    for value in values :
        print("{0} : hello function {1}".format(value, data))

print()

# 함수 호출
print_3_times('test1', 'test2')
print_3_times()
print_3_times('test1', 'test2', 'test3', data = 'test5')

def argument_test(a, b = 20, c = 30) : # b와 c에 기본값을 설정해준다.
    print("{0} : {1} : {2}".format(a, b, c))

argument_test(10) # 10이 a로 넣어지고, b와 c는 기본값이 넣어진다.
argument_test(b = 200, c = 300, a = 100) # 순서 상관없이 변수에 값 매핑 100 : 200 : 300 으로 출력
argument_test(1000, 2000, 3000) # 순서대로 출력 1000 : 2000 : 3000

def return_none_test() : 
    return
    
print(return_none_test()) # None이 출력된다.

def return_test(a, b) :
    sum = a + b
    return sum

print(return_test(10, 20))

# 전달되는 가변 매개변수 곱해서 리턴하기
def mul(*values) :
    result = 1

    for value in values : 
        result *= value
    
    return result

print(mul(5, 7, 9, 10))