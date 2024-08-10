def make(n):
    C = {0: 0}
    for i in range(n):
        b = int(input(), 2)
        for k, v in dict(C).items():
            if C.get(k^b, 0) < v+1:
                C[k^b] = v+1
    return C
def calc(P, Q):
    yield 0
    for k, v in P.items():
        if k in Q:
            yield v + Q[k]
def solve():
    while 1:
        n, m = map(int, input().split())
        if n+m == 0:
            break
        yield max(calc(make(n//2), make(n-n//2)))
print(*solve(), sep="\n")