import sys
 
stdin = sys.stdin
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces
 
n, a, b = na()
mod = 1000000007
 
def comb(n, r, mod):
    if n < 0 or r < 0 or r > n: return 0
    nu = 1
    de = 1
    for i in range(r):
        nu = nu * (n-i) % mod
        de = de * (i+1) % mod
    return nu * inv(de, mod) % mod
 
def inv(a, mod):
    b = mod
    p, q = 1, 0
    while b > 0:
        c = a//b
        d = a; a = b; b = d % b
        d = p; p = q; q = d-c*q
    return p+mod if p < 0 else p
 
print((pow(2, n, mod) - comb(n, a, mod) - comb(n, b, mod) - 1)%mod)