import sys


def greedy(mt_time):
    cont = 0
    end = 0
    mt_time.sort(key=lambda x: x[0])
    mt_time.sort(key=lambda x: x[1])

    for i in mt_time:
        if i[0] >= end:
            end = i[1]
            cont += 1

    return cont


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    mt_time = []
    for _ in range(N):
        i, j = map(int, sys.stdin.readline().split())
        mt_time.append((i, j))

    print(greedy(mt_time))


'''
빨리 끝나는 회의 순서대로 정렬할 필요가 있다. 
빨리 끝날 수록 뒤에서 고려해볼 회의가 많기 때문에. 
'''