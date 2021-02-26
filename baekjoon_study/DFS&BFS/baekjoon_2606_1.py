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


def dfs(start):
    check_visit = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in check_visit:
            check_visit.append(n)
            if n in grape_dic:
                for i in reversed(grape_dic[n]):
                    if i not in check_visit:
                        stack.append(i)

    return print(len(check_visit)-1)


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    edge_num = int(sys.stdin.readline().strip())
    grape = [list(map(int, sys.stdin.readline().split())) for _ in range(edge_num)]
    grape_dic = make_grape(grape)
    dfs(1)
