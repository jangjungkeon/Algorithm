import sys

N = int(sys.stdin.readline())
t = []
p = []
d = [0] * (N+1)
result = 0

for i in range(N):
    t1, p1 = map(int, sys.stdin.readline().split())
    t.append(t1)
    p.append(p1)

for i in range(N+1):
    for j in range(i):
        d[i] = max(d[i], d[j])
        if j + t[j] <= i:
            d[i] = max(d[i], d[j] + p[j])

    result = max(result, d[i])

print(result)