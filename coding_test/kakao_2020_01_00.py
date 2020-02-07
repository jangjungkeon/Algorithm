s = 'xababcdcdababcdcd'
N = len(s)
s_list = list(s)
s_list_split = []
count = 0
temp = []
result = []

def solution(s):
    sum_list = []
    count_sol = 1
    if len(s) == 1:
        return s

    for i in range(len(s)):
        if i == len(s) - 1:
            if count_sol == 1:
                sum_list.append(s[i])
                break
            if count_sol > 1:
                a = str(count_sol) + s[i]
                sum_list.append(a)
                break
        if count_sol == 1:
            if s[i] != s[i + 1]:
                sum_list.append(s[i])
            else:
                count_sol += 1
                continue

        if count_sol > 1:
            if s[i] != s[i + 1]:
                a = str(count_sol) + s[i]
                sum_list.append(a)
                count_sol = 1
            else:
                count_sol += 1
    return "".join(sum_list)

    # 문자열을 N/2개로 나누기
    # 나누어진 문자열을 함수로 돌려 길이 확인하기
    # min 값으로 가장 작은 값 리턴하기




if __name__ == "__main__":
    for i in range(1, int(N / 2) + 1):  # i 를 1부터 하고 싶으면 range(a,b) 에서 a와 b에 1씩 추가하면 된다.
        count = 0
        for j in s_list:
            count += 1  # 아 인덱싱하는 방법이구나.
            temp.append(j)
            # i번째 요소까지 합쳐
            temp = ["".join(temp)]
            if count % i == 0 or count == N:
                s_list_split.append(temp[0])
                temp = []  # temp는 한번하고 초기화하는 것이 중요. -> 왜냐면 기본이니깐 중요하지.
        result.append(len(solution(s_list_split)))
        s_list_split = []

    print('result = ', min(result))

'''
# count를 없애고 enumerate 버전. 
for i in range(1, int(N / 2) + 1):  
    for j in enumerate(s_list, start=1):    
        temp.append(j[1])
        # i번째 요소까지 합쳐
        temp = ["".join(temp)]
        if j[0] % i == 0 or j[0] == N:
            s_list_split.append(temp[0])
            temp = []       # temp는 한번하고 초기화하는 것이 중요.
    result.append(len(solution(s_list_split)))
    s_list_split = []

'''
