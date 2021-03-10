import sys
from collections import deque


def bfs(i, s, e):
    if s == e:
        return 0
    board = [[0 for _ in range(i)] for _ in range(i)]
    # board = [[0] * i] * i         -> 이렇게쓰는 것은 좋지 못함. 왜냐하면 모두 메모리 주소가 같기때문에 하나를 바꾸면 전체가 바뀌는 기염을 토함.
    # print(board)
    # print(type(i))
    # print(b)
    board[s[0]][s[1]] = 1
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, 2, 1, -1, -2]
    q = deque()
    q.append(s)
    while q:
        a, b = q.popleft()
        # print(a, b)
        # print(e[0], e[1])
        # print(a, b)
        if a == e[0] and b == e[1]:
            return board[a][b] - 1
        for j in range(8):
            x = a + dx[j]
            y = b + dy[j]
            # print(f"a,b : {a, b} =  x :{x}, y: {y}")
            # print(i, type(i))
            if 0 <= x < i and 0 <= y < i and board[x][y] == 0:
                board[x][y] = board[a][b] + 1
                q.append([x, y])



if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        i = int(sys.stdin.readline().strip())
        s = list(map(int, sys.stdin.readline().strip().split()))
        e = list(map(int, sys.stdin.readline().strip().split()))
        print(bfs(i, s, e))
