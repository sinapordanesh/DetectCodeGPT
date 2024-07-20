from collections import deque
import sys


def suffle(deck, c):
    l = len(deck)
    if l % 2 == 0: mid = l//2
    else: mid = (l-1)//2
    deckA = deck[mid:]
    deckB = deck[:mid]
    deckC = []
    
    while(len(deckA) != 0 or len(deckB) != 0):
        deckC.extend(deckA[:c])
        deckA = deckA[c:]
        deckC.extend(deckB[:c])
        deckB = deckB[c:]

    return deckC

while(True):
    inp = sys.stdin.readline()
    if not inp: break
    deck = []
    n, r = map(int, inp[:-1].split())
    deck = [i for i in range(n)]
    c_list = map(int, sys.stdin.readline()[:-1].split())
    for c in c_list:
        deck = suffle(deck, c)

    print(deck[-1])
    #print(" ".join(map(str, deck)))