import sys

N, M = map(int, sys.stdin.readline().split())

b_card = list(map(int, sys.stdin.readline().split()))
max_l = {"gap": 1000000, "list": []}
for i in range(len(b_card)-2):
    for j in range(i+1, len(b_card)-1):
        for k in range(j+1, len(b_card)):
            if b_card[i] + b_card[j] + b_card[k] <= M and M - (b_card[i] + b_card[j] + b_card[k]) <= max_l["gap"]:
                max_l["gap"] = M - (b_card[i] + b_card[j] + b_card[k])
                max_l["elem"] = ([b_card[i], b_card[j], b_card[k]])

print(M - max_l["gap"])

'''
전체중에 M에 가장 가까운 카드 3장의 합. 
1. 3장이면서값(합이 21을 넘지 않으면)
2. M에 가장 가까운 

1, 2를 동시에 만족. 1번을 먼저 구해보고, 2번을 구해보자. 

'''