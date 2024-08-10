import sys
readline = sys.stdin.readline
from collections import Counter

MOD = 998244353
def fac(limit):
    fac = [1]*limit
    for i in range(2,limit):
        fac[i] = i * fac[i-1]%MOD
    faci = [None]*limit
    faci[-1] = pow(fac[-1], MOD -2, MOD)
    for i in range(-2, -limit-1, -1):
        faci[i] = faci[i+1] * (limit + i + 1) % MOD
    return fac, faci
fac, faci = fac(234139)
def comb(a, b):
    if not a >= b >= 0:
        return 0
    return fac[a]*faci[b]*faci[a-b]%MOD
def perm(a, b):
    if not a >= b >= 0:
        return 0
    return fac[a]*faci[a-b]%MOD

pr = 3
LS = 20
class NTT:
    def __init__(self):
        self.N0 = 1<<LS
        omega = pow(pr, (MOD-1)//self.N0, MOD)
        omegainv = pow(omega, MOD-2, MOD)
        self.w = [0]*(self.N0//2)
        self.winv = [0]*(self.N0//2)
        self.w[0] = 1
        self.winv[0] = 1
        for i in range(1, self.N0//2):
            self.w[i] = (self.w[i-1]*omega)%MOD
            self.winv[i] = (self.winv[i-1]*omegainv)%MOD
        used = set()
        for i in range(self.N0//2):
            if i in used:
                continue
            j = 0
            for k in range(LS-1):
                j |= (i>>k&1) << (LS-2-k)
            used.add(j)
            self.w[i], self.w[j] = self.w[j], self.w[i]
            self.winv[i], self.winv[j] = self.winv[j], self.winv[i]
        
    def _fft(self, A):
        M = len(A)
        bn = 1
        hbs = M>>1
        while hbs:
            for j in range(hbs):
                A[j], A[j+hbs] = A[j] + A[j+hbs], A[j] - A[j+hbs]
                if A[j] > MOD:
                    A[j] -= MOD
                if A[j+hbs] < 0:
                    A[j+hbs] += MOD
            for bi in range(1, bn):
                wi = self.w[bi]
                for j in range(bi*hbs*2, bi*hbs*2+hbs):
                    A[j], A[j+hbs] = (A[j] + wi*A[j+hbs])%MOD, (A[j] - wi*A[j+hbs])%MOD
            bn <<= 1
            hbs >>= 1
 
    def _ifft(self, A):
        M = len(A)
        bn = M>>1
        hbs = 1
        while bn:
            for j in range(hbs):
                A[j], A[j+hbs] = A[j] + A[j+hbs], A[j] - A[j+hbs]
                if A[j] > MOD:
                    A[j] -= MOD
                if A[j+hbs] < 0:
                    A[j+hbs] += MOD
            for bi in range(1, bn):
                winvi = self.winv[bi]
                for j in range(bi*hbs*2, bi*hbs*2+hbs):
                    A[j], A[j+hbs] = (A[j] + A[j+hbs])%MOD, winvi*(A[j] - A[j+hbs])%MOD
            bn >>= 1
            hbs <<= 1
    
    def convolve(self, A, B):
        LA = len(A)
        LB = len(B)
        LC = LA+LB-1
        M = 1<<(LC-1).bit_length()
        A += [0]*(M-LA)
        B += [0]*(M-LB)
        self._fft(A)
        self._fft(B)
        C = [0]*M
        for i in range(M):
            C[i] = A[i]*B[i]%MOD
        self._ifft(C)
        minv = pow(M, MOD-2, MOD)
        for i in range(LC):
            C[i] = C[i]*minv%MOD
        return C[:LC]
        
        return C
    
    def inverse(self, A):
        LA = len(A)
        dep = (LA-1).bit_length()
        M = 1<<dep
        A += [0]*(M-LA)
        
        g = [pow(A[0], MOD-2, MOD)]
        for n in range(dep):
            dl = 1<<(n+1)
            f = A[:dl]
            fg = self.convolve(f, g[:])[:dl]
            fgg = self.convolve(fg, g[:])[:dl]
            ng = [None]*dl
            for i in range(dl//2):
                ng[i] = (2*g[i]-fgg[i])%MOD
            for i in range(dl//2, dl):
                ng[i] = MOD-fgg[i]
            g = ng[:]
        return g[:LA]
    
    def integral(self, A):
        A = [1] + [A[i]*faci[i+2]%MOD for i in range(len(A))]

        
N = int(readline())
H = [int(readline()) for _ in range(2*N)]
Ch = list(Counter(H).values())
M = len(Ch)
table = [[] for _ in range(M)]


for c in Ch:
    res = [0]*(c//2 + 1)
    for i in range(c//2 + 1):
        res[i] = perm(c, 2*i)*faci[i]%MOD
        hoge = comb(c, 2*i)*fac[2*i]*faci[i]%MOD
    table.append(res)
 
FT = NTT()


for i in range(M-1, 0, -1):
    table[i] = FT.convolve(table[2*i], table[2*i+1])

ans = 0
for i in range(len(table[1])):
    ans = (ans + (-1 if i&1 else 1)*table[1][i]*comb(N, i)*fac[2*N-2*i]*fac[i]) % MOD
 
ans = ans*pow((MOD+1)//2, N, MOD)*faci[N]%MOD
print(ans)
