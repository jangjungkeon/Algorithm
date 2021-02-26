import sys


def func(i, j):
    global M, N, dp, data
    if dp[i][j] > 0:
        return

    dp[i][j] = 0
    # 상
    if i > 0 and data[i][j] < data[i - 1][j]:
        if dp[i - 1][j] < 0:
            func(i-1, j)
        dp[i][j] += dp[i - 1][j]

    # 하
    if i < M - 1 and data[i][j] < data[i + 1][j]:
        if dp[i + 1][j] < 0:
            func(i+1, j)
        dp[i][j] += dp[i + 1][j]

    # 좌
    if j > 0 and data[i][j] < data[i][j - 1]:
        if dp[i][j - 1] < 0:
            func(i, j - 1)
        dp[i][j] += dp[i][j - 1]

    # 우
    if j < N - 1 and data[i][j] < data[i][j + 1]:
        if dp[i][j + 1] < 0:
            func(i, j + 1)
        dp[i][j] += dp[i][j + 1]

    return


if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().split())
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    dp = [[-1 for _ in range(N)] for _ in range(M)]
    dp[0][0] = 1
    for i in range(M):
        for j in range(N):
            func(i, j)

    print(dp[-1][-1])

