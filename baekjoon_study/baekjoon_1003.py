import sys

T = int(sys.stdin.readline())

zero = [1,0,1]
one = [0,1,1]

def fibo(n):
    length = len(zero)
    if length <= n:
        for i in range(length, n+1):
            zero.append(zero[i-2] + zero[i-1])
            one.append(one[i-2] + one[i-1])
    print('%d %d' % (zero[n], one[n]))


for i in range(T):
    k = int(sys.stdin.readline())
    fibo(k)
