import collections
import sys


def math3(T):
    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        input_list = []
        sum = 1
        for _ in range(N):
            input_String = sys.stdin.readline().split()
            input_list.append(input_String[-1])
        c = collections.Counter(input_list)
        for i in c.values():
            sum *= i+1
        print(sum-1)
    return


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    math3(T)
