import sys


def check_LIS(i):
    s = 0
    e = len(tmp) - 1
    while True:
        mid = (s+e)//2
        if s == mid:
            if tmp[mid] >= i:
                return mid
            else:
                return mid + 1
        if tmp[mid] <= i:
            s = mid
        else:
            e = mid


def B_search():
    global tmp
    tmp = []
    for i in A:
        if not tmp:
            tmp.append(i)
            continue
        if tmp[-1] < i:
            tmp.append(i)
        else:
            tmp[check_LIS(i)] = i

    return len(tmp)


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    print(B_search())
