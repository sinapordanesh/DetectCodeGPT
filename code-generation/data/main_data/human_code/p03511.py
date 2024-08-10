def solve(l, s, t):
    queue = [(1, 0), (0, 1)]

    def gcd(a, b):
        r = a % b
        if r:
            d = a // b
            sb = queue.pop()
            sa = queue.pop()
            queue.append(sb)
            queue.append(tuple(x - d * y for x, y in zip(sa, sb)))
            return gcd(b, r)
        else:
            return b

    ls, lt = len(s), len(t)
    if ls > lt:
        s, t, ls, lt = t, s, lt, ls
    if (s * (lt // ls + 1) * 2)[:lt * 2] > t * 2:
        s, t, ls, lt = t, s, lt, ls
    g = gcd(ls, lt)
    l //= g
    ls //= g
    lt //= g
    a, b = queue[-1]
    a *= l
    b *= l
    k = b // ls
    b -= ls * k
    a += lt * k
    return s * a + t * b


l = int(input())
s = input()
t = input()
print(solve(l, s, t))
