class segTreeMin:
  # 区間最小値を求めるセグメント木
  inf = 10**10
  def __init__(s, num):
    s.N = 1
    while s.N < num:
      s.N *= 2
    s.inf = num
    s.T = [s.inf] * (2 * s.N)
  def do(s, l, r):
    #最小値
    return min(l, r)
  def set(s, L):
    for i in range(len(L)):
      s.update(i + 1, L[i])
  def update(s, x, v):
    k = x + s.N - 1
    s.T[k] = v
    while k > 0:
      k = (k - 1) // 2
      s.T[k] = s.do(s.T[2*k+1], s.T[2*k+2])
  def get(s, x):
    return s.T[x + s.N - 1]
  def getArea(s, l, r):
    L = l + s.N
    R = r + s.N
    p = s.inf
    while L < R:
      if R & 1:
        R -= 1
        p = s.do(p, s.T[R - 1])
      if L & 1:
        p = s.do(p, s.T[L - 1])
        L += 1
      L >>= 1
      R >>= 1
    return p

class segTreeMax:
  # 区間最大値を求めるセグメント木
  inf = -1
  def __init__(s, num):
    s.N = 1
    while s.N < num:
      s.N *= 2
    s.T = [s.inf] * (2 * s.N)
  def do(s, l, r):
    #最大値
    return max(l, r)
  def set(s, L):
    for i in range(len(L)):
      s.update(i + 1, L[i])
  def update(s, x, v):
    k = x + s.N - 1
    s.T[k] = v
    while k > 0:
      k = (k - 1) // 2
      s.T[k] = s.do(s.T[2*k+1], s.T[2*k+2])
  def get(s, x):
    return s.T[x + s.N - 1]
  def getArea(s, l, r):
    L = l + s.N
    R = r + s.N
    p = s.inf
    while L < R:
      if R & 1:
        R -= 1
        p = s.do(p, s.T[R - 1])
      if L & 1:
        p = s.do(p, s.T[L - 1])
        L += 1
      L >>= 1
      R >>= 1
    return p

N = int(input())
a = list(map(int, input().split()))

segMax = segTreeMax(N)
segMin = segTreeMin(N)

D = [[0] * 2 for _ in range(N)]
L = [0] * N

for i in range(N):
  t = a[i] - 1
  L[t] = i
  
ans = 0
for i in range(N):
  l = segMax.getArea(0, L[i] + 1)
  r = segMin.getArea(L[i], N)
  ans += (i + 1) * (L[i] - l) * (r - L[i])
  segMax.update(L[i], L[i])
  segMin.update(L[i], L[i])

print(ans)