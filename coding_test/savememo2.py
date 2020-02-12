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
def key_expand(key):
    n = len(key)
    key_expand_array = [[0 for i in range(3 * n - 2)] for i in range(3 * n - 2)]

    for i in range(n):
        for j in range(n):
            key_expand_array[i + n - 1][j + n - 1] = key[i][j]

    # cut key_expand_array
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            print(key_expand_array[0])
    #print("자르기 : ", key_expand_array[0][0:3][0:3])
    #print(key_expand_array)
    return key_expand_array

key_expand(key)
# answer
def answer(lock):
    answer = lock
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 1:
                answer[i][j] = 0
            else:
                answer[i][j] = 1
    return answer


# compare key_expand with answer
def solution(key, lock):
    # 3회전 해보기
    answer_array = answer(lock)
    n = len(key)
    for _ in range(3):
        key = key_rotation(key)
        key_expand_array = key_expand(key)
        cnt = 0
        for i in range(2 * n - 1):
            for j in range(2 * n - 1):
                if key_expand_array[i:i+n][j:j+n] == answer_array:
                    return True
    return False


