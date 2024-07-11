import sys
readline = sys.stdin.readline
write = sys.stdout.write
def parse(S):
    S = S + "$"
    cur = 0
    mp = {"01": 0}
    sp = {"01": {0}}
    sv = {"01": (0, 1)}
    lbl = 1
    fmt = "0{}{}1".format
    def comp(left, right):
        lcs, lb = left
        rcs, rb = right
        a0, b0 = sv[lb]
        a1, b1 = sv[rb]
        if a1*b0 != a0*b1:
            return a1*b0 - a0*b1
        if lcs is None and rcs is None:
            return 0
        ll, lr = lcs
        rl, rr = rcs

        cl = comp(ll, rl)
        if cl != 0:
            return cl
        cr = comp(lr, rr)
        if cr != 0:
            return cr
        return 0
    def expr():
        nonlocal cur, lbl
        if S[cur] == "x":
            cur += 1 # "x"
            return (None, "01")
        cur += 1 # "("
        left = expr()
        cur += 1 # " "
        right = expr()
        cur += 1 # ")"

        lb = left[1]; rb = right[1]

        eb = fmt(lb, rb) if lb < rb else fmt(rb, lb)
        if eb not in mp:
            mp[eb] = lbl
            sp[eb] = sp[lb] | sp[rb] | {lbl}
            sv[eb] = (len(sp[lb] & sp[rb]), len(sp[lb] | sp[rb]))
            lbl += 1
        if comp(left, right) < 0:
            left, right = right, left
        return ((left, right), eb)
    return expr()

def dfs(root, m):
    if root[0] is None:
        return "x"
    left, right = root[0]
    if m == 0:
        return "({} {})".format(dfs(left, 0), dfs(right, 1))
    return "({} {})".format(dfs(right, 0), dfs(left, 1))

def solve():
    S = readline().strip()
    if S == "0":
        return False
    res = parse(S)
    write(dfs(res, 0))
    write("\n")
    return True
while solve():
    ...
