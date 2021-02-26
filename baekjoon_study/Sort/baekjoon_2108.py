import collections
import sys


N = int(sys.stdin.readline().strip())

# 입력을 어떤 형태로 받을 것인가? -> 리스트로 입력받기
val_list = [int(sys.stdin.readline().strip()) for _ in range(N)]
val_list.sort()

# 첫째줄에는 산술평균, 소수점 첫째자리에서 '반올림'한 값 출력
fir_sol = sum(val_list) / len(val_list)
print(f"%1.f" % fir_sol)

# 둘째줄에는 중앙값을 출력
print(val_list[len(val_list) // 2])

# 셋째줄에는 최빈값을 출력 -> 손봐야함
trd_sol = collections.Counter(val_list)
trd_list = trd_sol.most_common()

if len(trd_list) > 1:
    if trd_list[0][1] == trd_list[1][1]:
        print(trd_list[1][0])
    else:
        print(trd_list[0][0])
else:
    print(trd_list[0][0])


# 네번째줄에는 범위를 출력
print(val_list[-1] - val_list[0])
