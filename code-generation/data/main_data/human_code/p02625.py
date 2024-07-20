N, M = list(map(int, input().split()))
MOD = 10 ** 9 + 7

class mod_pack:

    def __init__(self, MOD, MAX):
        self.MOD = MOD
        self.MAX = MAX
        self.fac, self.ifac = [1]*(MAX+1), [1]*(MAX+1)
        for i in range(1, MAX+1):
            self.fac[i] = self.fac[i-1]*i % MOD
            self.ifac[i] = self.ifac[i-1] * self.mpow(i, MOD-2) % MOD
    
    def mpow(self, x, n):
        ans = 1
        while n!=0:
            if n&1: ans = ans*x % self.MOD
            x = x*x % self.MOD
            n = n >> 1
        return ans

    def mcomb(self, m, n):
        if (m==0 and n==0): return 1
        return (self.ifac[m-n] * self.ifac[n] % self.MOD) * self.fac[m] % self.MOD

    def mperm(self, m, n):
        if (m < n): return 0
        return self.ifac[m-n] * self.fac[m] % MOD
    

mp = mod_pack(10**9+7, M)

tot = mp.mperm(M, N)
ans = 0
for k in range(1, N+1):
#    print(k, mp.mcomb(N, k), mp.mperm(M-k, N-k))
    ans = (ans + (-1)**(k-1) * mp.mcomb(N, k) * mp.mperm(M-k, N-k)) % MOD


print((tot * (tot - ans))%MOD)

