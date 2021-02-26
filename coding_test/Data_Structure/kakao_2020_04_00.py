def solution(words, queries):
    result = []
    for keyword in queries:
        # 물음표 정리
        cnt = 0
        a = keyword.find("?")
        if a > 0:
            keyword_slice = keyword[:a]
            for word in words:
                if len(keyword) == len(word) and word.startswith(keyword_slice):
                    cnt += 1
        else:
            b = keyword.rfind("?")
            keyword_slice = keyword[b+1:]
            print(keyword_slice)
            for word in words:
                if len(keyword) == len(word) and word.endswith(keyword_slice):
                    cnt += 1

        result.append(cnt)

    return result

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))