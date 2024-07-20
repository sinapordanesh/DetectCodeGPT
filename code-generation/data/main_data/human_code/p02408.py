import sys
from copy import copy


def main():
    length = int(sys.stdin.readline())
    given_cards = []
    for i in range(length):
        given_cards.append(sys.stdin.readline().strip())
    cards = []
    for i in ('S ', 'H ', 'C ', 'D '):
        for j in range(13):
            cards.append(i + str(j + 1))
    for card in copy(cards):
        if card in given_cards:
            del cards[cards.index(card)]
    for card in cards:
        print(card)
    return


if __name__ == '__main__':
    main()

