import sys


def func():
    c_sum = sum(c)
    dp = [[0 for _ in range(c_sum + 1)] for _ in range(N + 1)]
    result = c_sum

    for i in range(1, N+1):
        for j in range(1, c_sum+1):
            dp[i][j] = dp[i-1][j] if c[i-1] > j else max(dp[i-1][j], m[i-1] + dp[i-1][j-c[i-1]])

            if dp[i][j] >= M and j < result:
                result = j

    return print(result)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    m = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))
    func()

