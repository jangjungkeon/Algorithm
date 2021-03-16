import sys
from collections import deque


# 그래프 만들기
def makeGrape(grape):
    t_grape = {}
    for i in grape:
        if i[0] not in t_grape:
            t_grape[i[0]] = {i[1]}
        else:
            t_grape[i[0]].add(i[1])
        if i[1] not in t_grape:
            t_grape[i[1]] = {i[0]}
        else:
            t_grape[i[1]].add(i[0])
    return t_grape


def bfs(V, E, grape):
    if V == 1 and E == 1:
        return print('YES')
    q = deque()
    t_grape = makeGrape(grape)
    q.append(grape[0][0])
    chk = [0 for _ in range(V+1)]
    chk[grape[0][0]] = 1

    # print(t_grape)
    while q:
        a = q.popleft()
        b = t_grape[a]
        for i in b:
            # print(chk)
            if chk[i] == 0:
                chk[i] = chk[a] + 1
                q.append(i)
                continue
            if (chk[i] % 2) == (chk[a] % 2):
                return print("NO")
    return print("YES")


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        V, E = map(int, sys.stdin.readline().split())
        grape = []
        for _ in range(E):
            grape.append(list(map(int, sys.stdin.readline().split())))
        bfs(V, E, grape)
