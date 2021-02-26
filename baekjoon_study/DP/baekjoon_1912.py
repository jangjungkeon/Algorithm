import sys

N = int(sys.stdin.readline().strip())
seq = list(map(int, sys.stdin.readline().split()))

dp = [seq[0]]

for i in range(1, N):
    dp.append(max(dp[i-1] + seq[i], seq[i]))
print(max(dp))
