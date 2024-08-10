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
    N = I()
    ab = [LI() for _ in range(N)]
    cd = [LI() for _ in range(N)]
    ab.sort()
    ab_used = collections.OrderedDict()
    for i in ab:
        ab_used[tuple(i)] = False
    cd.sort()

    # x座標でソート 青点基準で考える
    # 青点は、自分よりx座標が小さい赤点の中でy座標が最大のものをとればよい
    ans = 0
    for c, d in cd:
        m = -1
        m_ab = (-1, -1)
        for a, b in ab:
            if a > c:
                break
            if not ab_used[(a, b)] and d > b > m:
                m = b
                m_ab = (a, b)
        if m_ab != (-1, -1):
            ab_used[m_ab] = True
            ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
