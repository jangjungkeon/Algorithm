# 두번째로 생각한 것으로 40분정도 걸린 듯

import sys


def check(x, y, num):
    # 가로가 괜찮은지 체크
    if num in arr_2D[x]:
        return False

    # 세로 배열
    for row in range(9):
        if num == arr_2D[row][y]:
            return False

    # 3 * 3 배열
    x_3 = x // 3
    y_3 = y // 3
    for row in range(3):
        if num in arr_2D[x_3 * 3 + row][y_3 * 3:y_3 * 3 + 3]:
            return False

    return True


def DFS(depth):
    if depth == blank_len:
        for i in range(9):
            print(*arr_2D[i])
        exit()
    else:
        for num in range(1, 10):
            x = blank[depth][0]
            y = blank[depth][1]
            if check(x, y, num):
                arr_2D[x][y] = num
                DFS(depth + 1)
                arr_2D[x][y] = 0


arr_2D = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if arr_2D[i][j] == 0]
blank_len = len(blank)
DFS(0)
