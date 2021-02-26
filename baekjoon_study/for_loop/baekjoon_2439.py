import sys      # 빠른 입력을 위한 모듈

N = int(sys.stdin.readline())

# rjust 함수를 활용하여 오른쪽, 왼쪽 정렬을 한다.
for i in range(1, N+1):
    print(('*' * i).rjust(N))