import sys

N = sys.stdin.readline().split()
print(max(int(N[0][::-1]), int(N[1][::-1])))