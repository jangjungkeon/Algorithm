import sys
import collections


def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    result = []
    cont = 1
    for i in range(N):
        for j in range(N):
            if B[i][j] == 1:
                cont1 = 1
                cont += 1
                B[i][j] = cont
                q = collections.deque()
                q.append([i, j, cont])
                while q:
                    a, b, c = q.popleft()
                    for k in range(4):
                        x = a + dx[k]
                        y = b + dy[k]
                        if 0 <= x < N and 0 <= y < N and B[x][y] == 1:
                            B[x][y] = c
                            cont1 += 1
                            q.append([x, y, c])
                result.append(cont1)
    print(len(result))
    for m in sorted(result):
        print(m)
    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    B = []
    for _ in range(N):
        B.append(list(map(int, sys.stdin.readline().split('\n')[0])))
    # print(B)
    bfs()

