import sys  # 빠른 입력을 위한 모듈
menu_bur = []
menu_be = []
set_min = 10000
# 입력 받은 햄버거, 음료를 나누기.
for i in range(5):
    if i < 3:
        menu_bur.append(int(sys.stdin.readline().strip()))
    else:
        menu_be.append(int(sys.stdin.readline().strip()))


for bur in menu_bur:
    for be in menu_be:
        if bur + be - 50 < set_min:
            set_min = bur + be - 50
        else:
            continue
print(set_min)
