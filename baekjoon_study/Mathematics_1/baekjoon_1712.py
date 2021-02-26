import sys

# A : 기본 비용, B : 가변비용, C : 노트북 가격
A, B, C = map(int, sys.stdin.readline().split())

# BEP 가 넘을 때의 경우.

if C-B == 0 or A/(C-B) <= 0:        # BEP 가 존재하지 않을 때 와 0으로 나눌 때(만일 0으로 나누는 경우를 체크 안해주면 런타임 에러가 뜸)
    print(-1)
else:                               # BEP 구하기
    print(int(A / (C - B)) + 1)

