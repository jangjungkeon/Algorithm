import sys
import collections


def B_search(A, B):
    dic_A = collections.Counter(A)
    for i in B:
        print(dic_A[i])
    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().strip())
    B = list(map(int, sys.stdin.readline().split()))
    B_search(A, B)
