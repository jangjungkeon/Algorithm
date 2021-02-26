import sys


def greedy(String):
    sum_val = 0
    for i in range(len(String)):
        tmp = sum(map(int, String[i].split('+')))
        if i == 0:
            sum_val += tmp
        else:
            sum_val -= tmp
    return sum_val


if __name__ == "__main__":
    String = sys.stdin.readline().split('-')
    print(greedy(String))
