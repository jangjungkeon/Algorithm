import sys  # 빠른 입력을 위한 모듈

N = int(sys.stdin.readline().strip())

# 한수인지 확인하기
cont = 0
# 한수인지 확인하고 갯수 세기
for i in range(1, N+1):
    list_int = list(map(int, str(i)))
    lenth = len(list(map(int, str(i))))
    if lenth == 1:          # 한자릿수라면 바로 한수 이므로 카운
        cont += 1
        continue
    for j in range(lenth):     # range(len([1,2,3])), int + list
        if j < lenth - 1:
            d = list_int[j+1] - list_int[j]
            if j == 0:          # 첫번째는 공차 세이브만 하기
                d_save = d
                continue
            if d != d_save:     # 공차가 어긋나는 항이 있으면 break
                break
        else:                   # 맨 마지막 항까지 살아 남으면 한수 갯수 세기
            cont += 1

# 한수의 갯수 출력
print(cont)