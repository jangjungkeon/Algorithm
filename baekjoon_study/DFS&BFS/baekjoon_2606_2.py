import sys
import collections


def bfs():
    q = collections.deque()
    cont = 0
    q.append(1)
    chk = [True for _ in range(cont_pc + 1)]
    chk[1] = False

    while q:
        a = q.popleft()
        if a in grape:
            a_list = grape[a]
            for node in a_list:
                if chk[node]:
                    chk[node] = False
                    q.append(node)
                    cont += 1

    return cont


if __name__ == "__main__":
    cont_pc = int(sys.stdin.readline().strip())
    cont_conn_pc = int(sys.stdin.readline().strip())
    grape = collections.defaultdict(set)
    for _ in range(cont_conn_pc):
        start, end = map(int, sys.stdin.readline().split())
        grape[start].add(end)
        grape[end].add(start)
    # defaultdict(<class 'set'>, {1: {2, 5}, 2: {1, 3, 5}, 3: {2}, 5: {1, 2, 6}, 6: {5}, 4: {7}, 7: {4}})
    # print(grape)
    print(bfs())
