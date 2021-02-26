def check_match(key, lock):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if key[i][j] + lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)

    key_right0 = [[0 for _ in range(n)] for _ in range(n)]
    key_right90 = [[0 for _ in range(n)] for _ in range(n)]
    key_right180 = [[0 for _ in range(n)] for _ in range(n)]
    key_right270 = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(m):
        for j in range(m):
            key_right0[i][j] = key[i][j]
            key_right90[i][j] = key[m-1-j][i]
            key_right180[i][j] = key[m-1-i][m-1-j]
            key_right270[i][j] = key[j][m-1-i]

    for key in [key_right0, key_right90, key_right180, key_right270]:
        for i in range(n):
            for j in range(n):
                left_up_key = [row[i:] + [0]*i for row in key[j:]] + [[0] * n]*j
                if check_match(left_up_key, lock):
                    return True
                left_down_key = [[0] * n] * j + [row[i:] + [0]*i for row in key[:n-j]]
                if check_match(left_down_key, lock):
                    return True
                right_up_key = [[0] * i + row[:n-i] for row in key[j:]] + [[0] * n]*j
                if check_match(right_up_key, lock):
                    return True
                right_down_key = [[0] * n] * j + [[0] * i + row[:n-i] for row in key[:n-j]]
                if check_match(right_down_key, lock):
                    return True
    return False