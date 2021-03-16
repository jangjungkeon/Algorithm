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

# 적절한 i와 stand_num 를 while 문으로 찾기
while True:
    i += 1
    stand_num += i
    if X <= stand_num:  # 만일 i = 3, stand_num = 6, X = 5
        break

# 홀수라면 // i, X, stand_num 은 이미 구함
'''
up = [ , ][i%2]
아래의 코드는 i, X, stand_num 사이의 규칙을 발견하지 못했을 때 저렇게 할 수 있다. 
규칙을 발견햇으면 좀더 짧은 코딩으로 가능할듯. 결국 규칙 발견을 못하면 노가다를 해야하는 것이 현실.
'''
if i % 2:
    if X % i == 0:
        up = 1  # X % i = 0 이면, X % i = i 로 바꿔주야함
        down = i

    else:
        up = i + 1 - (X % i)  # up + down = i + 1
        down = i + 1 - up

else:  # 짝수라면
    if (X + (i / 2)) % i == 0:
        up = i
        down = 1

    else:
        up = (X + (i / 2)) % i
        down = i + 1 - up


print(f"{int(up)}/{int(down)}")
