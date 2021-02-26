import sys

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
string = sys.stdin.readline().strip()
ret = 0
for i in range(len(string)):            # cpu 는 많이 쓰지만 메모리를 적게 쓰니깐 괜찮은 코드.
    for j in dial:
        if string[i] in j:
            ret += dial.index(j) + 3

print(ret)
