import sys
from collections import deque


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    queue = deque()
    for _ in range(T):
        order = sys.stdin.readline().split()
        if len(order) == 2:
            queue.append(int(order[1]))
        if order[0] == "pop":
            print(queue.popleft() if len(queue) != 0 else -1)
        if order[0] == "size":
            print(len(queue))
        if order[0] == "empty":
            print(1 if len(queue) == 0 else 0)
        if order[0] == "front":
            print(queue[0] if len(queue) != 0 else -1)
        if order[0] == "back":
            print(queue[-1] if len(queue) != 0 else -1)


'''
class Queue:
    def __init__(self):
        self.data = []
        self.number = 0

    def order(self, order):
        if len(order) == 2:
            return self.push(int(order[1]))
        if order[0] == "pop":
            return self.pop()
        if order[0] == "size":
            return self.size()
        if order[0] == "empty":
            return self.empty()
        if order[0] == "front":
            return self.front()
        if order[0] == "back":
            return self.back()
        return

    def push(self, x):
        self.data.append(x)
        self.number += 1

    def pop(self):
        if not self.data:
            return -1
        self.data.reverse()
        val = self.data[-1]
        del self.data[-1]
        self.data.reverse()
        self.number -= 1
        return val

    def size(self):
        return self.number

    def empty(self):
        return 1 if not self.data else 0

    def front(self):
        return -1 if not self.data else self.data[0]

    def back(self):
        return -1 if not self.data else self.data[-1]
        
                if order == ""
        if k is not None:
            print(k)

'''
