import sys
table = []
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
N = M = 0
N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# Clean한 카운트 세우기

def countClean():
    count = 0
    for i in range(N):
        for j in range(M):
            if table[i][j] > 1:
                count += 1
    return count

# 왼쪽방향으로 돌기
def leftturn(d):
    if d == 0:
        return 3
    else:
        return d -1


def clean(x, y, d, turncount):
    while True:
    # 퇴장하는 경로 먼저 세우기
        if turncount == 4:
            backX = x - dx[d]
            backY = y - dy[d]

            # 모두 청소가 되어 있는 경우, 뒤에 벽이 있는 경우
            if table[backX][backY] == 1:
                print(countClean())
                return

            # 뒤에 벽이 없는 경우
            else:
                x, y, d, turncount = backX, backY, d, 0

        # 현재 장소 청소하기
        if table[x][y] == 0:
            table[x][y] = 2

        # 왼쪽 방향에서 청소하기
        ld = leftturn(d)
        nx = x + dx[ld]
        ny = y + dy[ld]

        # 왼쪽 방향에 청소할 공간이 존재
        if table[nx][ny] == 0:
            x, y, d, turncount = nx, ny, ld, 0
        else:
            x, y, d, turncount  = x, y, ld, turncount+1

clean(r, c, d, 0)