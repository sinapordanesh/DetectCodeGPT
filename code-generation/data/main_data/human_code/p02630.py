from sys import stdin
input = stdin.readline
from collections import Counter
def solve():
    N = int(input())
    a = list(map(int,input().split()))
    Q = int(input())
    query = [tuple(map(int,inp.split())) for inp in stdin.read().splitlines()]
    cnt = Counter(a)
    s = sum(a)
    res = []
    for b,c in query:
        if cnt[b] != 0:
            cnt[c] += cnt[b]
            s += (c-b)*cnt[b]
            res.append(s)
            del cnt[b]
        else:
            res.append(s)
    print('\n'.join(map(str,res)))






if __name__ == '__main__':
    solve()
