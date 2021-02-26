import sys

N = int(sys.stdin.readline().strip())
cont = 0
title = '666'
while True:
    if '666' in title:
        cont += 1
    # 탈출 조건
    if cont == N:
        print(title)
        break
    title = str(int(title) + 1)


'''
N 10000이긴한데 그러면 어떻게 해야되지. 
for문으로 돌려서 N번째가 나오면 그 때 해야되나? 
1 - 666
2 - 1666
3 - 2666
4 - 3666
5 - 4666
5666
6660
6661
6662
6663
6664
6665
6666
6667
6668
6669
7666
8666
9666


666이 포함되어야함. 

666 부터 하는 것도 괜찮을듯


...
11 - 10

'''