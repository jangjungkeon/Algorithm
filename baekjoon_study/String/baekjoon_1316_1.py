import sys

cont = 0
T = int(sys.stdin.readline().strip())
for _ in range(T):
    string = sys.stdin.readline().strip()
    cont += list(string) == sorted(string, key=string.find)     # 맞으면 1
print(cont)