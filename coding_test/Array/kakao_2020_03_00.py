key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# key_rotation
def key_rotation(key):
    n = len(key)
    key_right90 = [[0 for i in range(n)] for i in range(n)]
    for row in range(n):
        for column in range(n):
            key_right90[row][column] = key[n - 1 - column][row]
    return key_right90

# key_expand
def lock_expand(lock):
    n = len(lock)
    lock_expand_array = [[0 for _ in range(3 * n)] for _ in range(3 * n)]

    for i in range(n):
        for j in range(n):
            lock_expand_array[i + n][j + n] = lock[i][j]

    return lock_expand_array


# compare key_expand with answer
def solution(key, lock):
    # 3회전 해보기
    n = len(lock)
    m = len(key)
    answer = [[1 for _ in range(len(lock))] for _ in range(len(lock))]

    for _ in range(4):
        key = key_rotation(key)
        for i in range(3 * n - 2):
            for j in range(3 * n - 2):
                # 이 부분을 고치고 싶은데. 어떻게 해야할지 잘 모르겠다.
                # tmp = lock_expand_array 이렇게 처음에 썼는데 잘 안되드라. 왜그런지 잘 모르겠어
                # 자꾸 lock_expand_array 값이 중복되어...
                tmp = lock_expand(lock)
                tmp_2 = []
                for k in range(m):
                    for u in range(m):
                        tmp[i + k][j + u] += key[k][u]

                for v in range(n):
                    tmp_2.append(tmp[v + n][n:2 * n])

                if tmp_2 == answer:
                    return True

    return False


print(solution(key, lock))