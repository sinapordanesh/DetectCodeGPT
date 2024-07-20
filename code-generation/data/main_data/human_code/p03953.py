import numpy as np


def test(n, xxx, m, k, aaa):
    # print(xxx)
    print(np.diff(xxx))
    for _ in range(k):
        for a in aaa:
            x, y, z = xxx[a - 2:a + 1]
            b = x - (y - x)
            c = z + (z - y)
            xxx[a - 1] = (b + c) // 2
        # print(xxx)
        print(np.diff(xxx))


n = int(input())
xxx = list(map(int, input().split()))
m, k = map(int, input().split())
aaa = list(map(int, input().split()))

doubling = np.arange(n - 1, dtype=np.int64)
for a in aaa:
    doubling[a - 2], doubling[a - 1] = doubling[a - 1], doubling[a - 2]

perm = np.arange(n - 1, dtype=np.int64)
while k:
    if k & 1:
        perm = perm[doubling]
    doubling = doubling[doubling]
    k >>= 1

diff = np.diff(xxx)[perm]
diff = np.insert(diff, 0, xxx[0])
print('\n'.join(map(str, diff.cumsum())))
