# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def primeFact(n):
    """
    nの素因数をlistで返す
    """
    factors = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            n //= i
            factors.append(i)
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors


n = int(input())
print(str(n)+": "+" ".join(map(str, primeFact(n))))

