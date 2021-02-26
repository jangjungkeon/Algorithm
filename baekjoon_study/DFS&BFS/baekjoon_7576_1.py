import sys, timeit
from collections import deque


def bfs():
    q = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(N):
        for j in range(M):
            if t[i][j] == 1:
                q.append([i, j])

    while q:
        p = q.popleft()
        for j in range(4):
            x = p[0] + dx[j]
            y = p[1] + dy[j]
            if 0 <= x < N and 0 <= y < M and t[x][y] == 0:
                t[x][y] = t[p[0]][p[1]] + 1
                q.append([x, y])
    result = 0
    for a in range(N):
        for b in range(M):
            if t[a][b] == 0:
                return print(-1)
            if t[a][b] > result:
                result = t[a][b]
    print(result - 1)


if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().split())
    t = []
    for _ in range(N):
        t.append(list(map(int, sys.stdin.readline().split())))
    # print(timeit.timeit('bfs()', setup='from __main__ import bfs', number=10000))
    bfs()





'''
백준 7576  시간비교

수정전
0.88384023
0.8968337030000004

수정후 
0.18379522500000078

'''