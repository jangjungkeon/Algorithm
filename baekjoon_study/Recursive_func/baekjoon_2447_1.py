# 전체를 * 로 만든 후 필요한 부분을 공백으로 처리하는 방법

import sys

N = int(sys.stdin.readline().strip())

# N * N 배열을 "*"로 초기화
star_init = [['*'] * N for _ in range(N)]


# 3의 지수 찾기
v = N; cont = 0
while v != 1:
    cont += 1
    v /= 3

for cont_ in range(cont):
    # 이렇게 짧은 변수 명명 너무 좋음
    idx = [i for i in range(N) if (i // 3**cont_) % 3 == 1]
    for i in idx:
        for j in idx:
            star_init[i][j] = ' '


print("\n".join(["".join([i for i in row])for row in star_init]))
