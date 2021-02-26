import sys


# 에라토스테네스의 체 방법으로 풀기

# 함수 구현 부분.
def make_prim(M, N):
    prim_list = [True] * (N + 1)  # 항상 for 문을 써서 배열이나 리스트를 만들 필요는 없다.
    prim_list[0] = False
    prim_list[1] = False

    # 소수가 아닌 것 거르기
    for i in range(2, int(N ** 0.5) + 1):
        if prim_list[i] == True:  # 소수라면
            for j in range(2 * i, N + 1, i):  # 해당 배수는 거르기.
                prim_list[j] = False

    # 소수인 것 출력하기
    for i in range(M, N + 1):
        if prim_list[i] == True:
            print(i)


# main
M, N = map(int, sys.stdin.readline().split())
make_prim(M, N)
