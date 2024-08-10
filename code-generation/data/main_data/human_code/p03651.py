
from math import gcd
from functools import reduce


def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    _max = max(A)
    g = reduce(gcd, A)

    if K <= _max and K % g == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    resolve()