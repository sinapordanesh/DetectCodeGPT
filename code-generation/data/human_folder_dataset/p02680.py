# ABC168F .(Single Dot)
from collections import deque

g=lambda:map(int,input().split())

N,M=g()

sortx=[]
sorty=[]

y_line=[0]*N
x_line=[0]*M

for i in range(N):
    a,b,c=g()
    sortx.append(a)
    sortx.append(b)
    sorty.append(c)
    y_line[i]=(a,b,c)
    
for i in range(M):
    d,e,f=g()
    sortx.append(d)
    sorty.append(e)
    sorty.append(f)
    x_line[i]=(d,e,f)
    
from bisect import bisect_left as bl
    
sortx=sorted(list(set(sortx)))
sorty=sorted(list(set(sorty)))

for i in range(N):
    a,b,c=y_line[i]
    a=bl(sortx,a)
    b=bl(sortx,b)
    c=bl(sorty,c)
    y_line[i]=(a,b,c)
    
for i in range(M):
    d,e,f=x_line[i]
    d=bl(sortx,d)
    e=bl(sorty,e)
    f=bl(sorty,f)
    x_line[i]=(d,e,f)
    
W=len(sortx)*2-1
H=len(sorty)*2-1
    
G=[1]*W*H

def make_graph(i,j,s=0):
    G[i+j*W]=s
    
def isOK(x,y):
    if 0<=x+y*W<W*H:
        return G[x+y*W]==1
    else:
        return False
    
def isSoto(x,y):
    return (not 0<=x+y*W<W*H)

def get_score(i,j):
    if i<=0 or j<=0  or i>=W or j>=H:
        return float('inf')
    elif i%2 and j%2:
        dx=sortx[(i+1)//2]-sortx[(i-1)//2]
        dy=sorty[(j+1)//2]-sorty[(j-1)//2]
        return dx*dy
    else:
        return 0

dic=[(-1,0),(1,0),(0,1),(0,-1)]
def search(i,j):
    res=[]
    for dx,dy in dic:
        if isOK(i+dx,j+dy) and (isOK(i+2*dx,j+2*dy) or isSoto(i+2*dx,j+2*dy)):
            res.append((i+2*dx,j+2*dy))
    return res

for a,b,c in y_line:
    for i in range(2*a,2*b+1):
        make_graph(i,2*c)
        
for d,e,f in x_line:
    for j in range(2*e,2*f+1):
        make_graph(2*d,j)
        
x0,y0=2*bl(sortx,0)-1,2*bl(sorty,0)-1

stack=deque()

for dx,dy in [(-1,-1),(-1,1),(1,1),(1,-1)]:
    if isOK(x0+dx,y0) or isOK(x0,y0+dy):
        stack.append((x0+dx,y0+dy))

stack.append((x0,y0))
res=0
make_graph(x0,y0,1)
while stack:
    x,y=stack.popleft()
    if isSoto(x,y):
        res+=get_score(x,y)
        break
    if not isOK(x,y):
        continue
    res+=get_score(x,y)
    for nx,ny in search(x,y):
        stack.append((nx,ny))
    make_graph(x,y)

print(res if res<float('inf') else 'INF')