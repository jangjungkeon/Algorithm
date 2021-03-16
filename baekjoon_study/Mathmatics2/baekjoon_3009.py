import sys

'''
1. 수학적으로 점을 확인하는 방법
2. 코드를 통해 확인하는 방법
둘 중 빠른 것을 해보자. 
'''

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
e, f = map(int, sys.stdin.readline().split())

# 가장 긴변 구하기
line_1 = (a-c)**2 + (b-d)**2
line_2 = (a-e)**2 + (b-f)**2
line_3 = (c-e)**2 + (d-f)**2
if line_1 > line_2 and line_1 > line_3:
    # line 1이 가장 김 (e,f)
    print(f"{a+c - e} {b+d - f}")
    exit()
if line_2 > line_1 and line_2 > line_3:
    # line 2이 가장 김 (c,d)
    print(f"{a + e - c} {b + f - d}")
    exit()
if line_3 > line_1 and line_3 > line_2:
    # line 3이 가장 김 (a,b)
    print(f"{e + c - a} {d + f - b}")
    exit()