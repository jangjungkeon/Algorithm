import sys


# 피보나치 수열
def fibo(n):
    # 탈출문
    if n == 0:
        return 0
    if n == 2 or n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


n = int(sys.stdin.readline().strip())
print(fibo(n))
