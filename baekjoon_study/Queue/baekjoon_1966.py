import sys
from collections import deque


class Node(object):
    def __init__(self, doc, pri):
        self.doc = doc
        self.pri = pri


def print_Q(m, n, a):
    q = deque()
    for i in range(m):
        q.append(Node(i, a[i]))     # q = [Node(순서, 중요도), Node(순서, 중요도), Node(순서, 중요도)]
    while True:
        if q[0].pri >= max(a):
            k = q[0].doc
            a.remove(q.popleft().pri)
            if k == n:
                print(m - len(q))
                return
        else:
            q.append(q.popleft())


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        m, n = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        print_Q(m, n, a)

'''
4 2
A B C D
1 2 3 4

CDAB +2

ABCDEF
DEFAB + 1, 5

큐에 먼저 넣기. 

1,1,9,1,1,1 

'''