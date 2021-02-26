import sys

# 입력

def sum_func(sum_oper):
    sum = progre[0]
    for i in range(N-1):
        if sum_oper[i] == '+':
            sum = sum + progre[i+1]
        elif sum_oper[i] == '-':
            sum = sum - progre[i+1]
        elif sum_oper[i] == 'x':
            sum = sum * progre[i+1]
        else: # '/' 일때
            if sum < 0:
                sum = -(abs(sum) // progre[i+1])
            else:
                sum = sum // progre[i+1]
    return sum

def DFS(depth):
    if depth == N-1:
        if tuple(sum_oper) in check_oper:
            return
        else:
            check_oper.append(tuple(sum_oper))
            result.append(sum_func(sum_oper))
            return

    # oper_transf = ['+', '+', '-', 'x', '/']
    for i in range(N - 1):
        if not check[i]:
            check[i] = True
            sum_oper.append(oper_transf[i])
            DFS(depth + 1)
            check[i] = False
            sum_oper.pop()



N = int(sys.stdin.readline().strip())
progre = list(map(int, sys.stdin.readline().split()))
# 연산자는 '+' '-' 'x' '/'  순서로
oper = list(map(int, sys.stdin.readline().split()))
oper_transf = []
result = []
sum_oper = []
check = [False for _ in range(N-1)]
check_oper = []
for _ in range(oper[0]):
    oper_transf.append('+')
for _ in range(oper[1]):
    oper_transf.append('-')
for _ in range(oper[2]):
    oper_transf.append('x')
for _ in range(oper[3]):
    oper_transf.append('/')

DFS(0)

print(max(result))
print(min(result))