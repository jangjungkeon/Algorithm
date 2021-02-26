import sys

M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
prime_num = []

for i in range(M, N+1):
    cont = 0
    # 소수 체크하기
    for j in range(1, i+1):
        if i % j == 0:
            cont += 1
    if cont == 2:
        prime_num.append(i)
# 만일 소수가 없을 때
if prime_num == []:
    print(-1)
    exit()
else:
    print((sum(prime_num)))
    print(prime_num[0])