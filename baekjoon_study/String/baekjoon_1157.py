import sys
import collections

S = sys.stdin.readline().strip().lower()
C = collections.Counter(S)      # C 에 문자의 요소와 갯수를 쌍으로 하는 딕셔너리를 생
test = C.most_common(2)         # 생성된 딕셔너리에서 요소의 갯수 값이 가장 큰 2개를 출력
if len(test) == 1:              # 그런데 요소가 1개면 그냥 출력
    print(test[0][0].upper())   # 대문자 잊지말고
    exit()                      # 프로그램 종료.
else:
    if test[0][1] == test[1][1]:
        print('?')
    else:
        print(test[0][0].upper())