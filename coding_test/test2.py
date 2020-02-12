lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

answer = [[1 for _ in range(len(lock))] for _ in range(len(lock))]

for i in range(len(lock)):
    for j in range(len(lock)):
        print(answer[i][j])
        print(answer)
