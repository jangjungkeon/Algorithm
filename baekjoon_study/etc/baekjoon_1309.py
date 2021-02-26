import sys


# 인수 값 인트로 받기
N = int(sys.stdin.readline())

# 초기 셋팅해 놓기, 끝 값은 넉넉하게 100010으로 여유있게 둔다.
dp = [[0, 0, 0] for i in range(100010)]

# 기본값 만들어 놓기

dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1


# 주 dp 코드
for i in range(2, N + 2):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    if not i == N + 1:
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901



print(dp[N+1][0])