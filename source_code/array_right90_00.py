# 배열을 90도 오른쪽으로 돌리는 함수
# 180, 270도는 함수를 중복해서 활용하면 가능.
def right90(a, n):
    a_right90 = [[0 for i in range(n)] for j in range(n)]

    for row in range(n):
        for column in range(n):
            a_right90[row][column] = a[n - 1 - column][row]
    return a_right90


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(a)

print(right90(a, n))