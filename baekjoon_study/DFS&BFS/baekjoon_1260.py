import sys


def make_grape(grape):
    grape_dic = {}
    for i in grape:
        key = i[0]
        val = i[1]
        if key not in grape_dic:
            grape_dic[key] = []
        if val not in grape_dic:
            grape_dic[val] = []
        grape_dic[key].append(val)
        grape_dic[val].append(key)
    for i in grape_dic:
        grape_dic[i].sort()
    return grape_dic


def dfs(V):
    check_visit = []
    stack = [V]

    while stack:
        n = stack.pop()
        if n not in check_visit:
            check_visit.append(n)
            if n in grape_dic:
                for i in reversed(grape_dic[n]):
                    if i not in check_visit:
                        stack.append(i)

    return print(*check_visit)


def bfs(V):
    check_visit = []
    q = [V]

    while q:
        n = q.pop(0)
        if n not in check_visit:
            check_visit.append(n)
            if n in grape_dic:
                for i in grape_dic[n]:
                    if i not in check_visit:
                        q.append(i)
    return print(*check_visit)


if __name__ == "__main__":
    N, M, V = map(int, sys.stdin.readline().split())
    grape = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    grape_dic = make_grape(grape)
    dfs(V)
    bfs(V)
