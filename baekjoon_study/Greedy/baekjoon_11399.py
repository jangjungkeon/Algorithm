import sys

N = int(sys.stdin.readline().strip())

P = list(map(int, sys.stdin.readline().split()))
P.sort()

sum_p = 0
tmp = 0

for i in P:
    tmp += i
    sum_p += tmp

print(sum_p)
