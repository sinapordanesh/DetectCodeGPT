import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
from math import gcd

class SegTree:
    def __init__(self, N, ele):
        self.num = 2**(N-1).bit_length()
        self.el = ele
        self.data = [ele]*(2*self.num)

    def calc(self, x, y):
        return gcd(x, y)

    def update(self, idx, x):
        idx += (self.num - 1)
        self.data[idx] = x
        while idx > 0:
            idx = (idx-1)//2
            self.data[idx] = self.calc(self.data[2*idx+1], self.data[2*idx+2])

    def prod(self, l, r):
        L = l + self.num
        R = r + self.num
        res = self.el
        while L < R:
            if L & 1:
                res  = self.calc(res, self.data[L-1])
                L += 1
            if R & 1:
                R -= 1
                res = self.calc(res, self.data[R-1])
            L >>= 1
            R >>= 1
        return res

    def get(self, idx):
        idx += (self.num - 1)
        return self.data[idx]
    

n = int(input())
A = list(map(int, input().split()))
seg = SegTree(n, 0)
for i, a in enumerate(A):
    seg.update(i, a)

ans = 0
for i in range(n):
    g = seg.get(i)
    seg.update(i, 0)
    ans = max(ans, seg.prod(0, n))
    seg.update(i, g)
print(ans)