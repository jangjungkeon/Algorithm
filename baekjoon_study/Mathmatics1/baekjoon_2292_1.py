'''
1, 7, 19, 37...
계차 수열을 수식으로 풀지 않고 반복문으로 쉽게 풀 수 있다.
'''

import sys

N = int(sys.stdin.readline().strip())
a = 1
d = 6
num_room = 1
if N == 1:     # 1일 때 계산하기
    print(1)
else:
    while True:
        a += d      # 계차수열의 공차 넣어주기
        num_room += 1
        if N <= a:  # 해당 범위 안에 존재한다면
            print(num_room)
            break
        d += 6