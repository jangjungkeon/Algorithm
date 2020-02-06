import sys
import collections


# N x M 의 직사각형 판을 만들기
N, M = map(int, sys.stdin.readline().split())
table = [list(sys.stdin.readline()) for _ in range(N)]
check = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx, dy = (-1,0,1,0), (0,1,0,-1)
q = collections.deque()


# init() 초기 함수 만들기
def init():
    rx, ry, bx, by = [0] * 4
    for i in range(N):
        for j in range(M):
            if table[i][j] == 'R':
                rx, ry = i, j
            if table[i][j] == 'B':
                bx, by = i, j
    check[rx][ry][bx][by] = True
    q.append((rx, ry, bx, by, 0))


# 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기
def move(rx, ry, dx, dy, c):
    while table[rx + dx][ry + dy] != '#' and table[rx][ry] != 'O':
        rx += dx
        ry += dy
        c += 1
    return rx, ry, c


def bfs():
    #  기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d > 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            # 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패
            if table[nbx][nby] == 'O':
                continue
            if table[nrx][nry] == 'O':
                print(d+1)
                return
            # 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx - dx[i], nry - dy[i]
                else:
                    nbx, nby = nbx - dx[i], nby - dy[i]
            if not check[nrx][nry][nbx][nby]:
                check[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d+1))

    print(-1)

init()
bfs()

