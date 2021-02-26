import sys          # 빠른 입력을 위한 모듈

# 입력 받기
S = sys.stdin.readline().strip()
Alphabet = 'abcdefghijklmnopqrstuvwxyz'


for i in Alphabet:      #  i = 'a' or 'b'
    if i == 'z':            # 마지막 % 기호를 없애기 위해서
        print(S.find(i))
        continue            # continue 를 하지 않으면 아래 print가 한번 더됨
    print(S.find(i), end=" ")      # find 로 기호 찾고, end로 공백 추가
