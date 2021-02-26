import sys      # 빠른 입력을 위한 모듈

N = int(sys.stdin.readline())

for i in range(1, 10):
    print("{} * {} = {}".format(N, i, N*i))