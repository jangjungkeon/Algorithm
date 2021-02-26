import sys  # 빠른 입출력을 위한
sum = 0
for _ in range(5):
    score = int(sys.stdin.readline())
    if score < 40:
        score = 40
    sum += score

print(int(sum/5))
