import sys

N = int(sys.stdin.readline().strip())
w_h = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    w_h.append([x, y, 1])

for i in w_h:
    for j in w_h:
        # 덩치 비교, 키와 몸무게가 작으면 +1
        if i[0] < j[0] and i[1] < j[1]:
            i[2] += 1

# 리스트의 내용을 한줄로 출력하기.
for i in range(len(w_h)):
    print(w_h[i][2], end=' ')






'''
몸무게가 가장 많이 나가는 친구부터 정렬. 
하나하나 비교해야하나?
처음에는 모두가 1등인걸로. 
  
'''