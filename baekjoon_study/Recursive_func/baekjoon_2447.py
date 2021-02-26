## 프랙탈 도형을 그리는 문제이다.

import sys

def stars(star):
    matrix = []
    for i in range(3 * len(star)):
        if i // len(star) == 1:
            matrix.append(star[i % len(star)] + ' ' * len(star) + star[i % len(star)])
        else:
            matrix.append(star[i % len(star)] * 3)
    return list(matrix)


star = ['***', '* *', "***"]
N = int(sys.stdin.readline().strip())
cont = 0
while N != 3:
    cont += 1
    N /= 3

for _ in range(cont):
    star = stars(star)
for i in star:
    print(i)