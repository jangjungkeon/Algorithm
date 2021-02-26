import sys


N = int(sys.stdin.readline().strip())
if N == 1:
    print(0)
    exit()

cont = 0
cal_list = [N]

def make_list(cal_list):
    lst = []
    for i in cal_list:
        lst.append(i - 1)
        if i % 3 == 0:
            lst.append(i / 3)
        if i % 2 == 0:
            lst.append(i / 2)
    return lst


while True:
    cal_list = make_list(cal_list)
    cont += 1
    # 탈출문
    if min(cal_list) == 1:
        print(cont)
        break
