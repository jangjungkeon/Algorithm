import sys


def cal_dist(depth):
    global min_val
    if depth == 2:
        tmp_val = (tmp_list[0][0] - tmp_list[1][0]) ** 2 + \
                  (tmp_list[0][1] - tmp_list[1][1]) ** 2
        if tmp_val < min_val:
            min_val = tmp_val
        return

    for i in range(N):
        if not check[i]:   # TRUE 이면
            check[i] = True
            tmp_list.append(dot_list[i])
            cal_dist(depth + 1)
            tmp_list.pop()
            # 중복하지 않도록.
            if depth != 0:
                check[i] = False

    return min_val


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    dot_list = []
    check = [False for _ in range(N)]
    min_val = 10000000000
    tmp_list = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        dot_list.append((x, y))
    print(cal_dist(0))
