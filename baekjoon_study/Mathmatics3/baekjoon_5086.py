import sys


def math():
    while True:
        A, B = map(int, sys.stdin.readline().split())
        if A == 0 and B == 0:
            break

        if B % A == 0:
            print("factor")
            continue

        if A % B == 0:
            print("multiple")
            continue

        print("neither")
    return


if __name__ == "__main__":
    math()


'''
factor : 첫번째 숫자가 두번째 숫자의 약수라면 -> 크기 비교
8 16
16의 약수 
if A <= B
16 % 8 == 0 -> 약수 맞음

multiple : 첫 번째 숫자가 두 번째 숫자의 배수라면 
if A > B 
32 4 
32 % 4 == 0

else:
neither


'''