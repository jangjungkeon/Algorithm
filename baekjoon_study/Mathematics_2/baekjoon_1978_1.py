## 소수의 말 그대로 해석한 사례. 깔끔하다.

import sys

N = int(sys.stdin.readline().strip())
check_list = list(map(int, sys.stdin.readline().split()))
res = 0
for i in check_list:
    cont = 0
    if i == 1:
        continue
    for j in range(1, i+1):
        if i % j == 0:      # 소인수를 2개만 갖는 다면.
            cont += 1
    if cont == 2:
        res += 1

print(res)