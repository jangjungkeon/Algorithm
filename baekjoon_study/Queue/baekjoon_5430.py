import sys
from collections import deque


def fun(func_list, arr):
    rev_val = 0
    if arr[0] != "":
        dq = deque(arr)
    else:
        dq = deque()
    for i in func_list:
        if i == "R":
            rev_val += 1        # 홀수가 리버스
        else:
            if len(dq) != 0:
                if rev_val % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
            else:
                print("error")
                return

    if rev_val % 2 != 0:
        dq.reverse()
    return print("[" + ",".join(dq) + "]")


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        func_list = sys.stdin.readline().strip()
        n = int(sys.stdin.readline().strip())
        arr = sys.stdin.readline().strip()
        arr = arr[1:-1].split(",")
        fun(func_list, arr)
