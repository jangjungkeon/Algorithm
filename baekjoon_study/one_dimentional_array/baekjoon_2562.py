import sys      # 빠른 입력을 위한 모듈

List = []
for i in range(1, 10):
    List.append((int(sys.stdin.readline().strip())))

Max_num = max(List)
print(Max_num)
Max_pos = List.index(Max_num)      # 인덱스 함수로 max 위치 찾기. cf) find 함수는 문자열 특화임.
print(Max_pos + 1)

