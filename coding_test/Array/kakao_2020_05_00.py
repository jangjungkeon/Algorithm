def solution(n, build_frame):
    map = [[0 for _ in range(n)] for _ in range(n)]
    for i in build_frame:
        x = i[0]; y = i[1]; a = i[2]; b = i[3]
        if b == 0:
            if map[x][y] > 0:
                map[x][y] = 0
        else: # b = 1, do construct
            if map[x][y] > 0:
                continue
            else:
                if a == 0:   # Pillar
                   # 바닥위 or 보의 한쪽끝 또는 다른 기둥
                    if y == 0:
                        map[x][y] = 1
                    if x == 0:
                        if map[x][y - 1] == 1:
                            map[x][y] = 1
                    else:
                        if map[x][y - 1] == 1 or map[x - 1][y] == 2:
                            map[x][y] = 1
                else:   # beam
                    if y == 0:
                        continue
                    if map[x][y - 1] == 1:  # 한쪽 끝 부분이 기둥 위
                        map[x][y] = 2
                    if x = 0:
                    if map[x - 1][y] == 2 and map[x + 1][y] == 2:  # 양쪽 끝부분이 다른 보와 연결
                        map[x][y] = 2

def __getitem__():

# map[x][y] = 0 : 아무것도 없음
# map[x][y] = 1 : 기둥이 존재
# map[x][y] = 2 : 보가 존재


    # sorting
    pass

build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
               [5, 0, 0, 1], [5, 1, 0, 1], {4, 2, 1, 1}, [3, 2, 1, 1]]
n = 5

solution(n, build_frame)