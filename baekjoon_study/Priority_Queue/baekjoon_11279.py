import sys


def priority_q(a):
    # a = [1,2,4,3]
    global pos_a
    for i in a:
        if i == 0:
            # 가장 큰 값을 출력하고, 그값을 배열에서 제거.
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
                mid = (s+e) // 2
                if s <= e:
                    if i >= q[s]:
                        pos_a = s+1
                    else:
                        pos_a = s
                    break
                if i >= q[mid]:
                    s = mid + 1
                else:
                    e = mid - 1
            q.insert(pos_a, i)
    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    x = [int(sys.stdin.readline().strip()) for _ in range(N)]
    q = []
    priority_q(x)

