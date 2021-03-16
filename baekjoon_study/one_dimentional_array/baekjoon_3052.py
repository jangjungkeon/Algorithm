import sys  # 빠른 입력을 위한 모듈

list = []
for _ in range(10):             # 10 번 루프 돌리기
    i = int(sys.stdin.readline().strip())       # 입력값 받기
    list.append(i % 42)                         # 나머지 구하기.

print(len(set(list)))           # 겹치는게 몇개인지 세어보기.