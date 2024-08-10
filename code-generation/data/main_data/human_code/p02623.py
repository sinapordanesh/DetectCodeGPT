from itertools import accumulate
from bisect import bisect_left

ri = lambda S: [int(v) for v in S.split()]


def rii():
    return ri(input())


N, M, K = rii()
A = rii()
B = rii()

i = j = 0

pA = [0] + list(accumulate(A))
pB = [0] + list(accumulate(B))

ans = 0
for i, a in enumerate(pA):
    br = 0
    if K >= a:
        r = K - a
        br = i
    
    if r:
        j = bisect_left(pB, r)
        if j != len(pB):
            if pB[j] > r:
                j -= 1
            br += j
    
    ans = max(ans, br)

print(ans)