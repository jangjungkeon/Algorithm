import sys
sys.setrecursionlimit(10 ** 4)

def make_cabge(i, j):
    if type(cabge_pos_map[i][j]) == list:       # 검사했느냐의 의미인듯
        return

    cabge_pos_map[i][j] = []
    if cabge_pos[i][j] == 1:
        cabge_pos_map[i][j].append([i, j])

    # 상
    if i > 0 and cabge_pos[i][j] == 1 and cabge_pos[i-1][j] == 1:
        if type(cabge_pos_map[i-1][j]) != list:
            make_cabge(i-1, j)
        cabge_pos_map[i][j].append([i-1, j])

    # 하
    if i < N-1 and cabge_pos[i][j] == 1 and cabge_pos[i+1][j] == 1:
        if type(cabge_pos_map[i+1][j]) != list:
            make_cabge(i+1, j)
        cabge_pos_map[i][j].append([i+1, j])

    # 좌
    if j > 0 and cabge_pos[i][j] == 1 and cabge_pos[i][j-1] == 1:
        if type(cabge_pos_map[i][j-1]) != list:
            make_cabge(i, j-1)
        cabge_pos_map[i][j].append([i, j-1])

    # 우
    if j < M-1 and cabge_pos[i][j] == 1 and cabge_pos[i][j+1] == 1:
        if type(cabge_pos_map[i][j+1]) != list:
            make_cabge(i, j+1)
        cabge_pos_map[i][j].append([i, j+1])

    return


def bfs():
    check_visit = []
    tmp = 0

    for i in range(N):
        for j in range(M):
            q = []

            if cabge_pos_map[i][j] and [i, j] not in check_visit:   # 방문을 아직 하지 않았다면
                q.append([i, j])
                while q:
                    n = q.pop(0)
                    x = n[0]
                    y = n[1]
                    if n not in check_visit:
                        check_visit.append(n)
                        # 만일 연결된 간선이 있다면
                        if cabge_pos_map[x][y]:
                            for m in cabge_pos_map[x][y]:
                                if m not in check_visit:
                                    q.append(m)
                tmp += 1
    return print(tmp)


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().split())
        cabge_pos = [[0 for _ in range(M)] for _ in range(N)]
        for _ in range(K):
            x, y = map(int, sys.stdin.readline().split())
            cabge_pos[y][x] = 1

        cabge_pos_map = [[0 for _ in range(M)] for _ in range(N)]   # 초기화
        for i in range(N):
            for j in range(M):
                make_cabge(i, j)
        bfs()
