import sys

# N-1을 중간에 옮기고, -> 가장 아래 원판을 마지막에 -> 그리고 중간에 있는 N-1을 마지막으로 옮기기
def hanoi(n,a,b,c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)


N = int(sys.stdin.readline().strip())
cont = 0
# 하노이의 탑에서 카운트 규칙은 f(n) = f(n-1)*2 + 1
for i in range(N):
    cont = cont*2 + 1

print(cont)
if N <= 20:
    hanoi(N, 1, 2, 3)
