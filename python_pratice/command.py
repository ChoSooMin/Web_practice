# list type : [str, int, float, boolean, list] [[1, 2, 3], [1, 2]] list 안의 list가 들어갈 경우, 안에 있는 list의 각 길이가 꼭 같을 필요는 없다.
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print(list_a + list_b, " + 연산 후 list_a : ", list_a) # list_a 값을 변하게 하려면 list_a에 할당을 다시 해줘야 한다.

# 할당했을 경우
# list_a = list_a + list_b
# print("list_a 할당", list_a)

# 함수
# append(), insert(), del, pop()
print(list_a.append(4), "append 후 list_a", list_a) # list_a의 마지막 index+1에 4라는 원소를 넣어라
print(list_a.insert(1, 5), "insert 후 list_a", list_a) # list_a의 1번 인덱스에 5라는 값을 넣어라
print(list_a.pop(1), "pop(1) 삭제 후 list_a", list_a) # list_a의 1번 인덱스 원소 삭제
print(list_a.remove(1), "remove(1) 삭제 후 list_a", list_a) # 첫번째 만나는 값 1을 삭제해라

# for 반복자 in 반복할 수 있는 데이터(list, dictionary, string) : 
#   실행문
index = 0 # index 같이 출력하기 위해
for data in list_a :
    # print(index, data)
    print("list_a[{0}] : {1}".format(index, data)) # list_a[0] : 2, list_a[1] : 3, list_a[2] : 4의 형식으로 출력된다.
    index += 1