import sys       # 빠른 입력을 위한 모듈

N = int(sys.stdin.readline().strip())

# 입력값 받기 .
score = list(map(int, sys.stdin.readline().split()))        # int형 리스트로 입력 받기.
score_max = max(score)          # 가장 큰 값 구하기.
score_fraud = []

# 입력값을 주어진 식에 맞춰  변환하기
for i in score:
    score_fraud.append((i/score_max)*100)       # 값 변환하기

# 평균 구하기 - 답 찾기
print(sum(score_fraud)/len(score_fraud))        # 평균 구하기.


'''
1.아 평균을 구할때는 numpy 외에는 따로 빌트인 함수가 없구나.
2.공백으로 띄워진 숫자들을 입력으로 받을 때 : int형 + 리스트로 받기
3.최대값 꾸하기~? 
'''