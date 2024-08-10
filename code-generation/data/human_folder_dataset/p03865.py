import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: map(int, sys.stdin.readline().split())
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
# debug = lambda *a, **kw: print(*a, **kw, file=sys.stderr)

s = ins()


def solve():
    lreq = s[0] == s[-1]
    odd = len(s) % 2 == 1
    return odd ^ lreq


print("First" if solve() else "Second")
