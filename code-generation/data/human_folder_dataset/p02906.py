import sys
input=sys.stdin.readline

def find_parent(x):
    y=parent[x]
    if y<0:
        return x
    parent[x]=find_parent(y)
    return parent[x]

def connect(a,b):
    c=find_parent(a)
    d=find_parent(b)
    if c==d:
        return
    if parent[c]<parent[d]:
        parent[c]+=parent[d]
        parent[d]=c
    else:
        parent[d]+=parent[c]
        parent[c]=d
    return

N,M,Q=map(int,input().split())
data=[[],[]]
for i in range(Q):
    a,b,c=map(int,input().split())
    data[c].append((a,b))
    
parent=[-1]*N
for a,b in data[0]:
    connect(a,b)

cnt=0
for u in parent:
    if u<0:
        cnt+=1

for a,b in data[1]:
    if find_parent(a)==find_parent(b):
        print("No")
        sys.exit()

if M==N-1:
    if not data[1]:
        print("Yes")
    else:
        print("No")
else:
    M-=N
    if M<=cnt*(cnt-1)//2-cnt:
        print("Yes")
    else:
        print("No")