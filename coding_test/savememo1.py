p = "()))((()"

def check(p):
    l = 0
    for i in p:
        if i == '(':
            l += 1
        else:
            l -= 1
            if l < 0:
                return False
    return l == 0


def seperate(p):
    l = r = 0
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        else:
            r += 1
        if l > 0 and l == r:
            return p[:i+1], p[i+1:]


def solution(p):
    print(1)
    # 재귀함수의 종료 조건
    if p == '':
        return p
    u, v = seperate(p)
    if check(u):
        #print(u + solution(v))
        return u + solution(v)
    return f"({solution(v)}){''.join([i == ')' and '(' or ')' for i in u[1:-1]])}"

solution(p)