# 시간 초과지만 나만의 코드임.

import sys

N = int(sys.stdin.readline().strip())
cont = 0
queen_pos = []


def check(depth, i, queen_pos):  # queen_pos = [[depth, i], [depth, i]...]

    # 퀸의 위치 체크하기
    # 세로 : i == pos[1]
    # 우하 대각선 : depth - i == pos[0] - pos[1]
    # 좌하 대각선 : depth + i == pos[0] + pos[1]
    for pos in queen_pos:
        if i == pos[1] or depth - i == pos[0] - pos[1] or depth + i == pos[0] + pos[1]:
            return False
    return True


def DFS(depth):
    global cont
    if depth == N:
        cont += 1
        return

    for i in range(N):
        # 퀸의 위치에 맞는지 체크하기
        if check(depth, i, queen_pos):
            queen_pos.append([depth, i])
            DFS(depth + 1)
            queen_pos.pop()


DFS(0)
print(cont)
