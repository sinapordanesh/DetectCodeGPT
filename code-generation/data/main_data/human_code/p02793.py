import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
import math
from functools import reduce

n = int(readline())
a = list(map(int,readline().split()))

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

x = reduce(lcm, a)

ans = 0
for i in range(n):
    ans += x // a[i]

print(ans%1000000007)