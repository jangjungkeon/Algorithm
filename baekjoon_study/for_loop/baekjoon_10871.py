import sys      # 빠른 입력을 위한 모듈

N, X = map(int, sys.stdin.readline().split())
list = sys.stdin.readline().split()
sol = []
for i in list:
    i = int(i)
    if i < X:
        sol.append(str(i))

sol_string = " ".join(sol)
print(sol_string)

