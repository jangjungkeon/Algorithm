import sys

N, K = map(int, sys.stdin.readline().split())
bag = []
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]


for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    bag.append((w, v))

# dp[i][j] : i는 물품의 최대 인덱스, j는
#
# 배낭의 최대 무게
for i in range(1, N+1):
    for j in range(1, K+1):
        if bag[i-1][0] > j:     # bag[i-1][0] : i-1일때 가방의 무게. 배낭에 물건을 넣었을 때 최대무게를 초과한다면
            dp[i][j] = dp[i-1][j]
        else:       # 새로운 물품 + 최대 무게를 넘어서지 않는다
            dp[i][j] = max(bag[i-1][1] + dp[i-1][j-bag[i-1][0]], dp[i-1][j])


print(dp[N][K])
'''
4 7
6 13
4 8
3 6
5 12
'''
