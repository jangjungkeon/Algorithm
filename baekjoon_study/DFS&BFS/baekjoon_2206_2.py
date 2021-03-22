import sys
import collections


def bfs():
    q = collections.deque()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    B[0][0][1] = 1
    q.append([0, 0, 1])

    while q:
        a, b, c = q.popleft()
        if a == N - 1 and b == M - 1:
            return B[a][b][c]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M:
                if B[x][y][2] == 0 and B[x][y][c] == 0:
                    B[x][y][c] = B[a][b][c] + 1
                    q.append([x, y, c])
                elif B[x][y][2] == 1 and c == 1:
                    B[x][y][0] = B[a][b][c] + 1
                    q.append([x, y, 0])
    return -1


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    B = []
    for _ in range(N):
        tmp = []
        for i in list(sys.stdin.readline().split('\n')[0]):
            tmp.append([0, 0, i])
        B.append(tmp)
    print(bfs())
