import sys


def check(N, a, b):
    global cont_b, cont_w
    tmp = board[a][b]
    for i in range(a, a + N):
        for j in range(b, b + N):
            if board[i][j] != tmp:
                return False        # 거짓이라는 얘기는 쪼갤 수 있다는 얘기
    if board[a][b]:
        cont_b += 1
    else:
        cont_w += 1
    return True


def cut(N, a, b):
    global cont_b, cont_w
    if N == 1:
        if board[a][b]:
            cont_b += 1
        else:
            cont_w += 1
        return

    if not check(N, a, b):
        cut(N // 2, a, b)
        cut(N // 2, a, b + N // 2)
        cut(N // 2, a + N // 2, b)
        cut(N // 2, a + N // 2, b + N // 2)

    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]   # 각 요소의 타입은 문자이다.
    cont_b = 0
    cont_w = 0
    cut(N, 0, 0)
    print(cont_w)
    print(cont_b)




'''
결국 관건은 쪼갤 수 있느냐의 여부를 확실히 아는 것이 가장 중요한 방법이었다. 
N -> N/2 -> (N/2)/2 -> ...
for i in range(N/2)
1차 2차 3차 

cut(N, 0, 0)
def cut(N, s, e):
    
    # 탈출문 
    if N == 1:
        for i in range(s, s+2)
            for j in range(e, e+2)
                if board[i][j] == "1"
                    cont_b += 1
                else:
                    cont_w += 1
        return 
        
    1사분면 
    sum_1 = 0
    b1 = board[s][e+N//2]
    for i in range(s, s + N//2)
        for j in range(e + N//2,e + N)
            sum_1 += b1
            if i != 0 and j != N//2 and b1 != board[i][j]:
                cut((N//2)//2, 0, N//2)
    if sum_1 == N**2:
        cont_b += 1
    if sum_1 == 0:
        cont_w += 1
    sum_1 = 0
        
    2사분면
    sum_2 = 0
    b2 = board[0][0]
    for i in range(N//2)
        for j in range(N//2)
        sum_2 += b2
        if i != 0 and j != 0 and b2 != board[i][j]:
            cut((N//2)//2, b2)
        
    3사분면 
    for i in range(N//2, N)
        for j in range(N//2)
        
    4사분면
    for i in range(N//2, N)
        for j in range(N//2, N)
    
    return
'''

'''
(a,b) 
1사분면 : (a,b+N//2)
2사분면 : (a,b)
3사분면 : (a+N//2,b)
4사분면 : (a+N//2,b+N//2)

def check(a,b,n):
    tmp = board[a][b]
    for i in range(a, a + N//2)
        for j in range(b, b + N//2)
            if board[i][j] != tmp:
                return False        거짓이라는 얘기는 쪼갤 수 있다는 얘기
    if tmp == "1":
            cont_b += 1
        else:
            cont_w += 1
    return True         
1사분면
    if not check(a,b+N//2,1):
        cut(N//2, a,b+N//2)

2사분면
    if not check(a,b,2):
        cut(N//2, a, b)
        
3사분면
    if not check(a+N//2,b,3):
        cut(N//2, a, b)


4사분면
    if not check(a+N//2,b+N//2,4):
        cut(N//2, a+N//2, b+N//2)

                       
'''


'''
for i in range(N/2)
1차 2차 3차 

cut(N)
def cut(N, s, e):
    if N == 1:
    
        return
    for i in range(N):
        
'''

'''
# 1사분면
    if not check(N, a, b + N // 2):
        cut(N // 2, a, b + N // 2)

    # 2사분면
    if not check(N, a, b):
        cut(N // 2, a, b)

    # 3사분면
    if not check(N, a + N // 2, b):
        cut(N // 2, a + N // 2, b)

    # 4사분면
    if not check(N, a + N // 2, b + N // 2):
        cut(N // 2, a + N // 2, b + N // 2)
'''
