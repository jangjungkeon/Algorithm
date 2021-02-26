import sys

# 테스트 케이스 입력

T = int(sys.stdin.readline().strip())

for _ in range(T):
    S = sys.stdin.readline().split()
    R = int(S[0])       # R = 정수, 반복횟수
    S = S[1]            # S = 입력값, 문자열
    tmp = ''            # tmp = print 를 위한 용도
    for i in S:
        tmp += i*R      # 문자 반복하기
    print(tmp)