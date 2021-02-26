import sys


def check(n, a, b):
    tmp = board[a][b]
    for i in range(a, a + n):
        for j in range(b, b + n):
            if tmp != board[i][j]:
                return False
    # 다 같다면?
    return True


def quad_tree(n, a, b):
    sol = []
    if n == 1:
        return board[a][b]

    if not check(n, a, b):      # 쪼갤 수 있다면
        sol.append("(")
        sol.append(quad_tree(n // 2, a, b))
        sol.append(quad_tree(n // 2, a, b + n // 2))
        sol.append(quad_tree(n // 2, a + n // 2, b))
        sol.append(quad_tree(n // 2, a + n // 2, b + n // 2))
        sol.append(")")
    else:
        sol.append(board[a][b])

    return "".join(map(str, sol))


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    board = [list(map(int, sys.stdin.readline().strip()))for _ in range(N)]
    print(quad_tree(N, 0, 0))

'''
쿼드트리 
쪼갤수 있는지 확인
쪼갤수 있따면 쪼개고 
쪼갬의 끝 = 모두가 1 or 0일 때 

쪼개지면 () 추가?
sol.insert(0,"(")
sol.insert(-1,")")
(0000)
(0(0011)(0(0111)01)1)
0 (0011) ()
() 
'''