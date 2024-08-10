# from sys import stdin
# input = stdin.readline
from collections import Counter

def solve():
    x = list(map(int,input().split()))
    for i,v in enumerate(x):
        if v == 0:
            print(i+1)
            return


if __name__ == '__main__':
    solve()
