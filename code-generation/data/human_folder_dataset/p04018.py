import sys
readline = sys.stdin.readline

class Rollinhash:
    def __init__(self, S):
        N = len(S)
        self.mod = 10**9+9
        self.base = 2009          
        self.has = [0]*(N+1)
        self.power = [1]*(N+1)
        for i in range(N):
            s = S[i]
            self.has[i+1] = (self.has[i]*self.base + s)%self.mod
            self.power[i+1] = self.power[i]*self.base%self.mod
 
    def rh(self, i, j):
        return (self.has[j] - self.has[i]*self.power[j-i])%self.mod

MOD = 10**9+7
 
S = list(map(ord, readline().strip()))
N = len(S)
if len(set(S)) == 1:
    print(N)
    print(1)
else:
    Rs = Rollinhash(S)
    
    tabler = [True]*(N+1)
    for d in range(1, 1+N//2):
        r = Rs.rh(0, d)
        for i in range(1, N//d):
            if r != Rs.rh(i*d, (i+1)*d):
                break
            tabler[(i+1)*d] = False
    tablel = [True]*(N+1)
    for d in range(1, 1+N//2):
        r = Rs.rh(N-d, N)
        for i in range(1, N//d):
            if r != Rs.rh(N-(i+1)*d, N-i*d):
                break
            tablel[N-(i+1)*d] = False
    
    if tabler[N]:
        print(1)
        print(1)
    else:
        print(2)
        ans = 0
        for i in range(N+1):
            if tabler[i] and tablel[i]:
                ans += 1
        assert ans > 0, ''
        print(ans)
        