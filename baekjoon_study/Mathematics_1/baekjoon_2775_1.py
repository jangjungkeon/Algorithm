import sys

for _ in range(int(sys.stdin.readline().strip())):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())

    v = [i for i in range(1, n+1)]
    for _ in range(k):
        for j in range(1, n):
            # 핵심이 이 한 문장인데 이것을 생각하기는 너무 어렵다. 높은 경지에 올라야 할듯.
            v[j] += v[j-1]
    print(v[n-1])