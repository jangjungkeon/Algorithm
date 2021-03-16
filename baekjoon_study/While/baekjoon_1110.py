import sys     # 빠른 입력을 위한 모듈

N = sys.stdin.readline().strip()        # N 입력.
init_N = N
cont = 0

while True:
    if len(N) == 1:         # 한자리 수일 때 0을 앞에 추가하기.
        N = '0' + N
    N_sum = str(int(N[0]) + int(N[1]))     # 문자열이기에 int 로 바꾸고 다시 문자열로.
    N_new = N[-1] + N_sum[-1]
    if N_new[0] == '0':             # '07' 같은 숫자가 나올 수도 있기에 조치.
        N_new = N_new[-1]
    N = N_new
    cont += 1
    if init_N == N:             # while 탈출
        print(cont)
        break