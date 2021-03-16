import sys


def mul_matrx(A, B):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for m in range(N):
                result[i][j] += A[i][m] * B[m][j]
            result[i][j] %= C
    return result


def spl_conq(B):
    if B == 2:
        return mul_matrx(A, A)
    if B == 1:
        return A

    if B % 2 == 0:
        tmp = spl_conq(B // 2)
        return mul_matrx(tmp, tmp)
    else:
        tmp = spl_conq(B // 2)
        tmp_1 = mul_matrx(tmp, A)
        return mul_matrx(tmp, tmp_1)


if __name__ == "__main__":
    N, B = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1000:
                A[i][j] = 0
    C = 1000
    sol = spl_conq(B)
    for i in sol:
        print(*i)
