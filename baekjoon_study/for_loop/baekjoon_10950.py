import sys      # 빠른 입력을 위한 모듈

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)