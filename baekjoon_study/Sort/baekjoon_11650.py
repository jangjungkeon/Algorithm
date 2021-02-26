import sys

N = int(sys.stdin.readline().strip())
input_list = []

# 입력을 리스트에 받는데, 튜플로 받을까
for _ in range(N):
    (x, y) = map(int, sys.stdin.readline().split())
    input_list.append((x, y))

# 정렬을 어떻게 하지 먼저 sort 함수 사용?
for i in sorted(input_list):
    print(i[0], i[1])
