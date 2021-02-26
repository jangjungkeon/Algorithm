import sys


def func(N, A):
    dp = [[0 for _ in range(N)] for _ in range(N)]

    for d in range(1, N):
        for i in range(N-d):
            j = i + d
            if d == 1:
                dp[i][j] = A[i][0]*A[i][1]*A[j][1]
                continue
            dp[i][j] = min([dp[i][m] + dp[m+1][j] + A[i][0]*A[m][1]*A[j][1] for m in range(i, j)])

    return print(dp[0][N-1])


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    A = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    func(N, A)
