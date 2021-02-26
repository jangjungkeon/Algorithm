import sys


def B_search(A, B):
    A.sort()
    for i in B:
        start = 0
        end = N - 1
        while True:
            mid = (start + end) // 2
            if i == A[mid]:
                print(1)
                break
            if start == mid:
                print(1) if i == A[end] else print(0)
                break
            if i < A[mid]:
                end = mid
            if i > A[mid]:
                start = mid
    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().strip())
    B = list(map(int, sys.stdin.readline().split()))
    B_search(A, B)

