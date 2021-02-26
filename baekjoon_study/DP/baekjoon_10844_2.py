import sys

N = int(sys.stdin.readline().strip())
sum_cal = 0

def make_list(cal_list):
    lst = []

    for val in cal_list:
        if val == 0:
            lst.append(1)
        elif val == 9:
            lst.append(8)
        else:
            lst.append(val - 1)
            lst.append(val + 1)
    return lst


for i in range(1, 10):
    cal_list = [i]
    cont = 1
    while True:
        if cont == N:
            sum_cal += len(cal_list)
            break
        cont += 1
        cal_list = make_list(cal_list)


print(sum_cal % 1000000000)
