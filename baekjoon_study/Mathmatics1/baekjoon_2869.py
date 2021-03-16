import sys

# 높이, 낮, 밤 속도 입력 A,B,V

A, B, V = map(int, sys.stdin.readline().split())
k = (V - A) / (A - B)

# 정수일 때
if int(k) == k:
    print(int(k + 1))
# 소수일 때
else:
    print(int(k + 2))

# 삼항 연산자를 사용한 숏코딩
# print(int(k+1) if k == int(k) else int(k+2))


