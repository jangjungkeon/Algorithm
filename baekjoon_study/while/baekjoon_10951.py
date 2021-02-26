import sys  #  빠른 입력을 위한 모듈

while 1:
    C = sys.stdin.readline().split()        # 값 입력.
    if C == []:         # while 문 탈출 조건.
        break
    print(int(C[0])+int(C[1]))



'''
몇개의 테스트 케이스가 주어졌는지 알 수 없다면 EOF까지 받으면 된다. 
'''