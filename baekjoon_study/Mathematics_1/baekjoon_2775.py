import sys

# 2차원 배열 만들기
a = [[0 for _ in range(15)] for _ in range(15)]
for j in range(15):
    a[0][j] = j

# 규칙은 데이터를 테이블화 시켜서 파악.
for o in range(1, 15):
    for p in range(1, 15):
        a[o][p] = a[o-1][p] + a[o][p-1]

T = int(sys.stdin.readline().strip())
num = []
for _ in range(2*T):
    num.append(sys.stdin.readline().strip())

# k층, n호 값 찾기
for i in range(0, len(num), 2):
    k, n = int(num[i]), int(num[i+1])
    print(a[k][n])


'''
a = [j for j in range(1, n+1)]
for l in range(1, n+1):
    a[] = a[l] + a[l-1]
    
n,k = 14개, 14개 // a[k][n]
a[1][1] = a[0][1] + a[1][0] 
a[1][2] = a[0][2] + a[1][1] 
a[1][3] = a[0][3] + a[1][2] 
a[2][1] = a[1][1] + a[2][0] 
a[2][2] = a[1][2] + a[2][1]  
a[2][3] = a[1][3] + a[2][2]
a[3][1] = a[2][1] + a[3][0]
a[3][2] = a[2][2] + a[3][1]
a[3][3] = a[2][3] + a[3][2]

a = 15 x 15 [0]으로 채우기 + a[0][0~14] = i

 
'''

## 2차원 배열 : [[0 for i in range(n)] for j in range(k)]

