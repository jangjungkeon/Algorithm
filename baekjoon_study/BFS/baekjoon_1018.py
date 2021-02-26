import sys
import copy


def paint(board):
    # board를 w로 칠할 때 : 두개 더해서 짝수
    cont_w = 0
    cont_b = 0
    board_tmp_ = copy.deepcopy(board)
    # board[0][0] == 'B'로 바꾸고 싶을 때
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0 and board_tmp_[i][j] == 'W':  # 짝수라면
                board_tmp_[i][j] = 'B'
                cont_b += 1
                continue
            if (i + j) % 2 == 1 and board_tmp_[i][j] == 'B':  # 홀수라면
                board_tmp_[i][j] = 'W'
                cont_b += 1
                continue

    # board[0][0] == 'W'로 바꾸고 싶을 때
    board_tmp_ = board
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1 and board_tmp_[i][j] == 'W':  # 홀수라면
                board_tmp_[i][j] = 'B'
                cont_w += 1
                continue
            if (i + j) % 2 == 0 and board_tmp_[i][j] == 'B':  # 짝수라면
                board_tmp_[i][j] = 'W'
                cont_w += 1
                continue

    return min(cont_w, cont_b)

# N(행) x M(열)

N, M = map(int, sys.stdin.readline().split())
sol_list = []

# board 받기
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

# board 자르기
for i in range(N-7):
    for j in range(M-7):
        board_tmp = [board[i:i+8][k][j:j+8] for k in range(8)]
        sol_list.append(paint(board_tmp))


print(min(sol_list))