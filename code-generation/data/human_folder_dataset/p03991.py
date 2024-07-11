import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

N = int(readline())
m = map(int,read().split())
AB = zip(m,m)

MOD = 924844033

graph = [[] for _ in range(N+1)]
for a,b in AB:
    graph[a].append(b)
    graph[b].append(a)

root = 1
parent = [0] * (N+1)
order = []
stack = [root]
while stack:
    x = stack.pop()
    order.append(x)
    for y in graph[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        stack.append(y)

size = [1] * (N+1)  # size of subtree
for v in order[::-1]:
    size[parent[v]] += size[v]

P = [0] * N
for s in size[2:]:
    P[s] += 1
    P[N-s] += 1

class ModArray(np.ndarray):
    def __new__(cls, input_array):
        obj = np.asarray(input_array, dtype=np.int64).view(cls)
        return obj
    
    @classmethod
    def zeros(cls, *args):
        obj = np.zeros(*args, dtype=np.int64)
        return obj.view(cls)
    
    @classmethod
    def ones(cls, *args):
        obj = np.ones(*args, dtype=np.int64)
        return obj.view(cls)
    
    @classmethod
    def arange(cls, *args):
        obj = np.arange(*args, dtype=np.int64) % MOD
        return obj.view(cls)
    
    @classmethod
    def powers(cls, a, N):
        B = N.bit_length()
        x = cls.ones(1<<B)
        for n in range(B):
            x[1<<n:1<<(n+1)] = x[:1<<n] * a
            a *= a; a %= MOD
        return x[:N]
    
    @classmethod
    def _set_constant_array(cls, N):
        x = cls.arange(N); x[0] = 1
        fact = x.cumprod()
        x = cls.arange(N,0,-1); x[0] = pow(int(fact[-1]), MOD-2, MOD)
        fact_inv = x.cumprod()[::-1]
        inv = cls.zeros(N)
        inv[1:N] = fact_inv[1:N] * fact[0:N-1]
        fact.flags.writeable = False
        fact_inv.flags.writeable = False
        inv.flags.writeable = False
        cls._fact = fact; cls._fact_inv = fact_inv; cls._inverse = inv
        
    @classmethod
    def fact(cls, N):
        if (getattr(cls, '_fact', None) is None) or len(cls._fact) < N:
            cls._set_constant_array(max(N, 10 ** 6))
        return cls._fact[:N]

    @classmethod
    def fact_inv(cls, N):
        if (getattr(cls, '_fact', None) is None) or len(cls._fact) < N:
            cls._set_constant_array(max(N, 10 ** 6))
        return cls._fact_inv[:N]

    @classmethod
    def inverse(cls, N):
        if (getattr(cls, '_fact', None) is None) or len(cls._fact) < N:
            cls._set_constant_array(max(N, 10 ** 6))
        return cls._inverse[:N]
    
    @classmethod
    def convolve_small(cls, f, g):
        Lf = len(f); Lg = len(g); L = Lf + Lg - 1
        if min(Lf, Lg) < 100 or Lf + Lg < 300:
            return (np.convolve(f,g) % MOD).view(cls)
        else:
            fft = np.fft.rfft; ifft = np.fft.irfft; n = 1 << L.bit_length()
            return (np.rint(ifft(fft(f, n) * fft(g, n))[:L]).astype(np.int64) % MOD).view(cls)
    
    @classmethod
    def convolve(cls, f, g, fft_killer=False):
        Lf = len(f); Lg = len(g)
        if Lf < Lg:
            f, g = g, f
            Lf, Lg = Lg, Lf
        if Lg <= (1 << 17) or (not fft_killer):
            fl = f & (1 << 15) - 1; fh = f >> 15
            gl = g & (1 << 15) - 1; gh = g >> 15
            x = cls.convolve_small(fl, gl)
            z = cls.convolve_small(fh, gh)
            y = cls.convolve_small(fl+fh, gl+gh) - x - z
            return x + (y << 15) + (z << 30)
        g = g.resize(Lf)
        n = Lf // 2
        fl = f[:n]; fh = f[n:].copy()
        gl = g[:n]; gh = g[n:].copy()
        x = ModArray.convolve(fl, gl)
        z = ModArray.convolve(fh, gh)
        fh[:len(fl)] += fl; gh[:len(gl)] += gl
        y = ModArray.convolve(fh, gh)
        P = x.resize(Lf + Lf)
        P[n : n+len(x)] -= x
        P[n : n+len(y)] += y
        P[n : n+len(z)] -= z
        P[n+n : n+n+len(z)] += z
        return P[:Lf+Lg-1]
    
    def print(self, sep=' '):
        print(sep.join(self.astype(str)))
        
    def resize(self, N):
        L = len(self)
        if L >= N:
            return self[:N]
        A = np.resize(self, N).view(self.__class__)
        A[L:] = 0
        return A
    
    def diff(self):
        return np.diff(self) % MOD
               
    def cumprod(self):
        L = len(self); Lsq = int(L**.5+1)
        A = self.resize(Lsq**2).reshape(Lsq, Lsq)
        for n in range(1,Lsq):
            A[:,n] *= A[:,n-1]
        for n in range(1,Lsq):
            A[n] *= A[n-1,-1]
        return A.ravel()[:L]

    def __array_wrap__(self, out_arr, context=None):
        if out_arr.dtype == np.int64:
            if context and context[0] == np.mod:
                 return out_arr
            np.mod(out_arr, MOD, out=out_arr)
            return out_arr
        else:
            return np.asarray(out_arr)

P = ModArray(P)
fact = ModArray.fact(N+10)
fact_inv = ModArray.fact_inv(N+10)

Q = ModArray.convolve(P * fact[:N], fact_inv[:N][::-1])[N-1:]
Q *= fact_inv[:N]

x = fact[N] * fact_inv[:N+1] * fact_inv[:N+1][::-1] * N
x[:-1] -= Q

x[1:].print(sep='\n')