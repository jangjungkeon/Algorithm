import sys


T = int(sys.stdin.readline().strip())
dp = [0 for i in range(100)]
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    if N < 5:
        print(dp[N-1])
    else:
        for i in range(5, N):
            dp[i] = dp[i - 1] + dp[i - 5]
        print(dp[N - 1])
