from string import digits
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def parse(S, mp):
    M = 32768

    cur = 0

    def transpose(m):
        p, q, v = m
        res = [[0]*p for i in range(q)]
        for i in range(q):
            for j in range(p):
                res[i][j] = v[j][i]
        return q, p, res

    def submatrix(m, a, b):
        p0, q0, v0 = m
        pa, qa, va = a
        pb, qb, vb = b
        assert pa == pb == 1
        va0 = va[0]; vb0 = vb[0]
        res = [[0]*qb for i in range(qa)]
        for i in range(qa):
            ei = va0[i]
            for j in range(qb):
                ej = vb0[j]
                res[i][j] = v0[ei-1][ej-1]
        return qa, qb, res

    def neg(m0):
        p0, q0, v0 = m0
        res = [[0]*q0 for i in range(p0)]
        for i in range(p0):
            for j in range(q0):
                res[i][j] = (-v0[i][j]) % M
        return p0, q0, res

    def emul(k, m):
        p, q, v = m
        res = [[0]*q for i in range(p)]
        for i in range(p):
            for j in range(q):
                res[i][j] = k * v[i][j] % M
        return p, q, res

    def mul(m0, m1):
        p0, q0, v0 = m0
        p1, q1, v1 = m1
        if p0 == q0 == 1:
            k0 = v0[0][0]
            if p1 == q1 == 1:
                k1 = v1[0][0]
                return 1, 1, [[k0*k1]]
            return emul(k0, m1)
        elif p1 == q1 == 1:
            k1 = v1[0][0]
            return emul(k1, m0)

        assert q0 == p1
        res = [[0]*q1 for i in range(p0)]
        for i in range(p0):
            for j in range(q1):
                res[i][j] = sum(v0[i][k] * v1[k][j] for k in range(q0)) % M
        return p0, q1, res

    def add(m0, m1):
        p0, q0, v0 = m0
        p1, q1, v1 = m1
        assert p0 == p1 and q0 == q1
        res = [[0]*q0 for i in range(p0)]
        for i in range(p0):
            for j in range(q0):
                res[i][j] = (v0[i][j] + v1[i][j]) % M
        return p0, q0, res

    def sub(m0, m1):
        p0, q0, v0 = m0
        p1, q1, v1 = m1
        assert p0 == p1 and q0 == q1
        res = [[0]*q0 for i in range(p0)]
        for i in range(p0):
            for j in range(q0):
                res[i][j] = (v0[i][j] - v1[i][j]) % M
        return p0, q0, res

    def matrix():
        nonlocal cur
        cur += 1 # "["
        R = []
        r = 0
        while 1:
            p, q, v = expr()
            R.append((r, 0, p, q, v))
            c = q
            while S[cur] == ' ':
                cur += 1 # " "
                p, q, v = expr()
                R.append((r, c, p, q, v))
                c += q
            r += p
            if S[cur] == "]":
                break
            cur += 1 # ";"
        cur += 1 # "]"
        res = [[0]*c for i in range(r)]
        for r0, c0, p, q, v in R:
            for i in range(p):
                for j in range(q):
                    res[r0+i][c0+j] = v[i][j]
        return r, c, res

    def number():
        nonlocal cur
        v = 0
        while S[cur] in digits:
            v = (10*v + int(S[cur])) % M
            cur += 1 # digits
        return 1, 1, [[v]]

    def factor():
        nonlocal cur
        s = 0
        while S[cur] == "-":
            s ^= 1
            cur += 1 # "-"
        c = S[cur]
        if c == "(":
            cur += 1 # "("
            r = expr()
            cur += 1 # ")"
        elif c == "[":
            r = matrix()
        elif c in digits:
            r = number()
        else:
            r = mp[c]
            cur += 1 # var

        while S[cur] in "('":
            if S[cur] == "'":
                t = 0
                while S[cur] == "'":
                    t ^= 1
                    cur += 1 # "'"
                if t:
                    r = transpose(r)
            else:
                cur += 1 # "("
                a = expr()
                cur += 1 # ","
                b = expr()
                cur += 1 # ")"
                r = submatrix(r, a, b)
        return neg(r) if s else r

    def term():
        nonlocal cur
        r = factor()
        while S[cur] == "*":
            cur += 1 # "*"
            r1 = factor()
            r = mul(r, r1)
        return r

    def expr():
        nonlocal cur
        r = term()
        while S[cur] in "+-":
            op = S[cur]
            cur += 1 # "+-"
            r1 = term()

            if op == "+":
                r = add(r, r1)
            else:
                r = sub(r, r1)
        return r
    return expr()

def solve():
    N = int(readline())
    if N == 0:
        return False
    mp = {}
    for i in range(N):
        v, s = readline().strip().split("=")
        mp[v] = res = parse(s, mp)
        p, q, v = res
        for cs in v:
            write(" ".join(map(str, cs)))
            write("\n")
    write("-"*5)
    write("\n")
    return True
while solve():
    ...
