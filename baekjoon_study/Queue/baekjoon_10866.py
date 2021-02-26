import sys
from collections import deque


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    queue = deque()
    for _ in range(T):
        order = sys.stdin.readline().split()
        if order[0] == "push_front":
            queue.appendleft(int(order[1]))
        if order[0] == "push_back":
            queue.append(int(order[1]))
        if order[0] == "pop_front":
            print(queue.popleft() if len(queue) != 0 else -1)
        if order[0] == "pop_back":
            print(queue.pop() if len(queue) != 0 else -1)
        if order[0] == "size":
            print(len(queue))
        if order[0] == "empty":
            print(1 if len(queue) == 0 else 0)
        if order[0] == "front":
            print(queue[0] if len(queue) != 0 else -1)
        if order[0] == "back":
            print(queue[-1] if len(queue) != 0 else -1)
