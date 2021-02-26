import sys

N = list(sys.stdin.readline().strip())

print(int("".join(sorted(N, reverse=True))))