import sys
readline = sys.stdin.readline

class BIT:
    #1-indexed
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.p = 2**(n.bit_length() - 1)
        self.dep = n.bit_length()
    def get(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
    
    def bl(self, v):
        if v <= 0:
            return -1
        s = 0
        k = self.p
        for _ in range(self.dep):
            if s + k <= self.size and self.tree[s+k] < v:
                s += k
                v -= self.tree[s+k]
            k //= 2
        return s + 1

N, K = map(int, readline().split())
MOD = 998244353
P = list(map(int, readline().split()))

r = (K-1)*pow(K, MOD-2, MOD)

L = [pow(r, max(0, i-K+1), MOD) for i in range(N)]
Linv = [pow(l, MOD-2, MOD) for l in L]
T1 = BIT(N)
T2 = BIT(N)

ans = 0
asum = 0
ti = (MOD+1)//2
for i in range(N):
    ans += i - T2.get(P[i])
    g1 = T1.get(P[i])
    ans = (ans + ti*L[i]*(2*g1-asum))%MOD
    T2.add(P[i], 1)
    T1.add(P[i], Linv[i])
    asum = (asum + Linv[i]) % MOD
print(ans)