N, Q = map(int, input().split())
S = list(input())

class bit:
  def __init__(self, N):
    self.__N = N
    self.__a = [0] * N
  def add_(self, x, v):
    x += 1
    while x < self.__N:
      self.__a[x] += v
      x += x & -x
  def show_(self):
    print(self.__a[1:])
    
  def sum_(self, x):
    ans = 0
    while x > 0:
      ans += self.__a[x]
      x -= x & -x
    return ans
  def sub_sum_(self, x, y):
    return self.sum_(y) - self.sum_(x)
prev = "0"
BIT = bit(N)
for i, val in enumerate(S):
  if prev == "A" and val == "C":
    BIT.add_(i-1, 1)
  prev = val
for i in range(Q):
  x, y = map(int, input().split())
  x -= 1
  y -= 1
  print(BIT.sub_sum_(x,y))