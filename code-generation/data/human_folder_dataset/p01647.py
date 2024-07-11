from itertools import combinations
import sys
readline = sys.stdin.readline
write = sys.stdout.write
cs = "XX23456789TJQKA"
ss = "SHDC"
def conv(s):
    return ss.index(s[0]), cs.index(s[1])
c_mp = {}
for i in range(9):
    es = []
    for j in range(5):
        es.append(((i+j)%13)+2)
    xs = tuple(sorted(es))
    c_mp[xs] = es[-1]
c_mp[2, 3, 4, 5, 14] = 5

def calc(p):
    xs = [b for a, b in p]
    xs.sort()
    key = tuple(xs)
    mp = {}
    for x in xs:
        mp[x] = mp.get(x, 0) + 1
    ys = sorted(mp.items(), key = lambda x: (x[1], x[0]), reverse = True)
    m = p[0][0]
    s = (all(a == m for a, b in p))
    if s and xs == [10, 11, 12, 13, 14]:
        # Royal straight flush
        return [9, 0]
    if s and key in c_mp:
        # Straight flush
        return [8, c_mp[key]]
    if ys[0][1] == 4:
        # Four of a kind
        p, q = ys
        return [7, (p[0], q[0])]
    if ys[0][1] == 3 and ys[1][1] == 2:
        # Full house
        p, q = ys
        return [6, (p[0], q[0])]
    if s:
        # Flush
        return [5, xs[::-1]]
    if key in c_mp:
        # Straight
        return [4, c_mp[key]]
    if ys[0][1] == 3:
        # Three of a kind
        p, q0, q1 = ys
        return [3, (p[0], q0[0], q1[0])]
    if ys[0][1] == 2 and ys[1][1] == 2:
        # Two pairs
        p0, p1, q = ys
        return [2, (p0[0], p1[0], q[0])]
    if ys[0][1] == 2:
        # One pair
        p, q0, q1, q2 = ys
        return [1, (p[0], q0[0], q1[0], q2[0])]
    # High card
    return [0, xs[::-1]]

def select(C):
    k = None
    for p in combinations(C, r = 5):
        r = calc(p)
        if k is None or k < r:
            k = r
    return k

def check(A, B, C):
    PA = select(A + C)
    PB = select(B + C)
    return PA > PB

def solve():
    s = readline().strip()
    if s == "#":
        return False
    *A, = map(conv, s.split())
    *B, = map(conv, readline().split())
    *C, = map(conv, readline().split())
    E = [[1]*15 for i in range(4)]
    for p, q in A + B + C:
        E[p][q] = 0
    cnt = su = 0
    for i0 in range(4):
        for j0 in range(2, 15):
            if E[i0][j0] == 0:
                continue
            for i1 in range(4):
                for j1 in range(2, 15):
                    if E[i1][j1] == 0 or (i0, j0) >= (i1, j1):
                        continue
                    if check(A, B, C + [(i0, j0), (i1, j1)]):
                        cnt += 1
                    su += 1
    write("%.16f\n" % (cnt / su))
    return True
while solve():
    ...

