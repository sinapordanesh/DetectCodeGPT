import sys
readline = sys.stdin.readline
class Lazysegtree:
    def __init__(self, A, fx, ex, fm, em, fa, initialize = True):
        #fa(operator, idx)の形にしている、data[idx]の長さに依存する場合などのため
        self.N = len(A)
        self.N0 = 2**(self.N-1).bit_length()
        self.dep = (self.N-1).bit_length()
        self.fx = fx
        """
        self.fa =
        self.fm = fm
        """

        self.ex = ex
        self.em = em
        self.lazy = [em]*(2*self.N0)
        if initialize:
            self.data = [self.ex]*self.N0 + A + [self.ex]*(self.N0 - self.N)
            for i in range(self.N0-1, -1, -1):
                self.data[i] = self.fx(self.data[2*i], self.data[2*i+1]) 
        else:
            self.data = [self.ex]*(2*self.N0)

    def fa(self, ope, idx):
        if ope[0]:
            k = idx.bit_length()
            return (idx - (1<<(k-1)))*(1<<(self.dep+1-k)) + ope[1]
        return self.data[idx]
    
    def fm(self, x, y):
        if x[0] == 1:
            return x
        else:
            return y
    
    def __repr__(self):
        s = 'data'
        l = 'lazy'
        cnt = 1
        for i in range(self.N0.bit_length()):
            s = '\n'.join((s, ' '.join(map(str, self.data[cnt:cnt+(1<<i)]))))
            l = '\n'.join((l, ' '.join(map(str, self.lazy[cnt:cnt+(1<<i)]))))
            cnt += 1<<i
        return '\n'.join((s, l))
    
    def _ascend(self, k):
        k = k >> 1
        c = k.bit_length()
        for j in range(c):
            idx = k >> j
            self.data[idx] = self.fx(self.data[2*idx], self.data[2*idx+1])
            
    def _descend(self, k):
        k = k >> 1
        idx = 1
        c = k.bit_length()
        for j in range(1, c+1):
            idx = k >> (c - j)
            if self.lazy[idx] == self.em:
                continue
            self.data[2*idx] = self.fa(self.lazy[idx], 2*idx) 
            self.data[2*idx+1] = self.fa(self.lazy[idx], 2*idx+1)
            self.lazy[2*idx] = self.fm(self.lazy[idx], self.lazy[2*idx])
            self.lazy[2*idx+1] = self.fm(self.lazy[idx], self.lazy[2*idx+1])
            self.lazy[idx] = self.em
            
            
    def query(self, l, r):
        L = l+self.N0
        R = r+self.N0
        self._descend(L//(L & -L))
        self._descend(R//(R & -R)-1)
        
        sl = self.ex
        sr = self.ex                                                                   

        while L < R:
            if R & 1:
                R -= 1
                sr = self.fx(self.data[R], sr)
            if L & 1:
                sl = self.fx(sl, self.data[L])
                L += 1
            L >>= 1
            R >>= 1
        return self.fx(sl, sr)
    
    def operate(self, l, r, x):
        L = l+self.N0
        R = r+self.N0

        Li = L//(L & -L)
        Ri = R//(R & -R)
        self._descend(Li)
        self._descend(Ri-1)
        
        while L < R :
            if R & 1:
                R -= 1
                self.data[R] = self.fa(x, R)
                self.lazy[R] = self.fm(x, self.lazy[R])
            if L & 1:
                self.data[L] = self.fa(x, L)
                self.lazy[L] = self.fm(x, self.lazy[L])
                L += 1
            L >>= 1
            R >>= 1
        
        self._ascend(Li)
        self._ascend(Ri-1)

INF = 10**18+3

H, W = map(int, readline().split())
T = Lazysegtree([0]*W, min, INF, None, (0, 0), None, initialize = True)
N0 = T.N0
Ans = [None]*H
for qu in range(H):
    a, b = map(int, readline().split())
    a -= 1
    if a == 0:
        T.operate(a, b, (1, INF))
    else:
        x = T.query(a-1, a)
        T.operate(a, b, (1, x-a+1))
    ans = T.query(0, N0) + qu + 1
    if ans >= INF:
        ans = -1
    Ans[qu] = ans 
print('\n'.join(map(str, Ans)))