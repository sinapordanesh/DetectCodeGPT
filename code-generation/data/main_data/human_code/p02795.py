import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    h, w, n = int(input()), int(input()), int(input())
    print(min((n - 1) // h + 1, (n - 1) // w + 1))
resolve()