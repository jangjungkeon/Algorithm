import sys  # 빠른 입력을 위한 모듈

N = int(sys.stdin.readline().strip())           # strip 해주는 꼼꼼함 잊지말자.

# N이 1이라면
if N == 1:
    print('*')

# N이 1이 아니라면
else:
    # N이 홀수
    if N % 2:
        for i in range(1, 2*N+1):
            if i % 2:                                       # if i % 2: 라는 것은 홀수라면 이라고 바로 해석해버리자.
                print(('* '*int((((N-1)/2)+1)))[:-1])       # 뒤에 문자열 자르기 기술, 문자열에 float 은 곱하기 못하니깐 int 로 형변환(casting) 시켜야
            else:
                print((' *'*int(((N-1)/2))))
    # N이 짝수
    else:
        for i in range(1, 2*N+1):
            if i % 2:
                print(('* '*int(N/2))[:-1])
            else:
                print((' *'*int(N/2)))


