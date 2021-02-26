import sys


def spl_conq1(A, B, C):
    if B <= 2:
        return (A ** B) % C

    if B % 2 == 0:
        return spl_conq1(A, B // 2, C) ** 2 % C
    else:
        return ((spl_conq1(A, B // 2, C) ** 2) * A) % C


def spl_conq2(N, K):  # 1,000,000,007 로 나누기
    N_remain = 1
    K_remain = 1

    for i in range(1, N + 1):
        N_remain *= i
        N_remain %= p

    for j in range(1, K + 1):
        K_remain *= j
        K_remain %= p

    for k in range(1, N - K + 1):
        K_remain *= k
        K_remain %= p

    return (N_remain * spl_conq1(K_remain, p - 2, p)) % p


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    p = 1000000007
    print(spl_conq2(N, K))


'''
303317497

N,K > 100000007 보다 크게되면 다시 나눠라? 이게 가능한가? 
만일 이게 가능하다면 이 방법대로 하면 괜찮을 듯한대. 

이 방법에 대해서 고민해 보자. 

(N)!K! (N-K)!
 
 
페르마의 소정리를 활용.
nCk 와 나머지가 같은 수를 공식에서 찾아야겠다. 
NCK 에서 N봅다 작은 소수. 
5C2
2,3
a = 2
p = 3
2**2 % 3 = 1

p : 소수
a, p 는 서로소 

10C2 = 45
2, 3, 5, 7
a ** (p-1) % p = 1
소수를 찾기 
11 ** 6 % 7 = 1

nCk

n = 3
p = 5

4**5 % 5 = (3**5 + 1) % 5

p(p−1)⋯(p−n+1)
-----------------
​n(n−1)⋯1	



nk_part = solve(nk_part, p-2) % p

nk_part^(p-2) -> 분모 

'''
