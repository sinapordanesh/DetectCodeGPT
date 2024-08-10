n = int(input())
A = list(map(int, input().split()))
A.sort()
from itertools import accumulate
C = [0]+A
C = list(accumulate(C))

def is_ok(x):
    if x < 0:
        return False
    cur = C[x+1]
    for i in range(x+1, n):
        if A[i] <= 2*cur:
            cur += A[i]
        else:
            break
    else:
        return True
    return False

ng = -1
ok = n-1
while ng+1 < ok:
    c = (ok+ng)//2
    if is_ok(c):
        ok = c
    else:
        ng = c

ans = n-ok
print(ans)