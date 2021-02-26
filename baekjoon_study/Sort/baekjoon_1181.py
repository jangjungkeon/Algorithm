import sys


N = int(sys.stdin.readline().strip())

# 문자열을 입력받이 리스트로 저장. input_list = ['문자열', '문자열', ...]
input_list = [sys.stdin.readline().strip() for _ in range(N)]

# 중복을 제거(set) +
# 사전순으로 먼저 정렬 + 길이순으로 정렬
input_list = sorted(list(set(input_list)))

# 출력
for i in sorted(input_list, key=len):
    print(i)
