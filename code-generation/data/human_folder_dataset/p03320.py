from fractions import Fraction
def S(n):
  res = 0
  while n:
    n, r = divmod(n, 10)
    res += r
  return res
k = int(input())
n = 1
for _ in range(k):
  print(n)
  n += 1
  m = Fraction(n, S(n))
  temp = n
  for d in range(len(str(n))+1):
    x = 10**(d+1)*(n//(10**(d+1))+1)-1
    if Fraction(x, S(x)) < m:
      m = Fraction(x, S(x))
      temp = x
  n = temp