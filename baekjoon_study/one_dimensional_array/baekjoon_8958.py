import sys  # 빠른 입력을 위한 모듈

N = int(sys.stdin.readline().strip())

for _ in range(N):
    test = sys.stdin.readline().strip()        # 값 입력.
    score = 0
    tmp = 0
    # 하나하나 검사하기
    for i in test:
        if i == 'O':        # 'O' 일 때, 연속된 O 에 가점 주는 알고리즘.
            score += tmp + 1
            tmp += 1
        else:               # 'x' 일때
            tmp = 0
    print(score)