import sys


def LCS(a, b):
    global current
    prev = [0]*len(a)               # prev = [0,0,0,0... len(a)개]
    for i, r in enumerate(a):        # a = ACAYKP, b = CAPCAK
        current = []
        for j, c in enumerate(b):
            if r == c:
                e = prev[j-1]+1 if i * j > 0 else 1
            else:
                e = max(prev[j] if i > 0 else 0, current[-1] if j > 0 else 0)
            current.append(e)
        prev = current
    return current[-1]


A_string = sys.stdin.readline().strip()
B_string = sys.stdin.readline().strip()

print(LCS(A_string, B_string))

'''
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP 와 CAPCAK 의 LCS는 ACAK 가 된다.

A_string=ACAYKP

B_string=CAPCAK

>> ACAK 

def lcs(a, b):
    prev = [0]*len(a)               # prev = [0,0,0,0... len(a)개]
    for i,r in enumerate(a):        # a = ACAYKP, b = CAPCAK
        current = []
        for j,c in enumerate(b):
            if r==c:
                e = prev[j-1]+1 if i * j > 0 else 1
            else:
                e = max(prev[j] if i > 0 else 0, current[-1] if j > 0 else 0)
            current.append(e)
        prev = current
    return current[-1]

 = [0,1,1,1,2,2]
 = [1,1,1,2,2,2]
 = [0,2,2,2,3,3]
 = [0,2,2,2,3,3]
prev = [0,2,2,2,3,4]
current = [0,2,3,3,3,4]

'''
