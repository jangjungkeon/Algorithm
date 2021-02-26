'''
1. X가 어디 그룹에 속하는지 확인
2. 해당 그룹의 정보 2가지를 체크. 홀짝, 범위 i
3. 홀짝에 따라 +,- 방향을 정하고, 위아래 값을 따로 정함
4. 답구함

'''
import sys

X = int(sys.stdin.readline().strip())

stand_num = 0       # 범위의 제일 마지막 끝자리수, 기준이 되는 수.
i = 0               # 해당 범위내에 분자 자리에서 가장 큰 수
while True:
    i += 1
    stand_num += i
    if X <= stand_num:  # 만일 i = 3, stand_num = 6, X = 5
        # 홀수라면
        if i % 2:
            if X % i == 0:
                up = 1        # X % i = 0 이면, X % i = i 로 바꿔주야함
                down = i
                break
            else:
                up = i + 1 - (X % i)  # up + down = i + 1
                down = i + 1 - up
                break
        else:   # 짝수라면
            if (X + (i/2)) % i == 0:
                up = i
                down = 1
                break
            else:
                up = (X + (i/2)) % i
                down = i + 1 - up
                break
print(f"{int(up)}/{int(down)}")
