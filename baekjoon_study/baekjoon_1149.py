import sys

N = int(sys.stdin.readline())

a = []

# a의 메모리를 미리 확보해 놓기
for i in range(N):
    a.append([0,0,0])

for i in range(N):
    R_cost, G_cost, B_cost = map(int, sys.stdin.readline().split())

    if i == 0:
        a


