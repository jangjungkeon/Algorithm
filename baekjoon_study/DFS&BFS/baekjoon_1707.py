import sys
from collections import deque


def bfs(V, E, t_grape, s):
    if V == 1 and E == 1:
        return True
    q = deque()
    q.append(s)
    chk[s] = 1

    # print(t_grape)
    while q:
        a = q.popleft()
        if a in t_grape:
            b = t_grape[a]
            for i in b:
                # print(chk)
                if chk[i] == 0:
                    chk[i] = -chk[a]
                    q.append(i)
                    continue
                if chk[i] == chk[a]:
                    return False
    return True


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        V, E = map(int, sys.stdin.readline().split())
        grape = {}
        # grape1 = [[] for _ in range(V+1)]
        chk = [0 for _ in range(V + 1)]
        isTrue = True
        for _ in range(E):
            m, n = map(int, sys.stdin.readline().split())
            if m not in grape:
                grape[m] = {n}
            else:
                grape[m].add(n)
            if n not in grape:
                grape[n] = {m}
            else:
                grape[n].add(m)
            # grape1[m].append(n)
            # grape1[n].append(m)
        for s in range(1, V+1):
            if chk[s] == 0:
                if not bfs(V, E, grape, s):
                    isTrue = False
                    break
        print("YES" if isTrue else "NO")















