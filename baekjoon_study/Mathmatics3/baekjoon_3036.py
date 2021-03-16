import copy
import sys


def math(N):
    N_list = []
    for i in range(2, N+1):
        while N % i == 0:
            N_list.append(i)
            N /= i
            if N == 1:
                return N_list
    return


def cal(tmp_num):
    numerator = 1
    if len(tmp_num) == 0:
        pass
    else:
        for i in tmp_num:
            numerator *= i
    return str(numerator)


def rotate(ring):           # ring = [12, 3, 8, 4]
    first_list = math(ring[0])      # first_list = [2,2,3]
    for val in ring[1:]:
        tmp_num = copy.deepcopy(first_list)        # tmp_num = [2,2,3]
        tmp_num_t = copy.deepcopy(first_list)
        tmp_den = math(val)         # tmp_den = [3]
        for i in tmp_num_t:
            if i in tmp_den:
                tmp_num.remove(i)
                tmp_den.remove(i)
        print(cal(tmp_num)+"/"+cal(tmp_den))
    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    ring = list(map(int, sys.stdin.readline().split()))
    rotate(ring)
