import sys


def sort():
    q = []
    global pos_a, mid
    for i in a:
        if i == 0:
            if len(q) == 0:
                print(0)
                continue
            else:
                print(q.pop())
                continue
        else:
            s = 0
            e = len(q) - 1
            if e == -1:
                q.append(i)
                continue
            while s <= e:
                mid = (s + e) // 2
                if abs(i) < abs(q[mid]):
                    s = mid + 1
                elif abs(i) == abs(q[mid]):
                    if i > q[mid]:
                        e = mid - 1
                    else:
                        s = mid + 1
                else:
                    e = mid - 1

            if abs(i) <= abs(q[mid]) and i < abs(q[mid]):
                pos_a = mid + 1
            else:
                pos_a = mid
            q.insert(pos_a, i)
    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    a = [int(sys.stdin.readline().strip()) for _ in range(N)]
    sort()


#########################
# 위의 코드는 아래의 코드를 리펙토링한 코드. 정확히 마지막 하나의 값을 선택. 양 옆 두개의 위치를 파악해야.
# 아래의 코드는 맨 처음 성공한 코드. 마지막 2개의 값을 선택. 그 사이 3개 안에 위치를 파악해야

#########################
import sys


def sort():
    q = []
    global pos_a
    for i in a:
        if i == 0:
            if len(q) == 0:
                print(0)
                continue
            else:
                print(q.pop())
                continue
        else:
            s = 0
            e = len(q) - 1
            if e == -1:
                q.append(i)
                continue
            while True:
                mid = (s + e) // 2
                if s == mid:
                    if abs(i) <= abs(q[e]) and i < abs(q[e]):
                        pos_a = e + 1
                    elif abs(i) <= abs(q[mid]) and i < abs(q[mid]):
                        pos_a = mid + 1
                    else:
                        pos_a = mid
                    break
                if abs(i) < abs(q[mid]):
                    s = mid
                elif abs(i) == abs(q[mid]):
                    if i > q[mid]:
                        e = mid
                    else:
                        s = mid
                else:
                    e = mid
            q.insert(pos_a, i)
    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    a = [int(sys.stdin.readline().strip()) for _ in range(N)]
    sort()


