import sys

# 상근이가 배달해야하는 N 키로 입력
N = int(sys.stdin.readline().strip())

# 만일 5로 나눠진다면
if N % 5 == 0:
    print(int(N / 5))
    exit()

# i : N을 5로 나눈 몫(범위 : 0 ~ 몫)
for i in range(int(N/5), -1, -1):
    rest = N - (5 * i)
    if rest % 3 == 0:       # 5kg 로 묶고, 남은 3kg로 남나?
        print(i + int(rest / 3))
        exit()
    else:
        continue
# for 문 다 돌았는데도 없으면 -1
print(-1)


'''
for 문으로 열라게 돌려도 될듯. 먼저 5kg로 끝까지해보고 3kg 되면 go 
안되면 하나씩 줄이기. 
int(N/5) > 몫

'''