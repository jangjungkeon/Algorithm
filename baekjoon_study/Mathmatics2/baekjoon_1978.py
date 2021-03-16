import sys

N = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))
not_prim_cont = 0

for num in num_list:            # 주어진 숫자를 하나씩 꺼내서 검사
    breaker = False
    if num == 1:
        not_prim_cont += 1
        continue
    for i in range(2, num):     # 주어진 수보다 작은 수 2개의 곱의 모든 경우의 수 구하기
        if breaker:
            break
        for j in range(i, num):
            if i*j == num:
                not_prim_cont += 1
                breaker = True
                break

print(len(num_list) - not_prim_cont)

'''
소수의 정의 : 자신보다 작은 두개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수
정의대로 다 해봐야하나? 노가다로 구해볼까? 
'''