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
        val = self.stack_val[-1]
        del self.stack_val[-1]
        return val

    def size(self):
        return len(self.stack_val)


def check_vps2(input_str):
    for i in input_str:
        if i == "(" or i == "[":
            stack_vps2.push(i)
            continue
        if i == ")":
            if stack_vps2.pop() != "(":
                return print("no")
            continue
        if i == "]":
            if stack_vps2.pop() != "[":
                return print("no")
            continue

    print("no") if stack_vps2.size() != 0 else print("yes")
    return


if __name__ == "__main__":
    input_str = ""
    while True:
        stack_vps2 = Stack()
        input_str = sys.stdin.readline().rstrip()
        if input_str == ".":
            break
        check_vps2(input_str)
