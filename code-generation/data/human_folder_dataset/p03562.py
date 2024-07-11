# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline
sys.setrecursionlimit(10**5)

n,x = readline().split()
n = int(n)
x = int(x,2)
*a, = map(lambda x:int(x,2), read().split())

def gcd(a,b):
    c = 0
    while b:
        if a < b:
            a,b = b,a
            continue
        a ^= b<<(a.bit_length() - b.bit_length())
    return a

v = 0
for ai in a: v = gcd(ai,v)

MOD = 998244353
p2 = [1]
for _ in range(5000): p2.append(p2[-1]*2%MOD)

dv = v.bit_length()
dx = x.bit_length()

def dfs(x,y,d):
    if d < dv:
        return int(x >= y)
    else:
        bx = x>>(d-1)&1
        by = y>>(d-1)&1
        if bx and by:
            return (p2[d-dv] + dfs(x,y,d-1)) %MOD
        elif not bx and by:
            return dfs(x,y^(v<<(d-dv)),d-1)
        elif not by and bx:
            return (p2[d-dv] + dfs(x,y^(v<<(d-dv)),d-1)) %MOD
        else:
            return dfs(x,y,d-1)

print(dfs(x,0,dx))


