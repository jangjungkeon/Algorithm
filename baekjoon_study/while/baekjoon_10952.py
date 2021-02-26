import sys    # 빠른 입력을 위한 모듈

while 1:
    A, B = map(int, sys.stdin.readline().split())
    if A+B == 0:
        break
    print(A+B)