# 시간 초과 작품
import sys, timeit


def bfs():
    q = []
    c = []      # 순회한 곳 체크 및 토마토가 없는 곳함 포
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cont = 0

    for i in range(N):
        for j in range(M):
            if t[i][j] == 1:
                q.append([i, j])
            elif t[i][j] == -1:
                c.append([i, j])

    while q:
        # 종료 조건
        length = len(q)
        for d in range(length):     # 이것만 수정해보자.
            # print(f"횟수 : {d} length : {length}")
            p = q.pop(0)
            if p not in c:
                c.append(p)
                for j in range(4):
                    x = p[0] + dx[j]
                    y = p[1] + dy[j]
                    if 0 <= x < N and 0 <= y < M and t[x][y] == 0 and [x, y] not in c:
                        q.append([x, y])
        cont += 1
    # 토마토가 모두 익지 않으면
    # if len(c) < N*M:
    #     return print(-1)
    # # 토마토가 모두 익으면
    # else:
    #     return print(cont - 1)


if __name__ == "__main__":

    M, N = map(int, sys.stdin.readline().split())
    t = []
    for _ in range(N):
        t.append(list(map(int, sys.stdin.readline().split())))
    print(timeit.timeit('bfs()', setup='from __main__ import bfs', number=10000))

