import sys      # 빠른 입력을 위한 모듈

N = int(sys.stdin.readline().strip())

for i in range(1, N+1):     # 1에서 N(중간) 까지
    print('*' * i)

for j in range(1, N):       # 중간에서 끝까지
    print('*' * (N-j))


#######################################
import sys      # 빠른 입력을 위한 모듈

N = int(sys.stdin.readline().strip())

for i in range(1, 2*N):
    if i < N + 1:       # 가장 별이 많은 중간 지점까지는 정주행
        print('*' * i)
    if i > N:           # 중간 지점 이후에는 다르게 적용
        print('*' * (2 * N - i))

