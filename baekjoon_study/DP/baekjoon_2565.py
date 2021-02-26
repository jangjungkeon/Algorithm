import sys

N = int(sys.stdin.readline().strip())
pole = []

dp = [1 for _ in range(N)]
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    pole.append([x, y])

pole.sort(key=lambda a: a[0])

for i in range(N):
    for j in range(N):
        if j > i and pole[j][1] > pole[i][1]:
            if dp[j] < dp[i] + 1:
                dp[j] = dp[i] + 1

print(N - max(dp))

'''
dp[x] : x
dp[x] = 5
4 6 7 9 10
N - 최댓값


가장 긴 증가 부분 수열? 
x1 < x2 -> y1 < y2 : 정상
x1 < x2 -> y1 > y2 : 겹치는 경우. 

겹치면 계속 자르기? 최대값을 찾는거야. 
'''