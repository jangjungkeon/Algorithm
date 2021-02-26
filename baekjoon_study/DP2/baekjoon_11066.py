import sys


def func(k, page):
    table = [[0 for _ in range(k)] for _ in range(k)]

    # table[i][j] = i번째에서 j번째까지 파일 합의 최솟값
    # table[i][j] = table[i][j-1] + page[j] + min(minimum)
    # 4 3 3 5
    for i in range(k-1):
        table[i][i+1] = page[i] + page[i+1]
        # table[0][1]
        for j in range(i+2, k):
            table[i][j] = table[i][j-1] + page[j]
            # table[0][2]
    # min 을 찾아보기
    for d in range(2, k):
        for i in range(k-d):
            j = i + d
            minimum = [table[i][m] + table[m+1][j] for m in range(i, j)]
            table[i][j] += min(minimum)

    return print(table[0][k-1])


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        k = int(sys.stdin.readline().strip())
        page = list(map(int, sys.stdin.readline().split()))
        func(k, page)

