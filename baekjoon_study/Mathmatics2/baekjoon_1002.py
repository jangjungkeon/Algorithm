import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    if distance == 0:
        if r1 == r2:
            print(-1)
            continue


    if distance < abs(r2-r1) or distance > r1+r2:
        print(0)
        continue
    if distance > abs(r2-r1) and distance < r1+r2:
        print(2)
        continue
    if distance == abs(r2-r1) or distance == abs(r1+r2):
        print(1)
        continue
