class SegTree:
    X_unit = -10**10
    X_f = max

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)

from bisect import bisect_left
mod = 998244353
N = int(input())
robots = []
for i in range(N):
    Xi,Di = map(int,input().split())
    robots.append((Xi,Di))
robots.sort(key=lambda x:x[0])
X = [rob[0] for rob in robots]
D = [rob[1] for rob in robots]

ST = SegTree(N)
ST.set_val(N-1,N-1)
for i in range(N-1)[::-1]:
    r = bisect_left(X,X[i]+D[i])
    if i+1 == r:
        ST.set_val(i,i)
    else:
        ST.set_val(i,ST.fold(i+1,r))
to = ST.X[N:]
dp = [0]*(N+1)
dp[0] = 1
for i in range(N):
    dp[to[i]+1] += dp[i]
    dp[to[i]+1] %= mod
    dp[i+1] += dp[i]
    dp[i+1] %= mod
print(dp[N])