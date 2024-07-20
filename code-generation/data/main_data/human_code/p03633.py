from math import gcd
from functools import reduce

def lcm(x, y):
  return (x*y) // gcd(x, y)

N = int(input())
TS = [int(input()) for _ in range(N)]

print(reduce(lcm, TS))
