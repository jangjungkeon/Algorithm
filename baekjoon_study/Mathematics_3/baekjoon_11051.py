import sys


def dp(N, K):
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N+1):
        for j in range(i+1):
            if j == 0 or i == j:
                dp[i][j] = 1
                continue
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

    return print(dp[N][K] % 10007)


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    dp(N, K)


'''
이 문제는 점화식의 규칙을 미리 알았는데도 오래걸리네...

미리 알았는데도 오래걸림. 

dp는 점화식 규칙 + 초기값 요 두개를 알면 될듯? 
'''