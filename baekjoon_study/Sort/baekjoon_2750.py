import sys

N = int(sys.stdin.readline().strip())

input_list = [int(sys.stdin.readline().strip()) for _ in range(N)]

input_list.sort()

for i in input_list:
    print(i)
