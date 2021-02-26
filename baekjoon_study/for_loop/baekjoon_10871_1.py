# 이게 더 짧고 좋은듯. 간결하고
import sys      # 빠른 입력을 위한 모듈

N, X = map(int, sys.stdin.readline().split())

for i in list(map(int, sys.stdin.readline().split())):
    if i < X:
        # print 의 옵션 중에 end 옵션을 사용해보았다.
        print(i, end=' ')
