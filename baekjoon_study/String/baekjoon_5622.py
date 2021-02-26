import sys

str_num = sys.stdin.readline().strip()

# 각 문자가 몇초가 걸리는지
table = {'A': 3, 'B': 3, 'C': 3, 'D': 4, 'E': 4, 'F': 4, 'G': 5, 'H': 5, 'I': 5,
         'J': 6, 'K': 6, 'L': 6, 'M': 7, 'N': 7,
         'O': 7, 'P': 8, 'Q': 8, 'R': 8, 'S': 8, 'T': 9,
         'U': 9, 'V': 9, 'W': 10, 'X': 10, 'Y': 10,
         'Z': 10}

# 할머니의 문자를 초로 치환
time = 0
for i in str_num:
    time += table[i]
print(time)


