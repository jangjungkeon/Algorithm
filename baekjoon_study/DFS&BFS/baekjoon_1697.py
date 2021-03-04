import sys
from collections import deque


def bfs():
    # 1초에 N+1, N-1, 2N 이렇게 이동 가능.
    cont = 0
    q = deque()
    q.append([n, cont])
    # print(q)
    while q:
        a = q.popleft()
        # print(a)
        p = a[0]
        d = a[1]
        if p == k:
            return print(d)
        c[p] = True
        if p + 1 <= 100000 and c[p+1] is False:
            q.append([p+1, d+1])
        if p - 1 >= 0 and c[p-1] is False:
            q.append([p-1, d+1])
        if p * 2 <= 100000 and c[p*2] is False:
            q.append([p*2, d+1])


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    c = [False] * 100001
    bfs()
