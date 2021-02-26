import sys


def check_dist(mid):
    sc = house[0]
    distance = mid
    cont = 1
    for i in range(1, N):
        if sc + distance <= house[i]:
            cont += 1
            sc = house[i]
    return cont


def max_dist():
    house.sort()
    s = 1
    e = (house[-1] - house[0])//(C-1)
    while s <= e:
        mid = (s+e)//2
        if check_dist(mid) >= C:
            answer = mid
            s = mid + 1
        else:
            e = mid - 1
    return answer


if __name__ == "__main__":
    N, C = map(int, sys.stdin.readline().split())
    house = [int(sys.stdin.readline().strip()) for _ in range(N)]
    print(max_dist())

'''
문제를 이해할 필요가 있다. 


'''