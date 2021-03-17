import sys
import collections


def bfs(I, S, E):
    # I 는 체스판의 한변의 길이, S는 시작점, E는 종점
    grape = [[0 for _ in range(I)] for _ in range(I)]       # [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], ...]
    q = collections.deque()
    q.append(S)
    grape[S[0]][S[1]] = 1
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, 2, 1, -1, -2]

    while q:
        a, b = q.popleft()
        if a == E[0] and b == E[1]:
            break

        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < I and 0 <= y < I and grape[x][y] == 0:
                # grape[a][b]는 직전위치.
                grape[x][y] = grape[a][b] + 1
                q.append([x, y])

    return grape[E[0]][E[1]] - 1


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        I = int(sys.stdin.readline().strip())
        S = list(map(int, sys.stdin.readline().split()))        # [0, 0]
        E = list(map(int, sys.stdin.readline().split()))        # [7, 0]
        print(bfs(I, S, E))





