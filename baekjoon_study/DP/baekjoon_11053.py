import sys

N = int(sys.stdin.readline().strip())
Subsequence = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(N)]
for i in range(N):
    for j in range(N):
        if j > i and Subsequence[j] > Subsequence[i]:
            if dp[j] < dp[i] + 1:
                dp[j] = dp[i] + 1



print(max(dp))

'''
test case
6
1 2 1 3 2 5
>> 4
5               
8 9 1 2 3 
>> 3
7
1 4 5 2 3 4 5
>> 5
4
1 4 2 3
>> 3
6
1 2 1 1 1 1
>> 2

12
1 2 3 4 5 4 3 2 1 2 3 4
>> 5


dp[x] : x번째 수를 마지막 원소로 가지는 lis의 길이
'''