import sys      # 빠른 입력을 위한 모듈

num_N = int(sys.stdin.readline().strip())

# 인트로 mapping 후 리스트로 바꾸고 합하기
print(sum(list(map(int, sys.stdin.readline().strip()))))        # strip 을 쓰는 것을 생활화하자.
