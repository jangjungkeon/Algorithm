import sys      # 빠른 입력을 위한 모듈

T = int(sys.stdin.readline())

for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(i, A+B))