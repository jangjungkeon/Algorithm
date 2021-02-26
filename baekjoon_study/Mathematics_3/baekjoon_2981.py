# 시간초과 작품
import sys


def math(input_list):
    K = max(input_list)
    sol = []

    for i in range(2, K + 1):
        tmp = K % i
        check = True
        for j in range(N):
            if input_list[j] % i != tmp:
                check = False
                break
        if check:
            sol.append(i)
    print(*sol)
    return

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    input_list = [int(sys.stdin.readline().strip()) for _ in range(N)]
    math(input_list)

'''
일단 나머지가 0인 것도 있을 수도 잇음. 가장 작은 값을 기준으로 해야하나? 
L = 6, 999,999,999, 1,000,000,000
500,000,001
L = 2, 5, 7
min(L) = K
sol = []
tmp = 0



for i in range(2, K+1)
    tmp = K % i
    check = True
    for j in range(N):
        if L[j] % i != tmp:
            check = False
            break
    if check:
        sol.append(i)
    

'''


'''
그냥 수학 문제였다. 

각수의 차이에서 공통 약수를 찾는다. 

1. 2개씩 묶기.
2. 2개씩  

'''