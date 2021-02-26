# 재귀 버전. 그러나 시간초과

import sys

N = int(sys.stdin.readline().strip())


N_cont = 0
N_val = ''


def dfs(depth):
    global N_val, N_cont
    if depth == N:
        N_cont += 1
        return

    for i in range(10):  # 1 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        if N_val == '':
            if i == 0:
                continue
            else:
                N_val += str(i)
                dfs(depth + 1)
                N_val = N_val[:-1]
        else:
            if N_val[-1] == 0 and i == 1:
                N_val += str(i)
                dfs(depth + 1)
                N_val = N_val[:-1]
            if N_val[-1] != 0 and (i == int(N_val[-1]) - 1 or i == int(N_val[-1]) + 1):
                N_val += str(i)
                dfs(depth + 1)
                N_val = N_val[:-1]


dfs(0)
print(N_cont % 1000000000)