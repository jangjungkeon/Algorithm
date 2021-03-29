import sys
import collections


def dfs():
    q = collections.deque()
    q.append(V)
    result = []
    chk = [True for _ in range(N+1)]

    while q:
        a = q.pop()
        # 방문하기
        if chk[a]:
            chk[a] = False
            result.append(a)
            if a in grape:
                a_nodes = grape[a]
                for node in reversed(sorted(a_nodes)):
                    q.append(node)

    return print(*result)


def bfs():
    q = collections.deque()
    q.append(V)
    result = []
    chk = [True for _ in range(N + 1)]

    while q:
        a = q.popleft()
        if chk[a]:
            chk[a] = False
            result.append(a)
            if a in grape:
                a_nodes = grape[a]
                for node in sorted(a_nodes):
                    q.append(node)

    return print(*result)



if __name__ == "__main__":
    N, M, V = map(int, sys.stdin.readline().split())
    grape = collections.defaultdict(set)
    for _ in range(M):
        Start, End = map(int, sys.stdin.readline().split())
        grape[Start].add(End)
        grape[End].add(Start)
    dfs()
    bfs()
