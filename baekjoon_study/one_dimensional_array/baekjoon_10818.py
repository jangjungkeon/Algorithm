import sys  # 빠른 입력을 위한 모듈

N = int(sys.stdin.readline().strip())       # N 받기
List = list(map(int, sys.stdin.readline().split()))     # N개의 값들 리스트로 받고 map으로 int로 변환후 list

print(min(List), end=' ')      # 공백을 뒤에 넣기.
print(max(List))