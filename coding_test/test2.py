s = 'aaaa'
length = len(s)
spl = []
for i in range(1, int(length/2) +1):
    tmp = s
    begin = 0; end = begin + i
    while tmp:
        spl.append(tmp[begin:end])
        tmp = tmp[end:]