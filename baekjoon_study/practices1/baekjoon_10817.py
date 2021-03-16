import sys      # 빠른 입력을 위한 모듈

input_list = sys.stdin.readline().split()
input_list[0] = int(input_list[0])
input_list[1] = int(input_list[1])
input_list[2] = int(input_list[2])
input_list.sort()                       # 정렬, sorted()는 정렬된 리스트를 반환

print(input_list[1])

