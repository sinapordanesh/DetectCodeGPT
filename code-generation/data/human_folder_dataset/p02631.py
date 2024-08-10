from sys import stdin
input = stdin.readline
from collections import Counter
def solve():
    N = int(input())
    a = list(map(int,input().split()))
    assert N & 1 == 0
    s = 0
    res = []
    for v in a:
        s ^= v
    for v in a:
        res.append(s^v)
    print(' '.join(map(str,res)))







if __name__ == '__main__':
    solve()
