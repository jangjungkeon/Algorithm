s = 'aaaavvdadfsfweqerrrrebbaccc'
N = len(s)
s_list = list(s)
s_list_split = []
count = 0
temp = []
result = []


def solution(s):
    sum_list = []
    count_sol = 1
    for i in range(len(s)):
        if i == len(s) - 1:
            if count_sol == 1:
                sum_list.append(s_list[i])
                break
            if count > 1:
                a = str(count_sol) + s_list[i]
                sum_list.append(a)
                count_sol = 1
                break
        if count_sol == 1:
            if s_list[i] != s_list[i + 1]:
                sum_list.append(s_list[i])
            else:
                count_sol += 1
                continue

        if count_sol > 1:
            if s_list[i] != s_list[i + 1]:
                a = str(count_sol) + s_list[i]
                sum_list.append(a)
                count_sol = 1
            else:
                count_sol += 1

    # 문자열을 N/2개로 나누기
    # 나누어진 문자열을 함수로 돌려 길이 확인하기
    # min 값으로 가장 작은 값 리턴하기


for i in range(1, int(N / 2) + 1):
    count = 0
    for j in s_list:
        count += 1
        temp.append(j)
        # i번째 요소까지 합쳐
        temp = ["".join(temp)]
        if count % i == 0 or count == N:
            s_list_split.append(temp[0])
            temp = []
    print(s_list_split)
    s_list_split = []

    result.append(solution(s_list_split))
    print(s_list_split)
    s_list_split = []
print(result)










