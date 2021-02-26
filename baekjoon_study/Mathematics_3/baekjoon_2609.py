import collections
import sys


def divisor(A):
    divisor_list = []
    if A == 1:
        return {1:1}

    for i in range(2, A + 1):
        while A % i == 0:
            divisor_list.append(i)
            A /= i
            if A == 1:
                return collections.Counter(divisor_list)


def math(divisor_a, divisor_b):
    sum_gcd = 1
    sum_lcm = 1
    for i in divisor_a:
        if i in divisor_b:
            sum_lcm *= i**(max(divisor_a[i], divisor_b[i]))
            sum_gcd *= i**(min(divisor_a[i], divisor_b[i]))
        else:
            sum_lcm *= i**divisor_a[i]

    for i in divisor_b:
        if i not in divisor_a:
            sum_lcm *= i**divisor_b[i]
    print(sum_gcd)
    print(sum_lcm)
    return


if __name__ == "__main__":
    A, B = map(int, sys.stdin.readline().split())
    divisor_a = divisor(A)
    divisor_b = divisor(B)
    math(divisor_a, divisor_b)

'''
첫줄에 최대 공약수 : 약수들 중에 겹치는 수중 가장 큰 수.
둘째 줄에 최소 공배수 : 소인수 

10 20
24 18
24 : 2223
18 : 233
긱 수의 소인수 리스트를 구한 후

하나씩 비교해가는 것. 

def math(divisor_a, divisor_b):
    sum_gcd = 0
    sum_lcd = 0
    gcd = {}  
    lcm = {}  
    for i in divisor_a:
        if i in divisor_b:
            lcm[i] = max(divisor_a[i],divisor_b[i])
            gcd[i] = min(divisor_a[i],divisor_b[i])
        else:
            lcm[i] = divisor_a[i]
    
    for i in divisor_b:
        if not i in lcm:
            lcm[i] = divisor_b[i]
    
    for i in gcd:
        sum_gcd += i**gcd[i]
    
    for i in lcm:
        sum_lcm += i**lcm[i]
        
    print(gcd)
    print(lcm)
    return 

자체를 합치는 것도 방법일 숭 ㅣㅆ음 리스트를 합쳐서.
 

'''
