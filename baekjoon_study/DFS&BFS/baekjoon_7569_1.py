import sys
import collections


def bfs():
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    if cont + contm == H*N*M:
        return 0

    while q:
        # z, x, y
        a, b, c = q.popleft()
        for i in range(6):
            z = a + dx[i]
            x = b + dy[i]
            y = c + dz[i]
            if 0 <= x < N and 0 <= y < M and 0 <= z < H and B[z][x][y] == 0:
                # H, N, M
                B[z][x][y] = B[a][b][c] + 1
                q.append([z, x, y])

    result = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if B[i][j][k] > result:
                    result = B[i][j][k]
                elif B[i][j][k] == 0:
                    return -1
    return result - 1


if __name__ == "__main__":
    M, N, H = map(int, sys.stdin.readline().split())
    q = collections.deque()
    B = []
    cont = 0
    contm = 0
    for i in range(H):
        tmp1 = []
        for j in range(N):
            tmp2 = []
            for idx, k in enumerate(list(map(int, sys.stdin.readline().split()))):
                tmp2.append(k)
                if k == 1:
                    cont += 1
                    q.append([i, j, idx])
                elif k == -1:
                    contm += 1
            tmp1.append(tmp2)
        B.append(tmp1)
    print(bfs())
