import math

def find_num(N):
    x1, y1, r1, x2, y2, r2 = map(int, N.split(' '))

    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if (dist == 0):
        if (r1 == r2):
            print('-1')
        else:
            print('0')
    else:
        if (dist < r1 + r2):
            if (dist + min(r1, r2)) == max(r1, r2):
                print(1)
            elif (dist + min(r1, r2) < max(r1, r2)):
                print(0)
            else:
                print(2)
        elif (dist == r1 + r2):
            print('1')
        else:
            print('0')


n = int(input())

for i in range(0, n):
    N = input()
    find_num(N)