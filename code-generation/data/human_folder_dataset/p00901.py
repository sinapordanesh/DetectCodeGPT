MOD = 2011
while 1:
    n = int(input())
    if n == 0:
        break
    S = [input() for i in range(n)]
    w = len(S[0])

    def parse(bcur, bright, top, bottom):
        #print("parse", bcur, bright, top, bottom)
        base = -1
        for i in range(bcur, bright):
            for j in range(top, bottom+1):
                if S[j][i] != '.':
                    base = j
                    break
            if base != -1:
                break
        cur = bcur
        def read():
            nonlocal cur
            c = None
            while 0 <= base < n and cur < bright:
                #print("cur", base, cur, bright)
                #print(S[base][cur:])
                c = S[base][cur]
                if c != '.':
                    break
                cur += 1
            return c
        def fraction():
            nonlocal cur
            #print("fraction", cur, top, bottom)
            left = cur
            while cur < w and S[base][cur] == '-':
                cur += 1
            right = cur+1 if cur < w else cur
            dividend = parse(left, right, top, base-1)
            divisor = parse(left, right, base+1, bottom)
            #print("deb", S[base][cur:], dividend, divisor)
            #print("<fraction", dividend, divisor, (dividend * pow(divisor, MOD-2, MOD)) % MOD)
            return (dividend * pow(divisor, MOD-2, MOD)) % MOD
        def primary():
            nonlocal cur
            #print("primary", cur, top, bottom)
            c = read()
            if c == '(':
                cur += 1 # '('
                v = expr()
                cur += 1 # ')'
                #print("<primary", v)
                return v
            else:
                cur += 1 # digit
                #print("<primary", c)
                return int(c)
        def powexpr():
            nonlocal cur
            #print("powexpr", cur, top, bottom)
            v = primary()
            #print("<powexpr", cur, base, v)
            if 0 < base and cur < bright and S[base-1][cur] in "0123456789":
                #print("abc", v, int(S[base-1][cur]))
                return pow(v, int(S[base-1][cur]), MOD)
            return v
        def factor():
            nonlocal cur
            #print("factor", cur, top, bottom)
            c = read()
            if c == '-':
                if S[base][cur+1] == '.':
                    cur += 1 # '-'
                    return -factor()
                else:
                    return fraction()
            return powexpr()

        def term():
            nonlocal cur
            #print("term", cur, top, bottom)
            result = 1
            while 1:
                v = factor()
                result *= v
                result %= MOD
                c = read()
                if c != '*':
                    break
                cur += 1
            return result

        def expr():
            nonlocal cur
            #print("expr", cur, top, bottom)
            op = '+'
            result = 0
            while 1:
                v = term()
                #print("<expr", v)
                c = read()
                result += v if op == '+' else MOD-v
                result %= MOD
                if not c or c not in '+-':
                    #print("break", result, v, c, op)
                    break
                cur += 1
                op = c
            #print("<result", result)
            return result
        v = expr()
        #print("<parse", v)
        return v
    print(parse(0, w, 0, n-1))