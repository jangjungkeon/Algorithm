result = []
result = set(result)        # result 를 집합으로 만들어보리기.
for i in range(1, 10001):
    if i not in result:         # 집합에 i 가 없으면
        while i < 10000:
            i = i + sum(list(map(int, list(str(i)))))       # 자릿수를 분리해서 합치기 신공.
            result.add(i)       # 생성자가 있는 숫자들을 집어 넣기.

for i in range(1, 10001):
    if i not in result:     # result 안에 없다면 = 셀프 넘버라면
        print(i)
