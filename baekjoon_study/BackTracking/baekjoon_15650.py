import sys

N, M = map(int, sys.stdin.readline().split())

check = [False] * N         # 중복 방지를 위한 flag
result = []

def backtracking(depth, N, M):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    for i in range(N):
        if not check[i]:        # 이미 한거, 중복은 패스 해.
            check[i] = True     # 중복 제거.(1 1) (2 2) 이런거 방지
            if len(result) == 0 or result[-1] < i+1:
                result.append(i+1)
                backtracking(depth+1, N, M)
                check[i] = False    #
                result.pop()        # 출력한 내용 제거.
            else:
                check[i] = False

backtracking(0, N, M)


'''
N = 4, M = 2
1 2
1 3
1 4
2 3
2 4
3 4
'''
