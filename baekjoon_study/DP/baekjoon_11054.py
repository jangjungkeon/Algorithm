import sys

N = int(sys.stdin.readline().strip())
bitonic = list(map(int, sys.stdin.readline().split()))
dpF = [1 for _ in range(N)]
dpR = [1 for _ in range(N)]
sol = [1 for _ in range(N)]


for i in range(N):
    for j in range(N):
        if j > i and bitonic[j] > bitonic[i]:
            if dpF[j] < dpF[i] + 1:
                dpF[j] = dpF[i] + 1


for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if j < i and bitonic[j] > bitonic[i]:
            if dpR[j] < dpR[i] + 1:
                dpR[j] = dpR[i] + 1


for i in range(N):
    sol[i] = dpF[i] + dpR[i]


print(max(sol) - 1)

'''
5
1 4 2 5 3
> 4

7
1 4 5 9 7 1 2
> 6
'''