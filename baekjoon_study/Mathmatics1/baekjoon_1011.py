import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x

    # distance가 1~4까지는 아래의 while 문에 적용하기 어렵다.
    if distance == 1:
        print(1)
        continue

    i = 0
    # 횟수를 찾는 반복문
    while True:
        i += 1
        # 복잡한대, distance가 어떤 범위에 속하고 있는지 확인하기. n^2<x<=(n+1)^2
        if distance > i ** 2 and distance <= (i+1) ** 2:
            # n 범위에 속하는 것을 확인하면 횟수는 2*n or 2*n+1 둘 중 하나이다. (규칙 발견)
            # 둘 중 고르는 기준은 distance가 n^2 + n을 넘는지 확인하는 것.
            # 해당 기준을 넘으면 2*n+1, 그렇지 않으면 2*n
            solution = 2*i if distance <= i**2 + i else 2*i+1
            print(solution)
            break