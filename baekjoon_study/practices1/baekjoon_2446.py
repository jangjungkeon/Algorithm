import sys      # 빠른 입력을 위한 모듈

N = int(sys.stdin.readline().strip())

for i in range(1, 2*N):
    if i < N + 1:
        print(' ' * (i-1) + ('*'*(2*(N-i)+1)))     # 중간 지점까지, ' '의 갯수 + '*' 의 갯수 등차수열 구하기
    if i > N:
        print(' ' * (2*N-1-i) + ('*'*(2*i-2*N+1)))      # 마지막 까지, , ' '의 갯수 + '*' 의 갯수 등차수열 구하기

