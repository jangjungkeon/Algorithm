import sys
from collections import deque


def rotate(M, N, a):
    dq = deque()
    cont = 0
    for i in range(1, M+1):
        dq.append(i)
    for i in range(N):
        b = dq.index(a[i])
        c = len(dq) - b
        if b > c:      # 인덱스 나옴.
            dq.rotate(c)
            cont += c
        else:
            dq.rotate(-b)
            cont += b
        dq.popleft()
    return print(cont)


if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    rotate(M, N, a)
