import sys

def make_prim_list(n):
    # prim_list_bool, prim_list 초기화
    prim_list_bool = [True] * (n)
    prim_list_bool[0] = prim_list_bool[1] = False
    prim_list = []

    # 소수가 아닌 수는 거르기.
    for i in range(2, int(n ** 0.5) + 1):
        if prim_list_bool[i]:  # 소수라면
            for j in range(2 * i, n, i):
                prim_list_bool[j] = False

    # 소수를 선별해서 prim_list 에 넣기
    for i in range(2, n):
        if prim_list_bool[i]:
            prim_list.append(i)
    return prim_list

def Gold_barh(n, prim_list):
    # 파악된 소수 중에서 골드바흐 파티션 찾기
    # 중간값에 가장 근접한 값 mid
    mid = max([i for i in range(len(prim_list)) if prim_list[i] <= n/2])
    for i in range(mid, -1, -1):
        for j in range(mid, len(prim_list)):
            if prim_list[i] + prim_list[j] == n:
                return print(f"{prim_list[i]} {prim_list[j]}")


# main
T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    prim_list = make_prim_list(n)
    Gold_barh(n, prim_list)

