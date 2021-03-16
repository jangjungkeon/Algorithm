# 이미 구현된 클래스로 꿀빨기
import sys
import itertools


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    N_list = [i for i in range(N)]
    print(len(list(itertools.combinations(N_list, K))))


'''
N C K 값 구하기

'''
