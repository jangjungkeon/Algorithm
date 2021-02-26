import sys


def mul_matrx(A, B):
    N = len(A)
    M = len(A[0])
    K = len(B[0])
    result = [[0 for _ in range(K)] for _ in range(N)]
    for i in range(N):
        for j in range(K):
            for m in range(M):
                result[i][j] += A[i][m] * B[m][j]
            result[i][j] %= C
    return result


def spl_conq_fibo(N):
    if N == 2:
        return mul_matrx(A, A)
    if N == 1:
        return A
    if N == 0:
        return [[1, 0], [0, 1]]

    if N % 2 == 0:
        tmp = spl_conq_fibo(N // 2)
        return mul_matrx(tmp, tmp)
    else:
        tmp = spl_conq_fibo(N // 2)
        tmp_1 = mul_matrx(tmp, A)
        return mul_matrx(tmp, tmp_1)


def fibo(N):
    return mul_matrx(spl_conq_fibo(N), B)[0][0]


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    C = 1000000
    A = [[1, 1], [1, 0]]
    B = [[1], [0]]
    print(fibo(N-1))



'''
1000000 으로 나눈 나머지를 출력. 

A = [[1, 1], [1, 0]]

'''