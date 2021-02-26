import sys
import time


def cut_tree(height):
    cutted_tree = 0
    for i in tree_height:
        if i > height:
            cutted_tree += i - height
    return cutted_tree


def max_height(M):
    s = 0
    e = max(tree_height)
    mid = (s+e)//2
    while True:
        if cut_tree(mid) < M:
            e = mid
        else:
            s = mid
        mid = (s + e) // 2
        if s == mid:
            if cut_tree(mid+1) >= M:
                return mid + 1
            return mid


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    tree_height = list(map(int, sys.stdin.readline().split()))
    start = time.time()
    print(max_height(M))
    end = time.time() - start
    print(f"실행시간 : {end}")

'''
실행시간 : 0.0001590251922607422

'''