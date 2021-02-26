import sys


class Stack:
    def __init__(self):
        self.stack_val = []

    def order(self, order):
        if len(order) == 2:
            return self.push(int(order[1]))
        if order[0] == "pop":
            return self.pop()
        if order[0] == "size":
            return self.size()
        if order[0] == "empty":
            return self.empty()
        if order[0] == "top":
            return self.top()
        return

    def push(self, x):
        if type(x) == int:
            self.stack_val.append(x)

    def pop(self):
        if self.size() == 0:
            return -1
        del_val = self.stack_val[-1]
        del self.stack_val[-1]
        return del_val

    def size(self):
        return len(self.stack_val)

    def empty(self):
        return 1 if self.size() == 0 else 0

    def top(self):
        return self.stack_val[-1] if self.size() != 0 else -1


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    Stack = Stack()
    for _ in range(N):
        order = sys.stdin.readline().split()
        k = Stack.order(order)
        if k is not None:
            print(k)
