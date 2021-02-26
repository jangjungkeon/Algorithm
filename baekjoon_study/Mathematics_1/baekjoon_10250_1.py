import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    # H,W,N 입력 받기
    H, W, N = map(int, sys.stdin.readline().split())
    # cont : 호수, a : 층
    cont = (N+H-1)//H
    a = N % H if N % H != 0 else H
    print(str(100*a+cont))
    #print("%d%02d" % (a, cont))

    ## 이거는 왜 안되는거냐;;