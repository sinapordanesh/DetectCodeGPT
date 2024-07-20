class BIT():
 
    __slots__ = ["n", "data"]
 
    def __init__(self, li):
        self.n = len(li) + 1
        self.data = [0] + li
        for i in range(1, self.n):
            if i + (i & -i) < self.n:
                self.data[i + (i & -i)] += self.data[i]
 
    def add(self, i, a):
        i += 1
        while i < self.n:
            self.data[i] += a
            i += i & -i
        
    def acc(self, i):
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        return res
    
    def fold(self, l, r):
        res = 0
        while l < r:
            res += self.data[r]
            r -= r & -r
        while r < l:
            res -= self.data[l]
            l -= l & -l
        return res

import bisect
n = int(input())
TF = []
for _ in range(n):
  s = input()
  if "." not in s:
    s += "."
  a, b = s.split(".")
  k = len(b)
  c = int(a+b)
  t = 0
  while c%2 == 0:
    c //= 2
    t += 1
  f = 0
  while c%5 == 0:
    c //= 5
    f += 1
  TF.append((t-k, f-k))
TF.sort()
ans = 0
U = 50
bit = BIT([0]*100)
temp = n
for t, f in TF:
  r = bisect.bisect_left(TF, (-t, -U))
  while temp > r:
    temp -= 1
    nt, nf = TF[temp]
    bit.add(nf+U, 1)
  ans += n-temp - bit.acc(-f+U)
for t, f in TF:
  if min(t, f) >= 0:
    ans -= 1
ans //= 2
print(ans)