import sys      # 빠른 입력을 위한 모듈

T = int(sys.stdin.readline())
result = 0
for i in range(1, T+1):
    result += i

print(result)
