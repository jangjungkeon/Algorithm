import sys


def func():
    q = []
    global pos_a, mid
    for i in a:
        s = 0
        tmp = len(q)
        e = tmp - 1
        if not q:
            q.append(i)
            print(i)
            continue
        while s <= e:
            print(f"s:{s}, e:{e}")
            mid = (s + e) // 2
            if i >= q[mid]:
                s = mid + 1
            else:
                e = mid - 1
        print(f"mid : {mid}")
        pos_a = mid + 1 if i > q[mid] else mid
        q.insert(pos_a, i)
        print(q[tmp // 2]) if N % 2 else print(min(q[tmp // 2], q[(tmp // 2) + 1]))
        print(q)
    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    a = [int(sys.stdin.readline().strip()) for _ in range(N)]
    func()
