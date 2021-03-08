import sys
from collections import deque


class Person:

    def __init__(self, position, cont, skill):
        self.position = position
        self.cont = cont
        self.skill = skill


class Chk:

    def __init__(self, isWall):
        self.isWall = isWall
        self.skill_used = False
        self.skill_unused = False

    def chked(self):
        # 둘다 방문했다면
        if self.skill_unused is True and self.skill_used is True:
            return True
        else:
            return False


def bfs():
    q = deque()
    cont = 1
    # 벽을 뚫었으면 True, 안뚫었으면 False
    skill = False
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q.append(Person((0, 0), cont, skill))

    while q:
        p = q.popleft()
        if p.position == (N-1, M-1):
            return print(p.cont)
        # 벽뚫기를 사용하지 않았으면
        if p.skill is False:
            b[p.position[0]][p.position[1]].skill_unused = True
        else:
            b[p.position[0]][p.position[1]].skill_used = True
        for i in range(4):
            x = p.position[0] + dx[i]
            y = p.position[1] + dy[i]
            if 0 <= x < N and 0 <= y < M and b[x][y].chked() is False:
                # 벽을 안부숴두 됨.
                if b[x][y].isWall == 0:
                    q.append(Person((x, y), p.cont + 1, p.skill))
                # 벽을 부숴야만함.
                if b[x][y].isWall == 1 and p.skill is False:
                    q.append(Person((x, y), p.cont + 1, True))

    return print(-1)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    # b = [[Chk()] * M] * N     # --> Chk가 모두 같은 메모리 주소를 사용한다.
    b = []
    for _ in range(N):
        tmp = []
        for i in list(map(int, sys.stdin.readline().split('\n')[0])):
            tmp.append(Chk(i))
        b.append(tmp)
    bfs()
