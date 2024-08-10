import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split()))
P = [p-1 for p in P]

class SegmentTree:
  def __init__(self, n, e):
    self.n = n
    self.e = e
    self.size = 2 ** ((n - 1).bit_length())
    self.node = [self.e] * (2 * self.size)
 
  def build(self, array):
    for i in range(self.n):
      self.node[self.size + i] = array[i]
 
  def get(self, i):
    i += self.size
    ret = self.node[i]
    while i > 1:
      i >>= 1
      ret += self.node[i]
    return ret
 
  def add(self, l, r, val):
    l, r = l + self.size, r + self.size
    while l < r:
      if l & 1:
        self.node[l] += val
        l += 1
      if r & 1:
        r -= 1
        self.node[r] += val
      l, r = l >> 1, r >> 1
      
STA = SegmentTree(N,0)
STB = SegmentTree(N,0)

STA.build(list(range(N)))
STB.build(list(range(N)[::-1]))

prev = P[0]
for p in P[1:]:
  toadd = (STA.get(prev)+STB.get(prev)) - (STA.get(p)+STB.get(p)) + 1
  toadd = max(0,toadd)
  if p>prev:
    STA.add(p,N,toadd)
    if p+1 <= N-1:
      STB.add(p+1,N,-toadd)
  else:
    STB.add(0,p+1,toadd)
    if p >= 1:
      STA.add(0,p,-toadd)
  prev = p
  
ansa = [STA.get(i) for i in range(N)]
ansb = [STB.get(i) for i in range(N)]

mina = min(ansa)
minb = min(ansb)

ansa = [i-mina+1 for i in ansa]
ansb = [i-minb+1 for i in ansb]

print(*ansa)
print(*ansb)
