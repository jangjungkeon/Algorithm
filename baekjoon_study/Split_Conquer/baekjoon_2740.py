import sys


def mul_matrx(A, B, M, N, K):
    result = [[0 for _ in range(K)] for _ in range(N)]
    for i in range(N):
        for j in range(K):
            for m in range(M):
                result[i][j] += A[i][m] * B[m][j]
    for i in result:
        print(*i)
    return


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    M, K = map(int, sys.stdin.readline().split())
    B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    mul_matrx(A, B, M, N, K)
