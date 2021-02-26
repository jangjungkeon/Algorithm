import sys


def func():
    dp = [0 for _ in range(k+1)]
    dp[0] = 1
    for i in A:  # A = [1, 2, 5]
        for j in range(1, k+1):
            if j - i >= 0:
                dp[j] += dp[j-i]
    return dp[k]


if __name__ == "__main__":
    N, k = map(int, sys.stdin.readline().split())
    A = [int(sys.stdin.readline().strip()) for _ in range(N)]
    print(func())
