import sys      # 빠른 입력을 위한 모듈

N = int(sys.stdin.readline().strip())

for _ in range(N):
    # 학생들 성적 입력 받기
    score_list = list(map(int, sys.stdin.readline().split()))
    # 학생들 성적 평균 구하기
    mean = (sum(score_list[1:]))/score_list[0]
    # 평균이 넘는 학생 수 구하기
    cont = 0
    for i in score_list[1:]:
        if i > mean:
            cont += 1

    # 평균이 넘는 학생 비율 구하기 // 지시자를 활용. cf) round 함수가 있긴 있음.
    print("%.3f%%" % (100*cont/score_list[0]))