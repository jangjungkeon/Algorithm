import sys

N = int(sys.stdin.readline().strip())
title = '666'
while N:
    if '666' in title:
        N -= 1
    title = str(int(title) + 1)

print(int(title) - 1)