import sys

N, K = map(int, sys.stdin.readline().split())

coin = [int(sys.stdin.readline().strip()) for _ in range(N)]

coin_cont = 0

for i in sorted(coin, reverse=True):
    if K >= i:  # 나눌 수 있다.
        quotient = (K // i)
        K %= i
        coin_cont += quotient

print(coin_cont)



'''

for i in sorted(coin, reverse=True):
    if K >= i:   # 나눌 수 있다.
        K - (K//i) * i 
        coin_cont += K//i


'''

