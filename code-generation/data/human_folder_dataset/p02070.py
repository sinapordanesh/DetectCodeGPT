from functools import reduce

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

for i in range(N):
    P[i] -= 1
    Q[i] -= 1

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# return [g, x, y]
# g = gcd(a, b)
# x, y satisfies a x + b y = g
def extgcd(a, b):
    if b == 0:
        return [a, 1, 0]
    g, x, y = extgcd(b, a%b)
    return [g, y, x - a//b * y]

# eq0: x = a0 (mod m0)
# eq1: x = a1 (mod m1)
# returns [xt, mod] such that x = xt + k mod for integer k.
def crt(eq0, eq1):
    a0, m0 = eq0
    a1, m1 = eq1

    g = gcd(m0, m1)

    if a0 % g != a1 % g:
        print(-1)
        exit(0)

    if g > 1:
        m0 //= g
        m1 //= g

        while True:
            gt = gcd(m0, g)
            if gt == 1:
                break
            m0 *= gt
            g //= gt
        
        m1 *= g

        a0 %= m0
        a1 %= m1

    g, p, q = extgcd(m0, m1)
    
    x = a0 * q * m1 + a1 * p * m0
    mod = m0 * m1
    x = x % mod

    return [x, mod]

eqs = []
for i in range(N):
    a = []
    for j in range(3 * N):
        if len(a) == 2:
            break
        if P[i] == i:
            a.append(j)
        P[i] = Q[P[i]]
    if len(a) != 2:
        print(-1)
        exit(0)
    eqs.append([a[0], a[1] - a[0]])

x, mod = reduce(crt, eqs, (0, 1))
print(x % mod)
