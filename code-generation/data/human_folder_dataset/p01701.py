from fractions import Fraction


def rec(s):
  if s[0] == 'n':
    if len(s) > 5:
      t = rec(s[5:])
      return [(t[0] - 45) * 2, t[1] + 1]
    else:
      return [0, 0]
  else:
    if len(s) > 4:
      t = rec(s[4:])
      return [(t[0] + 45) * 2, t[1] + 1]
    else:
      return [90, 0]

while True:
  s = input()
  if s == "#":
    break
  
  [n, d] = rec(s)
  d = 2 ** d
  ans = Fraction(n, d)
  print(ans)