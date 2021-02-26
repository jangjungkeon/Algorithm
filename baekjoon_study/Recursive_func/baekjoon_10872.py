import sys

def factoral(N):
    # 탈출문
    if N == 0:
        return 1
    else:
        return N * factoral(N-1)

N = int(sys.stdin.readline().strip())
print(factoral(N))
