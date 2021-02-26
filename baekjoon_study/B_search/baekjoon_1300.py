import sys


def check_fun(mid):
    tmp = 0
    for i in range(1, N + 1):
        tmp += min(mid // i, N)
    return tmp


def func():
    global answer
    s = 1
    e = N*N
    while s <= e:
        mid = (s+e) // 2
        if check_fun(mid) >= k:
            answer = mid
            e = mid - 1
        else:
            s = mid + 1
    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())
    print(func())


'''
    for i in range(1, N+1):
        for j in range(1, N+1):
            A[i][j] = i * j
            B.append(i * j)
            
이것을 다 계산하는 것은 실질적으로 말이 안됨. 그러면? 

갯수 

'''