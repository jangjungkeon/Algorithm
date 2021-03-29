import sys


def bfs():
    board[0][0] = 1
    q = [[0, 0]]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        a, b = q[0][0], q[0][1]
        del q[0]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and board[x][y] == "1":
                q.append([x, y])
                board[x][y] = board[a][b] + 1
    print(board[N-1][M-1])


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(sys.stdin.readline().split('\n')[0]))
    bfs()


