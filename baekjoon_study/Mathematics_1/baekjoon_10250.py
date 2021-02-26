import sys

def Room_check(H, N):
    cont = 0
    s = 0
    # N이 머무르는 호수 파악
    while True:
        cont += 1
        s += H
        if N <= s:
            break
    # a : N이 머무르는 층수(N % H)
    # cont : N이 머무르는 호수
    a = N % H if N % H != 0 else H
    return print("%d%02d" % (a, cont))


T = int(sys.stdin.readline().strip())

for _ in range(T):
    # H,W,N 입력 받기
    H, W, N = map(int, sys.stdin.readline().split())
    Room_check(H, N)