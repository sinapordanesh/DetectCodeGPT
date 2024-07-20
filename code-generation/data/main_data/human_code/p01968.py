# -*- coding: utf-8 -*-
from collections import Counter
def inpl(): return tuple(map(int, input().split()))

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)
if C[-2] % 2 == 0:
    ans = [i+1 for i, a in enumerate(A) if abs(a) == 2]
    print(len(ans))
    if len(ans):
        print(*ans, sep="\n")
elif C[-1] > 0:
    ans = [i+1 for i, a in enumerate(A) if abs(a) == 2] + [A.index(-1) + 1]
    print(len(ans))
    if len(ans):
        print(*sorted(ans), sep="\n")
else:
    d = N -A[::-1].index(-2)
    ans = [i+1 for i, a in enumerate(A) if abs(a) == 2]
    del ans[ans.index(d)]
    print(len(ans))
    if len(ans):
        print(*ans, sep="\n")
