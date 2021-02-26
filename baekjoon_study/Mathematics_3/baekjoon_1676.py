import collections
import sys


def math3(N):
    # N = 10
    arrList = []
    for i in range(2, N+1):         # i = 2 ~ 10
        tmp = i
        for j in range(2, i+1):
            while tmp % j == 0:
                arrList.append(j)   # arrList = [i의 소인수들]
                tmp /= j
            if tmp == 1:
                break
    # arrList = [모든 인수를 담음] 이제 2와 5의 갯수를 확인하면됨.
    if 2 not in arrList or 5 not in arrList:
        print(0)
        exit()
    c = collections.Counter(arrList)
    print(min(c.get(2), c.get(5)))

    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    math3(N)
