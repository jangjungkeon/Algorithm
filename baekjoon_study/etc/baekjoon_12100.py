import sys

N = int(sys.stdin.readline())

# table 생성
table = [[[int(i), 0] for i in sys.stdin.readline().split()] for _ in range(N)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

# move 함수
def move(x, y, dx, dy):
    while x and