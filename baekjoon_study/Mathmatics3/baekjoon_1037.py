import sys


def math(divisor):
    divisor.sort()
    return divisor[0] * divisor[-1]


if __name__ == "__main__":
    N = sys.stdin.readline().strip()
    divisor = list(map(int, sys.stdin.readline().split()))
    print(math(divisor))

'''
약수 중에 1과 자기자신을 제외한 약수들.
약수의 개수 
1,2,4,8

9
1 3 9

16
1 2 4 8 16

20
1 2 4 5 10 20

12
1 2 3 4 6 12

15
1 3 5 15

22
1 2 11 22

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
'''