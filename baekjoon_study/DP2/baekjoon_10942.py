import sys


def func():
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    # distance = 1
    for i in range(1, N+1):
        dp[i][i] = 1

    # distance = 2
    for i in range(1, N):
        if board[i-1] == board[i]:
            dp[i][i+1] = 1

    # distance >= 3
    for d in range(2, N):
        for i in range(1, N+1-d):
            if board[i-1] == board[i+d-1] and dp[i+1][i+d-1] == 1:
                dp[i][i+d] = 1
                # i <= N-d

    for q in question:
        i = q[0]
        j = q[1]
        print(dp[i][j])
    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    board = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().strip())
    question = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
    func()


'''
길이가 1 : 무조건 펠린
길이가 2 : 숫자가 같으면 펠린
길이가 3 이상 : 양쪽 끝의 숫자 비교 & dp[i-1][j-1] ==1

[[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 0, 0, 0, 0, 0, 0], 
[0, 0, 1, 0, 0, 0, 0, 0], 
[0, 0, 0, 1, 0, 0, 0, 0], 
[0, 0, 0, 0, 1, 0, 0, 0], 
[0, 0, 0, 0, 0, 1, 0, 0], 
[0, 0, 0, 0, 0, 0, 1, 0], 
[0, 0, 0, 0, 0, 0, 0, 1]] 


    for i in range(1, N+1):
        for j in range(1, N+1):
            if i <= j:
                if i == j:  # dp[1][1] ~ dp[N][N]
                    dp[i][j] = 1
                    continue
                if j - i == 1:
                    # board = 1 2 1 3 1 2 1
                    if board[i-1] == board[j-1]:
                        dp[i][j] = 1
                    continue
                if j - i >= 2:
                    if board[i-1] == board[j-1] and dp[i+1][j-1] == 1:
                        dp[i][j] = 1
'''