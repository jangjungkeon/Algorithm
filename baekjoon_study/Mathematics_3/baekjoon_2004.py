import sys


def cont(N, num):
    cont = 0
    # 1~N 사이의 수들이 num을 인수로 몇개를 가지고 있을 것인가.
    tmp = num
    while N >= num:
        cont += N // num
        num *= tmp
    return cont


    # NCM = N! / (M! * (M-N)!)
    # N_2 - (M_2 +(M-N)_2) 와 N_5 - (M_5 +(M-N)_5)
    # 2와 5의 인수중 작은 수

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    print(min(cont(N,2) - cont(M,2) - cont(N-M,2),
              cont(N,5) - cont(M,5) - cont(N-M,5)))
