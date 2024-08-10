class LazySegmentTree():

    def __init__(self, n, f, g, h, ef, eh):
        """
        :param n: 配列の要素数
        :param f: 取得半群の元同士の積を定義
        :param g: 更新半群の元 xh が配列上の実際の値にどのように作用するかを定義
        :param h: 更新半群の元同士の積を定義　（更新半群の元を xh と表記）
        :param x: 配列の各要素の値。treeの葉以外は xf(x1,x2,...)
        """
        self.n = n
        self.f = f
        self.g = lambda xh, x: g(xh, x) if xh != eh else x
        self.h = h
        self.ef = ef
        self.eh = eh
        l = (self.n - 1).bit_length()
        self.size = 1 << l
        self.tree = [self.ef] * (self.size << 1)
        self.lazy = [self.eh] * ((self.size << 1) + 1)
        self.plt_cnt = 0

    def built(self, array):
        """
        arrayを初期値とするセグメント木を構築
        """
        for i in range(self.n):
            self.tree[self.size + i] = array[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.f(self.tree[i<<1], self.tree[(i<<1)|1])

    def update(self, i, x):
        """
        i 番目の要素を x に更新する
        """
        i += self.size
        self.propagate_lazy(i)
        self.tree[i] = x
        self.lazy[i] = self.eh
        self.propagate_tree(i)

    def get(self, i):
        """
        i 番目の値を取得（ 0-indexed ） ( O(logN) )
        """
        i += self.size
        self.propagate_lazy(i)
        return self.g(self.lazy[i], self.tree[i])

    def update_range(self, l, r, x):
        """
        半開区間 [l, r) の各々の要素 a に op(x, a)を作用させる （ 0-indexed ）　（ O(logN) ）
        """
        if l >= r:
            return
        l += self.size
        r += self.size
        l0 = l//(l&-l)
        r0 = r//(r&-r)
        self.propagate_lazy(l0)
        self.propagate_lazy(r0-1)
        while l < r:
            if r&1:
                r -= 1              # 半開区間なので先に引いてる
                self.lazy[r] = self.h(x, self.lazy[r])
            if l&1:
                self.lazy[l] = self.h(x, self.lazy[l])
                l += 1
            l >>= 1
            r >>= 1
        self.propagate_tree(l0)
        self.propagate_tree(r0-1)

    def get_range(self, l, r):
        """
        [l, r)への作用の結果を返す　(0-indexed)
        """
        l += self.size
        r += self.size
        self.propagate_lazy(l//(l&-l))
        self.propagate_lazy((r//(r&-r))-1)
        res_l = self.ef
        res_r = self.ef
        while l < r:
            if l & 1:
                res_l = self.f(res_l, self.g(self.lazy[l], self.tree[l]))
                l += 1
            if r & 1:
                r -= 1
                res_r = self.f(self.g(self.lazy[r], self.tree[r]), res_r)
            l >>= 1
            r >>= 1
        return self.f(res_l, res_r)

    def max_right(self, l, z):
        """
        以下の条件を両方満たす r を(いずれか一つ)返す
            ・r = l or f(op(a[l], a[l + 1], ..., a[r - 1])) = true
            ・r = n or f(op(a[l], a[l + 1], ..., a[r])) = false
        """
        if l >= self.n: return self.n
        l += self.size
        s = self.ef
        while 1:
            while l % 2 == 0:
                l >>= 1
            if not z(self.f(s, self.g(self.lazy[l], self.tree[l]))):
                while l < self.size:
                    l *= 2
                    if z(self.f(s, self.g(self.lazy[l], self.tree[l]))):
                        s = self.f(s, self.g(self.lazy[l], self.tree[l]))
                        l += 1
                return l - self.size
            s = self.f(s, self.g(self.lazy[l], self.tree[l]))
            l += 1
            if l & -l == l: break
        return self.n

    def min_left(self, r, z):
        """
        以下の条件を両方満たす l を(いずれか一つ)返す
            ・l = r or f(op(a[l], a[l + 1], ..., a[r - 1])) = true
            ・l = 0 or f(op(a[l - 1], a[l], ..., a[r - 1])) = false
        """
        if r <= 0: return 0
        r += self.size
        s = self.ef
        while 1:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not z(self.f(self.g(self.lazy[r], self.tree[r]), s)):
                while r < self.size:
                    r = r * 2 + 1
                    if z(self.f(self.g(self.lazy[r], self.tree[r]), s)):
                        s = self.f(self.g(self.lazy[r], self.tree[r]), s)
                        r -= 1
                return r + 1 - self.size
            s = self.f(self.g(self.lazy[r], self.tree[r]), s)
            if r & -r == r: break
        return 0

    def propagate_lazy(self, i):
        """
        lazy の値をトップダウンで更新する　（ O(logN) ）
        """
        for k in range(i.bit_length()-1,0,-1):
            x = i>>k
            if self.lazy[x] == self.eh:
                continue
            laz = self.lazy[x]
            self.lazy[(x<<1)|1] = self.h(laz, self.lazy[(x<<1)|1])
            self.lazy[x<<1] = self.h(laz, self.lazy[x<<1])
            self.tree[x] = self.g(laz, self.tree[x])   # get_range ではボトムアップの伝搬を行わないため、この処理をしないと tree が更新されない
            self.lazy[x] = self.eh


    def propagate_tree(self, i):
        """
        tree の値をボトムアップで更新する　（ O(logN) ）
        """
        while i>1:
            i>>=1
            self.tree[i] = self.f(self.g(self.lazy[i<<1], self.tree[i<<1]), self.g(self.lazy[(i<<1)|1], self.tree[(i<<1)|1]))

    def __getitem__(self, i):
        return self.get(i)

    def __iter__(self):
        for x in range(1, self.size):
            if self.lazy[x] == self.eh:
                continue
            self.lazy[(x<<1)|1] = self.h(self.lazy[x], self.lazy[(x<<1)|1])
            self.lazy[x<<1] = self.h(self.lazy[x], self.lazy[x<<1])
            self.tree[x] = self.g(self.lazy[x], self.tree[x])
            self.lazy[x] = self.eh
        for xh, x in zip(self.lazy[self.size:self.size+self.n], self.tree[self.size:self.size+self.n]):
            yield self.g(xh,x)

    def __str__(self):
        return str(list(self))

#########################################################################################################

from itertools import accumulate
import sys
input = sys.stdin.readline

MOD = 998244353
off = 22
mask = 1<<22

N, Q = map(int, input().split())

P = [pow(10,p,MOD) for p in range(N+1)]
SP = [0]
for p in P:
    SP.append((SP[-1]+p)%MOD)
# クエリ関数
ef = 0
def f(x, y):
    x0, x1 = x>>off, x%mask
    y0, y1 = y>>off, y%mask
    res = x0*P[y1]+y0
    res %= MOD
    return (res<<off) + x1+y1
# merge関数
eh = -1
def h(a,b):
    return a if a != eh else b
# 更新関数（g が局所的か要確認
def g(a, x):
    x1 = x%mask
    res = a*SP[x1]%MOD
    return (res<<off) + x1

st = LazySegmentTree(N, f, g, h, ef, eh)

st.built([(1<<off) + 1]*N)
res = [""]*Q
for i in range(Q):
    L, R, D = map(int, input().split())
    st.update_range(L-1, R, D)
    res[i] = str((st.get_range(0,N)>>off)%MOD)
print("\n".join(res))


