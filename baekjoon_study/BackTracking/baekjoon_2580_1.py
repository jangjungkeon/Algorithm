# 맨 처음 생각한 것으로 매우 오래걸림 4시간 넘게

import collections
import sys

# 2차원 배열 arr_2D = [[0,3,5,4,6...], [7,8,2] ..]
arr_2D = []
cont = 0
tmp = []
for _ in range(9):
    arr_2D.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if arr_2D[i][j] == 0:
            cont += 1


def check():
    # 가로 배열
    for row in range(9):
        test_list = []
        for j in arr_2D[row]:
            if j > 0:
                test_list.append(j)
        if len(test_list) != len(set(test_list)):
            return False

    # 세로 배열
    for col in range(9):
        colum_list = []
        for row in range(9):
            if arr_2D[row][col] > 0:
                colum_list.append(arr_2D[row][col])
        if len(colum_list) != len(set(colum_list)):
            return False

    # 3 * 3 배열
    for i, j in [(0, 0), (3, 0), (6, 0), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]:
        i_3 = i // 3
        j_3 = j // 3
        square_list = []
        for row in range(3):
            square_list.extend(arr_2D[i_3 * 3 + row][j_3 * 3:j_3 * 3 + 3])
        while 0 in square_list:
            square_list.remove(0)
        if len(square_list) != len(set(square_list)):
            return False

    return True


def candidate_list(i, j):
    candi_list = []
    # 가로 줄에 비어있는 숫자 리스트 .
    row_list = []
    for num in range(1, 10):
        if not (num in arr_2D[i]):
            row_list.append(num)
    if len(row_list) == 1:
        return row_list
    candi_list.extend(row_list)

    # 세로 줄에 비어있는 숫자 리스트.
    colum_list = []
    colum_list_2 = []
    for row in range(9):
        colum_list.append(arr_2D[row][j])
    for num in range(1, 10):
        if not (num in colum_list):
            colum_list_2.append(num)
    if len(colum_list_2) == 1:
        return colum_list_2
    candi_list.extend(colum_list_2)

    # 3*3 체크
    square_list = []
    square_list_2 = []
    i_3 = i // 3
    j_3 = j // 3
    for row in range(3):
        square_list.extend(arr_2D[i_3 * 3 + row][j_3 * 3:j_3 * 3 + 3])
    for num in range(1, 10):
        if not (num in square_list_2):
            square_list_2.append(num)
    if len(square_list_2) == 1:
        return square_list_2
    candi_list.extend(square_list_2)

    candi_list = collections.Counter(candi_list)
    candi_list = candi_list.most_common()
    return candi_list


def DFS(n):
    if n == cont:
        for i in range(9):
            print(*arr_2D[i])
        exit()
    else:
        for i in range(9):
            for j in range(9):
                if check() and arr_2D[i][j] == 0:
                    for candi in candidate_list(i, j):
                        if type(candi) == int:
                            arr_2D[i][j] = candi
                        else:
                            arr_2D[i][j] = candi[0]
                        DFS(n + 1)
                        arr_2D[i][j] = 0

DFS(0)
