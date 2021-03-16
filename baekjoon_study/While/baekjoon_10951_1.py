import sys

for line in sys.stdin:
    A, B = map(int, line.split())
    print(A + B)


#########################################
# 예외처리 구문 try, except
while True:
    try:        # 평소와같은 코드 입력.
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:     # 예외(에러)가 나면 break 해라.
        break

#########################################

try:
    while 1:
        a, b = map(int, sys.stdin.readline().split())
        print((a+b))
except:
    exit()