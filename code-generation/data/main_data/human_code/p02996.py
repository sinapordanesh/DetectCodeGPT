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
    AB = [LI() for _ in range(N)]
    AB.sort(key=lambda x: x[1])

    ans = 'Yes'
    t = 0
    limit = 0
    for A, B in AB:
        limit = B
        t += A
        if t > limit:
            ans = 'No'
            break

    print(ans)

if __name__ == '__main__':
    resolve()
