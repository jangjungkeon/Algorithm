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


def make_LAN(N):
    s = 1
    last = 2**(31)-1
    e = last
    mid = (s + e) // 2
    while True:
        if pingpong(mid) >= N:
            break
        e = mid
        mid = (s+e)//2
    s = mid


    while True:
        mid = (s + e) // 2
        if s == mid:
            if pingpong(mid+1) >= N:
                return mid + 1
            return mid
        if pingpong(mid) >= N:
            s = mid
        if pingpong(mid) < N:
            e = mid


if __name__ == "__main__":
    K, N = map(int, sys.stdin.readline().split())
    A = [int(sys.stdin.readline().strip()) for _ in range(K)]
    start_t = time.time()
    print(make_LAN(N))
    end_t = time.time() - start_t
    #print(f"실행시간 : {end_t}")
