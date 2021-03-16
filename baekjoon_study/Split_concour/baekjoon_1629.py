import sys


def cal(A, C):
    cont = 0
    while A * cont <= C:
        cont += 1
    return cont


def spl_conq(B, C):
    if B <= n:
        return (A ** B) % C

    if B % 2 == 0:
        return spl_conq(B // 2, C) ** 2 % C
    else:
        return ((spl_conq(B // 2, C) ** 2)*A) % C


if __name__ == "__main__":
    A, B, C = map(int, sys.stdin.readline().split())
    n = cal(A, C)
    print(spl_conq(B, C))

