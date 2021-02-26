import sys

Alpha = sys.stdin.readline().strip()

# 문자열중 크로아티아 알파벳은 모두 0으로 변경하는 while 문
while 'c=' in Alpha or 'c-' in Alpha or 'dz=' in Alpha \
        or 'd-' in Alpha or 'lj' in Alpha or 'nj' in Alpha \
        or 's=' in Alpha or 'z=' in Alpha:
    Alpha = Alpha.replace('c=', '0')
    Alpha = Alpha.replace('c-', '0')
    Alpha = Alpha.replace('dz=', '0')
    Alpha = Alpha.replace('d-', '0')
    Alpha = Alpha.replace('lj', '0')
    Alpha = Alpha.replace('nj', '0')
    Alpha = Alpha.replace('s=', '0')
    Alpha = Alpha.replace('z=', '0')

print(len(Alpha))