import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    H, W, N = LI()

    # 黒マス1個が影響を与える3x3領域の数は9個
    # 黒マスごとに周りの各3x3に対して黒マス数をインクリメントすればよい
    cnt = collections.Counter()
    for _ in range(N):
        a, b = LI_()
        for i, j in itertools.product(range(-1, 2), repeat=2):
            c, d = a + i, b + j
            if 1 <= c < H - 1 and 1 <= d < W - 1:
                cnt[(c, d)] += 1

    ans = collections.Counter(cnt.values())
    print((H - 2) * (W - 2) - sum(list(ans.values())))
    for i in range(1, 10):
        print(ans[i])

if __name__ == '__main__':
    resolve()
