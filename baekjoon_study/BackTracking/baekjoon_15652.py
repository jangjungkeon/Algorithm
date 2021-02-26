import sys

N, M = map(int, sys.stdin.readline().split())

solution = []


def backtracking(depth, N, M):
    if depth == M:
        print(*solution)  # 리스트의 괄호를 벗겨내고 출력
    else:
        for i in range(N):
            if len(solution) == 0 or solution[-1] <= i + 1:
                solution.append(i + 1)
                backtracking(depth + 1, N, M)
                solution.pop()


backtracking(0, N, M)
