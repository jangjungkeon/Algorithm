import sys

N = int(sys.stdin.readline().strip())
dp = [[0 for _ in range(3)] for _ in range(N)]

for i in range(N):
    input_list = list(map(int, sys.stdin.readline().split()))
    if i == 0:
        dp[i][0] = input_list[0]
        dp[i][1] = input_list[1]
        dp[i][2] = input_list[2]
    else:
        # RGB 색깔을 하나씩 선택해서 모든 값을 보유한 상태에서 최솟값을 찾기.
        # >>> 다 구하고 고르기.
        dp[i][0] = input_list[0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = input_list[1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = input_list[2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[N - 1]))
