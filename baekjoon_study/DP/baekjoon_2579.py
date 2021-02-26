import sys

N = int(sys.stdin.readline().strip())
stair = [int(sys.stdin.readline().strip()) for _ in range(N)]
stair.insert(0, 0)
dp = [[0, 0] for _ in range(N+2)]


for i in range(N+1):
    dp[i][0] = stair[i] + dp[i-1][1]
    dp[i][1] = stair[i] + max(dp[i-2])

print(max(dp[N]))

'''

for 1 in range(N+1):
    dp[1][0] = stair[1] + dp[0][1]
    dp[1][1] = stair[1] + max(dp[-1])

마지막인 N = 300이거나, 점수가 10000이하일 때
최댓값, 최솟값 -> dp일 킹능성 존재. 

조건. 
1.계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
2.연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
3.마지막 도착 계단은 반드시 밟아야 한다.


총 점수의 최댓값 구하기. dp, dp, dp, dp, dp, dp, dp, dp, dp 
dp[i] = i번째 계단까지 점수의 최댓값
dp[i][0] : 1계단씩 오른 친구
dp[i][1] : 2계단씩 오른 친구


N = int(sys.stdin.readline().strip())
stair = [int(sys.stdin.readline().strip()) for _ in range(N)]
stair.insert(0, 0)
dp = [[0, 0] for _ in range(N+1)]

for i in range(N+1):
    dp[i][0] = stair[i] + dp[i-1][1]
    dp[i][1] = stair[i] + max(dp[i-2][0], dp[i-2][1])

마지막 도착계단을 밟아야한다. 






'''