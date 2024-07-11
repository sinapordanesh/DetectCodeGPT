import sys

#sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

n=II()
to=[[] for _ in range(n)]
for _ in range(n-1):
    u,v=MI1()
    to[u].append(v)
    to[v].append(u)
#print(to)

def far(u):
    stack=[(u,-1,0)]
    mxd=mxu=-1
    while stack:
        u,pu,d=stack.pop()
        if d>mxd:
            mxd=d
            mxu=u
        for v in to[u]:
            if v==pu:continue
            stack.append((v,u,d+1))
    return mxu,mxd

s,_=far(0)
t,dist=far(s)
#print(s,t,dist)

def makepath(u,t):
    stack=[(u,-1)]
    while stack:
        u,pu=stack.pop()
        while path and path[-1]!=pu:path.pop()
        path.append(u)
        if u==t:return
        for v in to[u]:
            if v==pu:continue
            stack.append((v,u))

path=[s]
makepath(s,t)
#print(path)

leg=[]
for u in path[1:-1]:leg.append(len(to[u])-2)
#print(leg)

if sum(leg)+dist+1!=n:
    print(-1)
    exit()

ans=[]
ans.append(1)
u=2
for l in leg:
    for v in range(u+1,u+1+l):
        ans.append(v)
    ans.append(u)
    u+=l+1
ans.append(u)

leg.reverse()
ans2=[]
ans2.append(1)
u=2
for l in leg:
    for v in range(u+1,u+1+l):
        ans2.append(v)
    ans2.append(u)
    u+=l+1
ans2.append(u)

if ans2<ans:ans=ans2
print(*ans)
