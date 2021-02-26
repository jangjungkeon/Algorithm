import sys

N = int(sys.stdin.readline().strip())
input_list = []
# 입력을 받고 위치를 변경하자.
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    # x, y 의 위치를 변경
    input_list.append([y, x])

for i in sorted(input_list):
    print(i[1], i[0])