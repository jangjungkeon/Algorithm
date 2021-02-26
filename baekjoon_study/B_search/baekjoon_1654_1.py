import sys
import time

def pingpong(n):
    cont = 0
    for i in A:
        tmp = i
        while True:
            tmp -= n
            if tmp < 0:
                break
            cont += 1
    return cont


def make_LAN(A, N):
    s = 1
    last = min(A)
    e = last
    while True:
        mid = (s + e) // 2
        if pingpong(mid) == N or s == mid:
            while pingpong(mid) == N:
                mid += 1
            return mid - 1
        if pingpong(mid) < N:
            e = mid
        if pingpong(mid) > N:
            s = mid
        '''
        269 * 2 = 538
        269 * 2 = 538
        '''


if __name__ == "__main__":
    K, N = map(int, sys.stdin.readline().split())
    A = [int(sys.stdin.readline().strip()) for _ in range(K)]
    start_t = time.time()
    print(make_LAN(A, N))
    end_t = time.time() - start_t
    print(f"실행시간 : {end_t}")

'''
실행시간 : 0.00012421607971191406
'''