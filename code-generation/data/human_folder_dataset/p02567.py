import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
a = list(map(int, input().split()))

class SegTree:
  def segfunc(self, x, y):
    return max(x, y)
  def __init__(self, n, ide_ele, init_val):
    #####単位元######
    self.ide_ele = ide_ele
    #num:n以上の最小の2のべき乗
    self.num = 2 ** (n - 1).bit_length()
    self.seg = [self.ide_ele] * 2 * self.num
    #set_val
    for i in range(n):
      self.seg[i + self.num - 1] = init_val[i]    
    #built
    for i in range(self.num - 2, -1, -1) :
      self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2]) 
  def update(self, k, x):
    k += self.num - 1
    self.seg[k] = x
    while k + 1:
      k = (k - 1) // 2
      self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2]) 
  def query(self, p, q):
    if q <= p:
      return self.ide_ele
    p += self.num - 1
    q += self.num - 2
    res = self.ide_ele
    while q - p > 1:
      if p & 1 == 0:
        res = self.segfunc(res, self.seg[p])
      if q & 1 == 1:
        res = self.segfunc(res, self.seg[q])
        q -= 1
      p = p // 2
      q = (q - 1) // 2
    if p == q:
      res = self.segfunc(res, self.seg[p])
    else:
      res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
    return res

seg = SegTree(N + 1, -1, [-1] + a)
for _ in range(Q):
  t, x, v = map(int, input().split())
  if t == 1: seg.update(x, v)
  if t == 2: print(seg.query(x, v + 1))
  if t == 3:
    ok = N + 1
    ng = x - 1
    while ok - ng > 1:
      m = (ok + ng) // 2
      if seg.query(x, m + 1) >= v: ok = m
      else: ng = m
    print(ok)