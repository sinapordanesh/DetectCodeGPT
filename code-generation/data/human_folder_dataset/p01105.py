def calc(s):
    def parse(a, b, c, d):
        nonlocal cur
        g = s[cur]; cur += 1
        if g == '-':
            return 1 ^ parse(a, b, c, d)
        if g == '(':
            p = parse(a, b, c, d)
            cmd = s[cur]; cur += 1
            q = parse(a, b, c, d)
            cur += 1 # ')'
            return p ^ q if cmd == '^' else p & q
        return eval(g)
    res = 0
    for b in range(16):
        cur = 0
        if parse(*map(int, format(b, '04b'))):
            res += 1 << b
    return res
base = "abcd10"
L = {}
for e in base:
    state = calc(e)
    L[state] = 1
ALL = 2**16-1
MAX = 10**18
for i in range(6):
    R = dict(L)
    for p in R:
        if R[p] < 16:
            L[p ^ ALL] = min(L.get(p ^ ALL, MAX), R[p] + 1)
        if R[p]+3 < 16:
            for q in R:
                if R[p] + R[q] + 3 <= 16:
                    L[p & q] = min(L.get(p & q, MAX), R[p] + R[q] + 3)
                    L[p ^ q] = min(L.get(p ^ q, MAX), R[p] + R[q] + 3)
while 1:
    s = input()
    if s == '.':
        break
    print(L[calc(s)])