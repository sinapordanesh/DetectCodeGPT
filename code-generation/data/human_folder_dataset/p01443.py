import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    A, B, P = map(int, readline().split())
    if A == B == P == 0:
        return False
    N = (B - A + 1)
    data = [0]*(N+1)
    def get(k):
        s = 0
        while k:
            s += data[k]
            k -= k & -k
        return s % P
    *V, = range(A, B+1)
    V.sort(key = str)
    for v in V:
        k = v+1 - A
        x = get(k) + 1
        while k <= N:
            data[k] += x
            k += k & -k
    write("%d\n" % (get(N) % P))
    return True
while solve():
    ...
