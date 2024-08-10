import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    k, q = map(int, input().split())
    D = list(map(int, input().split()))

    for _ in range(q):
        n, x, m = map(int, input().split())
        b = x
        for i in range(k):
            s = (n - 2 - i) // k + 1
            t = D[i] % m
            if t == 0:
                t = m
            b += s * t
        print(n - 1 - (b // m - x // m))
resolve()