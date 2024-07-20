from string import digits, ascii_uppercase
def parse(S):
    S += "$"
    cur = 0
    res = []
    def expr():
        nonlocal cur
        R = []; l = 0
        while 1:
            c = S[cur]
            if c in digits:
                v = number()
                if S[cur] == '(':
                    cur += 1 # '('
                    R0, l0 = expr()
                    cur += 1 # ')'
                    l += v * l0
                    R.append((v, l0, R0))
                else:
                    c = S[cur]
                    cur += 1 # 'A' ~ 'Z'
                    l += v
                    R.append((v, 1, [c]))
            elif c in ascii_uppercase:
                cur += 1 # 'A' ~ 'Z'
                l += 1
                R.append(c)
            else:
                break
        return R, l

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

    R, l = expr()
    return R, l

def solve(res, x):
    R, l = res
    if l <= x:
        return "0"
    cur = R
    while 1:
        for data in cur:
            if isinstance(data, str):
                if x == 0:
                    return data
                x -= 1
            else:
                v, l, R = data
                if x < v*l:
                    cur = R
                    x %= l
                    break
                x -= v*l

while 1:
    S, x = input().split()
    if S == "0":
        break
    x = int(x)
    R, l = res = parse(S)
    if l <= x:
        print("0")
        continue
    print(solve(res, x))

