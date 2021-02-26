import sys

N = int(sys.stdin.readline().strip())
input_list = []

for _ in range(N):
    element = sys.stdin.readline().split()
    element[0] = int(element[0])
    input_list.append(element)

for i in sorted(input_list, key=lambda x: x[0]):
    print(i[0], i[1])
