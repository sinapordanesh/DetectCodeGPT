from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

def calc(p,x):
    return p*(100+x)//100


while True:
    r,n = inpl()
    if r == 0:
        break
    else:
        heights = defaultdict(int)
        ans = INF
        for _ in range(n):
            xl,xr,h = inpl()
            heights[xl+0.1] = max(heights[xl+0.1],h)
            heights[xr-0.1] = max(heights[xr-0.1],h)
            for x in range(xl+1,xr):
                heights[x-0.1] = max(heights[x-0.1],h)
                heights[x+0.1] = max(heights[x+0.1],h)

        for x in range(-23,23):
            h = min(heights[x-0.1],heights[x+0.1])
            #print(x,h)
            if r > abs(x):
                tmp = h - (r**2-x**2)**(1/2)
                ans = min(ans,tmp+r)
        print(ans)

