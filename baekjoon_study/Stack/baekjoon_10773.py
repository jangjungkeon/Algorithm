import sys


class Stack:
    def __init__(self):
        self.stack_val = []

    def push(self, x):
        self.stack_val.append(x)
        return

    def pop(self):
        del self.stack_val[-1]
        return

    def sum_val(self):
        return sum(self.stack_val)


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    Stack = Stack()
    for _ in range(N):
        num = int(sys.stdin.readline().strip())
        Stack.push(num) if num != 0 else Stack.pop()
    print(Stack.sum_val())
