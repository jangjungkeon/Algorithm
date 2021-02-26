import sys


def cal(a,b):
    global cont_1, cont_0, cont_m1
    if board[a][b] == 1:
        cont_1 += 1
    elif board[a][b] == 0:
        cont_0 += 1
    else:
        cont_m1 += 1
    return


def check(N,a,b):
    tmp = board[a][b]
    for i in range(a, a + N):
        for j in range(b, b + N):
            if tmp != board[i][j]:
                return False

    return True


def quad_tree(N,a,b):
    global cont_1, cont_0, cont_m1
    if N == 1:
        cal(a, b)
        return

    if not check(N,a,b):
        quad_tree(N // 3, a, b)
        quad_tree(N // 3, a, b+N//3)
        quad_tree(N // 3, a, b+(N//3)*2)
        quad_tree(N // 3, a+N//3, b)
        quad_tree(N // 3, a+N//3, b+N//3)
        quad_tree(N // 3, a+N//3, b+(N//3)*2)
        quad_tree(N // 3, a + (N//3)*2, b)
        quad_tree(N // 3, a + (N//3)*2, b+N//3)
        quad_tree(N // 3, a + (N//3)*2, b+(N//3)*2)
    else:
        cal(a, b)

    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    cont_m1= 0
    cont_1 = 0
    cont_0 = 0
    quad_tree(N,0,0)
    print(cont_m1)
    print(cont_0)
    print(cont_1)


'''
9개

a,b
a,b+N//3
a,b+(N//3)*2
a+N//3, b
a+N//3,b+N//3
a+N//3,b+(N//3)*2
a + (N//3)*2, b
a + (N//3)*2, b+N//3
a + (N//3)*2, b+N//3*2



'''