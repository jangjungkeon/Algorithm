import sys
from collections import deque


def yosep(N, K):
    yose_deque = deque()
    result = []
    for i in range(1, N+1):
        yose_deque.append(i)
    yose_deque.rotate(N - K)        # 끝자리에 K번째 수를 두기 위해서
    while len(yose_deque) != 0:
        result.append(yose_deque.pop())
        yose_deque.rotate(-K)       # 매번 끝자리에 삭제될 수를 놓는다. K번째 수를 삭제하기때문에 -방향으로 rotate
    return print("<" + ", ".join(map(str, result)) + ">")


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    yosep(N, K)


'''
k=3
1,2,3,4,5,6,7
1,2,4,5,6,7
1,2,4,5,7
1,4,5,7
1,4,5

1.더블 링크드 서큘러 리스트를 구현
2.큐를 구현 

while len(card_deck) != 0:
    print(card_deck.pop())
    card_deck.rotate(K)

    K -= 1
<3, 6, 2, 7, 5, 1, 4>
'''