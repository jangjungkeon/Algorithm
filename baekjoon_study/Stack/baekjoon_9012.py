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
        del_val = self.stack_val[-1]
        del self.stack_val[-1]
        return True

    def size(self):
        return len(self.stack_val)

    def sum_val(self):
        return sum(self.stack_val)


def check_VPS(input_par):
    for i in input_par:
        if i == "(":
            stck_vps.push(i)
            continue
        if i == ")":
            if not stck_vps.pop():
                return print("NO")
            continue

    print("NO") if stck_vps.size() != 0 else print("YES")
    return


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        stck_vps = Stack()
        input_par = sys.stdin.readline().strip()
        check_VPS(input_par)
'''
stack으로 구현 
'''