# 1932번 정수 삼각형과 비슷 한 문제, 위층 대각선의 합이 아래층이다.
import sys

N = int(sys.stdin.readline().strip())

dp = [[0 for _ in range(10)] for _ in range(101)]
dp[1][0] = 0
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]


print(sum(dp[N]) % 1000000000)



'''
# 1932번 정수 삼각형과 비슷 한 문제, 위층 대각선의 합이 아래층이다.

import sys

N = int(sys.stdin.readline().strip())

dp = [[0 for _ in range(10)] for _ in range(101)]
dp[0][0] = 0
for i in range(1, 10):
    dp[0][i] = 1
for i in range(1, N+1):
    for j in range(N)
        if j == 0:
            dp[i][0] = dp[i-1][1]
        if j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 


print(sum(dp[N]) % 1000000000)

'''