import sys
from collections import deque


def bfs():
    q = deque()
    # (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if b[i][j][k] == 1:           # b[z][y][x]
                    q.append([i, j, k])

    while q:
        a = q.popleft()
        for i in range(6):
            x = a[2] + dx[i]
            y = a[1] + dy[i]
            z = a[0] + dz[i]
            if 0 <= z < H and 0 <= y < N and 0 <= x < M and b[z][y][x] == 0:
                b[z][y][x] = b[a[0]][a[1]][a[2]] + 1
                q.append([z, y, x])
    result = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if b[i][j][k] == 0:
                    return print(-1)
                if b[i][j][k] > result:
                    result = b[i][j][k]

    if result == 1:
        return print(0)
    else:
        return print(result - 1)


if __name__ == "__main__":
    M, N, H = map(int, sys.stdin.readline().split())
    b = []
    for _ in range(H):
        tmp = []
        for _ in range(N):
            tmp.append(list(map(int, sys.stdin.readline().split())))
        b.append(tmp)
    bfs()




