import sys

T = int(sys.stdin.readline())


for i in range(T):
    a, b = map(int, sys.stdin.readline().split())

    # 참된 리스트 만들기
    number_list = []
    temp = 1
    for _ in range(b):
        temp *= a
        temp %= 10
        if temp in number_list:
            break
        number_list.append(temp)


    # 결과 가져오기
    result = number_list[b % len(number_list)-1]
    if result == 0:
        print(10)
    else:
        print(result)