import sys


def math(N):
    for i in range(2, N+1):
        while N % i == 0:
            print(i)
            N /= i
            if N == 1:
                return
    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    math(N)

