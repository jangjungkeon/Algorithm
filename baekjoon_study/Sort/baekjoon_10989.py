import sys

N = int(sys.stdin.readline().strip())

cont_list = [0] * 10001

# 입력과 동시에 갯수 세기 - 메모리 아끼기
for _ in range(N):
    val = int(sys.stdin.readline().strip())
    cont_list[val] += 1

# cont_list의 값 출력하기 - 메모리 아끼기
for i in range(len(cont_list)):
    for _ in range(cont_list[i]):
        print(i)
