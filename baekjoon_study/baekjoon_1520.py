import sys

def dp(i : int, j : int):
    global m, n, table, path
    if path[i][j] > 0:
        return

    path[i][j] = 0

    # up
    if i > 0 and table[i][j] < table[i-1][j]:
        if path[i-1][j] < 0:
            dp(i-1, j)
        path[i][j] += path[i-1][j]

    # down
    if i < m-1 and table[i][j] < table[i+1][j]:
        if path[i+1][j] < 0:
            dp(i+1, j)
        path[i][j] += path[i+1][j]

    # left
    if j > 0 and table[i][j] < table[i][j-1]:
        if path[i][j-1] < 0:
            dp(i, j-1)
        path[i][j] += path[i][j-1]

    # right
    if j < n-1 and table[i][j] < table[i][j+1]:
        if path[i][j+1] < 0:
            dp(i, j+1)
        path[i][j] += path[i][j+1]


m, n = map(int, sys.stdin.readline().split())

path = []
table = []

for i in range(m):
    table.append(list(map(int, sys.stdin.readline().split())))
    path.append([-1] * n)

path[0][0] = 1

for i in range(m):
    for j in range(n):
        dp(i, j)
        print(i, j, path[i][j])

print(path[-1][-1])