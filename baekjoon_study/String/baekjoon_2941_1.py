import sys

cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']       # 만약 여기서 내가 리스트를 만들어봤다면 어땠을까?, 만약 내가 여기서 리스트를 만들어봤다면

string = sys.stdin.readline().strip()

# string 변화시키기.
for i in cro_alpha:
    if i in string:         # string! 너 i 갖고 있냐? 있어? 그럼 아래로.
        string = string.replace(i, '0')

print(len(string))