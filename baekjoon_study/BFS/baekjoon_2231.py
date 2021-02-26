import sys

# 가장 작은 생성자를 구하라.
# 그러면 생성자는 무엇인가? 분해합으로 탄생된 수의 요소들.

N = int(sys.stdin.readline().strip())
solution = []
# 101*a + 11*b + 2*c = N
for i in range(10):
    for j in range(10):
        for k in range(10):
            for m in range(10):
                for n in range(10):
                    for l in range(10):
                        if 100001*i + 10001*j + 1001*k + 101*m + 11*n + 2*l == N:
                            solution.append(100000*i + 10000*j + 1000*k + 100*m + 10*n + l)

if not solution:
    print(0)
else:
    print(min(solution))


'''
N의 가장 작은 생성자 
N의 가장 작은 생성자. 

256의 생성자 : 245(245 + 2 + 4 + 5)

216
1+9+8+ 198

9*6 -> 3자리가 안됨
1~2자리 

N + () = 

1. N의 생성자를 모두 확인 --> 작업시작
N의 생성자를 어떻게 구하지. 
N = 216
a+b+c+a*100+b*10+c = 216
101*a + 11*b + 2*c = N 
1000000
abcdef

인 abc 를 찾아라. 

2. 그중에서 가장 작은 수 확인. 


'''