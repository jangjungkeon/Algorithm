import sys
import math


def math_gcd(input_list):
    global gcd_val
    input_list_m = []
    gcd_val_list = []

    for i in range(N):
        for j in range(i+1, N):
            input_list_m.append(abs(input_list[i] - input_list[j]))

    for i in range(1, len(input_list_m)):
        if i == 1:
            gcd_val = math.gcd(input_list_m[i-1], input_list_m[i])
            continue
        gcd_val = math.gcd(input_list_m[i], gcd_val)

    if N == 2:
        gcd_val = abs(input_list[0] - input_list[1])

    for i in range(2, int(gcd_val**0.5)+1):
        if gcd_val % i == 0:
            gcd_val_list.append(i)
            if i != gcd_val // i:
                gcd_val_list.append(gcd_val // i)
    gcd_val_list.append(gcd_val)
    print(*sorted(gcd_val_list))
    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    input_list = [int(sys.stdin.readline().strip()) for _ in range(N)]
    math_gcd(input_list)
