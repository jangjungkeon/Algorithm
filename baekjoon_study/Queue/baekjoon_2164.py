import sys
from collections import deque


def deck(N):
    card_deck = deque()      # card_deck = [4,3,2,1]
    for i in range(1, N+1):
        card_deck.appendleft(i)
    while len(card_deck) != 1:
        card_deck.pop()
        card_deck.appendleft(card_deck.pop())

    return print(card_deck)


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    deck(N)
