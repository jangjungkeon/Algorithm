import sys  # 입력을 빠르게 수행하는 모듈 소환

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
