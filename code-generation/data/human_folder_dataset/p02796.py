import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    A = []
    for _ in range(int(input())):
        x, l = map(int, input().split())
        A.append((x - l, x + l))

    A.sort(key = lambda x : x[1])
    ans = 0
    now = -INF
    for l, r in A:
        if now <= l:
            now = r
            ans += 1
    print(ans)
resolve()