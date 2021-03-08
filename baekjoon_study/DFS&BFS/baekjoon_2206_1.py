import sys
from collections import deque


def bfs():
    q = deque()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    v = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    v[0][0][1] = 1
    q.append([0, 0, 1])
    while q:
        a, b, w = q.popleft()
        if a == n - 1 and b == m - 1:
            return v[a][b][w]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if s[x][y] == 0 and v[x][y][w] == 0:
                    v[x][y][w] = v[a][b][w] + 1
                    q.append([x, y, w])
                elif s[x][y] == 1 and w == 1:
                    v[x][y][0] = v[a][b][w] + 1
                    q.append([x, y, 0])
    return -1


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    s = []
    for _ in range(n):
        s.append(list(map(int, sys.stdin.readline().split('\n')[0])))
    print(bfs())
