import sys


class Stack:
    def __init__(self):
        self.stack_val = []

    def push(self, x):
        self.stack_val.append(x)
        return

    def pop(self):
        if self.size() == 0:
            return False
        del self.stack_val[-1]

    def size(self):
        return len(self.stack_val)

    def top(self):
        return self.stack_val[-1] if self.size() != 0 else -1


def make_seq(a):
    i = 0
    result = []
    for j in range(1, n + 1):
        stack_seq.push(j)
        result.append("+")
        while i != len(a) and stack_seq.top() == a[i]:
            stack_seq.pop()
            i += 1
            result.append("-")

    if stack_seq.size() != 0:
        print("NO")
    else:
        for i in result:
            print(i)
    return


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    a = [int(sys.stdin.readline().strip()) for _ in range(n)]
    stack_seq = Stack()
    make_seq(a)
