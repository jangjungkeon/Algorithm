'''
            (w,h)
      (x,y)
(0,0)
'''

import sys

x, y, w, h = map(int, sys.stdin.readline().split())

# 최솟값 찾기
min = 10000
# x 부터
if x <= min:
    min = x
if w-x <= min:
    min = w-x
if y <= min:
    min = y
if h-y <= min:
    min = h-y

print(min)