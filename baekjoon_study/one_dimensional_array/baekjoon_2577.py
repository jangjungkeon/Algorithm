import sys      # 빠른 입력을 위한 모듈

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())
K = str(A*B*C)
for i in range(10):
    cont = 0
    for j in K:                # 문자열도 이터러블이다
        if j == str(i):         # 해당 문자가 쓰인 횟수 기록.
            cont += 1
        else:
            continue
    print(cont)                 # 해당 문자가 인 횟수 출력쓰

######################################################
import sys          # 빠른 입력을 위한 모듈

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())
K = str(A*B*C)

for i in range(10):
    print(K.count(str(i)))          # 해당문자를 세어주는 간단한 메서드