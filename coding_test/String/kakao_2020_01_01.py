def solution(s):
    length = len(s)
    answer = 99999
    if length == 1:
        answer = 1

    else:
        for i in range(1, int(length/2) + 1):
            temp = s
            spl = []
            begin = 0; end = begin + i
            # 문자열을 나누기
            while temp:
                spl.append(temp[begin:end])
                temp = temp[end:]

            newstr = ""
            cnt = 1
            before_val = spl[0]
            for idx, val in enumerate(spl):
                if idx:
                    if val == before_val:
                        cnt += 1
                        if idx == len(spl) - 1:
                            newstr += str(cnt) + before_val
                    else:
                        if cnt > 1:
                            newstr += str(cnt) + before_val
                            if idx == len(spl) - 1:
                                newstr += val
                        else:
                            newstr += before_val
                            if idx == len(spl) - 1:
                                newstr += val
                        cnt = 1
                        before_val = val
            new_str_length = len(newstr)
            if new_str_length < answer:
                answer = new_str_length

    return answer


a = "aabbaccc"
print(solution(a))