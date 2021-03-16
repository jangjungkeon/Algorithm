import sys


def math(N, K):
    sum = 1
    for i in range(N, N-K, -1):
        sum *= i
    for j in range(K, 0, -1):
        sum /= j
    return print(int(sum))


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    math(N, K)


'''
N C K 값 구하기


'''
