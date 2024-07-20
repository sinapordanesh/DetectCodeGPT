import sys
readline = sys.stdin.readline
write = sys.stdout.write
from string import digits

def convert(S):
    S = S + "$"
    cur = 0
    def expr():
        nonlocal cur
        res = []
        op = '+'
        while 1:
            r = fact()
            if op == '-':
                for e in r:
                    e[0] *= -1
            res.extend(r)
            if S[cur] not in '+-':
                break
            op = S[cur]
            cur += 1 # '+' or '-'
        r = []
        for e0 in res:
            k0, es0 = e0
            for e1 in r:
                k1, es1 = e1
                if es0 == es1:
                    e1[0] += k0
                    break
            else:
                r.append(e0)
        res = list(filter(lambda x: x[0] != 0, r))
        res.sort()
        return res

    def fact():
        nonlocal cur
        res = [[1, []]]
        while 1:
            r = idt()
            r0 = []
            for v0, es0 in res:
                for v1, es1 in r:
                    d = {}
                    for k, v in es0:
                        d[k] = d.get(k, 0) + v
                    for k, v in es1:
                        d[k] = d.get(k, 0) + v
                    *es, = d.items()
                    es.sort()
                    r0.append([v0*v1, es])
            res = r0

            while S[cur] == ' ':
                cur += 1 # ' '
            if S[cur] in '+-$)':
                break
        return res
    def idt():
        nonlocal cur
        while S[cur] == ' ':
            cur += 1 # ' '
        if S[cur] == '(':
            cur += 1 # '('
            r = expr()
            cur += 1 # ')'
        elif S[cur] in digits:
            v = number()
            r = [[v, []]]
        else:
            c = S[cur]
            cur += 1 # 'a' ~ 'z'

            while S[cur] == ' ':
                cur += 1 # ' '
            if S[cur] == '^':
                cur += 1 # '^'
                while S[cur] == ' ':
                    cur += 1 # ' '
                v = number()
            else:
                v = 1
            r = [[1, [(c, v)]]]
        return r

    def number():
        nonlocal cur
        v = 0
        while 1:
            c = S[cur]
            if c not in digits:
                break
            v = 10*v + int(c)
            cur += 1 # '0' ~ '9'
        return v

    res = expr()
    return res


def solve():
    s0 = readline().strip()
    if s0 == '.':
        return False
    d0 = convert(s0)
    while 1:
        s = readline().strip()
        if s == '.':
            break
        d = convert(s)
        write("yes\n" if d0 == d else "no\n")
    write(".\n")
    return True
while solve():
    ...
