import sys


def make_grape(i, j):
    if type(house_map[i][j]) == list:       # 검사했느냐의 의미인듯
        return

    house_map[i][j] = []
    if house[i][j] == 1:
        house_map[i][j].append([i, j])

    # 상
    if i > 0 and house[i][j] == 1 and house[i-1][j] == 1:
        if type(house_map[i-1][j]) != list:
            make_grape(i-1, j)
        house_map[i][j].append([i-1, j])

    # 하
    if i < N-1 and house[i][j] == 1 and house[i+1][j] == 1:
        if type(house_map[i+1][j]) != list:
            make_grape(i+1, j)
        house_map[i][j].append([i+1, j])

    # 좌
    if j > 0 and house[i][j] == 1 and house[i][j-1] == 1:
        if type(house_map[i][j-1]) != list:
            make_grape(i, j-1)
        house_map[i][j].append([i, j-1])

    # 우
    if j < N-1 and house[i][j] == 1 and house[i][j+1] == 1:
        if type(house_map[i][j+1]) != list:
            make_grape(i, j+1)
        house_map[i][j].append([i, j+1])

    return


def bfs():
    check_visit = []
    result = []

    for i in range(N):
        for j in range(N):
            q = []
            tmp = 0
            if house_map[i][j] and [i, j] not in check_visit:
                q.append([i, j])
                while q:
                    n = q.pop(0)
                    x = n[0]
                    y = n[1]
                    if n not in check_visit:
                        check_visit.append(n)
                        tmp += 1
                        # 만일 연결된 간선이 있다면
                        if house_map[x][y]:
                            for m in house_map[x][y]:
                                if m not in check_visit:
                                    q.append(m)
                result.append(tmp)
    print(len(result))
    for sol in sorted(result):
        print(sol)
    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    house = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    house_map = [[0 for _ in range(N)] for _ in range(N)]   # 초기화 작업
    for i in range(N):
        for j in range(N):
            make_grape(i, j)
    bfs()
