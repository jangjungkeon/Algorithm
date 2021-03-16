import sys


# 소수의 갯수 체크, 에라토스테네스의 체 방식으로 체크
def check_prim(n):
    # 탈출문
    if n == 0: exit()
    prime_list = [True] * (2*n+1)   # 가장 끝에 있는 값으로 곱해줌
    prime_list[0] = False
    prime_list[1] = False

    # 소수 아닌 것 솎아내기
    for i in range(2, int((2*n)**0.5)+1):
        if prime_list[i]:
            for j in range(2*i, 2*n+1, i):
                prime_list[j] = False
    cont = 0
    for i in range(n+1, 2*n+1):
        if prime_list[i]:
            cont += 1
    return print(cont)


while True:
    n = int(sys.stdin.readline().strip())
    check_prim(n)
