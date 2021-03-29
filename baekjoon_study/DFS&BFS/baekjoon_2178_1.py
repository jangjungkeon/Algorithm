import sys
import collections


def bfs():
    q = collections.deque()
    q.append([0, 0])
    chk = [[0 for _ in range(M)] for _ in range(N)]
    chk[0][0] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        a, b = q.popleft()
        if a == N-1 and b == M-1:
            return chk[a][b]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and chk[x][y] == 0 and B[x][y] == 1:
                chk[x][y] = chk[a][b] + 1
                q.append([x, y])

    return chk[N-1][M-1]


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    B = []
    for _ in range(N):
        B.append(list(map(int, sys.stdin.readline().split('\n')[0])))
    # print(B)        # [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
    print(bfs())
