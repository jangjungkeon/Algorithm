import sys
import collections


def bfs():
    q = collections.deque()
    q.append(N)
    chk = [0 for _ in range(100001)]

    while q:
        a = q.popleft()
        dx = [-1, 1, a]
        if a == K:
            return chk[a]
        for i in range(3):
            b = a + dx[i]
            if 0 <= b <= 100000 and chk[b] == 0:
                chk[b] = chk[a] + 1
                q.append(b)
    return chk[K]


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    print(bfs())
