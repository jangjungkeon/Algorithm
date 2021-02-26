import sys      # 빠른 입력을 위한 모듈

# 인자 받기
N = int(sys.stdin.readline())
result = []
for i in range(1, N+1):
    result.append(i)

for j in result[::-1]:
    print(j)