import sys

# 입력값을 받는다.
T = int(sys.stdin.readline())

for i in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    planets = []

    for j in range(n):
        planets.append(sys.stdin.readline())

    count = 0

    for planet in planets:
        planet = planet.split()
        xc = int(planet[0])
        yc = int(planet[1])
        r = int(planet[2])

# 식을 세운다.
        d1 = ((x1-xc)**2 + (y1-yc)**2)**0.5
        d2 = ((x2-xc)**2 + (y2-yc)**2)**0.5

        if d1 < r and d2 < r:
            continue

        elif d1 > r and d2 > r:
            continue

        else:
            if d1 < r:
                count += 1

            if d2 < r:
                count += 1

    print(count)
