import sys

T = int(sys.stdin.readline().strip())
cont = 0
break_com = 0
for _ in range(T):
    string = sys.stdin.readline().strip()
    for i in range(len(string)):        # 하나씩 검사할 때, range() 로 검사하는 것이 유용.
        str_cont = string.count(string[i])      # 겹치는 문자의 갯수
        if i == len(string) - 1:        # 마지막 루프라면 ok
            cont += 1
            break
        if str_cont != 1:         # 중복되는 숫자가 있다면
            start = string.find(string[i])      # 시작 aaa 의 맨앞
            end = string.rfind(string[i])       # 끝 aaa 의 맨 끝
            for j in string[start:end + 1]:    # string[start:end]
                if string[i] != j:
                    break_com = 1
                    break
            if break_com == 1:
                break_com = 0
                break
        else:
            continue
print(cont)