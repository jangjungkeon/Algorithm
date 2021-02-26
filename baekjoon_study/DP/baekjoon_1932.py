import sys


N = int(sys.stdin.readline().strip())

triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * (i+1) for i in range(N)]
dp[0][0] = triangle[0][0]
dp[1][0] = triangle[1][0] + triangle[0][0]
dp[1][1] = triangle[1][1] + triangle[0][0]

for i in range(2, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = triangle[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = triangle[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[N-1]))
